import java.util.*;

class Solution {
    // wallpaper : 바탕화면의 상태를 나타낸 문자열 배열
//     "." : 빈칸
//     "#" : 파일이 있는 칸
        
//     최소한의 드래그 거리로 모든 파일을 선택해서 지우려고 함.
//     x와 y 최솟값 부터 x, y 최댓값까지 거리 구하면 되는 거 아님?
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        List<Integer> xList = new ArrayList<Integer>();
        List<Integer> yList = new ArrayList<Integer>();
        
        int i = 0;
        for(String ss: wallpaper){
            String[] s = ss.split("");
            for(int j = 0; j < s.length; j++){
                if(s[j].equals("#")){
                    xList.add(i);
                    yList.add(j);
                }
            }
            i++;
        }
        Collections.sort(xList);
        Collections.sort(yList);
        answer[0] = (xList.get(0));
        answer[1] = (yList.get(0));
        answer[2] = (xList.get(xList.size() - 1)) + 1;
        answer[3] = (yList.get(yList.size() - 1)) + 1;
        
        return answer;
    }
}