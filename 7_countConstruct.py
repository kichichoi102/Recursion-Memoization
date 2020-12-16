def countConstruct(target, wordBank):
    if target == "":
        return 1

    count = 0

    for word in range(len(wordBank)):
        if target.find(wordBank[word]) == 0:
            suffix = target[len(wordBank[word]) : len(target)]
            numWays = countConstruct(suffix, wordBank)
            count += numWays

    return count

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e",
#     "ee",
#     "eee",
#     "eeee",
#     "eeeee",
#     "eeeeee"
# ]))


