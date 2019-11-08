fout=open("data/new-data.csv","a")
for line in open("data/2019.11.01-count.csv"):
    fout.write(line)
for num in range(2,9):
    f = open("data/2019.11.0"+str(num)+"-count.csv")
    f.__next__() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()