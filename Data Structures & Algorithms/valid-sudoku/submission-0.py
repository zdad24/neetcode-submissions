class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows for duplicates
        for i in range(9):
            rowseen = set()
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                elif num in rowseen:
                    return False
                else:
                    rowseen.add(num)

        # check columns for duplicates
        for i in range(9):
            columnseen = set()
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                elif num in columnseen:
                    return False
                else:
                    columnseen.add(num)

        # check 3x3
        rows = 0

        for x in range(9):
            block_row = x // 3  # Try this!
            block_col = x % 3   # And this!
    
            rows = block_row * 3
            columns = block_col * 3

            blockseen = set()
            for i in range(rows, rows + 3):
                for j in range(columns, columns + 3):
                    num = board[i][j]
                    if num == ".":
                        continue
                    elif num in blockseen:
                        return False
                    else:
                        blockseen.add(num)

        # valid sudoku
        return True
