# translations.py
# ---------------------------------------------------------
# Zweisprachige Übersetzungen für das gesamte Dashboard
# Deutsch (de) / Englisch (en)
# ---------------------------------------------------------

translations = {

    # -----------------------------------------------------
    # Allgemein / Zugriffsschutz
    # -----------------------------------------------------
    "all_option": {
        "de": "Alle",
        "en": "All"
    },
    "login_required": {
        "de": "Bitte zuerst einloggen.",
        "en": "Please log in first."
    },
    "login_or_register_required": {
        "de": "Bitte zuerst registrieren oder einloggen.",
        "en": "Please register or log in first."
    },

    # -----------------------------------------------------
    # Login
    # -----------------------------------------------------
    "login_title": {
        "de": "🔐 Login",
        "en": "🔐 Login"
    },
    "username": {
        "de": "Benutzername",
        "en": "Username"
    },
    "password": {
        "de": "Passwort",
        "en": "Password"
    },
    "login_button": {
        "de": "Login",
        "en": "Login"
    },
    "login_success": {
        "de": "Login erfolgreich!",
        "en": "Login successful!"
    },
    "login_error": {
        "de": "Benutzername oder Passwort falsch.",
        "en": "Incorrect username or password."
    },

    # -----------------------------------------------------
    # Registrierung
    # -----------------------------------------------------
    "register_title": {
        "de": "📝 Registrierung",
        "en": "📝 Registration"
    },
    "email": {
        "de": "E-Mail",
        "en": "Email"
    },
    "register_button": {
        "de": "Registrieren",
        "en": "Register"
    },
    "register_success": {
        "de": "Registrierung erfolgreich! Du kannst dich jetzt einloggen.",
        "en": "Registration successful! You can now log in."
    },
    "register_error": {
        "de": "Fehler: Benutzername oder E-Mail existiert bereits.",
        "en": "Error: Username or email already exists."
    },

    # -----------------------------------------------------
    # Sidebar
    # -----------------------------------------------------
    "nav_header": {
        "de": "Navigation",
        "en": "Navigation"
    },
    "logged_in_as": {
        "de": "Angemeldet als",
        "en": "Logged in as"
    },
    "logout": {
        "de": "🚪 Logout",
        "en": "🚪 Logout"
    },

    # -----------------------------------------------------
    # Startseite
    # -----------------------------------------------------
    "home_title": {
        "de": "🌍 Analyse der Importe kritischer Rohstoffe in Deutschland: Entwicklung einer datengetriebenen ETL- und Dashboard-Plattform",
        "en": "🌍 Analysis of Germany's Imports of Critical Raw Materials: Development of a Data-Driven ETL and Dashboard Platform"
    },
    "home_intro": {
        "de": "**Willkommen zu unserem Dashboard-Projekt über kritische Rohstoffe**.",
        "en": "**Welcome to our dashboard project on critical raw materials**."
    },
    "home_description": {
        "de": "Dieses Multi-Page-Dashboard besteht aus:",
        "en": "This multi-page dashboard consists of:"
    },
    "home_point_analysis": {
        "de": "1. **Analyse** – Deskriptive Analyse der Importe (Werte, Mengen, Preis pro kg, Zeitreihen).",
        "en": "1. **Analysis** – Descriptive analysis of imports (values, quantities, price per kg, time series)."
    },
    "home_point_risk": {
        "de": "2. **Risikoanalyse** – Diversität, Abhängigkeiten, Konzentrationsrisiken, HHI je Land und Produkt, HHI-Trends.",
        "en": "2. **Risk analysis** – Diversity, Dependencies, concentration risks, HHI by Country and Product, HHI trends."
    },
    "home_point_summary": {
        "de": "3. **Summary** – Top-5 Länder je Produkt, Top-5 Produkte je Jahr, automatische Insights.",
        "en": "3. **Summary** – Top‑5 countries per product, Top‑5 products per year, automatic insights."
    },
    "home_data_basis": {
        "de": "Die Daten basieren auf einem **Star-Schema** in PostgreSQL oder Supabase mit:",
        "en": "The data is based on a **star schema** in PostgreSQL or Supabase with:"
    },
    "home_data_tables": {
        "de": "- `users`\n- `dim_years`, `dim_countries`, `dim_products`\n- `fact_imports` (Mengen, Gewichte, Werte)",
        "en": "- `users`\n- `dim_years`, `dim_countries`, `dim_products`\n- `fact_imports` (quantities, weights, values)"
    },
    "home_sidebar_hint": {
        "de": "**Nutzen Sie die Seitenleiste links, um zwischen den Dashboards zu wechseln**.",
        "en": "**Use the sidebar on the left to navigate between dashboards**."
    },

    # -----------------------------------------------------
    # Analyse-Seite
    # -----------------------------------------------------
    "analysis_title": {
        "de": "📊 Analyse deutscher– Importe kritischer Rohstoffe",
        "en": "📊 Analysis of German Imports of Critical Raw Materials"
    },
    "filter_header": {
        "de": "Filter",
        "en": "Filters"
    },
    "filter_years": {
        "de": "Jahre auswählen",
        "en": "Select years"
    },
    "filter_countries": {
        "de": "Länder auswählen",
        "en": "Select countries"
    },
    "filter_products": {
        "de": "Produkte auswählen",
        "en": "Select products"
    },

    # KPIs
    "kpi_total_value": {
        "de": "Gesamtwert (USD)",
        "en": "Total value (USD)"
    },
    "kpi_total_weight": {
        "de": "Gesamtgewicht (kg)",
        "en": "Total weight (kg)"
    },
    "kpi_avg_price": {
        "de": "Ø Preis (USD)",
        "en": "Avg. price (USD)"
    },
    "kpi_price_per_kg": {
        "de": "Preis pro kg (USD/kg)",
        "en": "Price per kg (USD/kg)"
    },

    # Charts
    "chart_value_by_country": {
        "de": "Importwert nach Ländern",
        "en": "Import value by country"
    },
    "chart_value_by_product": {
        "de": "Importwert nach Produkten",
        "en": "Import value by product"
    },
    "chart_value_per_year": {
        "de": "Zeitreihe: Importwert pro Jahr",
        "en": "Time series: import value per year"
    },
    "chart_ppk_per_year": {
        "de": "Zeitreihe: Preis pro kg über die Jahre",
        "en": "Time series: price per kg over the years"
    },
    "chart_yoy": {
        "de": "📉 Year-over-Year Veränderung (Importwert)",
        "en": "📉 Year-over-Year change (import value)"
    },

    "no_data": {
        "de": "Keine Daten für die aktuelle Filterauswahl.",
        "en": "No data for the current filter selection."
    },

    # Risiko-Karte
    "risk_map_title": {
        "de": "🌍 Geografische Risiko-Karte: Importabhängigkeit",
        "en": "🌍 Geographic risk map: import dependency"
    },
    "dependency": {
        "de": "Abhängigkeit",
        "en": "Dependency"
    },

    # CSV
    "download_title": {
        "de": "📥 Daten herunterladen",
        "en": "📥 Download data"
    },
    "download_csv": {
        "de": "CSV herunterladen",
        "en": "Download CSV"
    },

    # Tabelle
    "detail_table": {
        "de": "Detailtabelle",
        "en": "Detailed table"
    },

    # -----------------------------------------------------
    # Risikoanalyse-Seite
    # -----------------------------------------------------
    "risk_title": {
        "de": "⚠️ Risikoanalyse kritischer Rohstoffe",
        "en": "⚠️ Risk analysis of critical raw materials"
    },
    "risk_heatmap": {
        "de": "🔥 Risiko-Heatmap: Importabhängigkeit",
        "en": "🔥 Risk heatmap: import dependency"
    },
    "hhi_title": {
        "de": "📉 HHI-Konzentrationsindex (Lieferländer)",
        "en": "📉 HHI concentration index (supplier countries)"
    },
    "no_hhi": {
        "de": "Keine Daten für HHI-Berechnung.",
        "en": "No data available for HHI calculation."
    },
    "china_exposure_title": {
        "de": "🇨🇳 China Exposure pro Produkt",
        "en": "🇨🇳 China exposure per product"
    },
    "no_china_imports": {
        "de": "Keine China-Importe in der aktuellen Filterauswahl.",
        "en": "No Chinese imports in the current filter selection."
    },
    "no_china_data": {
        "de": "Keine Daten für China-Exposure.",
        "en": "No data available for China exposure."
    },
    "hhi_trend_title": {
        "de": "📈 Risiko-Trend: HHI über die Jahre",
        "en": "📈 Risk trend: HHI over the years"
    },
    "hhi_country_product": {
        "de": "📊 HHI je Land und Produkt",
        "en": "📊 HHI by Country and Product"
    },
    "select_at_least_one_product": {
        "de": "Bitte mindestens ein Produkt auswählen.",
        "en": "Please select at least one product."
    },
    "no_data_for_product": {
        "de": "Keine Daten für dieses Produkt verfügbar.",
        "en": "No data available for this product."
    },
    # -----------------------------------------------------
    # Summary-Seite
    # -----------------------------------------------------
    "summary_title": {
        "de": "📘 Summary – Top 5 & Insights",
        "en": "📘 Summary – Top 5 & Insights"
    },
    "top5_countries_title": {
        "de": "🌍 Top 5 Länder je Produkt",
        "en": "🌍 Top 5 countries per product"
    },
    "no_top5_countries": {
        "de": "Keine Daten für Top-5 Länder je Produkt.",
        "en": "No data for Top‑5 countries per product."
    },
    "top5_products_title": {
        "de": "📦 Top 5 Produkte pro Jahr",
        "en": "📦 Top 5 products per year"
    },
    "no_top5_products": {
        "de": "Keine Daten für Top-5 Produkte pro Jahr.",
        "en": "No data for Top‑5 products per year."
    },

    # Insights
    "insights_title": {
        "de": "🧠 Automatische Insights",
        "en": "🧠 Automatic insights"
    },
    "insight_top_country": {
        "de": "• **{land}** ist aktuell das wichtigste Lieferland mit **{share:.1f}%** Anteil am Importwert.",
        "en": "• **{land}** is currently the most important supplier with **{share:.1f}%** of total import value."
    },
    "insight_top_product": {
        "de": "• Das Produkt **{prod}** dominiert die Importe mit **{share:.1f}%** Anteil.",
        "en": "• The product **{prod}** dominates imports with **{share:.1f}%** share."
    },
    "insight_dependency_high": {
        "de": "• ⚠️ Die Importabhängigkeit von einem einzelnen Land ist **kritisch hoch** (über 50%).",
        "en": "• ⚠️ Import dependency on a single country is **critically high** (over 50%)."
    },
    "insight_trend_up": {
        "de": "• Die Importe steigen aktuell um **{pct:.1f}%** gegenüber dem Vorjahr.",
        "en": "• Imports are currently increasing by **{pct:.1f}%** compared to last year."
    },
    "insight_trend_down": {
        "de": "• Die Importe sinken aktuell um **{pct:.1f}%** gegenüber dem Vorjahr.",
        "en": "• Imports are currently decreasing by **{pct:.1f}%** compared to last year."
    },
    "no_insights": {
        "de": "Keine aussagekräftigen Insights für die aktuelle Filterauswahl.",
        "en": "No meaningful insights for the current filter selection."
    },
    "summary_overview_title": {
    "de": "📘 Gesamtübersicht",
    "en": "📘 Overview"
},

"summary_no_data": {
    "de": "Für die ausgewählten Filter liegen keine Daten vor.",
    "en": "No data available for the selected filters."
},

"summary_hhi_label": {
    "de": "Gesamt-HHI",
    "en": "Overall HHI"
},

"summary_hhi_help": {
    "de": "Der Herfindahl-Hirschman-Index misst die Konzentration der Lieferländer. Höhere Werte bedeuten stärkere Abhängigkeit.",
    "en": "The Herfindahl-Hirschman Index measures supplier concentration. Higher values indicate stronger dependence."
},

"summary_diversity_label": {
    "de": "Diversität",
    "en": "Diversity"
},

"summary_diversity_help": {
    "de": "1 - HHI. Höhere Werte bedeuten diversifiziertere Lieferketten.",
    "en": "1 - HHI. Higher values indicate more diversified supply chains."
},

"summary_countries_label": {
    "de": "Anzahl Länder",
    "en": "Number of Countries"
},

"summary_countries_help": {
    "de": "Wie viele Lieferländer in den gefilterten Daten enthalten sind.",
    "en": "How many supplier countries are included in the filtered data."
},

"summary_products_label": {
    "de": "Anzahl Produkte",
    "en": "Number of Products"
},

"summary_products_help": {
    "de": "Wie viele Produkte aktuell ausgewählt wurden.",
    "en": "How many products are currently selected."
},

"risk_low": {
    "de": "Niedrig",
    "en": "Low"
},

"risk_medium": {
    "de": "Mittel",
    "en": "Medium"
},

"risk_high": {
    "de": "Hoch",
    "en": "High"
},

"summary_risk_title": {
    "de": "Risiko-Einstufung",
    "en": "Risk Classification"
},

"summary_interpretation_title": {
    "de": "Interpretation",
    "en": "Interpretation"
},

"summary_interpretation": {
    "de": "Der Gesamt-HHI beträgt {hhi}. Dies entspricht einer Diversität von {diversity}. Die Analyse basiert auf {countries} Ländern und {products} ausgewählten Produkten. Ein höherer HHI weist auf eine stärkere Abhängigkeit von wenigen Lieferländern hin.",
    "en": "The overall HHI is {hhi}, corresponding to a diversity of {diversity}. The analysis is based on {countries} countries and {products} selected products. A higher HHI indicates stronger dependence on a small number of supplier countries."
},
"summary_interpretation_dual": {
    "de": "Der Gesamt-HHI beträgt {hhi_total} und wird als {risk_total} eingestuft. "
          "Der durchschnittliche Produkt-HHI liegt bei {hhi_avg} und wird als {risk_avg} bewertet. "
          "Während der Gesamt-HHI die Abhängigkeit über alle Produkte hinweg misst, zeigt der Produkt-HHI, "
          "wie konzentriert die Lieferkette einzelner Rohstoffe ist.",
    "en": "The total HHI is {hhi_total}, classified as {risk_total}. "
          "The average product HHI is {hhi_avg}, classified as {risk_avg}. "
          "While the total HHI measures dependence across all products, the product-level HHI shows "
          "how concentrated the supply chain is for individual raw materials."
},
"presentation_start_title": {
    "de": "🎓 Abschlussprojekt Präsentation",
    "en": "🎓 Final Project Presentation"
},

"presentation_start_subtitle": {
    "de": "Kritische Rohstoffe – Deutschland",
    "en": "Critical Raw Materials – Germany"
},

"presentation_start_description": {
    "de": "Eine interaktive Präsentation über Abhängigkeiten, Risiken und strategische Handlungsmöglichkeiten.",
    "en": "An interactive presentation about dependencies, risks, and strategic actions."
},

"presentation_start_button": {
    "de": "▶️ Präsentation starten",
    "en": "▶️ Begin Presentation"
},
"pres_analysis_title": {
    "de": "📘 Analyse – Präsentation",
    "en": "📘 Analysis – Presentation"
},
"presentation_start_title": {
    "de": "🎓 Abschlussprojekt Präsentation",
    "en": "🎓 Final Project Presentation"
},

"presentation_start_subtitle": {
    "de": "Critical Raw Materials – Deutschland",
    "en": "Critical Raw Materials – Germany"
},

"presentation_start_description": {
    "de": "Eine interaktive Präsentation über Abhängigkeiten, Risiken und strategische Handlungsmöglichkeiten.",
    "en": "An interactive presentation about dependencies, risks, and strategic actions."
},

"presentation_start_button": {
    "de": "▶️ Präsentation starten",
    "en": "▶️ Begin Presentation"
},

"pres_analysis_title": {
    "de": "📘 Analyse – Präsentation",
    "en": "📘 Analysis – Presentation"
},

"pres_risk_title": {
    "de": "📕 Risikoanalyse – Präsentation",
    "en": "📕 Risk Analysis – Presentation"
},

"pres_summary_title": {
    "de": "📗 Summary – Präsentation",
    "en": "📗 Summary – Presentation"
},

"pres_next_risk": {
    "de": "➡️ Weiter zur Risikoanalyse",
    "en": "➡️ Continue to Risk Analysis"
},

"pres_next_summary": {
    "de": "➡️ Weiter zur Summary",
    "en": "➡️ Continue to Summary"
},

"pres_end": {
    "de": "🏁 Präsentation beenden",
    "en": "🏁 End Presentation"
},

"pres_1_intro": {
    "de": "Herzlich willkommen in unserem Abschlussprojekt. In diesem analysieren wir die deutschen Importe kritischer Rohstoffe, die für die Herstellung von E‑Batterien unverzichtbar sind. Wir zeigen, wie Deutschland von einzelnen Ländern abhängig ist und welche Risiken daraus entstehen.",
    "en": "Welcome to our final project. In this presentation, we analyze Germany’s imports of critical raw materials essential for battery production. We show how dependent Germany is on individual countries and what risks arise from this."
},

"pres_2_motivation": {
    "de": "Die Nachfrage nach Batterierohstoffen steigt stark. Gleichzeitig sind viele dieser Rohstoffe hoch konzentriert — oft auf nur ein oder zwei Länder. Das macht die Lieferketten verwundbar. Rohstoffe wie Lithium, Nickel, Kobalt oder Graphit sind nicht einfach ersetzbar. Wenn es hier zu einem Engpass kommt:\n• Batteriefabriken können nicht produzieren\n• Autohersteller müssen die Produktion stoppen\n• Preise für E‑Autos steigen\n• Lieferzeiten verlängern sich\n• Europa verliert Wettbewerbsfähigkeit\n• politische Abhängigkeiten werden sichtbar",
    "en": "Demand for battery raw materials is rising sharply. At the same time, many of these materials are highly concentrated — often in just one or two countries. This makes supply chains vulnerable. Materials like lithium, nickel, cobalt or graphite cannot easily be substituted. If a shortage occurs:\n• Battery factories cannot produce\n• Car manufacturers must stop production\n• Prices for electric cars rise\n• Delivery times increase\n• Europe loses competitiveness\n• political dependencies become visible"
},

"pres_3_goal": {
    "de": "Unser Ziel war es, diese Abhängigkeiten transparent zu machen und Risiken sichtbar zu machen — in einem interaktiven Dashboard, das Politik und Industrie als Entscheidungsgrundlage nutzen können. Es soll Entscheidungsträgern helfen, Risiken frühzeitig zu erkennen und strategisch zu handeln.",
    "en": "Our goal was to make these dependencies transparent and highlight risks — in an interactive dashboard that policymakers and industry can use for decision‑making. It helps decision‑makers identify risks early and act strategically."
},

"pres_4_data": {
    "de": "Die Daten haben wir von der UN‑Comtrade‑Seite extrahiert, als CSV heruntergeladen, in Power BI transformiert und in einem Star‑Schema in PostgreSQL gespeichert. Mit einer ETL‑Pipeline haben wir die Daten bereinigt und harmonisiert. Das Dashboard wurde mit Streamlit umgesetzt.",
    "en": "We extracted the data from the UN Comtrade website, downloaded it as CSV, transformed it in Power BI, and stored it in a star schema in PostgreSQL. Using an ETL pipeline, we cleaned and harmonized the data. The dashboard was implemented with Streamlit."
},

"pres_5_overview": {
    "de": "Das Projekt besteht aus drei Dashboards: Analyse, Risikoanalyse und Summary. Damit lassen sich sowohl Details als auch strategische Muster erkennen.",
    "en": "The project consists of three dashboards: Analysis, Risk Analysis, and Summary. This allows both detailed and strategic patterns to be identified."
},

"pres_6_kpis": {
    "de": "Die KPIs zeigen sofort die wichtigsten Größen: Gesamtwert, Gesamtgewicht und Preis pro kg. Der Preis pro kg ist ein Frühindikator für Marktverknappungen.",
    "en": "The KPIs immediately show the most important metrics: total value, total weight, and price per kg. The price per kg is an early indicator of market shortages."
},

"pres_7_countries": {
    "de": "Hier sehen wir, welche Länder und Produkte dominieren. Diese Informationen sind entscheidend, um Prioritäten zu setzen.",
    "en": "Here we see which countries and products dominate. This information is crucial for setting priorities."
},

"pres_8_heatmap": {
    "de": "Die Heatmap zeigt, welche Kombinationen aus Produkt und Land besonders kritisch sind. Hohe Werte bedeuten hohe Abhängigkeit.",
    "en": "The heatmap shows which combinations of product and country are particularly critical. High values indicate high dependency."
},

"pres_9_hhi": {
    "de": "Der HHI‑Index misst die Konzentration der Lieferländer. Ein hoher Wert bedeutet: wenige Länder dominieren — ein Risiko.",
    "en": "The HHI index measures the concentration of supplier countries. A high value means that few countries dominate — a risk."
},

"pres_10_summary": {
    "de": "Das Summary‑Dashboard fasst alles zusammen: Top‑5 Länder je Produkt, Top‑5 Produkte je Jahr und automatische Insights.",
    "en": "The summary dashboard brings everything together: Top‑5 countries per product, Top‑5 products per year, and automatic insights."
},

"pres_11_batteries": {
    "de": "Diese Rohstoffe sind zentrale Bestandteile moderner Lithium‑Ionen‑Batterien. Jede Veränderung in der Versorgung hat direkte Auswirkungen auf die Energiewende. Ohne Lithium, Nickel, Kobalt und Graphit gibt es keine Batterien — und ohne Batterien keine E‑Mobilität.",
    "en": "These raw materials are essential components of modern lithium‑ion batteries. Any change in supply has direct effects on the energy transition. Without lithium, nickel, cobalt and graphite, there are no batteries — and without batteries, no e‑mobility."
},

"pres_12_industry": {
    "de": "Lieferengpässe führen zu steigenden Preisen, Produktionsverzögerungen und geringerer Planungssicherheit — besonders für Automobilhersteller. Das betrifft nicht nur Automobilhersteller, sondern die gesamte Wertschöpfungskette.",
    "en": "Supply shortages lead to rising prices, production delays, and reduced planning certainty — especially for car manufacturers. This affects not only car manufacturers but the entire value chain."
},

"pres_13_policy": {
    "de": "Die EU reagiert mit dem kritischen Rohstoffen Act. Unser Dashboard liefert genau die Daten, die für solche Entscheidungen notwendig sind.",
    "en": "The EU is responding with the Critical Raw Materials Act. My dashboard provides exactly the data needed for such decisions."
},

"pres_14_recommendations": {
    "de": "Die wichtigsten Maßnahmen sind:\n1. Diversifizierung der Lieferländer\n2. Aufbau strategischer Partnerschaften\n3. Investitionen in Recycling\n4. Kontinuierliches Monitoring",
    "en": "The most important measures are:\n1. Diversification of supplier countries\n2. Building strategic partnerships\n3. Investing in recycling\n4. Continuous monitoring"
},

"pres_15_conclusion": {
    "de": "Unser Dashboard schafft Transparenz, identifiziert Risiken und liefert eine datenbasierte Grundlage für strategische Entscheidungen. Es verbindet technische Umsetzung mit wirtschaftlicher und geopolitischer Relevanz.",
    "en": "Our dashboard creates transparency, identifies risks, and provides a data‑driven foundation for strategic decisions. It combines technical implementation with economic and geopolitical relevance."
},

"section_intro": {"de": "Einführung", "en": "Introduction"},
"section_motivation": {"de": "Motivation", "en": "Motivation"},
"section_goal": {"de": "Zielsetzung", "en": "Objective"},
"section_data": {"de": "Datenbasis", "en": "Data Basis"},
"section_overview": {"de": "Dashboard Übersicht", "en": "Dashboard Overview"},
"section_kpis": {"de": "KPIs", "en": "KPIs"},
"section_countries": {"de": "Länder & Produkte", "en": "Countries & Products"},
"section_heatmap": {"de": "Risiko Heatmap", "en": "Risk Heatmap"},
"section_hhi": {"de": "HHI Index", "en": "HHI Index"},
"section_batteries": {"de": "Bedeutung für E‑Batterien", "en": "Importance for E‑Batteries"},
"section_industry": {"de": "Industrieauswirkungen", "en": "Industry Impact"},
"section_summary": {"de": "Summary Dashboard", "en": "Summary Dashboard"},
"section_policy": {"de": "Politik", "en": "Policy"},
"section_recommendations": {"de": "Empfehlungen", "en": "Recommendations"},
"section_conclusion": {"de": "Fazit", "en": "Conclusion"},

"pres_9_hhi": {
    "de": "Der Herfindahl‑Hirschman‑Index (HHI) misst die Konzentration der Lieferländer. Die EU verwendet folgende Schwellenwerte:\n\n• HHI < 0,30 → geringe Konzentration\n• 0,30 ≤ HHI < 0,50 → mittlere Konzentration\n• HHI ≥ 0,50 → hohe Konzentration\n\n**Formel des Gesamt‑HHI:**\n\n$$ HHI = \\sum_{i=1}^{n} s_i^2 $$\n\nwobei:\n- \\( s_i \\) = Importanteil des Landes i\n- \\( n \\) = Anzahl der Lieferländer\n\n**Beispiel:**\nEin Land liefert 70% und zwei weitere je 15%:\n\n$$ HHI = 0.7^2 + 0.15^2 + 0.15^2 = 0.535 $$\n\n→ nach EU‑Logik ein kritisch hoher Wert.\n\n**Diversitätsindex (Gegenteil von HHI):**\n\n$$ Diversität = 1 - HHI $$\n\nBeispiel:\n\n$$ Diversität = 1 - 0.535 = 0.465 $$\n\n→ geringe Diversität bedeutet hohe Abhängigkeit.",
    
    "en": "The Herfindahl‑Hirschman Index (HHI) measures the concentration of supplier countries. The EU uses the following thresholds:\n\n• HHI < 0.30 → low concentration\n• 0.30 ≤ HHI < 0.50 → medium concentration\n• HHI ≥ 0.50 → high concentration\n\n**Formula of total HHI:**\n\n$$ HHI = \\sum_{i=1}^{n} s_i^2 $$\n\nwhere:\n- \\( s_i \\) = import share of country i\n- \\( n \\) = number of supplier countries\n\n**Example:**\nOne country supplies 70% and two others 15% each:\n\n$$ HHI = 0.7^2 + 0.15^2 + 0.15^2 = 0.535 $$\n\n→ critically high under EU logic.\n\n**Diversity index (inverse of HHI):**\n\n$$ Diversity = 1 - HHI $$\n\nExample:\n\n$$ Diversity = 1 - 0.535 = 0.465 $$\n\n→ low diversity means high dependency."
},

"footer_project_info": {
    "de": "🎓 Abschlussprojekt von Alex & Amedee - 🏛️ DSI Berlin - 🗓️ 06.02.2026",
    "en": "🎓 Final project by Alex & Amedee - 🏛️ DSI Berlin - 🗓️ 06 Feb 2026"
}
}