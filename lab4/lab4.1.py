def climb_stairs(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    
    if n == 0 or n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    
    return memo[n]

if __name__ == "__main__":
    n = int(input("Шатны тоог оруулна уу: "))  
    result = climb_stairs(n)
    print(f"Хэдэн аргаар авирах аргууд {n} steps: {result}")
