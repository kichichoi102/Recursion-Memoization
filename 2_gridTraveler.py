def gridTraveler(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print(gridTraveler(3,3))
print(gridTraveler(0,3))
print(gridTraveler(1,3))
print(gridTraveler(2,1))