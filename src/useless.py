def useless_loop():
    i = 1
    while True:
        if i % 7 != 0:
            print(i)
        else:
            break
        i += 1
