txt = '''
a v k l A a
'''
print(txt.split())

word_count = {}

for word in txt.lower().split():
    if word in word_count:
        word_count[word]+= 1
    else:    
        word_count[word] = 1
print(word_count)
