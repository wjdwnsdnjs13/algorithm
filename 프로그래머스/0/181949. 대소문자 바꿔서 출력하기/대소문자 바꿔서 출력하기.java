import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] a = sc.next().split("");
        String answer = "";
        for(String n: a){
            answer += (n.matches("[a-z]")?n.toUpperCase():n.toLowerCase());
        }
        System.out.println(answer);
    }
}