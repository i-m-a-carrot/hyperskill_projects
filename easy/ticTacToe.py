class TicTacToe:
    def __init__(self, values):
        self.values = values

    def display(self):
        result = f'''---------
| {self.values[0][0]} {self.values[0][1]} {self.values[0][2]} |
| {self.values[1][0]} {self.values[1][1]} {self.values[1][2]} |
| {self.values[2][0]} {self.values[2][1]} {self.values[2][2]} |
---------'''
        return result
    def check_common(self,expected):
        for x in range(3):
            if self.values[x][0] + self.values[x][1] + self.values[x][2] == expected or self.values[0][x] + self.values[1][x] + self.values[2][x] == expected:
                return True
        if self.values[0][0] + self.values[1][1] + self.values[2][2] == expected or self.values[2][0] + self.values[1][1] + self.values[0][2] == expected:
            return True

    def get_result(self, x, o, count_input):
        result = ""
        if (x == True and o == True) or abs(count_input.count('X') - count_input.count('O')) > 1:
            result = "Impossible"
        elif x == True:
            result = "X wins"
        elif o == True:
            result = "O wins"
        elif count_input.count('_') == 0:
            result = "Draw"
        else:
            result = "Game not finished"
        return result

user = input("Enter cells: ")
board = [[user[0], user[1], user[2]],[user[3], user[4], user[5]],[user[6], user[7], user[8]]]

gameplay = TicTacToe(board)
print(gameplay.display())

check_x = gameplay.check_common("XXX")
check_o = gameplay.check_common("OOO")

result = gameplay.get_result(check_x,check_o, user)
print(result)


