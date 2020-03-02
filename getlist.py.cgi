#!C:\Python35-32\python.exe
# Import modules for CGI handling 
import cgi, cgitb, csv,re
cgitb.enable()
# defining indexing function
def allindex(list, item):
    return [index for index in range(len(list)) if list[index] == item]

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
shoplist = form.getvalue('shoplist')
# Save Data

           
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print("<style>")
print("body {background-image: url('atmarket.jpg');}")
print("h1   {color:white; text-align:center; left:300px; right:100px}")
print("p    {color:green;}")
print("table, th, td {border:2px solid #ccc; ;border-collapse: separate; border-radius: 1px; background-color: white;")
print("text-align: center;left:300px; right:100px; }")
print("table {background-image: url('sheet.jpg'); background-size: contain}")
print(".center {margin: auto; width: 50%; padding: 10px;}")
print("textarea {")
print("    width: 20%;")
print("    height: 150px;")
print("    padding: 12px 20px;")
print("    box-sizing: border-box;")
# print("    border: 2px solid #ccc;")
print("    border-style: none;")
print("    border-radius: 4px;")
print("    background-color: #f8f8f8;")
print("    font-size: 16px;")
print("    resize: none;")
print("    background-image: url('sheet.jpg');")
print("    background-size: cover;")
print("}")
print("</style>")
print ("<title>Shoplist - Second CGI Program</title>")


print ("</head>")

print ("<body>")
print ("<h1>Your list</h1>")
print("<div  style='text-align:center'>")
print("<form  method='post'>")

# Filing the input shoplist in shlist.txt
with open('shlist.txt','w')as g:
    g.write(shoplist)    
    
print("<textarea name='shoplist' rows='10' cols='30'>")
# Displaying list and allowing modification
with open ('shlist.txt','r') as g:
    for line in g:
        if len(line) is not 1:
            rtem=line.strip()
            ritem="'{}'".format(rtem)
            print("%s"%(ritem.replace("'","")))
print("</textarea ><br><br>")
print("<input type='submit' value='Submit'>")
print("</form>")
print("</div>")


if  "quick_list":
# Output
    
    print ("<h1> Route List</h1>")
    print("<table class='center' style='width:500px;'>")
    print("<tr>")
    print("<th style= 'width:200px'>Product</th>")
    print("<th style= 'width:100px'>Lowest Price</th>")
    print("<th style= 'width:100px'>Store</th>")
    
    # Retrieving data from spreadsheet(catalog.csv)   with stores and pricing info on available items
    with open('catalog.csv','r')as f:
        chart=csv.reader(f, delimiter=',')
        lchart=list(chart)
        store=lchart[0] #creates store list
        del store[0];
        del store[0];
        del store[0];
        titems=0 # counts item requested
        store_tot=[0 for i in range(len(store))] # List total prices for shop list on each store
        store_ct=[0 for i in range(len(store))]# Counts items available on each store
    #    
        with open ('shlist.txt','r') as g:
            shlist=g.readlines() # Reads the input list as a collection of 1 item lists
            for line in shlist:
                if len(line) is not 1:
                    stem=line.strip()
                    sitem="'{}'".format(stem)
                    print("<tr><td style= 'width:200px'> %s </td>"%(sitem.replace("'",""))) #prints input in output field
                    minprice='****'# starts output data 
                    minstore='****'
                    minunt=''
                    crrncy=''
                    titems=titems+1
                    for pline in lchart:
                        if sitem.lower() in pline: # finds price lines for the requested items
                            pduct = pline[0]
                            qtity = pline[1]
                            unt = pline[2]
                            del pline[0];
                            del pline[0];
                            del pline[0];
                            price=[float(x) for x in pline ]
                            store_tot=[sum(x) for x in zip(store_tot, price)]
                            inc=[1 if float(x)>0 else 0 for x in price ]
                            store_ct =[sum (x) for x in zip(store_ct,inc)]                      
                            if float(min(price))> 0: #Excludes stores with unavailable items for which a 0 price was assigned
                                minprice=min(price)
                            else:
                                rprice=[ip for ip in price if ip>0]
                                minprice=min(rprice)                        
                                
                            minstore=[store[i] for i in allindex(price,minprice)] # Lists all the stores with the lowest price for the requested item
                            minunt=unt
                            crrncy='$'
                           
                    print("<td style= 'width:100px'>%s %s %s</td>"%(crrncy,"{:10.2f}".format(minprice),minunt.replace("'",""))) #Print output table
                    print("<td><a>%s</a></td></tr>"%(", ".join(str(x.replace("'","")) for x in minstore)))
                        
    print("</table>")
    print("<br>")
    
    print("<table class='center' style='width:500px;'>")
    print("<tr>")
    print("<th style= 'width:200px'>Cheapest Stores</th>")
    print("<th style= 'width:100px'>Total</th>")
    print("<th style= 'width:100px'>% of items</th>")
    print("</tr>")
    print("<tr>")
    lowest_total=min(store_tot)
    cheapestore=[store[i] for i in allindex(store_tot,lowest_total)]
    def nitems(stori):
        return store_ct[store.index(stori)]
    def pctitems(stori):
        return nitems(stori)/titems*100
    def storetot(stori):
        return store_tot[store.index(stori)]
    
    for i in range(len(cheapestore)):
        if pctitems(cheapestore[i]) > 10:
            print("<td style= 'width:200px'> %s</td>"%(cheapestore[i].replace("'","")))
            print("<td style= 'width:100px'>$ %s / units</td>"%("{:10.2f}".format(lowest_total)))
            print("<td>%s%%</td></tr>"%( "{:10.1f}".format(pctitems(cheapestore[i]))))
            
    tstore=[x for x in store if pctitems(x)==100]
    if len(tstore)>0:
        tstore_tot=[storetot(x) for x in tstore]
        low_total=min(tstore_tot)
        cheapstore=[tstore[i] for i in allindex(tstore_tot,low_total)]        
        
        for i in range(len(cheapstore)):
            print("<td style= 'width:200px'> %s</td>"%(cheapstore[i].replace("'","")))
            print("<td style= 'width:100px'>$ %s / units</td>"%("{:10.2f}".format(low_total)))
            print("<td>%s%%</td></tr>"%( "{:10.1f}".format(pctitems(cheapstore[i]))))
    print("</table>")
    
if "detailed_list":
    print("<table>")
    print("<th>Product</th>")
    print("<th>Brand<th>")
    print("<th>Origin<th>")
    print("</table>")   
   
print("</body>")                        
print ("</html>")
