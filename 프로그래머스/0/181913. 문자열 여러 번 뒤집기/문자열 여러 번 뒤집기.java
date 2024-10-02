class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        // pre String이랑 result String 사용
        String pre = my_string;
        for(int[] q: queries){
            StringBuilder result = new StringBuilder();
            int s = q[0];
            int e = q[1];
            for(int i = 0; i < s; i++) result.append(pre.charAt(i));
            for(int i = e; i >= s; i--) result.append(pre.charAt(i));
            for(int i = e + 1; i < pre.length(); i++) result.append(pre.charAt(i));
            pre = result.toString();
        }
        return pre;
    }
}