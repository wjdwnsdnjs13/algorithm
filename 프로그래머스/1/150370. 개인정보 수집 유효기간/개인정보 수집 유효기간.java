import java.util.*;

class Solution {
    // 1 ~ n번으로 분류되는 개인정보 n개가 있음.
    // 약관 종류에 따라 보관 기간이 정해져 있음.
    // 약관 종류는 중복되지 않음
    // String[] privacies;
    String today;
    Map<String, Integer> termsMap;
    
    
    // day는 제외하고, year, month만 비교하기 편하게 합쳐서 계산하고
    // 만약 year, month 합보다 today가 작으면 패스, 같으면 day까지 비교, 크면 체크.
    public int[] solution(String today, String[] terms, String[] privacies) {
        // this.privacies = privacies;
        this.today = today;
        List<Integer> answer = new ArrayList<>();
        
        termsMap = new HashMap<>();
        for(String term: terms){
            String[] tmp = term.split(" ");
            termsMap.put(tmp[0], Integer.parseInt(tmp[1]));
        }
        
        for(int i = 0; i < privacies.length; i++){
            if(isExpired(privacies[i])) answer.add(i + 1);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public boolean isExpired(String privacy){
        int todayYearMonthIntValue = yearMonthToInt(today);
        int privacyYearMonthIntValue = yearMonthToInt(privacy);
        
        
        
        String[] tmp = privacy.split("\\.")[2].split(" ");
        int day = Integer.parseInt(tmp[0]);
        String type = tmp[1];
        
        int expiredYearMonthIntValue = privacyYearMonthIntValue + termsMap.get(type);
        if(todayYearMonthIntValue > expiredYearMonthIntValue) return true;
        else if(todayYearMonthIntValue == expiredYearMonthIntValue && Integer.parseInt(today.substring(8)) >= Integer.parseInt(privacy.substring(8, 10))) return true;
        return false;
    }
    
    public int yearMonthToInt(String yearMonth){
        String[] tmp = yearMonth.split("\\.");
        return (Integer.parseInt(tmp[0]) * 12) + Integer.parseInt(tmp[1]);
    }
}