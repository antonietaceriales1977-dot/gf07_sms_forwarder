[app]
title = GF07 Tracker
package.name = gf07tracker
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py

# Force SDK/NDK versions to match GitHub Actions
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_path = $ANDROIDNDK
android.sdk_path = $ANDROIDSDK
