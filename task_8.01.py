fname = input("Enter file name: ")
fh = open(fname)
inp =fh.read()
words = inp.split()
lst = list()
for word in words:
    if word not in lst:
        lst.append(word)
print(sorted(lst))        