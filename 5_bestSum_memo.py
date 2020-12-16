def bestSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortestArray = None

    for num in range(len(numbers)):
        remainder = target - numbers[num]
        result = bestSum(remainder, numbers, memo)
        if result is not None:
            result.append(numbers[num])
            if shortestArray == None or len(result) < len(shortestArray):
                shortestArray = result
    
    memo[target] = shortestArray
    return shortestArray


print(bestSum(7, [1,2,3]))
print(bestSum(7, [2,3]))
print(bestSum(7, [5,3,4,7]))
print(bestSum(7, [2,4]))
print(bestSum(8, [2,3,5]))
print(bestSum(0, [1,2,3,4]))  