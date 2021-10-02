import time
from multiprocessing import Process ,Queue
import numpy as np
start_time = time.time()

A = [[1, 2],
    [1, 2]]

B = [[1,2],
    [1,3]]

def innerLoop(i,ans,q):
    for j in range(len(B[0])):
        ans.append(A[i][j] * B[i][j])
    q.put(ans)
        
if __name__ == '__main__':
    

    processes = []
    ans = []
    q = Queue()
    for i in range(len(A)):
        p = Process(target=innerLoop, args=(i,ans,q,))
        processes.append(p)
        p.start()
    for p in processes: p.join()
    
    res=np.empty(len(A),dtype='object')
    a = np.zeros(shape=(len(A),len(B[0])))
    
    for i in range(len(res)):
        res[i]=q.get()
        
    for i in  range(len(a)):
        a[i] = res[i]  #res[len(a)-(i+1)]   
    print("--- %s seconds ---" % (time.time() - start_time), a)