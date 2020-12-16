def howSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    for num in range(len(numbers)):
        remainder = target - numbers[num]
        result =  howSum(remainder,numbers, memo)
        if result is not None:
            result.append(num)
            memo[target] = result
            return memo[target]

    memo[target] = None
    return None

print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(0, [1,2,3,4]))