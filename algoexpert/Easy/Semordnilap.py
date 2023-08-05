# O(n*m) time| O(n*m) space, n = size of 'words', m = size of the longest word
def semordnilap(words):
    # Write your code here.
    wordsSet = {word for word in words}
    sPairList = []
    for word in words:
        drow = word[::-1]
        if word != drow and drow in wordsSet:
            sPairList.append([word, drow])
            print(wordsSet)
            wordsSet.remove(drow)
            print(wordsSet)

    return sPairList

print(semordnilap(['diaper', 'test', 'abc', 'repaid']))