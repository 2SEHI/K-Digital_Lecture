package com.example.pythonserveruse;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import com.google.android.material.snackbar.Snackbar;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.Buffer;
import java.util.UUID;

public class itemInsertActivity extends AppCompatActivity {
    Button btninsert, btngallery, btncamera;
    EditText edititemname, editprice, editdescription;
    ImageView imageView;

    // 삽입 결과를 저장할 변수
    Boolean result = false;
    // 삽입 결과를 출력할 Handler
    Handler handler = new Handler(Looper.getMainLooper()){
        @Override
        public void handleMessage(Message msg) {
            if(result == true){
                // 삽입 결과를 화면에 출력합니다.
                Snackbar.make(imageView, "삽입 성공", Snackbar.LENGTH_LONG).show();

                // 삽입 성공후 입력 란을 초기화
                edititemname.setText("");
                editprice.setText("");
                editdescription.setText("");

                // 키보드 제거 - 입력란의 포커스를 해제
                InputMethodManager imm = (InputMethodManager)getSystemService(
                        INPUT_METHOD_SERVICE);
                // edititemname 의 포커스를 해제
                imm.hideSoftInputFromWindow(edititemname.getWindowToken(), 0);
                // edititemname 의 포커스를 해제
                imm.hideSoftInputFromWindow(editprice.getWindowToken(), 0);
                // edititemname 의 포커스를 해제
                imm.hideSoftInputFromWindow(editdescription.getWindowToken(), 0);
            }else{
                Snackbar.make(imageView, "삽입 실패", Snackbar.LENGTH_LONG).show();
            }
            super.handleMessage(msg);
        }
    };

    // 요청을 수행할 Thread
    class ThreadEx extends Thread{
        public void run(){
            try{
                // 요청 URL생성
                URL url = new URL("http://172.30.1.54:5000/insert");
                // 연결 객체 생성
                HttpURLConnection con = (HttpURLConnection)url.openConnection();
                con.setUseCaches(false);
                con.setConnectTimeout(30000);

                // 파일을 제외한 파라미터 생성
                String [] dataName = {
                        "itemname",
                        "price",
                        "description"
                };
                String [] data = {
                        edititemname.getText().toString(),
                        editprice.getText().toString(),
                        editdescription.getText().toString()
                };

                // 파일이 있으면 구분자생성
                String lineEnd = "\r\n";
                // 중복되지 않는 문자열 생성
                String boundary = UUID.randomUUID().toString();
                // 전송 방식 설정 : POST
                con.setRequestMethod("POST");
                // OutputStream으로 POST 데이터를 넘겨주겠다는 옵션
                con.setDoOutput(true);
                // InputStream으로 서버로 부터 응답을 받겠다는 옵션
                con.setDoInput(true);

                /**파일을 전송할 때만 설정*/
                // setRequestProperty : Request Header 값 세팅
                con.setRequestProperty("ENCTYPE", "multipart/form-data");
                con.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
                // 파라미터 구분을 위한 구분자 생성
                // Server가 이 것으로 파라미터를 구분합니다.
                String delimiter = "--" + boundary + lineEnd;
                // 파일을 제외한 파라미터를 하나의 문자열로 생성
                StringBuffer postDataBuilder= new StringBuffer();

                // 파일정보를 제외한 itemname, price, description에 대한 값 설정
                for(int i=0; i<data.length; i++){
                    postDataBuilder.append(delimiter);
                    postDataBuilder.append("Content-Disposition:form-data;name=\"" + dataName[i] + "\""
                            + lineEnd + lineEnd + data[i] + lineEnd);
                }

                // TODO
                // 파일명 생성
                String fileName = "penguins.jpg";
                // 파일이름을 파라미터로 추가
                if(fileName != null){
                    postDataBuilder.append(delimiter);
                    postDataBuilder.append(
                            "Content-Disposition:form-data;name=\"" +
                                    "pictureurl" + "\";filename=\"" +
                                    fileName + "\"" + lineEnd);
                }
                // 파라미터를 서버에 전송 : 텍스트들만
                DataOutputStream ds = new DataOutputStream(con.getOutputStream());
                ds.write(postDataBuilder.toString().getBytes());
                // 파일을 전송하고 파라미터 전송을 종료
                if(fileName != null){
                    ds.writeBytes(lineEnd);

                    // 카메라를 쓰면 이부분이 변경됨
                    // /res/raw 폴더의 파일 읽어들인다는 의미
                    InputStream fres = getResources().openRawResource(R.raw.penguins);
                    // penguins파일에 대해 현재 읽을수 있는 바이트수만큼 byte 배열을 생성
                    byte [] buffer = new byte[fres.available()];

                    int length = -1;
                    // 파일 전송
                    // 파일을 나누어서 DataOutputStream에 쓰기
                    while((length = fres.read(buffer)) != -1){
                        ds.write(buffer, 0, length);
                    }

                    ds.writeBytes(lineEnd);
                    ds.writeBytes(lineEnd);
                    ds.writeBytes("--" + boundary + "--" + lineEnd);
                    fres.close();
                }else {
                    // 파일이 없는 경우
                    ds.writeBytes(lineEnd);
                    ds.writeBytes("--" + boundary + "--" + lineEnd);
                }

                ds.flush();
                ds.close();

                // 웹서버의 응답 읽기
                BufferedReader br = new BufferedReader(
                        new InputStreamReader(con.getInputStream()));
                StringBuilder sb = new StringBuilder();
                while(true){
                    String line = br.readLine();
                    if(line == null){
                        break;
                    }
                    sb.append(line + "\n");
                }
                String json = sb.toString();
                Log.e("응답", json);

                // JSON 파싱
                JSONObject object = new JSONObject(json);
                // result 키의 결과를 저장
                result = object.getBoolean("result");

                // Handler에게 메시지 전송
                handler.sendEmptyMessage(0);

            }catch(Exception e){
                Log.e("요청 및 파싱 실패", e.getLocalizedMessage());
            }
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item_insert);

        btninsert = (Button)findViewById(R.id.btninsert);
        // 아이템 삽입 버튼을 누르면 Thread실행
        btninsert.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new ThreadEx().start();
            }
        });

        btngallery = (Button)findViewById(R.id.btngallery);
        btncamera = (Button)findViewById(R.id.btncamera);

        edititemname = (EditText)findViewById(R.id.edititemname);
        editprice = (EditText)findViewById(R.id.editprice);
        editdescription = (EditText)findViewById(R.id.editdescription);

        imageView = (ImageView)findViewById(R.id.imageview);


    }
}
