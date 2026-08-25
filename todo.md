# web2apk 300% Upgrade Plan

## 1. Project Foundation & Config
- [x] Create new project structure under /workspace/web2apk
- [x] Upgrade capacitor.config.json (plugins, server, logging, colorScheme)
- [x] Upgrade package.json (new deps, scripts, metadata, engines)
- [x] Create .nvmrc, .gitignore (comprehensive), .editorconfig
- [x] Add LICENSE (MIT), CONTRIBUTING.md, CODE_OF_CONDUCT.md
- [x] Add CHANGELOG.md (semantic versioning)

## 2. Web Layer — Rich PWA + Offline + UI
- [x] Build full PWA index.html with manifest, theme, meta tags
- [x] Add manifest.json (icons, theme, shortcuts, display)
- [x] Add service worker for offline caching
- [x] Add robots.txt, humans.txt, browserconfig.xml
- [x] Add assets/ (favicon set, og image)
- [x] Add styles.css, app.js (navigation, pull-to-refresh, status bar handling)
- [x] Add offline.html fallback page

## 3. Capacitor Plugins Integration
- [x] Add @capacitor/status-bar, splash-screen, haptics, app, keyboard, preferences, network, geolocation, camera, file-system, share, push-notifications, local-notifications, device, browser, toast, clipboard, share deps
- [x] Configure all plugins in capacitor.config.json
- [x] Update capacitor.settings.gradle and iOS packageClassList

## 4. Android Native Upgrades
- [x] Upgrade AndroidManifest (permissions, fileprovider, intent filters for deep links, backup rules, network security config)
- [x] Add network_security_config.xml for cleartext optional
- [x] Add backup_rules.xml + data_extraction_rules.xml
- [x] Upgrade MainActivity.java (plugin registration, lifecycle)
- [x] Upgrade build.gradle (versioning, flavors, signing config template, R8, bundle support)
- [x] Upgrade variables.gradle, gradle.properties (perf flags, AndroidX)
- [x] Upgrade proguard-rules.pro (real keep rules for WebView/JS)
- [x] Upgrade strings.xml, styles.xml, colors.xml, themes
- [x] Add proper splash + icon adaptive XML
- [x] Add res/xml file_paths, config

## 5. iOS Native Upgrades
- [x] Upgrade Info.plist (permissions usage strings, orientation, ATS, URL schemes, status bar, launch screen)
- [x] Upgrade AppDelegate.swift (plugin registration, push, deep links)
- [x] Upgrade SceneDelegate.swift (deep link handling)
- [x] Add capacitor.config.json (ios) with packageClassList
- [x] Add Podfile for plugins

## 6. GitHub Actions CI/CD — Multi-Workflow
- [x] build.yml — matrix Android debug+release+bundle, iOS sim
- [x] release.yml — tagged releases, signed APK/AAB, GitHub Releases
- [x] lint.yml — code quality, markdown lint, JSON validate
- [x] dependabot.yml — automated dependency updates
- [x] Add signing via secrets (keystore decode)
- [x] Add caching for gradle + npm
- [x] Add permissions hardening (contents: read)

## 7. Documentation 300%
- [x] Comprehensive README.md (features, quickstart, config, plugins, CI, signing, publishing Play Store + App Store, troubleshooting, FAQ)
- [x] CONFIGURATION.md (every config option documented)
- [x] PUBLISHING.md (store publishing guides)
- [x] PLUGINS.md (all plugins + usage examples)
- [x] ARCHITECTURE.md (how it works)
- [x] TROUBLESHOOTING.md
- [x] docs/ folder with diagrams

## 8. Scripts & Tooling
- [x] scripts/ — setup.sh, build-android.sh, build-ios.sh, generate-icons.sh, version-bump.mjs, release.sh, validate-config.mjs
- [x] Make targets via Makefile
- [x] .vscode/ settings + tasks + extensions
- [x] ESLint + Prettier + markdownlint config for web assets

## 9. App Icon & Splash Assets
- [x] Generate icon source + splash source via image tool
- [x] Provide @capacitor/assets source images (resources/)
- [x] Verify all generated assets exist and are valid (apple-touch-icon added, all mipmaps/splashes/iOS assets verified)

## 10. Quality Gates & Tests
- [x] Add JSON schema validation for config (validate-config.mjs created + passing)
- [x] Add markdown lint config (.markdownlint.jsonc created)
- [x] Run validate-config.mjs — 0 errors, 2 expected warnings
- [x] Run JSON/YAML/XML syntax checks on all config files — all pass
- [x] Verify JS syntax (app.js, version-bump.mjs, validate-config.mjs — all OK)
- [x] Fix index.html (removed stale capacitor.js + external script refs, fixed apple-touch-icon)

## 11. Final Packaging
- [x] Zip the upgraded project (web2apk-upgraded.zip, 7.5MB)
- [x] Verify structure with tree (15 dirs, 146 files)
- [x] Run full validation suite (config/JSON/YAML/XML/JS/shell/Makefile — all pass)
- [x] Deliver
