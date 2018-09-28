
while 1:
    if N % 2 == 1:
        print("weird")
        break
    elif N % 2 == 0 and N in range(2, 5):
        print("not weird")
        break
    elif N % 2 == 0 and N in range(5, 21):
        print("weird")
        break
    elif N % 2 == 0 and N > 20:
        print("not weird")
        break
