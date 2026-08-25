<div align="center">

# 🚀 web2apk — turn any website into a polished, installable mobile app

**Android (APK/AAB) + iOS, Capacitor-powered, GitHub-Actions-built, plugin-rich, PWA-ready, offline-capable.**

<img width="120" height="120" src="www/assets/icon-512.png" alt="web2apk logo" />

[![Build Mobile Apps](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/build.yml/badge.svg)](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/build.yml)
[![Lint](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/lint.yml/badge.svg)](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/lint.yml)
[![Release](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/release.yml/badge.svg)](https://github.com/FED-OS/Build-Mobile-Apps-Android-iOS/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%E2%89%A522-339933.svg)](https://nodejs.org)

<a href='https://ko-fi.com/fedpromptly' target='_blank'>
  <img height='36' style='border:0px;height:36px;' src='https://ko-fi.com/img/githubbutton_sm.svg' border='0' alt='Buy Me a Coffee at ko-fi.com' />
</a>

</div>

---

This repo wraps a website in a native Android **and** iOS shell using
[Capacitor](https://capacitorjs.com) and builds it automatically with
GitHub Actions — **no local Android Studio or Xcode required**. Every push
to `main` produces per-architecture Android APKs, a release AAB (Play Store
bundle), and an iOS Simulator build, all as downloadable artifacts.

> **What's new in v2.0?** This is a ground-up upgrade: 18 Capacitor plugins,
> a full PWA + offline service worker, hardened Android/iOS native configs,
> signed release builds, a multi-workflow CI/CD pipeline, Dependabot, a
> one-command setup, and comprehensive docs. See the
> [Changelog](CHANGELOG.md) for the full breakdown.

---

## ✨ Features

- **Cross-platform** — one codebase ships to Android (APK + AAB) and iOS.
- **Two modes** — load a live website via `server.url`, **or** bundle static
  files for full offline use.
- **PWA-ready** — manifest, theme color, maskable icons, and a service worker
  with an offline fallback page, all included out of the box.
- **18 Capacitor plugins** pre-wired — status bar, splash screen, haptics,
  app lifecycle, keyboard, network, geolocation, camera, file system, share,
  push & local notifications, device info, browser, toast, clipboard, and
  preferences. See [PLUGINS.md](PLUGINS.md).
- **Per-architecture APKs + universal** — `arm64-v8a`, `armeabi-v7a`, `x86`,
  `x86_64`, plus a `universal` APK that works everywhere.
- **Release AAB** — Play Store-ready Android App Bundle, in addition to APKs.
- **Signed release builds** — driven by GitHub Actions secrets; falls back to
  the debug key locally so it always builds out of the box.
- **Hardened native configs** — HTTPS-enforcing network security config,
  scoped backup rules, deep-link intent filters, ATS, and all required iOS
  permission usage strings.
- **Automated CI/CD** — `build.yml` (matrix build), `release.yml` (tagged
  releases → GitHub Releases), `lint.yml` (quality gates), and Dependabot.
- **One-command setup** — `make setup` or `scripts/setup.sh`.
- **Custom icons & splash** — generate native icon/splash assets from two
  source images via `@capacitor/assets`.

---

## 📦 Table of contents

1. [Quick start](#-quick-start)
2. [How it works](#-how-it-works)
3. [Configuration](#-configuration)
4. [Build locally](#-build-locally)
5. [CI/CD](#-cicd)
6. [Signing for production](#-signing-for-production-play-store)
7. [Publishing](#-publishing)
8. [App icon & splash screen](#-app-icon--splash-screen)
9. [Plugins](#-plugins)
10. [Project structure](#-project-structure)
11. [Troubleshooting](#-troubleshooting)
12. [FAQ](#-faq)
13. [Contributing](#-contributing)
14. [License](#-license)

---

## 🚀 Quick start

### Option A — load a live website (simplest)

1. **Point it at your site.** Open `capacitor.config.json` and add a
   `server.url`:

   ```json
   {
     "appId": "com.yourcompany.appname",
     "appName": "Your App",
     "webDir": "www",
     "server": {
       "url": "https://your-website.com",
       "androidScheme": "https"
     }
   }
   ```

2. **Set your identity.** Update `appId` (a unique reverse-domain id, e.g.
   `com.yourcompany.appname`) and `appName` (shown under the icon). Also
   update `android/app/src/main/res/values/strings.xml`,
   `android/app/build.gradle` (`applicationId` / `namespace`),
   `android/app/src/main/AndroidManifest.xml` (`<data android:scheme>`), and
   the iOS `Info.plist` URL scheme + bundle id. The helper script
   `scripts/setup.sh` can rename these for you.

3. **Push to GitHub.** Create a repo and push this folder. The workflow at
   `.github/workflows/build.yml` runs automatically on every push to `main`.

4. **Get your app.** Go to your repo's **Actions** tab → click the latest
   run → scroll to **Artifacts** → download `app-debug-apks` (easiest to
   install and test), `app-release-apks`, `app-release-aab`, or
   `app-ios-simulator`. Unzip, pick the APK matching your device (or the
   universal one), transfer it to your phone, and install it (allow
   "install from unknown sources" once).

### Option B — bundle static files (offline)

1. Delete the contents of `www/` and put your built website's files there
   instead (`index.html`, `css/`, `js/`, `assets/`, etc.). Make sure
   `server.url` is **not** set in `capacitor.config.json`. The app will then
   work without an internet connection — the included service worker caches
   the app shell and serves an offline fallback page when needed.

2. Follow steps 2–4 above.

> **Tip:** You can keep the bundled `www/` PWA shell as a starting point and
> just drop your own `index.html` and assets in. The service worker, manifest,
> and Capacitor bridge in `app.js` are ready to use.

---

## 🧠 How it works

For the full architecture, see [ARCHITECTURE.md](ARCHITECTURE.md). The short
version:

1. **`capacitor.config.json`** is the single source of truth — it tells
   Capacitor the `appId`, `appName`, where the web files live (`webDir`),
   and (optionally) the live `server.url` to load.
2. **`www/`** holds the web content. Either your bundled static site or the
   included PWA placeholder (ignored when `server.url` is set).
3. **`android/`** and **`ios/`** are native shell projects Capacitor
   generates. `npx cap sync` copies `www/` into them and wires up plugins.
4. **GitHub Actions** run `npm ci` → `npx cap sync` → Gradle/Xcode build →
   upload artifacts (and, for tags, publish a Release).

```
            ┌──────────────────────────────────────────────┐
            │            capacitor.config.json             │
            │   appId / appName / webDir / server.url      │
            └───────────────┬──────────────────────────────┘
                            │  npx cap sync
            ┌───────────────▼──────────────┐
            │            www/              │   (your site or bundled PWA)
            │  index.html, css, js, sw.js  │
            └───────────────┬──────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
  ┌───────────┐  Gradle assembleDebug/   ┌───────────┐  xcodebuild
  │  android/ │  assembleRelease/        │   ios/    │  (simulator)
  │  (APK/AAB)│  bundleRelease           │  (.app)   │
  └─────┬─────┘                          └─────┬─────┘
        └───────────────┬──────────────────────┘
                        ▼
              GitHub Actions artifacts
              (debug/release APKs, AAB, .app)
                        │
                        ▼ (on tag push)
                 GitHub Release
```

---

## ⚙️ Configuration

Everything is documented in [CONFIGURATION.md](CONFIGURATION.md). The key
fields in `capacitor.config.json`:

| Field | Required | Description |
|-------|----------|-------------|
| `appId` | ✅ | Unique reverse-domain id, e.g. `com.yourcompany.appname`. |
| `appName` | ✅ | Human-readable name shown under the app icon. |
| `webDir` | ✅ | Folder with your web files (default `www`). |
| `server.url` | — | Load a live website instead of bundled files. |
| `server.androidScheme` | — | `https` (default) or `http`. |
| `server.cleartext` | — | Allow HTTP traffic (not recommended). |
| `loggingBehavior` | — | `debug` / `production` / `none`. |
| `plugins` | — | Per-plugin config (splash, status bar, keyboard, …). |

---

## 🔨 Build locally

Prerequisites: Node 22, JDK 21 (Android), Xcode (iOS, macOS only).

```bash
# 1. Install deps
npm install

# 2. Sync web assets into native projects
npm run sync            # both platforms
npm run sync:android    # Android only
npm run sync:ios        # iOS only

# 3a. Build Android
npm run build:apk       # debug APKs
npm run build:release   # release APKs (debug-signed locally)
npm run build:bundle    # release AAB

# 3b. Build iOS (macOS only, simulator)
npm run build:ios

# 4. Open in the native IDE
npm run open:android    # opens Android Studio
npm run open:ios        # opens Xcode
```

There's also a **Makefile** with the same targets (`make build-apk`,
`make build-release`, `make sync`, `make assets`, …) and convenience
shell scripts in `scripts/` (see [Section 8](#-tooling)).

---

## 🤖 CI/CD

Three workflows live in `.github/workflows/`:

### `build.yml` — continuous build
Runs on every push/PR to `main` and via manual dispatch. A `validate` job
checks the config and structure first, then a **matrix** builds three Android
variants (`debug`, `release`, `bundle`) in parallel plus an iOS Simulator
build. Artifacts: `app-debug-apks`, `app-release-apks`, `app-release-aab`,
`app-ios-simulator`.

### `release.yml` — tagged releases
Triggered by pushing a tag like `v1.2.0`. Decodes a signing keystore from the
`KEYSTORE_BASE64` secret (if present), builds signed release APKs + AAB, and
creates a **GitHub Release** with auto-generated changelog notes and the
artifacts attached.

```bash
git tag v1.2.0
git push origin v1.2.0   # → triggers release.yml
```

### `lint.yml` — quality gates
Runs Prettier, markdownlint, JSON syntax checks, and the config validator on
every PR.

### Dependabot
`.github/dependabot.yml` opens weekly PRs to bump npm packages, GitHub
Actions, and Gradle dependencies.

---

## 🔐 Signing for production (Play Store)

The release APKs/AAB built by `build.yml` are signed with the Android
**debug key**, so they install fine for testing but Google Play will reject
them. To publish for real:

1. **Generate a keystore:**
   ```bash
   keytool -genkey -v -keystore release.keystore -alias my-key \
     -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **Add GitHub Actions secrets** to your repo (Settings → Secrets and
   variables → Actions):
   - `KEYSTORE_BASE64` — `base64 -w0 release.keystore` (the file contents)
   - `KEYSTORE_PASSWORD` — the keystore password
   - `KEY_ALIAS` — e.g. `my-key`
   - `KEY_PASSWORD` — the key password

3. The `release.yml` workflow decodes `KEYSTORE_BASE64` to a temp file and
   `build.gradle` reads `KEYSTORE_PATH` / `KEYSTORE_PASSWORD` / `KEY_ALIAS` /
   `KEY_PASSWORD` from the environment. Push a tag and you'll get a signed
   GitHub Release.

> Locally, release builds automatically fall back to the debug signing config
> so they always work without secrets.

---

## 📲 Publishing

See [PUBLISHING.md](PUBLISHING.md) for illustrated, step-by-step guides:

- **Google Play Store** — create a developer account, set up your app, upload
  the signed AAB, fill the store listing, and roll out.
- **Apple App Store** — enroll in the Apple Developer Program, configure
  signing & capabilities, archive in Xcode, and submit via App Store Connect.

---

## 🎨 App icon & splash screen

Source images live in `resources/`:

- `resources/icon/icon.png` — at least 1024×1024 PNG (the app icon source).
- `resources/splash/splash.png` — at least 2732×2732 PNG (the splash source).

Generate all native sizes (Android mipmaps, iOS asset catalog) with:

```bash
npm run assets            # both platforms
npm run assets:android    # Android only
npm run assets:ios        # iOS only
# or
make assets
# or
scripts/generate-icons.sh
```

This uses [`@capacitor/assets`](https://github.com/ionic-team/capacitor-assets).
The PWA icons in `www/assets/` (192, 512, maskable, favicon) are already
generated and referenced by `manifest.json`.

---

## 🧩 Plugins

18 official Capacitor plugins are installed and configured. The JS bridge in
`www/app.js` initializes status bar, splash, keyboard, network, app lifecycle,
back button, and haptics for you. See [PLUGINS.md](PLUGINS.md) for the full
list with code examples. Quick taste:

```js
import { Haptics } from '@capacitor/haptics';
await Haptics.impact({ style: 'medium' });

import { Share } from '@capacitor/share';
await Share.share({ title: 'Check this out', url: 'https://example.com' });
```

To add a new plugin: `npm install @capacitor/<plugin>` → `npm run sync` →
add any config to `capacitor.config.json` → document it in `PLUGINS.md` →
add native permissions if needed.

---

## 🗂️ Project structure

```
capacitor.config.json     # single source of app config (appId, name, plugins)
www/                      # web assets (your site or bundled PWA)
  index.html              # PWA shell / placeholder
  manifest.json           # PWA manifest
  sw.js                   # service worker (offline)
  app.js                  # Capacitor plugin bridge
  styles.css              # default styles
  offline.html            # offline fallback page
  assets/                 # icons, favicon, og image
android/                  # native Android project
ios/                      # native iOS project
resources/                # source icon & splash images
.github/workflows/        # CI/CD: build, release, lint
.github/dependabot.yml    # automated dependency updates
scripts/                  # helper shell + node scripts
docs/                     # long-form documentation
Makefile                  # convenience targets
```

---

## 🛠️ Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues. Highlights:

- **Blank screen / site won't load** — check `server.url` and your site's
  CSP / HTTPS. For HTTP sites, set `server.cleartext: true` (not recommended).
- **"Install blocked"** on Android — enable "Install unknown apps" for your
  browser/file manager.
- **Release APK rejected by Play** — it's debug-signed. Set up a real
  keystore and secrets (see [Signing](#-signing-for-production-play-store)).
- **iOS build fails** — run `npx cap sync ios` and, on macOS, `pod install`
  inside `ios/App`.

---

## ❓ FAQ

<details>
<summary><b>Do I need Android Studio / Xcode installed?</b></summary>

No. GitHub Actions builds everything in the cloud. You only need them
locally if you want to run on a device from your machine or tweak native
code.
</details>

<details>
<summary><b>Can I publish to the Play Store / App Store?</b></summary>

Yes. The release AAB/APKs are Play-ready once you sign with a real keystore
(see [Signing](#-signing-for-production-play-store)). For iOS you need an
Apple Developer account and code signing — see [PUBLISHING.md](PUBLISHING.md).
</details>

<details>
<summary><b>Will my site work offline?</b></summary>

If you bundle your files in `www/`, yes — fully offline. The included
service worker caches the app shell and shows `offline.html` when the
network is down. If you use `server.url`, offline behaviour depends on your
website's own caching.
</details>

<details>
<summary><b>How do I add push notifications?</b></summary>

`@capacitor/push-notifications` is already included. Configure Firebase
(`google-services.json` for Android, `GoogleService-Info.plist` for iOS),
add them to the project (they're git-ignored), and call the plugin from JS.
See [PLUGINS.md](PLUGINS.md).
</details>

<details>
<summary><b>How do I change the app id / name everywhere at once?</b></summary>

Run `scripts/setup.sh` which rewrites the placeholder `com.example.mywebapp`
/ "My Web App" across the Android and iOS native files for you.
</details>

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for the
workflow, code style, and PR process, and the
[Code of Conduct](CODE_OF_CONDUCT.md) for our community standards.

---

## 📄 License

[MIT](LICENSE) © web2apk contributors.

<div align="center">

Made with ❤️ by the [FED-OS](https://github.com/FED-OS) community ·
[Forum](https://www.fedpromptly.com/forum) ·
[Sponsor](https://github.com/sponsors/FED-OS)

</div>
