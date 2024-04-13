import java.util.*;

class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        // my_string의 s 인덱스부터 overwrite_string 길이만큼 overwrite_string으로 바꾼 문자열 리턴
        String[] result = my_string.split("");
        String[] overwrite_string_array = overwrite_string.split("");
        for(int i = 0; i < overwrite_string.length(); i++){
            result[s + i] = overwrite_string_array[i];
        }
        String answer = String.join("", result);
        return answer;
        
    }
}