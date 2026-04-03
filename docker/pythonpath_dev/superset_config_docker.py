# -*- coding: utf-8 -*-
"""
Кастомная конфигурация проекта «Цифровой двойник нефти».

Этот файл автоматически импортируется из superset_config.py
(через механизм superset_config_docker). Здесь задаются:
  - название продукта и брендинг
  - доступные языки и язык по умолчанию
  - favicon и логотипы
  - настройки темы оформления
"""

# ---------------------------------------------------------------
# Брендинг
# ---------------------------------------------------------------
APP_NAME = "Цифровой двойник нефти"

# Горизонтальный логотип для навбара
APP_ICON = "/static/assets/images/custom-logo.png"

# Favicon (иконка вкладки браузера)
FAVICONS = [{"href": "/static/assets/images/favicon.png"}]

# Подпись справа от логотипа (пусто — не показываем)
LOGO_RIGHT_TEXT = ""

# Тултип при наведении на логотип
LOGO_TOOLTIP = "Цифровой двойник нефти"

# Куда ведёт клик по логотипу
LOGO_TARGET_PATH = None

# ---------------------------------------------------------------
# Локализация — только русский, английский, китайский
# ---------------------------------------------------------------
BABEL_DEFAULT_LOCALE = "ru"

LANGUAGES = {
    "ru": {"flag": "ru", "name": "Русский"},
    "en": {"flag": "us", "name": "English"},
    "zh": {"flag": "cn", "name": "中文"},
}

# ---------------------------------------------------------------
# Тема оформления — переопределяем токены брендинга
# ---------------------------------------------------------------
THEME_DEFAULT = {
    "token": {
        # Брендинг
        "brandAppName": APP_NAME,
        "brandLogoUrl": APP_ICON,
        "brandLogoAlt": "Цифровой двойник нефти",
        "brandLogoHref": "/",
        "brandLogoHeight": "28px",
        "brandLogoMargin": "14px 0",
        # Спиннер
        "brandSpinnerUrl": None,
        "brandSpinnerSvg": None,
        # Цвета (фирменные: зелёный и красный Татнефти)
        "colorPrimary": "#00914C",
        "colorLink": "#00914C",
        "colorError": "#e04355",
        "colorWarning": "#fcc700",
        "colorSuccess": "#5ac189",
        "colorInfo": "#66bcfe",
        # Шрифты
        "fontUrls": [],
        "fontFamily": "Inter, Helvetica, Arial, sans-serif",
        "fontFamilyCode": "'IBM Plex Mono', 'Courier New', monospace",
        # Дополнительные токены
        "transitionTiming": 0.3,
        "brandIconMaxWidth": 37,
        "fontSizeXS": "8",
        "fontSizeXXL": "28",
        "fontWeightNormal": "400",
        "fontWeightLight": "300",
        "fontWeightStrong": "500",
        "fontWeightBold": "700",
        "colorEditorSelection": "#fff5cf",
    },
    "algorithm": "default",
}

THEME_DARK = {
    **THEME_DEFAULT,
    "token": {
        **THEME_DEFAULT["token"],
        "colorEditorSelection": "#5c4d1a",
    },
    "algorithm": "dark",
}
