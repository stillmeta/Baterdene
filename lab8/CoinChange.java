import java.util.Arrays;

public class CoinChange {

    public int coinChange(int[] coins, int amount) {
        int[] memo = new int[amount + 1];
        Arrays.fill(memo, -1);
        memo[0] = 0;

        return coinChangeHelper(coins, amount, memo);
    }
    
    private int coinChangeHelper(int[] coins, int amount, int[] memo) {
        if (amount < 0) {
            return -1;
        }
        if (memo[amount] != -1) {
            return memo[amount];
        }

        int minCoins = Integer.MAX_VALUE;

        for (int coin : coins) {
            int res = coinChangeHelper(coins, amount - coin, memo);
            if (res >= 0 && res < minCoins) {
                minCoins = res + 1;
            }
        }

        memo[amount] = (minCoins == Integer.MAX_VALUE) ? -1 : minCoins;
        return memo[amount];
    }

    public static void main(String[] args) {
        CoinChange cc = new CoinChange();

        int[] coins1 = {1, 2, 5};
        int amount1 = 11;
        int result1 = cc.coinChange(coins1, amount1);
        System.out.println("Minimum coins required: " + result1);

        int[] coins2 = {2};
        int amount2 = 3;
        int result2 = cc.coinChange(coins2, amount2);
        System.out.println("Minimum coins required: " + result2);

    }
}