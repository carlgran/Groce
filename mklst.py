#Third python mudule
# make lists module
import csv

#print(sitem, len(sitem))
with open('catalog.csv','r')as f:
	chart=csv.reader(f, delimiter=',')
	lchart=list(chart)
	store=lchart[0]
	del store[0];
	del store[0];
	del store[0];
	print(store)
	store_tot=[0 for i in range(len(store))]
	with open ('shlist.txt','r') as g:
		shlist=g.readlines()
		for line in shlist:
			if len(line) is not 1:
				stem=line.strip()
				sitem="'{}'".format(stem)
			for pline in lchart:
		#print(row[0])
				if sitem.lower() in pline:
					pduct = pline[0]
					qtity = pline[1]
					unt = pline[2]
					del pline[0];
					del pline[0];
					del pline[0];    
					price=[float(x) for x in pline ]
					store_tot=[sum(x) for x in zip(store_tot, price)]
					print (pduct)
print(min(store_tot))
print(store[store_tot.index(min(store_tot))])
	

