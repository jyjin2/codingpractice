from collections import deque

simulation = 1

while True:
    line = input().strip()
    # end of the input
    if line == '0':
        break
    
    # 1. input 쪼개기
    N, seq = line.split()
    N = int(N)

    dq = deque()
    
    print(f"Simulation {simulation}")
    for c in seq:
        # 2. ! -> 현재 content return
        if c == '!':
            print(''.join(dq))
        else:
            # seq access
            if c in dq:     # if alrd in cache
                dq.remove(c)    # remove and move it to the end(MRU)
            elif len(dq) == N:  # when cache is full
                dq.popleft()    # remove LRU
            
            dq.append(c)        # add data(MRU) to the end
            
    simulation += 1