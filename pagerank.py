arr = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,1],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ]

num = len(arr)
d = 0.8
num_iterations = 2

pagerank = [1/num]*num

for iteration in range(num_iterations+1):
    print(f"Iteration {iteration}:")
    if(iteration==0):
        pass
    else:
        for i in range(num):
            pr_sum=0
            for j in range(num):
                if(arr[j][i]==1):
                    outgoing = sum(arr[j])
                    pr_sum += pagerank[j]/outgoing
            pagerank[i]= (1-d)+ d * pr_sum
    for i in range(num):
        print(f"Node {i+1}: {pagerank[i]:.4f}")
        
                
