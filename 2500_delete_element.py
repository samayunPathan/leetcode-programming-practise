def max_ele(grid):
    length=len(grid);s=0
    while True:
        c_m=[]
        if len(grid[0])==0:
            break
        for i in range(length):
            c_e=max(grid[i])
            grid[i].remove(c_e)
            c_m.append(c_e)
        s+=max(c_m)
    return s


            


grid=[[1,2,4],[3,3,1]]
print(max_ele(grid))

g=[[1],[2]]
m=max(g[0])
print(m)
