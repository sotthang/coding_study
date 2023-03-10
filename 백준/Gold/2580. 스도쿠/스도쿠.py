import sys

def dfs(idx):
    if idx >= len(node):
        return True   
    i,j = node[idx]
    r,c = (i //3) * 3, (j //3) * 3
    nums1 = set([1,2,3,4,5,6,7,8,9])
    nums2 = set(sudoku[i] + [sudoku[k][j] for k in range(9)] +sudoku[r][c:c+3] + sudoku[r+1][c:c+3] + sudoku[r+2][c:c+3])
    for num in nums1 - nums2:
        sudoku[i][j] = num
        if dfs(idx+1): return True
        sudoku[i][j] = 0
    return False
        
sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
node = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

dfs(0)

for x in range(9):
    print(*sudoku[x])