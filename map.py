import xlrd 



#address=input('Enter file path :')
tags_name={'005B30DE':'arak  ','005B4433':'motor khaneh','00A4E9AC':'solar panels',
'00A99ADD':'karghah door','0060920D':'anbar malzomat','00746592':'mashonalat edareh',
'007474E4':'gym','00747BBA':'ٔmashinalat behind','00A9ABE0':'oil anbar',
'005B440D':'‍gas station','005B3C1A':'corner tower','00747435':'center tower','00607A0B':'karghah mohavateh'}

address='/home/kazem/project/data2.xls'

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0, 0) 

line_count=0
l=list()
d=dict()
l2=list()
for i in range(0,sheet.nrows):
    
    row=sheet.row_values(i)
    
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
    
    
    print('\n',tags_name[i])
    print(d[i])
    print("\n***********************************************************")
    

   
    
       
       


  
  
    