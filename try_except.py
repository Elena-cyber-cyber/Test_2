inp = input('Enter the temperature in Farengeit: ')
try:
    fahr = float(inp)
    geo = (fahr - 32.0) * 5.0 / 9.0
    print(geo)
except ValueError:
    print('Enter a valid number')

            

            
