#To find Completion Time
def finding_CT(at,bt):
    ct = list()
    ct.append(at[0] + bt[0])
    for i in range(1, len(bt)):
        ct.append(ct[i - 1] + bt[i])
    return ct

#To find TurnAround Time
def finding_TAT(at, ct):
    tat = list()
    for i in range(len(at)):
        tat.append(ct[i] - at[i])
    return tat

#To find Waiting Time
def finding_WT(tat,bt):
    wt = list()
    for i in range(len(bt)):
        wt.append(tat[i]-bt[i])
    return wt


if __name__ == "__main__":
    
    #n = int(input("no of processes "))
    
    arrival_time = list(map(int,input("enter arrival times with spaces ").split()))
    burst_time = list(map(int,input("enter burst times with spaces ").split()))


    assert len(arrival_time)==len(burst_time),"no of arrival and burst time entered should be equal"
    #sorting on basis of arrival time
    ab=(zip(arrival_time,burst_time))
    #using lambda funtion to set sorting on basis of only arrival time (so that when arrival time of multiple processes
    # are same they stay according to how they were enter i.e according to process id)
    ab=sorted(ab,key=lambda ab:ab[0])
    #print(ab)

    arrival_time=[x for x,y in ab]
    burst_time=[y for x,y in ab]
    #printing sorted arrival time
    print(arrival_time)
    #printing corresponding burst time
    print(burst_time)

    
    #calling funtion to calculate Completion Time
    CT = finding_CT(arrival_time, burst_time)
    print(" Completion Time ")
    print(CT)
    print("Average Completion Time: ",(sum(CT)/len(burst_time)))
    #calling funtion to calculate TurnAround Time
    TAT = finding_TAT(arrival_time, CT)
    print(" TurnAround Time ")
    print(TAT)
    print("Average TurnAround Time: ",(sum(TAT)/len(burst_time)))
    #calling funtion to calculate Waiting Time
    WT=finding_WT(TAT,burst_time)
    print(" Waiting Time ")
    print(WT)
    print("Average Waiting Time: ", (sum(WT) / len(burst_time)))
