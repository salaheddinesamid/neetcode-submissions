class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        duplicate = False

        # verify of the rows does not contain duplicates
        for i in range(0, len(board)): # index from 0 -> 9 (r(i))
            row_seen = set()
            for j in range(0, len(board[i])):
                current = board[i][j]

                if current == ".":
                    continue

                if current in row_seen:
                    return False
                row_seen.add(current)

        # verify the columns:
        for i in range(0, len(board)):
            col_seen = set()

            for j in range(0, len(board[i])):
                current = board[j][i]

                if current == ".":
                    continue
                if current in col_seen:
                    return False
                
                col_seen.add(current)

        # verify 3x3 boxes:
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_seen = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        current = board[i][j]

                        if current == '.':
                            continue
                        if current in box_seen:
                            return False

                        box_seen.add(current)
        return True



