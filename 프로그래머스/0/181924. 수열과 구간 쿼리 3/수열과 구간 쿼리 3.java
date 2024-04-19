class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // 원본 배열 arr에서 queries의 원소 i, j를 각각 바꿔서 진행함.
        // 쿼리 진행 후 결과 값을 리턴.
        for(int[] querie: queries){
            int i = querie[0];
            int j = querie[1];
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        return arr;
    }
}