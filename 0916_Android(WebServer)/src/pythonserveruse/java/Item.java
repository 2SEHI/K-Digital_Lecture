package com.example.pythonserveruse;

import java.io.Serializable;

public class Item implements Serializable {

    private int itemid;
    private String itemname;
    private int price;
    private String description;
    private String pictureurl;


    // 매개변수가 없는 생성자 - 일반적인 경우 사용용
   public Item(){

    }
    // 모든 속성을 파라미터로 넘겨받는 생성자
    // 테스트를 할 때 또는 외부에서 데이터를 읽어올 때
    public Item(int itemid, String itemname, int price, String description, String pictureurl) {
        this.itemid = itemid;
        this.itemname = itemname;
        this.price = price;
        this.description = description;
        this.pictureurl = pictureurl;
    }

    public int getItemid() {
        return itemid;
    }

    public void setItemid(int itemid) {
        this.itemid = itemid;
    }

    public String getItemname() {
        return itemname;
    }

    public void setItemname(String itemname) {
        this.itemname = itemname;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPictureurl() {
        return pictureurl;
    }

    public void setPictureurl(String pictureurl) {
        this.pictureurl = pictureurl;
    }

    // 디버깅을 위한 메소드
    // 인스턴스 이름을 출력하는 메소드에 대입하면 자동으로 호출됨
    @Override
    public String toString() {
        return "Item{" +
                "itemid=" + itemid +
                ", itemname='" + itemname + '\'' +
                ", price=" + price +
                ", description='" + description + '\'' +
                ", pictureurl='" + pictureurl + '\'' +
                '}';
    }
}
