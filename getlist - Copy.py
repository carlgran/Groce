#!C:\Python34\Python.exe
# Import modules for CGI handling 
import cgi, cgitb, csv
cgitb.enable()

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
print("h1   {color:blue; text-align:center; background-color:white; left:300px; right:100px}")
print("p    {color:green;}")
print("table, th, td {border: 1px solid black;border-collapse: collapse;text-align: center;left:300px; right:100px}")
print(".center {margin: auto; width: 50%; border: 3px solid green; padding: 10px;}")
print("</style>")
print ("<title>Shoplist - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h1>Your list</h1>")
print("<div  style='text-align:center'>")
print("<textarea name='shoplist' rows='10' cols='30'>%s</textarea style='backgound-color:Lightgreen'>" %(shoplist))
print("</div>")
 
print ("<h1> List</h1>")
with open('shlist.txt','w')as g:
    g.write(shoplist)
print("<table class='center' style='background-color: white; width:500px'>")
print("<tr><th style= 'width:200px'>Product</th><th style= 'width:100px'>Lowest price</th><th style= 'width:100px'>store</th>")
            
with open('catalog.csv','r')as f:
   stori=f.readline()
   stores=stori.split()
with open('sgst.lst','w') as h:
    with open('shlist.txt','r')as f:
        shlist=f.readlines()        
        for line in shlist:
            sitem=line.split()
#            print("<p>%s %s"%(sitem,len(sitem)))
            with open('catalog.csv','r')as f:
                chart=f.readlines()
                for line in chart:
                    entrs=line.split()
#                    print("<p>%s"%(entrs))
                    if len(sitem)>0 and " "sitem[0] in entrs:
                        minentrs=entrs.index(min(entrs))
#                        print("<p>%s %s %s"%(sitem[0],min(entrs),minentrs))
                        
                        print("<tr border ='1'><td style= 'width:200px'> %s </td>"%(sitem[0]))
                        print("<td style= 'width:100px'>$ %s</td>"%(min(entrs)))
                        print("<td>%s</td></tr>"%(stores[minentrs]))
print("</table>")
print("</body>")                        
print ("</html>")
