package com.example.pythonuse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebView;

public class WebActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        // WebView를 찾아와서 url을 출력
        WebView webView = (WebView)findViewById(R.id.webview);
		// TODO 서버쪽 IP로 수정할 것
        webView.loadUrl("http://서버쪽 IP:5000");
    }
}