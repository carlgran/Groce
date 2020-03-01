#!C:\Python34\Python.exe
# Import modules for CGI handling 
import cgi, cgitb, csv, os
cgitb.enable()

form = cgi.FieldStorage()

store_name = form.getvalue('store_name')
product= form.getvalue('product')
quantity = form.getvalue('quantity')
price = form.getvalue('price')

 

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print("<style>")
print("body {background-image: url('atmarket.jpg');}")
print("h1   {color:white; text-align:center; left:300px; right:100px}")
print("p {color:white}")
print("</style>")
print ("</head>")
print ("<body>")
print ("<h1>Thank you</h1>")
strname="'{}'".format(store_name)
sproduct="'{}'".format(product)
sqtity="'{}'".format(quantity)
sprice=price#"'{}'".format(price)

with open('catalog.csv','r')as f, open('catalog3.csv','w',newline='') as g:
    charti=csv.reader(f, delimiter=',')
    charto=csv.writer(g,delimiter=',')
    lchart=list(charti)
    lstore=lchart[0]
    newpline=[0 for i in range(len(lstore))]
    if strname in lstore:
       istore=lstore.index(strname)
       newpline[0]=sproduct.lower()
       newpline[1]=1
       newpline[2]=sqtity
       newpline[istore]=sprice
       hitt=0
       print(istore)
    for pline in lchart:   
        if sproduct.lower()in pline:
            hitt=hitt+1        
            pline[2]=sqtity
            pline[istore]=sprice
        charto.writerow(pline)
    if hitt==0:
        charto.writerow(newpline)
      
os.remove('catalog.csv')      
os.rename('catalog3.csv','catalog.csv')      

       

print("</body>")





