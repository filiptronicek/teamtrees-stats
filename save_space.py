    # -*- coding: utf-8 -*-
_file = open("data/combined-data.csv", "r")
text = _file.readlines()
for i, j in enumerate(text):
    if i % 2 == 0:
        del text[i]
           
_file.close()
_file = open("file.txt", "w")
for i in text:
    _file.write(i)
        
_file.close()