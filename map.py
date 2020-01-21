import csv

with open ('data.csv') as csv_file:
    csv_reader=csv.reader(csv_file ,delimiter=',')
    line_count=0
    l=list()
    d=dict()
    l2=list()
    for row in csv_reader:
               
        if line_count > 1:

            l.append((row[2],row[3][11:]) )
            #d[row[2]]=row[3][11:]
            
        line_count +=1
print(l)




i=len(l)-1

while i > 0 :
    
    x=l[i][0]

    for j in reversed(range(0,len(l))):

        if l[j][0] == x :

            l2.append(l[j][1])
            l.pop(j)
    if i == 0 : 
        break
    i=len(l)-1       
    print(i)
    print(len(l))
    print(l2,len(l2))
    
            
 
        


  

    #d[l[i][0]]=l2

   

  
    