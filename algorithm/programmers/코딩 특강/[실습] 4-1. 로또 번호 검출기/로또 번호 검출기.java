import java.util.*;

class Solution {
    public boolean solution(int[] lotto) {
        Set<Integer> set = new HashSet<>();
        Arrays.stream(lotto).forEach(v -> set.add(v));
        return set.size() == 6?true:false;
    }
}