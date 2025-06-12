cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 15
cabinet['spring']= 75
print(cabinet)
counts = dict()
names =['cwen','csev', 'zqian','cwen','csev']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)            
        
