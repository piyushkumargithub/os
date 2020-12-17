# frame = 4 
# pages = [ 7, 0, 1, 2, 0, 3, 0, 
#                 4, 2, 3, 0, 3, 2] 
pages=list(map(int,input("Enter pages separated by space").split()))
frame = int(input("Enter the no. of frames: "))

s = []  
  
pageFaults = 0

for i in pages: 
  
    
    if i not in s: 
  
        # Check if the list can hold equal pages 
        if(len(s) == frame): 
            s.remove(s[0]) 
            s.append(i) 
  
        else: 
            s.append(i) 
       
        pageFaults +=1
    else: 
 
        s.remove(i) 
       
        s.append(i) 
      
PF=pageFaults
print("page fault:" ,PF)
print("miss ratio:" ,round(PF/len(pages),2))
print("hit ration:",round(1-PF/len(pages),2))