def x_matrix(grid):
    for i in range(len(grid)):
        print(sum(grid[i]))
        for j in range(len(grid[i])):
            # print(sum(grid[j],grid[~j]))
            if( grid[i][j]!=0 or grid[i][~j]!=0 )and sum(grid[i])-sum(grid[i][j],grid[i][~j])==0:
                return True
    return False

grid=[[5,7,0],[0,3,1],[0,5,0]]
print(x_matrix(grid))