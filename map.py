import csv

with open ('/home/kazem/project/data.csv') as csv_file:
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



  
for i in range(0,len(l)):
    for j in range(0,len(l)): 

        if l[j][0] == l[0][0] :

            l2.append(l[j][1])
            l.pop(j)

        j+=1
        
        if j == len(l): 
            break

    i+=1    
    if i == len(l): 
        break  

    d[l[i][0]]=l2

    l2.clear()

  
    