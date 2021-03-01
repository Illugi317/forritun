with open('test.bin','wb+') as f:
    for x in range(5):
        f.write(x)
    f.close()
