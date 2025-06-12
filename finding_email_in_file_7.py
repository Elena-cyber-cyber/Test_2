"""fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:continue
    print(line)"""

"""abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)"""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
    if len(words) > 2:  # Убедимся, что список достаточно длинный
        print(words[2])

fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    print(line.rstrip())        
    

        
    
