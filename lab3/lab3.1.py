class Solution:
    def majorityElement(self, nums):
        def majority_element_rec(start, end):
            if start == end:
                return nums[start]

            mid = (start + end) // 2
            left_majority = majority_element_rec(start, mid)
            right_majority = majority_element_rec(mid + 1, end)

            if left_majority == right_majority:
                return left_majority

            left_count = sum(1 for i in range(start, end + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(start, end + 1) if nums[i] == right_majority)

            return left_majority if left_count > right_count else right_majority

        return majority_element_rec(0, len(nums) - 1)

if __name__ == "__main__":
    # Define a list of numbers instead of taking input
    nums = [3, 2, 3]  # Example list
    solution = Solution()
    result = solution.majorityElement(nums)
    print(f"Олонх элемент нь: {result}")