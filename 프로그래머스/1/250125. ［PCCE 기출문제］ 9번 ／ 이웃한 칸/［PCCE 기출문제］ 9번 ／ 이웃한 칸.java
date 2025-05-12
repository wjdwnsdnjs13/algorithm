import java.util.*;

class Solution {
    // 사방으로 같은 색을 찾을거임.
    
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[][] direct = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        String targetColor = board[h][w];
        for(int[] d: direct){
            int dx = h + d[0];
            int dy = w + d[1];
            if(dx < 0 || dy < 0 || dx >= board.length || dy >= board[0].length) continue;
            if(board[dx][dy].equals(targetColor)) answer++;
        }
        return answer;
    }
}