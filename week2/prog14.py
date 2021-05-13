fir = int(input())
sec = int(input())
third = int(input())
if fir == sec == third:
    print('3')
elif fir == sec or sec == third or fir == third:
    print('2')
else:
    print('0')
