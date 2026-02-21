myString = "Python Is A Powerful And Versatile Language."
print(myString)
wordList = myString.split()
wordList = sorted(wordList,reverse=True)
print(wordList)
wordList = [word.lower() for word in wordList]
print(wordList)