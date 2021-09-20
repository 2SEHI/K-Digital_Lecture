package com.example.pythonserveruse;


import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.InputStream;
import java.net.URL;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ItemAdapter extends BaseAdapter {

    // View 출력할 때 필요한 Context 변수 - Activity 를 대입
    Context context;
    // ListView 에 출력할 데이터
    List<Item> data;
    // 셀 모양의 아이디를 저장할 변수
    int layout;
    // xml 파일의 내용을 View 클래스로 변경하기 위한 변수
    LayoutInflater inflater;

    // 생성자 만들기
    public ItemAdapter(Context context, List<Item> data, int layout){
        this.context = context;
        this.data = data;
        this.layout = layout;
        this.inflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    // 행의 개수를 설정하는 메소드 - 반복문을 수행할 횟수
    @Override
    public int getCount() {
        return data.size();
    }

    // 기본 모양을 사용할 때 보여질 문자열을 설정하는 메소드
    @Override
    public Object getItem(int i) {
        return data.get(i).getItemid();
    }

    // 셀을 구별하기 위한 아이디를 설정하는 메소드
    @Override
    public long getItemId(int i) {
        return (long)i;
    }

    ImageView imageView;
    Bitmap bit;

    // 다운로드 받은 이미지를 출력해주는 핸들러
    Handler handler = new Handler(Looper.getMainLooper()){
        // msg 의 obj에 Map을 전달
        // Map의 imageview 키에 ImageView, bit 키에 Bitmap을 전송
        public void handleMessage(Message msg){
            // 전달받은 데이터 가져오기
            Map<String, Object> map = (Map<String, Object>)msg.obj;
            ImageView imageView = (ImageView)map.get("imageview");
            Bitmap bit = (Bitmap)map.get("bit");
            imageView.setImageBitmap(bit);
        }
    };

    // private 는 인스턴스가 접근 못합니다.
    class ImageThread extends Thread {
        String imagename;
        ImageView imageView;
        public void run(){
            try{
                // 이미지 다운로드를 스트림 생성
                InputStream inputStream = new URL("http://172.30.1.54:5000/imagedownload/" + imagename).openStream();
                // 이미지 다운로드
                Bitmap bit = BitmapFactory.decodeStream(inputStream);
                inputStream.close();
                // 핸들러에 전송할 데이터 만들기
                Message msg = new Message();
                Map<String, Object> map = new HashMap<String, Object>();
                map.put("bit", bit);
                map.put("imageview", imageView);
                msg.obj = map;

                // 핸들러를 Message와 함께 호출
                handler.sendMessage(msg);
            }catch(Exception e){
                Log.e("이미지 다운로드", "실패");
            }


        }
    }
    // 셀 모양을 설정하는 메소드
    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        // 출력할 셀을 생성
        // 먼저 출력할 셀을 가지고 생성
        View returnView = view;
        // 출력한 적이 없다면 직접 생성
        if(returnView == null){
            returnView = inflater.inflate(layout, viewGroup, false);
        }
        // R.id.itemname는 item_cell.xml의 android:id="@+id/itemname"와 매칭됨
        TextView itemname = (TextView)returnView.findViewById(R.id.itemname);
        itemname.setText(data.get(i).getItemname());

        TextView price = (TextView)returnView.findViewById(R.id.price);
        price.setText(data.get(i).getPrice() + "원");

        // 계산을 할게 아니라면 굳이 데이터타입을 숫자로 할 필요가 없습니다.
        TextView description = (TextView)returnView.findViewById(R.id.description);
        description.setText(data.get(i).getDescription());

        // 이미지 출력을 위한 부분
        ImageView imageView = (ImageView) returnView.findViewById(R.id.itemimage);
        ImageThread th = new ImageThread();
        th.imagename = data.get(i).getPictureurl();
        th.imageView = imageView;
        th.start();
        return returnView;
    }
}
