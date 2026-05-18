const historyList = document.querySelector("#historyList");

loadHistory();
document.addEventListener("leafscan:langchange", loadHistory);

async function loadHistory() {
  historyList.innerHTML = `<div class="loading-card">${escapeHtml(t("result.loading"))}</div>`;

  try {
    const response = await fetch(`/api/history?${apiLangQuery()}`);
    const data = await response.json();
    const items = data.items || [];

    if (!items.length) {
      historyList.innerHTML = `<div class="loading-card">${escapeHtml(t("history.empty"))}</div>`;
      return;
    }

    historyList.innerHTML = items.map(renderHistoryItem).join("");
  } catch (error) {
    historyList.innerHTML = `<div class="error-card">${escapeHtml(t("history.error"))}</div>`;
  }
}

function renderHistoryItem(item) {
  return `
    <a class="history-item" href="/result/${escapeHtml(item.session_id)}">
      <img src="/static/${escapeHtml(item.image_path)}" alt="Leaf prediction thumbnail">
      <div>
        <h3>${escapeHtml(item.disease)}</h3>
        <div class="history-meta">
          ${escapeHtml(item.severity)} ${escapeHtml(t("history.severity"))} · ${formatDate(item.created_at)} · ${Number(item.prediction_time).toFixed(3)}s
        </div>
      </div>
      <div class="history-confidence">${Number(item.confidence).toFixed(1)}%</div>
    </a>
  `;
}

function formatDate(value) {
  if (!value) return "—";
  const locale = getLang() === "hi" ? "hi-IN" : "en-IN";
  return new Date(value).toLocaleString(locale);
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
