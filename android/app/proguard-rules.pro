# ── web2apk ProGuard / R8 rules ────────────────────────────────────────

# Preserve line numbers for readable crash stack traces.
-keepattributes SourceFile,LineNumberTable
-renamesourcefileattribute SourceFile

# ── WebView / JavaScript bridge ────────────────────────────────────────
# Capacitor injects a JS interface; keep its members reachable from JS.
-keepclassmembers class com.getcapacitor.** {
    @android.webkit.JavascriptInterface <methods>;
}
-keep @interface com.getcapacitor.** { *; }
-keep class com.getcapacitor.** { *; }

# Keep any custom @JavascriptInterface in your own code.
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}

# WebView client / chrome client subclasses.
-keep class android.webkit.WebView { *; }
-keep class * extends android.webkit.WebViewClient
-keep class * extends android.webkit.WebChromeClient

# ── Capacitor plugins ──────────────────────────────────────────────────
# Plugin POJOs are reflected by the bridge.
-keep class com.getcapacitor.plugin.** { *; }
-keepclassmembers class * {
    @com.getcapacitor.annotation.CapacitorPlugin *;
}

# ── Cordova plugins ────────────────────────────────────────────────────
-keep class org.apache.cordova.** { *; }

# ── Google Play Services (push) ────────────────────────────────────────
-keep class com.google.android.gms.** { *; }
-keep class com.google.firebase.** { *; }

# ── Kotlin metadata ────────────────────────────────────────────────────
-dontwarn kotlin.**
-keep class kotlin.Metadata { *; }

# ── Keep model classes used by JSON serialization ──────────────────────
# Add your own data classes here, e.g.:
# -keep class com.example.mywebapp.model.** { *; }
