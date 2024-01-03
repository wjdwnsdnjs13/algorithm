import java.util.*;

class Solution {
    public boolean solution(String[] words) {
        Set<String> set = new HashSet<>();
        char lastSpelling = words[0].toCharArray()[words[0].length() - 1];
        String word = "";
        set.add(words[0]);
        for(int i = 1; i < words.length; i++){
            word = words[i];
            if(set.contains(word) || (lastSpelling != word.toCharArray()[0])) return false;
            lastSpelling = word.toCharArray()[word.length() - 1];
            set.add(word);
        }
        return true;
    }
}