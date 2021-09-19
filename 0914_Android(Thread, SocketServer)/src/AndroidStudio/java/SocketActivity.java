package com.example.pythonuse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.material.snackbar.Snackbar;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class SocketActivity extends AppCompatActivity {
    // View를 생성할 변수
    EditText edit;
    Button btn;

    // 전송받은 메시지를 저장할 변수
    String mes = "";

    // Thread가 전송받은 메시지를 출력할 Handler
    Handler handler = new Handler(Looper.getMainLooper()){
        public void handleMessage(Message msg){
            // 알림 메시지로 mes를 출력
            Snackbar.make(edit, mes, Snackbar.LENGTH_LONG).show();
        }
    };

    // 서버와 통신할 Thread 클래스
    class TCPThread extends Thread{
        public void run(){
            // 소켓 통신을 위한 변수
            Socket socket = null;
            // 소켓에 전송을 할 때 사용할 문자 스트림
            PrintWriter pw = null;
            // 소켓에서 읽어올 때 사용할 문자 스트림
            BufferedReader br = null;
            try{
                // 서버의 포트번호
                int port = 8000;
                // 소켓 생성
				// TODO 서버쪽 IP로 수정할 것
                socket = new Socket("서버쪽 IP", port);
                pw = new PrintWriter(socket.getOutputStream());
                // 입력한 내용 전송 - 버퍼에 전송
                pw.println(edit.getText().toString());
                // flush : 버퍼의 내용을 전송하고 비우기
                pw.flush();
                
                // 읽기 위한 스트림 생성
                br = new BufferedReader(
                        new InputStreamReader(
                                socket.getInputStream()));
                
                // 한 줄 읽어오기
                mes = br.readLine();
                // mes 를 출력하기 위한 핸들러 호출
                handler.sendEmptyMessage(0);

                pw.close();
                br.close();
                socket.close();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_socket);

        edit = (EditText) findViewById(R.id.edit);
        btn = (Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                TCPThread th = new TCPThread();
                th.start();
            }
        });
    }
}