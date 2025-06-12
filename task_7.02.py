fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.00
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    line = line.rstrip()
    atros = line.find('0')
    lego = float(line[atros:])
    print(lego)
    count = count +1
    print(count)
    total = total + lego
avr = float(total) / float(count)   
print("Average spam confidence: ", avr )

