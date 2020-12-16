def countConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    
    counter = 0

    for word in range(len(wordBank)):
        if target.find(wordBank[word]) == 0:
            suffix = target[len(wordBank[word]) : len(target)]
            result = countConstruct(suffix, wordBank, memo)
            memo[target] = result
            counter += memo[target]

    return counter

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
