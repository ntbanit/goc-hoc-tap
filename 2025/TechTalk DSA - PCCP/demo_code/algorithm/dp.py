# Fibonacci Problem using Dynamic Programming
def fibonacci(n):
    # Create a DP array to store Fibonacci numbers
    dp = [0] * (n + 1)
    dp[1] = 1  # Base cases: F(0) = 0, F(1) = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 2 dices target 7
# 1 + 6 , 2 + 5 , 3 + 4 

# 

# 10 dices target 14 

# Dice Count Problem using Dynamic Programming
# Count the number of ways to get a sum `target` using a dice (1 to 6)
def dice_count(target):
    # Create a DP array to store the number of ways to get each sum
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 1 way to get sum 0 (no dice rolls)

    for i in range(1, target + 1):
        for dice in range(1, 7):  # Dice values from 1 to 6
            if i - dice >= 0:
                dp[i] += dp[i - dice]

    return dp[target]


# Example Usage
if __name__ == "__main__":
    # Fibonacci Example
    n = 10
    print(f"Fibonacci({n}):", fibonacci(n))

    # Dice Count Example
    target = 7
    print(f"Number of ways to get sum {target} with dice:", dice_count(target))