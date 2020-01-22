import csv
address=str()
address=input()
#address='/home/kazem/project/data.csv'
with open (address) as csv_file:
    csv_reader=csv.reader(csv_file ,delimiter=',')
    line_count=0
    l=list()
    d=dict()
    l2=list()
    for row in csv_reader:
               
        if line_count > 1:

            l.append((row[2],row[3][11:]) )
            
            
        line_count +=1


i=len(l)-1

while i >= 0 :
    
    x=l[i][0]
    k=0
    for j in reversed(range(0,len(l))):

        if l[j][0] == x :

            l2.append(l[j][1])
            l.pop(j)
            k+=1

    
    i=len(l)-1  
    d[x]=l2[(len(l2)-k):]        


for i in d:
    
    
    print('\n',i)
    print(d[i])
    print("\n***********************************************************")
    

   
    
       
       


  
  
    