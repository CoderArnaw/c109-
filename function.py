def countwordsfromfile():
    filename=input("Enter the name of the file")
    numberofwords = 0
    f=open(filename)
    for line in f:
        words=line.split()
        numberofwords = numberofwords+len(words)

    print(numberofwords)
countwordsfromfile()
