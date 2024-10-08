import java.util.*;

class Solution2 {
    public int solution(String my_string, String is_suffix) {
        return my_string.endsWith(is_suffix)?1:0;
    }
}

class Solution {
    //13번 케이스 실패함
    public int solution(String my_string, String is_suffix) {
        List<String> words = new ArrayList();
        for(int i = 1; i <= my_string.length(); i++){
            words.add(my_string.substring(my_string.length() - i));
        }
        return words.contains(is_suffix)?1:0;
    }
}