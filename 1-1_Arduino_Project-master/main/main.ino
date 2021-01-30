#include <LedControl.h> 
#include "LED_data.h" //여기에 만든 데이터들 들어있음
#include "LED_Func.h" //여기에 만든 함수들 들어있음
#include "Play_MP3.h"

#include <Wire.h> // 터치센서 관련 라이브러리
#include <Adafruit_MPR121.h> // 터치센서 관련 라이브러리

Adafruit_MPR121 c1 = Adafruit_MPR121(); //터치 1번
Adafruit_MPR121 c2 = Adafruit_MPR121(); //터치 2번
uint16_t lasttouched = 0;
uint16_t currtouched = 0;
uint16_t lasttouched2 = 0;
uint16_t currtouched2 = 0;
int page = 4; //시작 페이지
                      
void setup()
{
    for(int i=0; i<4; i++) // 도트 매트릭스 0~3번
    {             
        l1.shutdown(i,false); // 디스플레이 초기화
        l2.shutdown(i,false);
        l3.shutdown(i,false);
        l4.shutdown(i,false);
        l1.setIntensity(i,1); // 도트 매트릭스 밝기 (매트릭스 번호, 밝기) 1~15
        l2.setIntensity(i,1);
        l3.setIntensity(i,1);
        l4.setIntensity(i,1);
        l1.clearDisplay(i); // i번 led를 꺼주는 함수
        l2.clearDisplay(i);
        l3.clearDisplay(i);
        l4.clearDisplay(i);
    }
    Serial.begin(115200);
    sd.begin(SD_SEL, SPI_HALF_SPEED);
    MP3player.begin();
    
    Serial.println(String("LED1번 인식된 모듈 개수 : ")+l1.getDeviceCount());
    Serial.println(String("LED2번 인식된 모듈 개수 : ")+l2.getDeviceCount());
    Serial.println(String("LED3번 인식된 모듈 개수 : ")+l3.getDeviceCount());
    Serial.println(String("LED4번 인식된 모듈 개수 : ")+l4.getDeviceCount());
    if (!c1.begin(0x5A)) { //터치센서 인식 확인
    Serial.println("MPR121-1 not found, check wiring?");
    
    }
    else{
    Serial.println("MPR121-1 found!");
    
    }
    if (!c2.begin(0x5D)) {
    Serial.println("MPR121-2 not found, check wiring?");
    
    }
    else{
    Serial.println("MPR121-2 found!");
    }
}

void loop(){
    // Get the currently touched pads
    String senser = "";
    currtouched = c1.touched();
    currtouched2 = c2.touched();
    for (int j = 1; j<3 ; j++) // 터치센서 구분
    {
        for (uint8_t i=0; i<12; i++) //터치센서 포트 구분
        {
            if ((currtouched & _BV(i)) && !(lasttouched & _BV(i))&& j==1) {
                Serial.print(i); Serial.println("-1 touched");
                senser = String(i)+String(j);
                Serial.println(senser);
            }
            if (!(currtouched & _BV(i)) && (lasttouched & _BV(i)) && j==1) {
                Serial.print(i); Serial.println("-1 released");
            }
            if ((currtouched2 & _BV(i)) && !(lasttouched2 & _BV(i)) && j==2) {
                Serial.print(i); Serial.println("-2 touched");
                senser = String(i)+String(j);
                Serial.println(senser);
            }
            // if it *was* touched and now *isnt*, alert!
            if (!(currtouched2 & _BV(i)) && (lasttouched2 & _BV(i)) &&j==2) {
                Serial.print(i); Serial.println("-2 released");
            }
        }
    }
    if(senser=="42")
    {
        MP3player.stopTrack();
        clean();
    }
  //페이지 선언
    if(senser=="82")
    {
        page=1; Serial.println("페이지1 실행합니다.");
    }
    else if(senser=="92")
    {
        page=2; Serial.println("페이지2 실행합니다.");
    }
    else if(senser=="102")
    {
        page=3; Serial.println("페이지3 실행합니다.");
    }
    else if(senser=="112")
    {
        page=4; Serial.println("페이지4 실행합니다.");
    }
    
    //beat_box
    if(page ==4 && senser=="02") {
      MP3player.stopTrack();
      MP3player.playTrack(191);
    }
     else if(page ==4 && senser=="12") {
      MP3player.stopTrack();
      MP3player.playTrack(194);
    }
     else if(page ==4 && senser=="22") {
      MP3player.stopTrack();
      MP3player.playTrack(193);
    }
     else if(page ==4 && senser=="32") {
      MP3player.stopTrack();
      MP3player.playTrack(192);
    }

    //beat_box

    //페이지 1
    if(page ==1 && senser=="32") {
      MP3player.stopTrack();
      MP3player.playTrack(101);
      ON_BLOCK(4,4);
      
    }
    else if(page ==1 && senser=="02") {
      MP3player.stopTrack();        
      MP3player.playTrack(102);
      ON_BLOCK(4,1);
    }
    else if(page ==1 && senser=="22") {
      MP3player.stopTrack();        
      MP3player.playTrack(103);
      ON_BLOCK(4,3);
    }
    else if(page ==1 && senser=="12") {
      MP3player.stopTrack();
      MP3player.playTrack(104);
      ON_BLOCK(4,2);
    }
    else if(page ==1 && senser=="31" || page ==1 && senser=="72") {
      MP3player.stopTrack();
      MP3player.playTrack(105);
      ON_BLOCK(1,4);
    }
    else if(page ==1 && senser=="01") {
      MP3player.stopTrack();
      MP3player.playTrack(106);
      ON_BLOCK(1,1);
    }
    else if(page ==1 && senser=="21") {
      MP3player.stopTrack();
      MP3player.playTrack(107);
      ON_BLOCK(1,3);
    }
    else if(page ==1 && senser=="11") {
      MP3player.stopTrack();
      MP3player.playTrack(108);
      ON_BLOCK(1,2);
    }
    else if(page ==1 && senser=="111") {
      MP3player.stopTrack();
      MP3player.playTrack(109);
      ON_BLOCK(3,4);
    }
    else if(page ==1 && senser=="81") {
      MP3player.stopTrack();
      MP3player.playTrack(110);
      ON_BLOCK(3,1);
    }
    else if(page ==1 && senser=="101") {
      MP3player.stopTrack();
      MP3player.playTrack(111);
      ON_BLOCK(3,3);
    }
    else if(page ==1 && senser=="91") {
      MP3player.stopTrack();
      MP3player.playTrack(112);
      ON_BLOCK(3,2);
    }
    else if(page ==1 && senser=="71") {
      MP3player.stopTrack();
      MP3player.playTrack(113);
      ON_BLOCK(2,4);
    }
    else if(page ==1 && senser=="41" || page ==1 && senser=="52") {
      MP3player.stopTrack();
      MP3player.playTrack(114);
      ON_BLOCK(2,1);
    }
    else if(page ==1 && senser=="61" ) {
      MP3player.stopTrack();
      MP3player.playTrack(115);
      ON_BLOCK(2,3);
    }
    else if(page ==1 && senser=="51" || page ==1 && senser=="62") {
      MP3player.stopTrack();
      MP3player.playTrack(116);
      ON_BLOCK(2,2);
    }
    //페이지 1 끝



  //페이지2
  if(page ==2 && senser=="31" || page ==2 && senser=="72") {
      MP3player.stopTrack();
      MP3player.playTrack(201);
      BLOCK_1(1,4,0);
    }
    else if(page ==2 && senser=="61" || page ==2 && senser=="72") {
      MP3player.stopTrack();
      MP3player.playTrack(202);
      BLOCK_1(2,3,0);
    }
    else if(page ==2 && senser=="91") {
      MP3player.stopTrack();
      MP3player.playTrack(203);
      BLOCK_1(3,2,0);
    }
    else if(page ==2 && senser=="02") {
      MP3player.stopTrack();
      MP3player.playTrack(204);
      BLOCK_1(4,1,0);
    }
    else if(page ==2 && senser=="01") {
      MP3player.stopTrack();
      MP3player.playTrack(205);
      BLOCK_1(1,1,0);
    }
    else if(page ==2 && senser=="51" || page ==2 && senser=="62") {
      MP3player.stopTrack();
      MP3player.playTrack(206);
      BLOCK_1(2,2,0);
    }
    else if(page ==2 && senser=="101") {
      MP3player.stopTrack();
      MP3player.playTrack(207);
      BLOCK_1(3,3,0);
    }
    else if(page ==2 && senser=="32") {
      MP3player.stopTrack();
      MP3player.playTrack(208);
      BLOCK_1(4,4,0);
    }
    else if(page ==2 && senser=="21") {
      MP3player.stopTrack();
      MP3player.playTrack(209);
      BLOCK_1(1,3,0);
    }
    else if(page ==2 && senser=="71") {
      MP3player.stopTrack();
      MP3player.playTrack(210);
      BLOCK_1(2,4,0);
    }
    else if(page ==2 && senser=="111") {
      MP3player.stopTrack();
      MP3player.playTrack(211);
      BLOCK_1(3,4,0);
    }
    else if(page ==2 && senser=="22") {
      MP3player.stopTrack();
      MP3player.playTrack(212);
      BLOCK_1(4,3,0);
    }
    else if(page ==2 && senser=="11") {
      MP3player.stopTrack();
      MP3player.playTrack(213);
      BLOCK_1(1,2,0);
    }
    else if(page ==2 && senser=="41" || page ==2 && senser=="52") {
      MP3player.stopTrack();
      MP3player.playTrack(214);
      BLOCK_1(2,1,0);
    }
    else if(page ==2 && senser=="81" ) {
      MP3player.stopTrack();
      MP3player.playTrack(215);
      BLOCK_1(3,1,0);
    }
    else if(page ==2 && senser=="12") {
      MP3player.stopTrack();
      MP3player.playTrack(216);
      BLOCK_1(4,2,0);
    }
//페이지 2끝


//페이지 3

    if(page ==3 && senser=="31" || page ==3 && senser=="72") {
      MP3player.stopTrack();
      MP3player.playTrack(131);
      ON_BLOCK(1,2);
      delay(300);
      OFF_BLOCK(1,2);
      delay(300);
      ON_BLOCK(1,1);
      delay(300);
      ON_BLOCK(1,3);
      delay(300);
      OFF_BLOCK(1,3);
      delay(300);
      ON_BLOCK(1,4);
      
      
    }
    else if(page ==3 && senser=="02") {
      MP3player.stopTrack();
      MP3player.playTrack(132);
      ON_BLOCK(2,2);
      delay(300);
      OFF_BLOCK(2,2);
      delay(300);
      ON_BLOCK(2,1);
      delay(300);
      ON_BLOCK(2,3);
      delay(300);
      OFF_BLOCK(2,3);
      delay(300);
      ON_BLOCK(2,4);
      
    }
    else if(page ==3 && senser=="21") {
      MP3player.stopTrack();
      MP3player.playTrack(133);
      ON_BLOCK(3,2);
      delay(300);
      OFF_BLOCK(3,2);
      delay(300);
      ON_BLOCK(3,1);
      delay(300);
      ON_BLOCK(3,3);
      delay(300);
      OFF_BLOCK(3,3);
      delay(300);
      ON_BLOCK(3,4);
      
    }
    else if(page ==3 && senser=="12") {
      MP3player.stopTrack();
      MP3player.playTrack(134);
      ON_BLOCK(4,2);
      delay(300);
      OFF_BLOCK(4,2);
      delay(300);
      ON_BLOCK(4,1);
      delay(300);
      ON_BLOCK(4,3);
      delay(300);
      OFF_BLOCK(4,3);
      delay(300);
      ON_BLOCK(4,4);
    }
    else if(page ==3 && senser=="11") {
      MP3player.stopTrack();
      MP3player.playTrack(135);
      OFF_BLOCK(4,1);
      delay(100);
      ON_BLOCK(4,2);
      delay(100);
      OFF_BLOCK(4,4);
      delay(100);
      ON_BLOCK(4,3);

      ON_BLOCK(3,4);
      delay(100);
      OFF_BLOCK(3,1);
      delay(100);
      ON_BLOCK(3,2);
      delay(100);
      OFF_BLOCK(3,4);
      delay(100);
      ON_BLOCK(3,3);

      ON_BLOCK(2,4);
      delay(100);
      OFF_BLOCK(2,1);
      delay(100);
      ON_BLOCK(2,2);
      delay(100);
      OFF_BLOCK(2,4);
      delay(100);
      ON_BLOCK(2,3);
      
      ON_BLOCK(1,4);
      delay(70);
      OFF_BLOCK(1,1);
      delay(70);
      ON_BLOCK(1,2);
      delay(70);
      OFF_BLOCK(1,4);
      delay(70);
      ON_BLOCK(1,3);
      delay(70);
      SHINE(0,2);
    }
    else if(page ==3 && senser=="22") {
      MP3player.stopTrack();
      MP3player.playTrack(136);
      ON_BLOCK(1,1);
      delay(100);
      ON_BLOCK(1,2);
      delay(100);
      ON_BLOCK(1,3);
      delay(100);
      ON_BLOCK(1,4);
      delay(100);
      ON_BLOCK(2,4);
      delay(100);
      ON_BLOCK(3,4);
      delay(100);
      ON_BLOCK(4,4);
    }
    else if(page ==3 && senser=="01") {
      MP3player.stopTrack();
      MP3player.playTrack(137);
      ON_BLOCK(4,3);
      delay(100);
      ON_BLOCK(4,2);
      delay(100);
      ON_BLOCK(4,1);
      delay(100);
      ON_BLOCK(3,1);
      delay(100);
      ON_BLOCK(2,1);
    }
    else if(page ==3 && senser=="32") {
      MP3player.stopTrack();
      MP3player.playTrack(138);
      ON_BLOCK(2,2);
      delay(100);
      ON_BLOCK(2,3);
      delay(100);
      ON_BLOCK(3,1);
      delay(100);
      ON_BLOCK(3,3);
      
    }
    else if(page ==3 && senser=="71") {
      MP3player.stopTrack();
      MP3player.playTrack(139);
      ON_BLOCK(3,2);
      delay(100);
      SHINE(0,6);
      
    }
    else if(page ==3 && senser=="81") {
      MP3player.stopTrack();
      MP3player.playTrack(140);
      OFF_BLOCK(3,2);
    }
    else if(page ==3 && senser=="61" || page ==3 && senser=="72") {
      MP3player.stopTrack();
      MP3player.playTrack(141);
      
      OFF_BLOCK(3,3);
      delay(100);
      OFF_BLOCK(2,3);
      delay(100);
      OFF_BLOCK(2,2);
      delay(100);
      OFF_BLOCK(2,1);
    }
    else if(page ==3 && senser=="91") {
      MP3player.stopTrack();
      MP3player.playTrack(142);
      OFF_BLOCK(3,1);
      delay(100);
      OFF_BLOCK(4,1);
      delay(100);
      OFF_BLOCK(4,2);
      delay(100);
      OFF_BLOCK(4,3);
      delay(100);
      OFF_BLOCK(4,4);
    }
    else if(page ==3 && senser=="51" || page ==3 && senser=="62") {
      MP3player.stopTrack();
      MP3player.playTrack(143);
      OFF_BLOCK(3,4);
      delay(100);
      OFF_BLOCK(2,4);
      delay(100);
      OFF_BLOCK(1,4);
      delay(100);
      OFF_BLOCK(1,3);
      delay(100);
      OFF_BLOCK(1,2);
      delay(100);
      OFF_BLOCK(1,1);
    }
    else if(page ==3 && senser=="101") {
      MP3player.stopTrack();
      MP3player.playTrack(144);
      printChar_Row(Row_Aclass);
      delay(700);
      clean();
      printChar_Row(Row_ban);
      delay(700);
      clean();
      for(int i=0; i<7; i++)
      {
          printChar_Row(heart);
          delay(300);
          printChar_Row(heart_emp);
          delay(300);
      }
      printChar_Row(Row_lee);
      delay(700);
      clean();
      printChar_Row(Row_duck);
      delay(700);
      clean();
      printChar_Row(Row_gi);
      delay(700);
      clean();
      for(int i=0; i<7; i++)
      {
          printChar_Row(heart);
          delay(300);
          printChar_Row(heart_emp);
          delay(300);
      }
    }

    //페이지3 끝
    
    lasttouched = currtouched;
    lasttouched2 = currtouched2;
    
    delay(100);
}
