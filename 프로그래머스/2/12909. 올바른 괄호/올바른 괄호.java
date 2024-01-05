class Solution {
    boolean solution(String s) {
        // (와 )의 갯수 카운팅으로 음수가 되면 false
        String[] str = s.split("");
        int count = 0;
        // Arrays.stream(str).forEach(v -> System.out.print(v));
        for(int i = 0; i < str.length; i++){
            if(count < 0) return false;
            if(str[i].equals("(")) count++;
            else count--;
        }
        
        return count == 0;
    }
}