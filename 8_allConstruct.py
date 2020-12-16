def allConstruct(target, wordBank):
    if target =="":
        return [[]]

    result = []
    
    for word in range(len(wordBank)):
        if target.find(wordBank[word]) == 0:
            suffix = target[len(wordBank[word]): len(target)]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = map(lambda ways: [wordBank[word], ways], suffixWays)
            result.append(list(targetWays))
            
    return result

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))




