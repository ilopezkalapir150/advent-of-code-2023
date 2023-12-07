def main():
    # part 1 code
    f = open("input.txt")
    ar = f.readlines()
    times = ar[0].strip().split()
    times = times[1:]
    dist = ar[1].strip().split()
    dist = dist[1:]
    
    # part 2... bad kerning!
    # f = open("input.txt")
    # ar = f.readlines()
    # times = ar[0].strip().split()
    # times[0] = ""
    # for i in range(len(times)-1):
    #     times[0] = times[0] + times[1+i]
    # times = [times[0]]
    # dist = ar[1].strip().split()
    # dist[0] = ""
    # for i in range(len(dist)-1):
    #     dist[0] = dist[0] + dist[1+i]
    # dist = [dist[0]]
    
    trialsCleared = [0]*len(times)
    for i in range(len(times)):
        for j in range(int(times[i])+1):
            if ( j * (int(times[i]) - j) > int(dist[i])):
                trialsCleared[i] += 1
        print("done with times[" + str(i) + "], i got " + str(trialsCleared[i]) + " record-breaking possibilities!")
    
    m = 1
    for i in range(len(trialsCleared)):
        m = m*trialsCleared[i]
        
    print("number of ways i can beat the record: " + str(m))
        
    

main()