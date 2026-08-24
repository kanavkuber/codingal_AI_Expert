def match_words(words):
    ctr = 0
    l = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            l.append(word)
    print("List of words with same first and last characters: ", l)
    return ctr

count = match_words(['ab', 'a', 'abba', 'accsd', 'amma', '1331', 'xxxxx'])
print ("Number of words with same first and last characters: ", count)