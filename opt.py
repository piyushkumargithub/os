def optimal_page_replacement(arr, frame):
    pf = 0
    page = []
    for i in range(frame):
        page.append(-1)
    for i in range(len(arr)):
        flag = 0
        for j in range(frame):
            if (page[j] == arr[i]):
                flag = 1
                break
        
        if flag == 0:
            fault = False
            new_slot = -1
            for s in range(frame):
                if page[s] == -1:
                    fault = True
                    new_slot = s
            
            if not fault:
                max_future = 0
                max_future_s = -1
                for s in range(frame):
                    if page[s] != -1:
                        found = False
                        for j in range(i, len(arr)):
                            if arr[j] == page[s]:
                                found = True
                                if j > max_future:
                                    max_future = j
                                    max_future_s = s
                                break
                        if not found:
                            max_future_s = s
                            break
                fault = True
                new_slot = max_future_s
            pf += 1
            page[new_slot] = arr[i]
    
    return pf

if __name__=='__main__':

    pages=list(map(int,input("Enter pages separated by space").split()))
    frame = int(input("Enter the no. of frames: "))
    
    PF=optimal_page_replacement(pages,frame)
    print("page fault:" ,PF)
    print("miss ratio:" ,round(PF/len(pages),2))
    print("hit ration:",round(1-PF/len(pages),2))
