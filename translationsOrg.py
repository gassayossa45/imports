# translations.py

translations = {
    # Beispiel-Einträge
    "error_user_exists": {
        "de": "Benutzername oder E-Mail existiert bereits.",
        "en": "Username or email already exists."
    },
        "login_title": {"de": "🔐 Login", "en": "🔐 Login"},
        "username": {"de": "Benutzername", "en": "Username"},
        "password": {"de": "Passwort", "en": "Password"},
        "login_button": {"de": "Login", "en": "Login"},
        "login_success": {"de": "Login erfolgreich!", "en": "Login successful!"},
        "login_error": {"de": "Benutzername oder Passwort falsch.", "en": "Incorrect username or password."},
        "nav_header": {"de": "Navigation", "en": "Navigation"},
        "logged_in_as": {"de": "Angemeldet als", "en": "Logged in as"},
        "logout": {"de": "🚪 Logout", "en": "🚪 Logout"}



}

translations.update({
    "register_title": {"de": "📝 Registrierung", "en": "📝 Registration"},
    "username": {"de": "Benutzername", "en": "Username"},
    "email": {"de": "E-Mail", "en": "Email"},
    "password": {"de": "Passwort", "en": "Password"},
    "register_button": {"de": "Registrieren", "en": "Register"},
    "register_success": {
        "de": "Registrierung erfolgreich! Du kannst dich jetzt einloggen.",
        "en": "Registration successful! You can now log in."
    },
    "register_error": {
        "de": "Fehler: Benutzername oder E-Mail existiert bereits.",
        "en": "Error: Username or email already exists."
    }
})

translations.update({

    # Zugriffsschutz
    "login_required": {
        "de": "Bitte zuerst einloggen.",
        "en": "Please log in first."
    },

    # Titel
    "analysis_title": {
        "de": "📊 Analyse deutscher– Importe kritischer Rohstoffe",
        "en": "📊 Analysis of German Imports of Critical Raw Materials"
    },

    # Filter
    "filter_header": {"de": "Filter", "en": "Filters"},
    "filter_years": {"de": "Jahre auswählen", "en": "Select years"},
    "filter_countries": {"de": "Länder auswählen", "en": "Select countries"},
    "filter_products": {"de": "Produkte auswählen", "en": "Select products"},
    "all_option": {"de": "Alle", "en": "All"},

    # KPIs
    "kpi_total_value": {"de": "Gesamtwert (USD)", "en": "Total value (USD)"},
    "kpi_total_weight": {"de": "Gesamtgewicht (kg)", "en": "Total weight (kg)"},
    "kpi_avg_price": {"de": "Ø Preis (USD)", "en": "Avg. price (USD)"},
    "kpi_price_per_kg": {"de": "Preis pro kg (USD/kg)", "en": "Price per kg (USD/kg)"},

    # Charts
    "chart_value_by_country": {"de": "Importwert nach Ländern", "en": "Import value by country"},
    "chart_value_by_product": {"de": "Importwert nach Produkten", "en": "Import value by product"},
    "no_data": {"de": "Keine Daten für die aktuelle Filterauswahl.", "en": "No data for the current filter selection."},

    "chart_value_per_year": {"de": "Zeitreihe: Importwert pro Jahr", "en": "Time series: import value per year"},
    "chart_ppk_per_year": {"de": "Zeitreihe: Preis pro kg über die Jahre", "en": "Time series: price per kg over the years"},

    "chart_yoy": {"de": "📉 Year-over-Year Veränderung (Importwert)", "en": "📉 Year-over-Year change (import value)"},

    # Risiko-Karte
    "risk_map_title": {
        "de": "🌍 Geografische Risiko-Karte: Importabhängigkeit",
        "en": "🌍 Geographic risk map: import dependency"
    },
    "dependency": {"de": "Abhängigkeit", "en": "Dependency"},

    # CSV
    "download_title": {"de": "📥 Daten herunterladen", "en": "📥 Download data"},
    "download_csv": {"de": "CSV herunterladen", "en": "Download CSV"},

    # Tabelle
    "detail_table": {"de": "Detailtabelle", "en": "Detailed table"},

    # Sidebar
    "nav_header": {"de": "Navigation", "en": "Navigation"},
    "logged_in_as": {"de": "Angemeldet als", "en": "Logged in as"},
    "logout": {"de": "🚪 Logout", "en": "🚪 Logout"}
})

translations.update({

    # Zugriffsschutz
    "login_required": {
        "de": "Bitte zuerst einloggen.",
        "en": "Please log in first."
    },

    # Titel
    "risk_title": {
        "de": "⚠️ Risikoanalyse kritischer Rohstoffe",
        "en": "⚠️ Risk analysis of critical raw materials"
    },

    # Filter
    "filter_header": {"de": "Filter", "en": "Filters"},
    "filter_years": {"de": "Jahre auswählen", "en": "Select years"},
    "filter_countries": {"de": "Länder auswählen", "en": "Select countries"},
    "filter_products": {"de": "Produkte auswählen", "en": "Select products"},
    "all_option": {"de": "Alle", "en": "All"},

    # Risiko-Heatmap
    "risk_heatmap": {
        "de": "🔥 Risiko-Heatmap: Importabhängigkeit",
        "en": "🔥 Risk heatmap: import dependency"
    },
    "no_data": {
        "de": "Keine Daten für die aktuelle Filterauswahl.",
        "en": "No data for the current filter selection."
    },

    # HHI
    "hhi_title": {
        "de": "📉 HHI-Konzentrationsindex (Lieferländer)",
        "en": "📉 HHI concentration index (supplier countries)"
    },
    "no_hhi": {
        "de": "Keine Daten für HHI-Berechnung.",
        "en": "No data available for HHI calculation."
    },

    # China Exposure
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

    # HHI-Trend
    "hhi_trend_title": {
        "de": "📈 Risiko-Trend: HHI über die Jahre",
        "en": "📈 Risk trend: HHI over the years"
    },

    # Tabelle
    "detail_table": {"de": "Detailtabelle", "en": "Detailed table"},

    # Sidebar
    "nav_header": {"de": "Navigation", "en": "Navigation"},
    "logged_in_as": {"de": "Angemeldet als", "en": "Logged in as"},
    "logout": {"de": "🚪 Logout", "en": "🚪 Logout"}
})
translations.update({

    # Zugriffsschutz
    "login_required": {
        "de": "Bitte zuerst einloggen.",
        "en": "Please log in first."
    },

    # Titel
    "summary_title": {
        "de": "📘 Summary – Top 5 & Insights",
        "en": "📘 Summary – Top 5 & Insights"
    },

    # Filter
    "filter_header": {"de": "Filter", "en": "Filters"},
    "filter_years": {"de": "Jahre auswählen", "en": "Select years"},
    "filter_products": {"de": "Produkte auswählen", "en": "Select products"},
    "filter_countries": {"de": "Länder auswählen", "en": "Select countries"},
    "all_option": {"de": "Alle", "en": "All"},

    # Top 5 Länder
    "top5_countries_title": {
        "de": "🌍 Top 5 Länder je Produkt",
        "en": "🌍 Top 5 countries per product"
    },
    "no_top5_countries": {
        "de": "Keine Daten für Top-5 Länder je Produkt.",
        "en": "No data for Top‑5 countries per product."
    },

    # Top 5 Produkte
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

    # Tabelle
    "detail_table": {"de": "Detailtabelle", "en": "Detailed table"},

    # Sidebar
    "nav_header": {"de": "Navigation", "en": "Navigation"},
    "logged_in_as": {"de": "Angemeldet als", "en": "Logged in as"},
    "logout": {"de": "🚪 Logout", "en": "🚪 Logout"}
})
translations.update({

    # Zugriffsschutz
    "login_or_register_required": {
        "de": "Bitte zuerst registrieren oder einloggen.",
        "en": "Please register or log in first."
    },

    # Titel
    "home_title": {
        "de": "🌍 Critical Raw Materials – Import & Risiko Dashboard",
        "en": "🌍 Critical Raw Materials – Import & Risk Dashboard"
    },

    # Willkommenstext
    "home_intro": {
        "de": "Willkommen zu meinem Dashboard-Projekt über **kritische Rohstoffe**.",
        "en": "Welcome to my dashboard project on **critical raw materials**."
    },

    "home_description": {
        "de": "Dieses Multi-Page-Dashboard besteht aus:",
        "en": "This multi-page dashboard consists of:"
    },

    "home_point_analysis": {
        "de": "1. **Analyse** – Deskriptive Analyse der Importe (Werte, Mengen, Preis pro kg, Zeitreihen, Heatmap).",
        "en": "1. **Analysis** – Descriptive analysis of imports (values, quantities, price per kg, time series, heatmap)."
    },

    "home_point_risk": {
        "de": "2. **Risikoanalyse** – Konzentrationsrisiken, Abhängigkeiten, China-Exposure, HHI-Trends.",
        "en": "2. **Risk analysis** – Concentration risks, dependencies, China exposure, HHI trends."
    },

    "home_point_summary": {
        "de": "3. **Summary** – Top-5 Länder je Produkt, Top-5 Produkte je Jahr, automatische Insights.",
        "en": "3. **Summary** – Top‑5 countries per product, Top‑5 products per year, automatic insights."
    },

    "home_data_basis": {
        "de": "Die Daten basieren auf einem **Star-Schema** in PostgreSQL mit:",
        "en": "The data is based on a **star schema** in PostgreSQL with:"
    },

    "home_data_tables": {
        "de": "- `dim_years`, `dim_countries`, `dim_products`\n- `fact_imports` (Mengen, Gewichte, Werte)",
        "en": "- `dim_years`, `dim_countries`, `dim_products`\n- `fact_imports` (quantities, weights, values)"
    },

    "home_sidebar_hint": {
        "de": "Nutzen Sie die Seitenleiste links, um zwischen den Dashboards zu wechseln.",
        "en": "Use the sidebar on the left to navigate between dashboards."
    }
})