def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestArray = None

    for num in range(len(numbers)):
        remainder = targetSum - numbers[num]
        result = bestSum(remainder, numbers)
        if result is not None:
            result.append(numbers[num])
            if shortestArray == None or len(result) < len(shortestArray):
                shortestArray = result

    return shortestArray

# Brute force
# time = O(n**m * m)
# Storage = O(m^2)

# Memoization
# time = O(m*n*m) = O(m**2 * n)
# Storage = (m**2)

print(bestSum(7, [1,2,3]))
print(bestSum(7, [2,3]))
print(bestSum(7, [5,3,4,7]))
print(bestSum(7, [2,4]))
print(bestSum(8, [2,3,5]))
print(bestSum(0, [1,2,3,4]))  