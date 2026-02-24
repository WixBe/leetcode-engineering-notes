class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh=0
        directions = [(0,1),(0,-1),(1,0),(-1,0)] #right, left,down, up

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        minu=0
        while queue and fresh>0:
            minu+=1
            for _ in range(len(queue)):
                x, y=queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>=len(grid) or ny>=len(grid[0]) or grid[nx][ny]==0 or grid[nx][ny]==2:
                        continue
                    queue.append((nx, ny))
                    grid[nx][ny]=2
                    fresh-=1
        return -1 if fresh >0 else minu