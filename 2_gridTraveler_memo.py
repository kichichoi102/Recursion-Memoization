def gridTraveler(m, n, memo = {}):
    key = (m,n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
    return memo[key]

print(gridTraveler(3,3))
print(gridTraveler(0,3))
print(gridTraveler(20,40))