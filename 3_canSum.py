def canSum(target, numbers):
    if target == 0:
        return True
    if target < 0:
        return False
    
    for num in range(len(numbers)):
        remainder = target - numbers[num]
        return canSum(remainder, numbers)

    return False


print(canSum(7, [7,3,1]))
print(canSum(7, [1,2,3]))
print(canSum(5, [7, 14]))