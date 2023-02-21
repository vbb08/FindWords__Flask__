def testing():
    fh=open('words.txt')
    for line in fh:
        line=line.rstrip()
        print(line)
testing()
