fn = input("Enter file name: ")
fh = open(fn)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
