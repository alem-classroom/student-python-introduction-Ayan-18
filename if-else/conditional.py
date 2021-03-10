num = int(input())

if num > 0:
    print(True)
elif num % 2 == 0:
    print(True)
elif num > 0 and num % 2 == 0:
    print(True)
elif num > 0 or num % 2 == 0:
    print(True)
else:
    print(False)
