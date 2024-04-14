class Solution {
    public String solution(String str1, String str2) {
        String[] strArray1 = str1.split("");
        String[] strArray2 = str2.split("");
        String answer = "";
        for(int i = 0; i < strArray1.length; i++){
            answer += strArray1[i];
            answer += strArray2[i];
        }
        return answer;
    }
}