import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        
        for(int i = 0; i < arr1.length; i++){
            List<Integer> list = new ArrayList<Integer>();
            for(int j = 0; j < arr1[0].length; j++){
                list.add(arr1[i][j] + arr2[i][j]);
            }
            answer.add(list);
        }
        
        int[][] result = new int[answer.size()][];
        for (int i = 0; i < answer.size(); i++) {
            List<Integer> row = answer.get(i);
            result[i] = new int[row.size()];
            for (int j = 0; j < row.size(); j++) {
                result[i][j] = row.get(j);
            }
        }

        return result;
    }
}