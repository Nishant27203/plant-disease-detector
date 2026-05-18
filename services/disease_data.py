from __future__ import annotations

# Bilingual disease guidance for farmers (English + Hindi).
# Medicines listed are common active ingredients / types — always follow local label and agri officer advice.

DISEASE_LIBRARY: dict[str, dict] = {
    "Bacterial_spot": {
        "severity": {"en": "High", "hi": "गंभीर"},
        "en": {
            "name": "Bacterial Spot",
            "treatment": "Copper-based bactericide",
            "solution": "Remove infected leaves, avoid overhead watering, and apply a copper-based bactericide following the product label.",
            "symptoms": "Small dark spots with yellow halos on leaves; spots may merge and cause leaf drop in humid weather.",
            "medicines": [
                {
                    "name": "Copper Oxychloride 50% WP (e.g. Blitox)",
                    "type": "Bactericide / Fungicide",
                    "usage": "Mix 2–2.5 g per litre water. Spray evenly on both leaf surfaces every 7–10 days.",
                },
                {
                    "name": "Streptomycin + Tetracycline (where permitted)",
                    "type": "Antibacterial spray",
                    "usage": "Use only as per local agriculture department guidance. Typically 5–10 g per 10 litres water.",
                },
            ],
            "organic": [
                "Neem oil 3–5 ml per litre water with mild soap.",
                "Remove and burn severely infected leaves away from the field.",
                "Use drip irrigation to keep leaves dry.",
            ],
            "prevention": [
                "Use disease-free seeds and resistant varieties.",
                "Avoid working in wet fields; disinfect tools with bleach solution.",
                "Maintain plant spacing for good airflow.",
            ],
            "when_to_apply": "Spray in the early morning or late evening. Start at first sign of spots; repeat after rain.",
            "safety": "Wear gloves, mask, and eye protection. Do not spray on windy days. Observe pre-harvest waiting period on the label.",
            "expert_note": "If more than 30% of plants are affected, contact your local Krishi Vigyan Kendra (KVK) or agriculture officer.",
        },
        "hi": {
            "name": "बैक्टीरियल स्पॉट (जीवाणु धब्बा)",
            "treatment": "तांबा आधारित जीवाणुनाशक",
            "solution": "संक्रमित पत्तियाँ हटाएँ, ऊपर से पानी देना बंद करें, और लेबल के अनुसार तांबा आधारित दवा का छिड़काव करें।",
            "symptoms": "पत्तियों पर पीले घेरे वाले छोटे काले धब्बे; नम मौसम में धब्बे बढ़कर पत्तियाँ झड़ सकती हैं।",
            "medicines": [
                {
                    "name": "कॉपर ऑक्सीक्लोराइड 50% WP (जैसे Blitox)",
                    "type": "जीवाणुनाशक / fungicide",
                    "usage": "2–2.5 ग्राम प्रति लीटर पानी मिलाएँ। हर 7–10 दिन में दोनों तरफ पत्तियों पर छिड़काव करें।",
                },
                {
                    "name": "स्ट्रेप्टोमाइसिन + टेट्रासाइक्लिन (जहाँ अनुमति हो)",
                    "type": "एंटीबैक्टीरियल स्प्रे",
                    "usage": "कृषि विभाग की सलाह से ही उपयोग करें। आमतौर पर 10 लीटर पानी में 5–10 ग्राम।",
                },
            ],
            "organic": [
                "नीम का तेल 3–5 ml प्रति लीटर पानी, थोड़ा साबुन मिलाकर।",
                "गंभीर रूप से संक्रमित पत्तियाँ हटाकर खेत से दूर जलाएँ।",
                "ड्रिप सिंचाई से पत्तियाँ सूखी रखें।",
            ],
            "prevention": [
                "रोग-मुक्त बीज और प्रतिरोधी किस्में लगाएँ।",
                "गीले खेत में काम न करें; औजारों को ब्लीच घोल से साफ करें।",
                "हवा के लिए पौधों के बीच दूरी रखें।",
            ],
            "when_to_apply": "सुबह जल्दी या शाम को छिड़काव करें। धब्बे दिखते ही शुरू करें; बारिश के बाद दोहराएँ।",
            "safety": "दस्ताने, मास्क और आँखों की सुरक्षा पहनें। तेज हवा में छिड़काव न करें। लेबल पर दिए अंतिम छिड़काव से कटाई का समय मानें।",
            "expert_note": "यदि 30% से अधिक पौधे प्रभावित हैं, तो नजदीकी KVK या कृषि अधिकारी से संपर्क करें।",
        },
    },
    "Early_blight": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Early Blight",
            "treatment": "Fungicide and pruning",
            "solution": "Prune lower infected leaves, improve airflow, mulch soil, and apply a chlorothalonil or copper fungicide if spread continues.",
            "symptoms": "Brown concentric rings (target-like spots) on lower older leaves; yellowing and premature leaf drop.",
            "medicines": [
                {
                    "name": "Mancozeb 75% WP",
                    "type": "Contact fungicide",
                    "usage": "2 g per litre water. Spray every 7–10 days; start before symptoms spread upward.",
                },
                {
                    "name": "Chlorothalonil 75% WP",
                    "type": "Protective fungicide",
                    "usage": "1.5–2 g per litre water. Alternate with Mancozeb to reduce resistance.",
                },
            ],
            "organic": [
                "Trichoderma viride bio-fungicide as per label.",
                "Remove lower yellow leaves and destroy away from field.",
                "Mulch soil to prevent spore splash from soil.",
            ],
            "prevention": [
                "Crop rotation — avoid tomato in same plot every year.",
                "Stake plants and prune lower 30 cm foliage.",
                "Avoid overhead irrigation in evening.",
            ],
            "when_to_apply": "Apply at first symptoms or preventively in humid season. Re-spray after heavy rain within 3–4 days if label allows.",
            "safety": "Do not mix with alkaline products. Keep spray away from children and livestock water sources.",
            "expert_note": "Early blight spreads fast in warm humid weather — act within 48 hours of spotting.",
        },
        "hi": {
            "name": "अर्ली ब्लाइट (प्रारंभिक झुलसा)",
            "treatment": "फंगीसाइड और छँटाई",
            "solution": "नीचे की संक्रमित पत्तियाँ काटें, हवा बढ़ाएँ, मल्चिंग करें, और फैलाव जारी रहे तो क्लोरोथैलोनिल या तांबा fungicide लगाएँ।",
            "symptoms": "नीचे की पुरानी पत्तियों पर भूरे गोलाकार छल्ले (निशाने जैसे धब्बे); पीलापन और समय से पहले पत्ती झड़ना।",
            "medicines": [
                {
                    "name": "मैंकोज़ेब 75% WP",
                    "type": "संपर्क fungicide",
                    "usage": "2 ग्राम प्रति लीटर पानी। हर 7–10 दिन; लक्षण ऊपर बढ़ने से पहले शुरू करें।",
                },
                {
                    "name": "क्लोरोथैलोनिल 75% WP",
                    "type": "सुरक्षात्मक fungicide",
                    "usage": "1.5–2 ग्राम प्रति लीटर। प्रतिरोध कम करने के लिए मैंकोज़ेब के साथ बारी-बारी से।",
                },
            ],
            "organic": [
                "Trichoderma viride जैव fungicide लेबल अनुसार।",
                "नीचे की पीली पत्तियाँ हटाकर खेत से दूर नष्ट करें।",
                "मिट्टी पर मल्च से मिट्टी की बूंदें कम करें।",
            ],
            "prevention": [
                "फसल चक्र — हर साल एक ही खेत में टमाटर न लगाएँ।",
                "पौधों को सहारा दें, नीचे 30 cm पत्तियाँ हटाएँ।",
                "शाम को ऊपर से सिंचाई न करें।",
            ],
            "when_to_apply": "पहले लक्षण पर या नम मौसम में रोकथाम हेतु। भारी बारish के 3–4 दिन内 लेबल अनुसार दोहराएँ।",
            "safety": "क्षारीय दवाओं के साथ मिलाएँ नहीं। बच्चों और पशुओं के पानी से दूर छिड़काव करें।",
            "expert_note": "गर्म नम मौसम में जल्दी फैलता है — धब्बे दिखते ही 48 घंटे में कार्रवाई करें।",
        },
    },
    "Late_blight": {
        "severity": {"en": "High", "hi": "गंभीर"},
        "en": {
            "name": "Late Blight",
            "treatment": "Urgent fungicide",
            "solution": "Remove badly infected plants, keep foliage dry, and apply a late-blight fungicide immediately to protect nearby plants.",
            "symptoms": "Large dark water-soaked patches on leaves; white fuzzy growth under leaves in humid conditions; rapid plant collapse.",
            "medicines": [
                {
                    "name": "Metalaxyl + Mancozeb (e.g. Ridomil Gold)",
                    "type": "Systemic + contact fungicide",
                    "usage": "2 g per litre water. Apply immediately; repeat every 7 days during wet weather.",
                },
                {
                    "name": "Dimethomorph + Mancozeb",
                    "type": "Anti-blight fungicide",
                    "usage": "As per label — typically 2 g/L. Critical for stopping spread in nearby plants.",
                },
            ],
            "organic": [
                "Remove and destroy infected plants immediately — do not compost.",
                "Improve drainage and reduce field humidity.",
                "Copper spray can give partial protection on healthy plants only.",
            ],
            "prevention": [
                "Monitor weather — late blight spreads in cool wet conditions.",
                "Use certified seed and resistant varieties where available.",
                "Avoid planting near potato fields (same pathogen family).",
            ],
            "when_to_apply": "Emergency spray within 24 hours of detection. Continue weekly until weather dries.",
            "safety": "Late blight is highly contagious — wash hands and tools after handling infected plants.",
            "expert_note": "Notify neighbouring farmers and local agriculture office — this disease can destroy entire fields in days.",
        },
        "hi": {
            "name": "लेट ब्लाइट (उपरान्त झुलसा)",
            "treatment": "तत्काल fungicide",
            "solution": "गंभीर रूप से संक्रमित पौधे हटाएँ, पत्तियाँ सूखी रखें, और बाकी पौधों की रक्षा के लिए तुरंत fungicide लगाएँ।",
            "symptoms": "पत्तियों पर बड़े गहरे पानी जैसे धब्बे; नमी में नीचे की तरफ सफेद फफूंद; पौधा जल्दी सूख जाता है।",
            "medicines": [
                {
                    "name": "Metalaxyl + Mancozeb (जैसे Ridomil Gold)",
                    "type": "Systemic + contact fungicide",
                    "usage": "2 ग्राम प्रति लीटर। तुरंत लगाएँ; गीले मौसम में हर 7 दिन दोहराएँ।",
                },
                {
                    "name": "Dimethomorph + Mancozeb",
                    "type": "Anti-blight fungicide",
                    "usage": "लेबल अनुसार — आमतौर पर 2 g/L। पास के पौधों में फैलाव रोकने के लिए जरूरी।",
                },
            ],
            "organic": [
                "संक्रमित पौधे तुरंत हटाकर नष्ट करें — खाद में न डालें।",
                "जल निकासी सुधारें, खेत की नमी कम करें।",
                "स्वस्थ पौधों पर तांबा स्प्रे आंशिक सुरक्षा दे सकता है।",
            ],
            "prevention": [
                "मौसम पर नज़र — ठंडे गीले मौसम में फैलता है।",
                "प्रमाणित बीज और प्रतिरोधी किस्में लगाएँ।",
                "आलू के खेत के पास टमाटर न लगाएँ।",
            ],
            "when_to_apply": "पता चलते 24 घंटे में emergency spray। मौसम सूखने तक साप्ताहिक दोहराएँ।",
            "safety": "बहुत संक्रामक — संक्रमित पौधों के बाद हाथ और औजार धोएँ।",
            "expert_note": "पड़ोसी किसानों और कृषि कार्यालय को सूचित करें — कुछ दिनों में पूरा खेत नष्ट हो सकता है।",
        },
    },
    "Leaf_Mold": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Leaf Mold",
            "treatment": "Humidity control and fungicide",
            "solution": "Increase ventilation, reduce humidity, remove affected leaves, and use a labeled fungicide when needed.",
            "symptoms": "Yellow patches on upper leaf surface; olive-green to gray fuzzy mold on underside; common in greenhouse or dense plantings.",
            "medicines": [
                {
                    "name": "Azoxystrobin + Difenoconazole",
                    "type": "Systemic fungicide",
                    "usage": "1 ml per litre water (check label). Spray underside of leaves thoroughly.",
                },
                {
                    "name": "Sulfur 80% WP",
                    "type": "Fungicide",
                    "usage": "2–3 g per litre. Do not use in very hot weather (>32°C) or with oil sprays.",
                },
            ],
            "organic": [
                "Improve ventilation in polyhouse; reduce plant density.",
                "Neem oil on leaf undersides weekly in mild cases.",
                "Remove heavily infected leaves promptly.",
            ],
            "prevention": [
                "Avoid night-time overhead watering.",
                "Use resistant varieties in humid regions.",
                "Sanitize greenhouse structures between seasons.",
            ],
            "when_to_apply": "When humidity is high and first yellow patches appear. Focus spray on leaf undersides.",
            "safety": "Sulfur can cause leaf burn in heat — spray in cool hours only.",
            "expert_note": "Leaf mold is often a greenhouse problem — fixing airflow is as important as medicine.",
        },
        "hi": {
            "name": "लीफ मोल्ड (पत्ती का फफूंद)",
            "treatment": "नमी नियंत्रण और fungicide",
            "solution": "हवा बढ़ाएँ, नमी कम करें, प्रभावित पत्तियाँ हटाएँ, जरूरत पर लेबल वाला fungicide लगाएँ।",
            "symptoms": "पत्ती के ऊपर पीले धब्बे; नीचे जैतून-हरे से भूरे फफूंद; पॉलीहाउस या घने रोपण में common।",
            "medicines": [
                {
                    "name": "Azoxystrobin + Difenoconazole",
                    "type": "Systemic fungicide",
                    "usage": "1 ml प्रति लीटर (लेबल देखें)। पत्तियों की नीचे की सतह पर अच्छी तरह छिड़काव।",
                },
                {
                    "name": "Sulfur 80% WP",
                    "type": "Fungicide",
                    "usage": "2–3 ग्राम प्रति लीटर। 32°C से ऊपर या तेल के साथ न लगाएँ।",
                },
            ],
            "organic": [
                "पॉलीहाउस में हवा बढ़ाएँ; पौधों की घनत्व कम करें।",
                "हल्के मामले में साप्ताहिक नीम तेल नीचे की तरफ।",
                "गंभीर पत्तियाँ तुरंत हटाएँ।",
            ],
            "prevention": [
                "रात में ऊपर से पानी न दें।",
                "नम क्षेत्रों में प्रतिरोधी किस्में।",
                "मौसम बदलने पर पॉलीहाउस साफ करें।",
            ],
            "when_to_apply": "नमी अधिक हो और पीले धब्बे दिखें तब। छिड़काव पत्ती की नीचे पर केंद्रित करें।",
            "safety": "गर्मी में sulfur से पत्ती जल सकती है — ठंडे समय में ही छिड़काव।",
            "expert_note": "अक्सर पॉलीहाउस की समस्या — दवा के साथ हवा ठीक करना भी जरूरी है।",
        },
    },
    "Septoria_leaf_spot": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Septoria Leaf Spot",
            "treatment": "Fungicide and sanitation",
            "solution": "Remove spotted leaves, clean plant debris, water at soil level, and apply a protective fungicide.",
            "symptoms": "Many small circular gray-brown spots with dark borders; tiny black dots (fungal bodies) visible in spots; starts on lower leaves.",
            "medicines": [
                {
                    "name": "Mancozeb 75% WP",
                    "type": "Protective fungicide",
                    "usage": "2 g per litre water every 7–10 days. Start when lower leaves show spots.",
                },
                {
                    "name": "Copper Oxychloride 50% WP",
                    "type": "Fungicide",
                    "usage": "2.5 g per litre. Good for organic-compliant farms when approved locally.",
                },
                {
                    "name": "Carbendazim 50% WP (severe cases)",
                    "type": "Systemic fungicide",
                    "usage": "1 g per litre — use only if spread is rapid; follow label PHI strictly.",
                },
            ],
            "organic": [
                "Remove and destroy infected lower leaves.",
                "Neem-based fungicide 3 ml/L weekly as preventive.",
                "Mulch around plants to reduce soil splash.",
            ],
            "prevention": [
                "Rotate crops — do not grow tomato/solanaceae in same soil yearly.",
                "Stake plants to keep foliage off ground.",
                "Irrigate at soil level in morning only.",
            ],
            "when_to_apply": "At first spot on lower leaves. Continue until harvest if weather stays wet — respect pre-harvest interval.",
            "safety": "Wash tomatoes before eating. Observe waiting period after last spray before harvest.",
            "expert_note": "Septoria rarely kills plants but reduces yield — treat early to protect fruit quality.",
        },
        "hi": {
            "name": "सेप्टोरिया लीफ स्पॉट (पत्ती धब्बा रोग)",
            "treatment": "Fungicide और सफाई",
            "solution": "धब्बेदार पत्तियाँ हटाएँ, खेत की रद्दी साफ करें, जड़ पर पानी दें, और सुरक्षात्मक fungicide लगाएँ।",
            "symptoms": "गहरे किनारे वाले छोटे गोल भूरे-धूसर धब्बे; धब्बों में छोटे काले बिंदु; नीचे की पत्तियों से शुरू।",
            "medicines": [
                {
                    "name": "Mancozeb 75% WP",
                    "type": "सुरक्षात्मक fungicide",
                    "usage": "2 ग्राम प्रति लीटर, हर 7–10 दिन। नीचे की पत्तियों पर धब्बे दिखते ही शुरू करें।",
                },
                {
                    "name": "Copper Oxychloride 50% WP",
                    "type": "Fungicide",
                    "usage": "2.5 ग्राम प्रति लीटर। जहाँ अनुमति हो organic खेतों के लिए उपयुक्त।",
                },
                {
                    "name": "Carbendazim 50% WP (गंभीर मामले)",
                    "type": "Systemic fungicide",
                    "usage": "1 g/L — तेज फैलाव पर; कटाई से पहले का समय (PHI) सख्ती से मानें।",
                },
            ],
            "organic": [
                "संक्रमित नीचे की पत्तियाँ हटाकर नष्ट करें।",
                "नीम आधारित fungicide 3 ml/L साप्ताहिक रोकथाम हेतु।",
                "पौधों के आसपास मल्च से मिट्टी की छींटें कम करें।",
            ],
            "prevention": [
                "फसल चक्र — हर साल solanaceae न लगाएँ।",
                "पौधों को सहारा दें, पत्तियाँ जमीन से ऊपर रखें।",
                "सुबह में सिर्फ जड़ पर सिंचाई करें।",
            ],
            "when_to_apply": "नीचे की पत्ती पर पहला धब्बा दिखते ही। गीले मौसम में कटाई तक जारी रखें — अंतिम छिड़काव का समय मानें।",
            "safety": "टमाटर खाने से पहले धोएँ। कटाई से पहले छिड़काव के बाद प्रतीक्षा अवधि मानें।",
            "expert_note": "पौधा कम मरता है पर उपज घटती है — फल की गुणवत्ता के लिए जल्दी इलाज करें।",
        },
    },
    "Spider_mites Two-spotted_spider_mite": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Spider Mites",
            "treatment": "Miticide or insecticidal soap",
            "solution": "Spray leaf undersides with water, use insecticidal soap or neem oil, and repeat treatment to control new mites.",
            "symptoms": "Fine yellow speckling on leaves; fine webbing under leaves; leaves turn bronze and dry in severe infestation.",
            "medicines": [
                {
                    "name": "Abamectin 1.9% EC (miticide)",
                    "type": "Acaricide / miticide",
                    "usage": "1–1.5 ml per litre. Spray underside of leaves; repeat after 5–7 days.",
                },
                {
                    "name": "Spiromesifen 22.9% SC",
                    "type": "Miticide",
                    "usage": "1 ml per litre as per label. Effective against egg and nymph stages.",
                },
                {
                    "name": "Neem oil 1% + insecticidal soap",
                    "type": "Organic option",
                    "usage": "5 ml neem + 2 ml soap per litre. Repeat every 3–4 days for 2 weeks.",
                },
            ],
            "organic": [
                "Strong water jet on leaf undersides every 2 days.",
                "Release predatory mites (Phytoseiulus) in greenhouse if available.",
                "Increase humidity slightly — mites hate wet conditions.",
            ],
            "prevention": [
                "Avoid dusty dry conditions; mites thrive in heat and drought stress.",
                "Remove weeds around field — alternate hosts.",
                "Inspect leaf undersides weekly in hot dry months.",
            ],
            "when_to_apply": "At first sign of speckling or webbing. Mites reproduce fast in heat — treat within 2–3 days.",
            "safety": "Miticides harm beneficial insects — spray only affected areas. Do not harvest until PHI on label.",
            "expert_note": "If entire field is webbed, combine cultural control with approved miticide immediately.",
        },
        "hi": {
            "name": "स्पाइडर माइट (मकड़ी जैसा कीट)",
            "treatment": "Miticide या कीटनाशक साबुन",
            "solution": "पत्तियों की नीचे पानी छिड़कें, insecticidal soap या नीम तेल लगाएँ, नए कीटों के लिए दोहराएँ।",
            "symptoms": "पत्तियों पर पीले छोटे धब्बे; नीचे जाल; गंभीर होने पर पत्ती कांस्य रंग की सूख जाती है।",
            "medicines": [
                {
                    "name": "Abamectin 1.9% EC (miticide)",
                    "type": "Acaricide",
                    "usage": "1–1.5 ml प्रति लीटर। नीचे की सतह पर; 5–7 दिन बाद दोहराएँ।",
                },
                {
                    "name": "Spiromesifen 22.9% SC",
                    "type": "Miticide",
                    "usage": "1 ml/L लेबल अनुसार। अंडे और नymphs पर प्रभावी।",
                },
                {
                    "name": "Neem oil 1% + insecticidal soap",
                    "type": "जैव विकल्प",
                    "usage": "5 ml neem + 2 ml soap/L। 2 सप्ताह तक हर 3–4 दिन।",
                },
            ],
            "organic": [
                "हर 2 दिन पत्ती की नीचे तेज पानी की धार।",
                "पॉलीहाउस में शिकारी mites (Phytoseiulus) छोड़ें यदि उपलब्ध।",
                "नमी थोड़ी बढ़ाएँ — mites को गीली जगह पसंद नहीं।",
            ],
            "prevention": [
                "धूल भरा सूखा मौसम न रखें; गर्मी और सूखे में फैलते हैं।",
                "खेत की खरपतवार हटाएँ।",
                "गर्म महीनों में साप्ताहिक नीचे की पत्ती जाँचें।",
            ],
            "when_to_apply": "धब्बे या जाल दिखते ही। गर्मी में 2–3 दिन में इलाज करें।",
            "safety": "Miticide लाभकारी कीटों को भी मारते हैं — सिर्फ प्रभावित जगह। PHI मानें।",
            "expert_note": "पूरे खेत में जाल हो तो तुरंत cultural + approved miticide दोनों करें।",
        },
    },
    "Target_Spot": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Target Spot",
            "treatment": "Fungicide and canopy management",
            "solution": "Remove infected foliage, improve spacing and airflow, and apply a broad-spectrum fungicide if symptoms progress.",
            "symptoms": "Brown spots with concentric rings resembling a target; spots may have yellow halos; spreads in warm humid weather.",
            "medicines": [
                {
                    "name": "Azoxystrobin 23% SC",
                    "type": "Systemic fungicide",
                    "usage": "1 ml per litre every 10–14 days. Rotate with contact fungicides.",
                },
                {
                    "name": "Difenoconazole 25% EC",
                    "type": "Systemic fungicide",
                    "usage": "0.5–1 ml per litre as per label.",
                },
            ],
            "organic": [
                "Remove infected leaves and improve plant spacing.",
                "Potassium bicarbonate spray 5 g/L as mild preventive.",
            ],
            "prevention": [
                "Avoid dense planting in humid regions.",
                "Use drip irrigation and morning watering only.",
                "Remove crop debris after harvest.",
            ],
            "when_to_apply": "When target-like rings first appear. Continue preventive sprays in rainy season if needed.",
            "safety": "Rotate fungicide groups to prevent resistance. Follow label rates — overdosing burns leaves.",
            "expert_note": "Target spot can be confused with early blight — photo + AI helps but confirm with extension officer if unsure.",
        },
        "hi": {
            "name": "टारगेट स्पॉट (निशाना धब्बा)",
            "treatment": "Fungicide और canopy प्रबंधन",
            "solution": "संक्रमित पत्तियाँ हटाएँ, दूरी और हवा बढ़ाएँ, लक्षण बढ़ें तो broad-spectrum fungicide लगाएँ।",
            "symptoms": "भूरे गोलाकार छल्ले जैसे निशाने; पीले घेरे; गर्म नम मौसम में फैलता है।",
            "medicines": [
                {
                    "name": "Azoxystrobin 23% SC",
                    "type": "Systemic fungicide",
                    "usage": "1 ml/L हर 10–14 दिन। contact fungicide के साथ बारी-बारी।",
                },
                {
                    "name": "Difenoconazole 25% EC",
                    "type": "Systemic fungicide",
                    "usage": "0.5–1 ml/L लेबल अनुसार।",
                },
            ],
            "organic": [
                "संक्रमित पत्तियाँ हटाएँ, पौधों के बीच दूरी बढ़ाएँ।",
                "Potassium bicarbonate 5 g/L हल्की रोकथाम।",
            ],
            "prevention": [
                "नम क्षेत्रों में घना रोपण न करें।",
                "ड्रिप सिंचाई, सुबह पानी।",
                "कटाई के बाद खेत की रद्दी हटाएँ।",
            ],
            "when_to_apply": "निशाना जैसे छल्ले दिखते ही। बारish के मौसम में preventive जारी रखें।",
            "safety": "प्रतिरोध से बचने fungicide बदलते रहें। अधिक मात्रा से पत्ती जलती है।",
            "expert_note": "अर्ली ब्लाइट से भ्रम हो सकता है — संदेह हो तो KVK से पुष्टि कराएँ।",
        },
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "severity": {"en": "High", "hi": "गंभीर"},
        "en": {
            "name": "Tomato Yellow Leaf Curl Virus",
            "treatment": "Vector control",
            "solution": "Remove infected plants, control whiteflies with sticky traps or insecticidal soap, and use resistant varieties in future planting.",
            "symptoms": "Upward curling of young leaves; yellowing at leaf edges; stunted plant growth; reduced fruit set.",
            "medicines": [
                {
                    "name": "Imidacloprid 17.8% SL (systemic)",
                    "type": "Insecticide for whitefly vector",
                    "usage": "0.3–0.5 ml per litre as soil drench or foliar — controls whitefly that spreads virus.",
                },
                {
                    "name": "Thiamethoxam 25% WG",
                    "type": "Insecticide",
                    "usage": "0.2 g per litre foliar spray on whitefly hotspots.",
                },
            ],
            "organic": [
                "Yellow sticky traps at 10–15 per acre for whitefly monitoring.",
                "Neem oil 5 ml/L on leaf undersides every 4 days.",
                "Uproot and destroy infected plants — no cure for virus itself.",
            ],
            "prevention": [
                "Use TYLCV-resistant tomato varieties (critical in endemic areas).",
                "Install 40-mesh insect net in nursery.",
                "Control weeds that host whiteflies.",
            ],
            "when_to_apply": "Whitefly control must start in nursery stage. Remove virus-infected plants immediately — do not wait.",
            "safety": "Viruses have no chemical cure — focus on vector control and resistant seeds.",
            "expert_note": "Contact seed supplier or KVK for TYLCV-resistant varieties suitable for your region.",
        },
        "hi": {
            "name": "टमाटर पीली पत्ती मरोड़ वायरस (TYLCV)",
            "treatment": "वाहक (whitefly) नियंत्रण",
            "solution": "संक्रमित पौधे हटाएँ, whitefly नियंत्रण करें, अगली बार प्रतिरोधी किस्म लगाएँ।",
            "symptoms": "नई पत्तियाँ ऊपर की ओर मुड़ना; किनारे पीले; पौधा छोटा रहना; फल कम लगना।",
            "medicines": [
                {
                    "name": "Imidacloprid 17.8% SL",
                    "type": "Whitefly के लिए कीटनाशक",
                    "usage": "0.3–0.5 ml/L मिट्टी या पत्ती पर — वायरस फैलाने वाली whitefly के लिए।",
                },
                {
                    "name": "Thiamethoxam 25% WG",
                    "type": "कीटनाशक",
                    "usage": "0.2 g/L whitefly वाली जगह पर छिड़काव।",
                },
            ],
            "organic": [
                "पीले sticky trap 10–15 प्रति एकड़ whitefly निगरानी हेतु।",
                "नीम तेल 5 ml/L हर 4 दिन नीचे की पत्ती पर।",
                "संक्रमित पौधा उखाड़कर नष्ट करें — वायरस की दवा नहीं।",
            ],
            "prevention": [
                "TYLCV-प्रतिरोधी टमाटर किस्में लगाएँ (endemic क्षेत्र में जरूरी)।",
                "नर्सरी में 40-mesh कीट जाल।",
                "whitefly वाली खरपतवार हटाएँ।",
            ],
            "when_to_apply": "whitefly नियंत्रण नर्सरी से शुरू। संक्रमित पौधा तुरंत हटाएँ।",
            "safety": "वायरस की रासायनिक दवा नहीं — वाहक नियंत्रण और प्रतिरोधी बीज पर ध्यान दें।",
            "expert_note": "KVK या बीज supplier से अपने क्षेत्र की TYLCV-प्रतिरोधी किस्म लें।",
        },
    },
    "Tomato_mosaic_virus": {
        "severity": {"en": "High", "hi": "गंभीर"},
        "en": {
            "name": "Tomato Mosaic Virus",
            "treatment": "Sanitation",
            "solution": "Remove infected plants, disinfect tools and hands, and avoid handling healthy plants after touching infected foliage.",
            "symptoms": "Mottled light and dark green mosaic pattern on leaves; leaf distortion; stunted growth; brown streaks on stems in severe cases.",
            "medicines": [
                {
                    "name": "No direct antiviral spray",
                    "type": "Management only",
                    "usage": "Focus on removing infected plants and disinfecting — viruses cannot be cured with fungicide/pesticide.",
                },
            ],
            "organic": [
                "Wash hands with soap before touching plants; do not smoke near crop (tobacco mosaic related).",
                "Disinfect pruning tools with 10% bleach or 70% alcohol between plants.",
                "Use virus-free certified seeds.",
            ],
            "prevention": [
                "Do not use tobacco products in the field.",
                "Control aphids which can spread some mosaic strains.",
                "Rotate with non-host crops.",
            ],
            "when_to_apply": "Remove suspect plants immediately. Disinfect tools after every infected plant.",
            "safety": "Mosaic virus spreads by contact — one infected tool can infect the whole nursery.",
            "expert_note": "Replace infected batch with certified virus-indexed seedlings from trusted nursery.",
        },
        "hi": {
            "name": "टमाटर मोज़ेक वायरस",
            "treatment": "सफाई और स्वच्छता",
            "solution": "संक्रमित पौधे हटाएँ, औजार और हाथ साफ करें, संक्रमित पत्ती छूने के बाद स्वस्थ पौधे न छुएँ।",
            "symptoms": "पत्तियों पर हल्के-गहरे हरे धब्बेदार मोज़ेक; पत्ती टेढ़ी; वृद्धि रुकना; तने पर भuri धारियाँ।",
            "medicines": [
                {
                    "name": "वायरस की सीधी दवा नहीं",
                    "type": "केवल प्रबंधन",
                    "usage": "संक्रमित पौधा हटाएँ और कीटाणुशोधन — fungicide/pesticide से वायरस ठीक नहीं होता।",
                },
            ],
            "organic": [
                "पौधों से पहले हाथ साबुन से धोएँ; खेत में तंबाकू न पिएँ।",
                "काट-छाँट के औजार bleach 10% या alcohol 70% से plant के बीच साफ करें।",
                "वायरस-मुक्त प्रमाणित बीज लें।",
            ],
            "prevention": [
                "खेत में तंबाकू उत्पाद न लाएँ।",
                "एफिड्स नियंत्रण — कुछ strains फैलाते हैं।",
                "गैर-मेज़बान फसल चक्र।",
            ],
            "when_to_apply": "संदिग्ध पौधा तुरंत हटाएँ। हर संक्रमित पौधे के बाद औजार साफ करें।",
            "safety": "संपर्क से फैलता है — एक गंदा औजार पूरी नर्सरी संक्रमित कर सकता है।",
            "expert_note": "विश्वसनीय नर्सरी से virus-indexed पौधे लगाएँ।",
        },
    },
    "healthy": {
        "severity": {"en": "None", "hi": "कोई नहीं"},
        "en": {
            "name": "Healthy Leaf",
            "treatment": "No treatment required",
            "solution": "The leaf appears healthy. Continue regular watering, balanced nutrition, and routine field monitoring.",
            "symptoms": "Uniform green colour, no spots, holes, or curling — leaf tissue looks normal.",
            "medicines": [],
            "organic": [
                "Continue balanced NPK and micronutrients as per soil test.",
                "Apply compost or vermicompost monthly for soil health.",
            ],
            "prevention": [
                "Inspect plants weekly for early signs of disease.",
                "Maintain consistent watering — avoid drought stress.",
                "Keep field weed-free to reduce pest pressure.",
            ],
            "when_to_apply": "No medicine needed. Continue preventive care and monitoring.",
            "safety": "Do not spray unnecessary pesticides on healthy plants — saves money and protects beneficial insects.",
            "expert_note": "Healthy plants today can get disease tomorrow — keep monitoring especially before flowering and fruiting.",
        },
        "hi": {
            "name": "स्वस्थ पत्ती",
            "treatment": "कोई इलाज जरूरी नहीं",
            "solution": "पत्ती स्वस्थ दिखती है। नियमित पानी, संतुलित खाद और नियमित निगरानी जारी रखें।",
            "symptoms": "समान हरा रंग, कोई धब्बा, छेद या मुड़न नहीं — पत्ती सामान्य।",
            "medicines": [],
            "organic": [
                "मिट्टी परीक्षण के अनुसार NPK और सूक्ष्म पोषक दें।",
                "मासिक compost या vermicompost से मिट्टी स्वस्थ रखें।",
            ],
            "prevention": [
                "साप्ताहिक पौधों की जाँच — रोग के शुरुआती संकेत।",
                "समान पानी — सूखे तनाव से बचें।",
                "खेत खरपतवार मुक्त — कीट कम होंगे।",
            ],
            "when_to_apply": "दवा की जरूरत नहीं। preventive देखभाल जारी रखें।",
            "safety": "स्वस्थ पौधों पर अनावश्यक कीटनाशक न छिड़कें — पैसा और लाभकारी कीट बचेंगे।",
            "expert_note": "आज स्वस्थ पौधा कल बीमार हो सकता है — फूल और फल से पहले विशेष निगरानी करें।",
        },
    },
    "powdery_mildew": {
        "severity": {"en": "Medium", "hi": "मध्यम"},
        "en": {
            "name": "Powdery Mildew",
            "treatment": "Sulfur or potassium bicarbonate fungicide",
            "solution": "Remove heavily affected leaves, improve airflow, avoid wet foliage, and apply a labeled powdery mildew treatment.",
            "symptoms": "White powdery coating on leaf surfaces; leaves may yellow and curl; common in dry days with cool nights.",
            "medicines": [
                {
                    "name": "Sulfur 80% WP",
                    "type": "Fungicide",
                    "usage": "2–3 g per litre. Spray in cool morning; avoid with oil sprays or above 32°C.",
                },
                {
                    "name": "Potassium Bicarbonate",
                    "type": "Contact fungicide / organic option",
                    "usage": "5 g per litre with 1 ml mild soap. Repeat every 5–7 days.",
                },
                {
                    "name": "Hexaconazole 5% SC",
                    "type": "Systemic fungicide",
                    "usage": "1 ml per litre for severe infection as per label.",
                },
            ],
            "organic": [
                "Milk spray 1:9 with water (some farmers use as mild preventive).",
                "Neem oil 3–5 ml/L weekly.",
                "Prune overcrowded leaves for airflow.",
            ],
            "prevention": [
                "Avoid excessive nitrogen fertilizer — soft growth is more susceptible.",
                "Plant resistant varieties in known powdery mildew areas.",
                "Space plants adequately.",
            ],
            "when_to_apply": "At first white powder on leaves. Treat before coating covers entire leaf.",
            "safety": "Sulfur sensitive varieties exist — test on few plants first if unsure.",
            "expert_note": "Powdery mildew spreads by wind — treat neighbouring rows preventively in outbreak seasons.",
        },
        "hi": {
            "name": "पाउडरी मिल्ड्यू (सफेद फफूंद)",
            "treatment": "Sulfur या potassium bicarbonate fungicide",
            "solution": "गंभीर पत्तियाँ हटाएँ, हवा बढ़ाएँ, गीली पत्ती न रखें, लेबल वाला इलाज लगाएँ।",
            "symptoms": "पत्तियों पर सफेद पाउडर जैसी परत; पीलापन और मुड़न; सूखे दिन ठंडी रात में common।",
            "medicines": [
                {
                    "name": "Sulfur 80% WP",
                    "type": "Fungicide",
                    "usage": "2–3 g/L। ठंडी सुबह; तेल के साथ या 32°C से ऊपर न लगाएँ।",
                },
                {
                    "name": "Potassium Bicarbonate",
                    "type": "Fungicide / जैव विकल्प",
                    "usage": "5 g/L + 1 ml साबुन। हर 5–7 दिन।",
                },
                {
                    "name": "Hexaconazole 5% SC",
                    "type": "Systemic fungicide",
                    "usage": "गंभीर संक्रमण में 1 ml/L लेबल अनुसार।",
                },
            ],
            "organic": [
                "दूध 1:9 पानी (कुछ किसान preventive के लिए)।",
                "नीम तेल 3–5 ml/L साप्ताहिक।",
                "भीड़ वाली पत्तियाँ काटकर हवा बढ़ाएँ।",
            ],
            "prevention": [
                "अधिक nitrogen खाद न दें — नरम पत्ती अधिक संवेदनशील।",
                "प्रतिरोधी किस्में लगाएँ।",
                "पौधों के बीच दूरी रखें।",
            ],
            "when_to_apply": "पहली सफेद परत दिखते ही। पूरी पत्ती ढकने से पहले इलाज।",
            "safety": "कुछ किस्में sulfur sensitive — पहले कुछ पौधों पर परीक्षण।",
            "expert_note": "हवा से फैलता है — outbreak में पड़ोस की कतारों पर preventive छिड़काव।",
        },
    },
}
