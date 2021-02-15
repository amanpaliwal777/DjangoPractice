import wikipedia
keywordss = input('Enter keyword to search: ')
a = wikipedia.search(keywordss)
a = wikipedia.summary(a)
print(a)