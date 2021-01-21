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

    def user_gameplay(self):
        store = "X"
        count = 0
        while True:
            check_x = self.check_common("XXX")
            check_o = self.check_common("OOO")
            user_input = input("Enter the coordinates: ").split()
            if user_input[0].isdecimal() and user_input[1].isdecimal():
                x = int(user_input[0])
                y = int(user_input[1])
                if x > 3 or y > 3:
                    print("Coordinates should be from 1 to 3!")
                elif self.values[x - 1][y - 1] in ["O", "X"]:
                    print("This cell is occupied! Choose another one!")
                else:
                    if store == "X":
                        self.values[x - 1][y - 1] = "X"
                        store = "O"
                        count += 1
                    else:
                        self.values[x - 1][y - 1] = "O"
                        store = "X"
                        count += 1
                    print(self.display())
                    check_x = self.check_common("XXX")
                    check_o = self.check_common("OOO")
                    if check_x == True:
                        print("X wins")
                        break
                    elif check_o == True:
                        print("O wins")
                        break 
                    elif count == 9:
                        print("Draw")
                        break
            else:
                print("You should enter numbers!")

user= "_________"
start_game = [[user[0], user[1], user[2]],[user[3], user[4], user[5]],[user[6], user[7], user[8]]]

result = TicTacToe(start_game)
result.user_gameplay()
