def calculate_minimum_coins(coins, rem, counter):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    if counter[rem - 1] != float("inf"):
        return counter[rem - 1]
    minimum = float("inf")

    for s in coins:
        result = calculate_minimum_coins(coins, rem - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    counter[rem - 1] = minimum if minimum != float("inf") else -1
    return counter[rem - 1]

class Solution:
    def coinChange(self, coins, amount):
        if amount < 1:
            return 0
        return calculate_minimum_coins(coins, amount, [float("inf")] * amount)

if __name__ == "__main__":
    coins_input = input("Зоосуудыг оруулна уу: ")
    coins = list(map(int, coins_input.split(',')))

    amount = int(input("хэмжээг оруулна уу: "))

    solution = Solution()
    result = solution.coinChange(coins, amount)

    if result == -1:
        print(f"It is not possible to make change for {amount} with the given coin denominations.")
    else:
        print(f"{amount} болгохын тулд зоосны хамгийн бага тоо бол: {result}")