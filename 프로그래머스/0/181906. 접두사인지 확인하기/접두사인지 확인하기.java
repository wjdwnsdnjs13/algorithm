class Solution {
    public int solution(String my_string, String is_prefix) {
        return is_prefix.length() > my_string.length()?0:my_string.substring(0, is_prefix.length()).equals(is_prefix)?1:0;
    }
}