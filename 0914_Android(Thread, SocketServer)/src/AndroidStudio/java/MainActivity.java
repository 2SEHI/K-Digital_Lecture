package com.example.pythonuse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView txt;
    Button btn;
    // 인덱스 변수
    int value;
    
    // Handler 생성 - Handler 클래스를 상속받는 클래스의 인스턴스
    // 이 문법을 자바에서는 Anonymous Class 라고 부름
    Handler handler = new Handler(Looper.getMainLooper()){

        @Override
        public void handleMessage(Message msg){
            txt.setText(value + "");
        }
    };

    class ValueThread extends Thread{
        // Thread가 시작되면 호출되는 메소드
        public void  run(){
            try{
                for (int i=0; i<10; i++){
                    value = value + 1;
                    // 1초씩 대기
                    Thread.sleep(1000);
                    // 인덱스를 문자열로 변경하여 저장
                    // txt.setText(value + "");

                    // 핸들러에게 메시지를 전송해서 처리해달라고 요청
                    handler.sendEmptyMessage(0);

                }
            }catch(Exception e){}
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt = (TextView)findViewById(R.id.txt);
        btn = (Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Thread 생성 후 실행
                ValueThread th = new ValueThread();
                th.start();
            }
        });
    }
}