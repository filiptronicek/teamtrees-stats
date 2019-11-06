from datetime import datetime
date = datetime.now()
countFile = "data/"+date.strftime("%Y.%m.%d")+"-count.csv"
rateFile = "data/"+date.strftime("%Y.%m.%d")+"-rate.csv"
def init(file):
    #We read the existing text from file in READ mode
    src=open(file,"r")
    fline="count,date\n"    #Prepending string
    oline=src.readlines()
    #Here, we prepend the string we want to on first line
    oline.insert(0,fline)
    src.close()
     
     
    #We again open the file in WRITE mode 
    src=open(file,"w")
    src.writelines(oline)
    src.close()
init(countFile)
init(rateFile)