from django_assets import Bundle, register

AVALAIBLE_BUNDLES = {
    'app_css': Bundle(
        'css/app.css',
        filters='yui_css',
        output='css/app.min.css'
    ),
    'ie_js': Bundle(
        "js/respond.src.js",
        filters='yui_js',
        output='js/respond.min.js'
    ),
    'modernizr_js': Bundle(
        "js/foundation5/vendor/custom.modernizr.js",
        filters='yui_js',
        output='js/modernizr.min.js'
    ),
    'app_js': Bundle(
        "js/foundation5/vendor/jquery.js",
        "js/foundation5/vendor/jquery.cookie.js",
        "js/foundation5/foundation/foundation.js",
        "js/foundation5/foundation/foundation.abide.js",
        "js/foundation5/foundation/foundation.accordion.js",
        "js/foundation5/foundation/foundation.alert.js",
        "js/foundation5/foundation/foundation.clearing.js",
        "js/foundation5/foundation/foundation.dropdown.js",
        "js/foundation5/foundation/foundation.interchange.js",
        "js/foundation5/foundation/foundation.joyride.js",
        "js/foundation5/foundation/foundation.magellan.js",
        "js/foundation5/foundation/foundation.offcanvas.js",
        "js/foundation5/foundation/foundation.orbit.js",
        "js/foundation5/foundation/foundation.reveal.js",
        "js/foundation5/foundation/foundation.tab.js",
        "js/foundation5/foundation/foundation.tooltip.js",
        "js/foundation5/foundation/foundation.topbar.js",
        "js/app.js",
        filters='yui_js',
        output='js/app.min.js'
    ),
}

ENABLED_BUNDLES = [
    'app_css',
    'modernizr_js',
    'app_js',
    #'ie_js',
]

for item in ENABLED_BUNDLES:
    register(item, AVALAIBLE_BUNDLES[item])
