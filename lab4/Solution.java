import java.util.Scanner;

class Solution {
    public int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int prev = 1, curr = 1;
        for (int i = 2; i <= n; i++) {
            int temp = curr;
            curr = prev + curr;
            prev = temp;
        }
        return curr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Шатны тоог оруулна уу: ");
        int n = scanner.nextInt();
        
        Solution solution = new Solution();
        int result = solution.climbStairs(n);
        System.out.println("Авирах тодорхой арга замуудын тоо " + n + " stairs: " + result);
    }
}
