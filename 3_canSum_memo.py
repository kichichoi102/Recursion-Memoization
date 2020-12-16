def canSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    
    for num in range(len(numbers)):
        remainder = target - numbers[num]
        if canSum(remainder,numbers, memo) == True:
            memo[target] = True
            return True
        return False

    memo[target] = False
    return False


print(canSum(7, [7,3,1]))
print(canSum(7, [1,2,3]))
print(canSum(5, [7, 14]))
