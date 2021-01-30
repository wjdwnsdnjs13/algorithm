#include <LedControl.h> 

LedControl l1=LedControl(22,23,24,4); //DIN22 GLK23 CS24
LedControl l2=LedControl(25,26,27,4); //DIN25 GLK26 CS27
LedControl l3=LedControl(28,29,30,4); //DIN28 GLK29 CS30
LedControl l4=LedControl(31,32,33,4); //DIN31 GLK32 CS33

void clean()
{ // 전체led를 꺼주는 함수
    for(int i = 0; i < 4; i++)
    {
        l1.clearDisplay(i);
        l2.clearDisplay(i);
        l3.clearDisplay(i);
        l4.clearDisplay(i);
    }
    return;
}

void SHINE(int delay_time=0,int repeat=1)
{ //깜빡 거리기. repeat 횟수만큼 반복
    int count = 0;
    while(repeat > count)
        {
        for(int i=1;i<=15;i++)
        {
            for(int j=0;j<4;j++)
            {
                l1.setIntensity(j,i);
                l2.setIntensity(j,i);
                l3.setIntensity(j,i);
                l4.setIntensity(j,i);
                delay(delay_time);
            }
        }
        for(int i=15;i>=1;i--)
        {
            for(int j=0;j<4;j++)
            {
                l1.setIntensity(j,i);
                l2.setIntensity(j,i);
                l3.setIntensity(j,i);
                l4.setIntensity(j,i);
                delay(delay_time);
            }
        }
        count++;
    }
    return;
}

void ALL_ON()
{ //모든 led 키기
    for(int i = 0; i<4; i++)
    {
        for(int j = 0; j<8; j++)
        { 
            l1.setRow(i,j,B11111111);
            l2.setRow(i,j,B11111111);
            l3.setRow(i,j,B11111111);
            l4.setRow(i,j,B11111111);
        }
    }
    return;
}

void ON_BLOCK(int num_led,int row)
{ // 좌표를 넣으면 8x8 LED 한 블록을 켜주는 함수
    for(int i = 0; i<8; i++)
    {
        if(num_led == 1)
        {
            l1.setRow(row-1,i,B11111111);
        }
        else if(num_led == 2)
        {
            l2.setRow(row-1,i,B11111111);
        }
        else if(num_led == 3)
        {
            l3.setRow(row-1,i,B11111111);
        }
        else if(num_led == 4)
        {
            l4.setRow(row-1,i,B11111111);
        }

    }
    return;
}

void OFF_BLOCK(int num_led,int row)
{ // 좌표를 넣으면 8x8 LED 한 블록을 꺼주는 함수
    for(int i = 0; i<8; i++)
    {
        if(num_led == 1)
        {
            l1.setRow(row-1,i,B00000000);
        }
        else if(num_led == 2)
        {
            l2.setRow(row-1,i,B00000000);
        }
        else if(num_led == 3)
        {
            l3.setRow(row-1,i,B00000000);
        }
        else if(num_led == 4)
        {
            l4.setRow(row-1,i,B00000000);
        }

    }
    return;
}

void HEART()
{ //테스트용 하트그리기
    byte heart[8] = { 
    B00000010,                                    
    B00000100,                                  
    B00001000,                                  
    B00010000,                                  
    B00001000,                                  
    B00000100,                                  
    B00000010,                                  
    B00000001                                                              
    };
    for(int i = 0; i<4; i++)
    {
        for (int j=0; j<8; j++)
        {
            {
                l1.setRow(i,j,heart[j]);
                l2.setRow(i,j,heart[j]);
                l3.setRow(i,j,heart[j]);
                l4.setRow(i,j,heart[j]);
            }
        }
    }
    /*
    l1.setColumn(1,0,heart[0]);
    l1.setColumn(1,1,heart[1]);
    l1.setColumn(1,2,heart[2]);
    l1.setColumn(1,3,heart[3]);
    l1.setColumn(1,4,heart[4]);
    l1.setColumn(1,5,heart[5]);
    l1.setColumn(1,6,heart[6]);
    l1.setColumn(1,7,heart[7]);
    */
    return;
}

void BLOCK_1(int num_led,int row,int delay_time=200)
{ // 좌표를 넣으면 좌표를 기준으로 좌우로 퍼지는 패턴
    switch(row)
    {
        case 1:
        {
            switch(num_led)
            {
                case 1:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led+3,row);
                    ON_BLOCK(num_led,row+3);
                }
                case 2:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led,row+3);
                }
                case 3:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led,row+3);
                }
                case 4:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led-3,row);
                    ON_BLOCK(num_led,row+3);
                }
            }
            
        }
        case 2:
        {
            switch(num_led)
            {
                case 1:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led+3,row);
                    ON_BLOCK(num_led,row+3);
                }
                case 2:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led+2,row);
                    
                }
                case 3:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led-2,row);
                }
                case 4:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row+2);
                    ON_BLOCK(num_led-3,row);
                    
                }
            }
        }
        case 3:
        {
            switch(num_led)
            {
                case 1:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led+3,row);
                }
                case 2:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led+2,row);
                    
                }
                case 3:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led-2,row);
                }
                case 4:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row+1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led-3,row);
                    
                }
            }
        }
        case 4:
        {
            switch(num_led)
            {
                case 1:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led+3,row);
                    ON_BLOCK(num_led,row-3);
                }
                case 2:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led+2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led,row-3);
                }
                case 3:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led+1,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led,row-3);
                }
                case 4:
                {
                    ON_BLOCK(num_led,row);
                    ON_BLOCK(num_led-1,row);
                    ON_BLOCK(num_led,row-1);
                    ON_BLOCK(num_led-2,row);
                    ON_BLOCK(num_led,row-2);
                    ON_BLOCK(num_led-3,row);
                    ON_BLOCK(num_led,row-3);
                }
            }
        }
    delay(delay_time);
    clean();
    }
    return;
}

void printChar_Row(byte data[4][4][8],int delay_time=0)
{//엑셀로 만든 그림을 매개변수로 주면 가로로 출력
    for(int i=0 ; i<4 ; i++)
    {
        for(int j=0 ; j<8 ; j++)
        {
                l1.setRow(i,j,data[0][i][j]);
                l2.setRow(i,j,data[1][i][j]);
                l3.setRow(i,j,data[2][i][j]);
                l4.setRow(i,j,data[3][i][j]);
                delay(delay_time);
        }
    }
    return;
}

void printChar_Col(byte data[4][4][8],int delay_time=0)
{//엑셀로 만든 그림을 매개변수로 주면 세로로 출력
    for(int i=3 ; i>=0 ; i--)
    {
        for(int j=0 ; j<8 ; j++)
        {
                l1.setColumn(i,j,data[0][i][j]);
                l2.setColumn(i,j,data[1][i][j]);
                l3.setColumn(i,j,data[2][i][j]);
                l4.setColumn(i,j,data[3][i][j]);
                delay(delay_time);
        }
    }
    return;
}
