const resultPage = document.querySelector("#resultPage");
const sessionId = resultPage.dataset.sessionId;

loadResult();
document.addEventListener("leafscan:langchange", loadResult);

async function loadResult() {
  resultPage.className = "loading-card";
  resultPage.innerHTML = `<div class="result-loading"><span class="button-spinner"></span><p>${escapeHtml(t("result.loading"))}</p></div>`;

  try {
    const response = await fetch(`/api/result/${sessionId}?${apiLangQuery()}`);
    const data = await response.json();
    if (!response.ok || !data.success) {
      resultPage.className = "error-card";
      resultPage.innerHTML = `<h1>${escapeHtml(t("result.notFound"))}</h1><p>${escapeHtml(data.error || t("result.loadError"))}</p>`;
      return;
    }
    renderResult(data);
  } catch (error) {
    resultPage.className = "error-card";
    resultPage.innerHTML = `<h1>${escapeHtml(t("result.loadError"))}</h1><p>${escapeHtml(t("result.refresh"))}</p>`;
  }
}

function renderResult(data) {
  const isAlert = data.severity && !["None", "कोई नहीं"].includes(data.severity);
  const confidence = Number(data.confidence).toFixed(1);

  resultPage.className = "result-page";
  resultPage.innerHTML = `
    <header class="result-hero ${isAlert ? "result-hero--alert" : "result-hero--ok"}">
      <div class="result-hero-text">
        <p class="eyebrow">${escapeHtml(t("result.eyebrow"))}</p>
        <h1>${escapeHtml(data.disease)}</h1>
        <p class="result-treatment-line">${escapeHtml(t("result.treatment"))}: ${escapeHtml(data.treatment)}</p>
      </div>
      <div class="result-confidence-ring" style="--confidence:${confidence}">
        <div class="result-confidence-inner">
          <span class="result-confidence-value">${confidence}%</span>
          <span class="result-confidence-label">${escapeHtml(t("result.confidence"))}</span>
        </div>
      </div>
    </header>

    <div class="result-stats">
      <div class="stat-chip ${isAlert ? "stat-chip--alert" : ""}">
        <span class="stat-label">${escapeHtml(t("result.severity"))}</span>
        <strong>${escapeHtml(data.severity)}</strong>
      </div>
      <div class="stat-chip">
        <span class="stat-label">${escapeHtml(t("result.inference"))}</span>
        <strong>${Number(data.prediction_time).toFixed(2)}s</strong>
      </div>
    </div>

    <div class="result-images">
      <figure class="result-image-card">
        <img src="/static/${escapeHtml(data.image_path)}" alt="Uploaded leaf">
        <figcaption>${escapeHtml(t("result.original"))}</figcaption>
      </figure>
      <figure class="result-image-card">
        <img src="/static/${escapeHtml(data.gradcam_image)}" alt="Grad-CAM heatmap">
        <figcaption>${escapeHtml(t("result.heatmap"))}</figcaption>
      </figure>
    </div>

    <section class="result-solution-card">
      <h2>${escapeHtml(t("result.solution"))}</h2>
      <p>${escapeHtml(data.solution)}</p>
    </section>

    <section class="result-panel">
      <h2 class="result-panel-title">${escapeHtml(t("result.topPredictions"))}</h2>
      <div class="prediction-cards">
        ${renderPredictionCards(data.top_predictions)}
      </div>
    </section>

    <section class="result-panel">
      <h2 class="result-panel-title">${escapeHtml(t("result.details"))}</h2>
      <div class="result-accordion">
        ${renderAccordionItem("symptoms", t("result.symptoms"), data.symptoms, "text")}
        ${renderAccordionItem("medicines", t("result.medicines"), data.medicines, "medicines")}
        ${renderAccordionItem("organic", t("result.organic"), data.organic, "list")}
        ${renderAccordionItem("prevention", t("result.prevention"), data.prevention, "list")}
        ${renderAccordionItem("when", t("result.when"), data.when_to_apply, "text")}
        ${renderAccordionItem("safety", t("result.safety"), data.safety, "text")}
        ${renderAccordionItem("expert", t("result.expert"), data.expert_note, "text")}
      </div>
    </section>

    <div class="result-actions">
      <a class="button primary" href="/">${escapeHtml(t("result.new"))}</a>
      <a class="button outline" href="/history">${escapeHtml(t("result.history"))}</a>
    </div>
  `;
}

function renderPredictionCards(items) {
  const list = items || [];
  if (!list.length) {
    return `<p class="result-empty">—</p>`;
  }
  return list.map((item, index) => `
    <article class="prediction-card ${index === 0 ? "prediction-card--top" : ""}">
      <div class="prediction-card-head">
        <span class="prediction-rank">#${index + 1}</span>
        <strong>${escapeHtml(cleanLabel(item.label))}</strong>
      </div>
      <div class="prediction-bar"><span style="width:${Number(item.confidence).toFixed(2)}%"></span></div>
      <span class="prediction-pct">${Number(item.confidence).toFixed(2)}%</span>
    </article>
  `).join("");
}

function renderAccordionItem(id, title, content, type) {
  if (!content || (Array.isArray(content) && !content.length)) {
    return "";
  }

  let body = "";
  if (type === "text") {
    body = `<p>${escapeHtml(content)}</p>`;
  } else if (type === "list") {
    body = `<ul class="tip-list">${content.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`;
  } else if (type === "medicines") {
    body = `<div class="medicine-grid">${content.map((med) => `
      <article class="medicine-card">
        <h4>${escapeHtml(med.name)}</h4>
        <p><strong>${escapeHtml(t("result.med.type"))}:</strong> ${escapeHtml(med.type)}</p>
        <p><strong>${escapeHtml(t("result.med.usage"))}:</strong> ${escapeHtml(med.usage)}</p>
      </article>
    `).join("")}</div>`;
  }

  const openFirst = id === "symptoms" || id === "medicines";
  return `
    <details class="result-acc-item result-acc-item--${id}" ${openFirst ? "open" : ""}>
      <summary>${escapeHtml(title)}</summary>
      <div class="result-acc-body">${body}</div>
    </details>
  `;
}

function cleanLabel(label) {
  return String(label || "").replace("Tomato___", "").replaceAll("_", " ");
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
