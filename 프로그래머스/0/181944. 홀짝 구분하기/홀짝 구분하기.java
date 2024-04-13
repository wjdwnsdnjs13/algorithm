import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String answer = Integer.toString(n) + ((n%2 == 1)?" is odd":" is even");
        System.out.println(answer);
    }
}