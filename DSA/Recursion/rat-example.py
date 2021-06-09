"""
Given a amze a rat is at starting position (0,0) we have to find the no of ways
in which it can reach Destination.
"""

def noofways(x,y,n,m):

    if x >= n:
        return 0
    if y >= m:
        return 0  
    if x==n-1 and y==m-1:
        return 1    

    ans = noofways(x,y+1,n,m) + noofways(x+1,y,n,m,grid)
    return ans

if __name__=="__main__":
    grid = [[1,0,0,1],[1,0,0,0],[1,1,0,0]]        
    n = len(grid)
    m = len(grid[0])
    print((noofways)(0,0,n,m,grid))