public class AggregateAnalysis {

    public static double calculateAmortizedCost(int n) {
        int totalCost = 0;

        for (int i = 1; i <= n; i++) {
            if (isPowerOfTwo(i)) {
                totalCost += i;
            } else {
                totalCost += 1;
            }
        }

        return (double) totalCost / n;
    }

    private static boolean isPowerOfTwo(int x) {
        return (x > 0) && ((x & (x - 1)) == 0);
    }

    public static void main(String[] args) {
        int n = 16; // Example input
        double amortizedCost = calculateAmortizedCost(n);

        System.out.println("For n = " + n + ", the amortized cost is: " + amortizedCost);
    }
}