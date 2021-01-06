def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count += island_detect(grid, i, j)
    return count

def island_detect(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
        return 0
    grid[i][j] = "0"
    island_detect(grid, i-1, j)
    island_detect(grid, i, j-1)
    island_detect(grid, i+1, j)
    island_detect(grid, i, j+1)
    return 1


if __name__ == "__main__":
    list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(list))