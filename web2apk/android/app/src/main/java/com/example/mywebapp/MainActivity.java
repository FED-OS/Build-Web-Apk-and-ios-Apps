package com.example.mywebapp;

import android.os.Bundle;

import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        // Plugins are auto-registered by Capacitor via capacitor.build.gradle.
        // Register any custom/native plugins here BEFORE super.onCreate().
        //
        // Example:
        // registerPlugin(MyCustomPlugin.class);

        super.onCreate(savedInstanceState);
    }
}
