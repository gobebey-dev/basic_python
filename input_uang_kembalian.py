uang = input('uang kamu: ')
utang = input('utang kamu: ')

total = int (uang) - int(utang)

print('sisa uang: ', total)
if total > 0:
    print('kembalian')
else:
    print('gk kembalian uang pas')