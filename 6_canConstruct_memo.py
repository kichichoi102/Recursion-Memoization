def canConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in range(len(wordBank)):
        if target.find(wordBank[word]) == 0:
            suffix = target[len(wordBank[word]) : len(target)]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] =  True
                return memo[target]

    memo[target] = False
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

