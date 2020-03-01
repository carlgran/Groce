
import csv, re
# with open ('catalog.csv',newline='') as csvfile:
#    spamreader = csv.reader(csvfile,delimiter=' ')
#    for line in spamreader:
# #      print(line)
with open ('shlist.txt','r') as g:
   shlist=g.readlines()
   for line in shlist:
      if len(line) is not 1:
         stem=line.strip()
         sitem="'{}'".format(stem)
         #print(sitem, len(sitem))
         with open('catalog.csv','r')as f:
            chart=csv.reader(f, delimiter=',')
            lchart=list(chart)
            store=lchart[0]
            for line in lchart:
               #print(row[0])
               if sitem in line:
                  del line[0];
                  del line[0];
                  price=line 
                  print (sitem.replace("'",""))                  
                  print(min(price),store[2+price.index(min(price))].replace("'",""))
with open('catalog.csv','r')as f:
   chart=csv.reader(f, delimiter=',')
   lchart=list(chart)                  
   print(lchart[0][0])                  
