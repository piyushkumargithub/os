from queue import Queue  
  

def pageFaults(pages, n, capacity): 
      
    s = set()  
  
    indexes = Queue()  
  
    page_faults = 0
    for i in range(n): 
           
        if (len(s) < capacity): 
                    
            if (pages[i] not in s): 
                s.add(pages[i])  
                page_faults += 1         
                indexes.put(pages[i]) 
  
    
        else:            
            if (pages[i] not in s): 

                val = indexes.queue[0]  
                indexes.get()   
                s.remove(val)    
                s.add(pages[i])  
                indexes.put(pages[i])                   
                page_faults += 1  
    return page_faults 
  
 
if __name__ == '__main__': 
    # pages = [7, 0, 1, 2, 0, 3, 0,  
    #             4, 2, 3, 0, 3, 2]
    # frame = 4
    pages=list(map(int,input("Enter pages separated by space").split()))
    frame = int(input("Enter the no. of frames: "))  
    n = len(pages)  
    
    PF=pageFaults(pages, n, frame)
    print("page fault:" ,PF)
    print("miss ratio:" ,round(PF/len(pages),2))
    print("hit ration:",round(1-PF/len(pages),2))