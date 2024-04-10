import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            System.out.print(str);
        }
    }
    public static void main2(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        String answer = "";
        for(int i = 0; i < n; i++){
            answer += str;
        }
        System.out.println(answer);
    }
}