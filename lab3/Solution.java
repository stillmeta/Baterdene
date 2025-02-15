import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        // Allow user to enter the size and elements of the array
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();

        int[] nums = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }

        // Create an instance of Solution and call sortArray method
        Solution solution = new Solution();
        solution.sortArray(nums);

        System.out.println("Sorted array:");
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void mergeSort(int[] array, int low, int high) {
        if (low >= high) {
            return;
        }
        int mid = low + (high - low) / 2;
        mergeSort(array, low, mid);
        mergeSort(array, mid + 1, high);
        merge(array, low, mid, high);
    }

    private void merge(int[] array, int low, int mid, int high) {
        int n1 = mid - low + 1;
        int n2 = high - mid;
        int[] leftPart = new int[n1];
        int[] rightPart = new int[n2];

        System.arraycopy(array, low, leftPart, 0, n1);
        System.arraycopy(array, mid + 1, rightPart, 0, n2);

        int p1 = 0, p2 = 0, writeInd = low;
        while (p1 < n1 && p2 < n2) {
            if (leftPart[p1] <= rightPart[p2]) {
                array[writeInd++] = leftPart[p1++];
            } else {
                array[writeInd++] = rightPart[p2++];
            }
        }

        while (p1 < n1) {
            array[writeInd++] = leftPart[p1++];
        }

        while (p2 < n2) {
            array[writeInd++] = rightPart[p2++];
        }
    }
}
