class Solution {
    public int solution(int n, String control) {
        for(int i = 0; i < control.length(); i++){
            char command = control.charAt(i);
            switch(command){
                case('w'):
                    n++;
                    break;
                case('s'):
                    n--;
                    break;
                case('d'):
                    n += 10;
                    break;
                case('a'):
                    n -= 10;
                    break;
            }
        }
        return n;
    }
}