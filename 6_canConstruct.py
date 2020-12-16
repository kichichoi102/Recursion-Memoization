def canConstruct(target, wordBank):
    if target == "":
        return True
    
    for word in range(len(wordBank)):
        if target.find(wordBank[word]) == 0:
            suffix = target[len(wordBank[word]): len(target)]
            if canConstruct(suffix, wordBank) == True:
                return True

    return False

# Brute Force
# time = O(n**m)
# storage = O(m**2)

# Memoization
# time = O(n*m**2)
# Storage = O(M**2) 

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))



