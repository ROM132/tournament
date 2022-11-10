import random


class tournament:
    groups = {
        0: [],
        1: [],
        2: [],
        3: [],
    }

    teams = {
        0: ["Barcelona"],
        1: ["Real Madrid"],
        2: ["Atletico Madrid"],
        3: ["Real Betis"],
        4: ["Osasuna"],
        5: ["Villarreal"],
        6: ["Athletic Bilbao"],
        7: ["Rom team"],
    }

    win_round1 = {
        0: [],
        1: [],
        2: [],
        3: [],
    }

    sami_final_win = {
        0: [],
        1: [],
    }

    def __init__(self):
        self.target = [0, 1, 2, 3, 4, 5, 6, 7]
        self.num = 0
        self.key = None
        self.the_key = None

        self.num1 = 0
        self.target1 = 0

    def Team_Sort(self):
        if not self.target:
            t.Game_score()
            exit()

        self.the_key = random.choice(self.target)
        t.check()
        if self.the_key in self.target:
            self.target.remove(self.the_key)
            t.Team_Sort()
        else:
            exit()

    def check(self):
        dic = [0, 1, 2, 3, 4, 5, 6, 7]

        while True:
            if not dic:
                break
            i = random.choice(dic)

            if self.num in [0, 4]:
                self.groups[0].append(self.teams[i][0])
                self.key = self.groups[0]
                self.num += 1
                dic.remove(i)

            elif self.num in [1, 5]:
                self.groups[1].append(self.teams[i][0])
                self.key = self.groups[1]
                self.num += 1
                dic.remove(i)

            elif self.num in [2, 6]:
                self.groups[2].append(self.teams[i][0])
                self.key = self.groups[2]
                self.num += 1
                dic.remove(i)

            elif self.num in [3, 7]:
                self.groups[3].append(self.teams[i][0])
                self.key = self.groups[3]
                self.num += 1
                dic.remove(i)

            else:
                break

    def Game_score(self):
        game_score_team1 = random.randint(0, 3)
        game_score_team2 = random.randint(0, 3)
        t.game_number()
        t.name(game_score_team1, game_score_team2, self.target1)

    def name(self, score_team1, score_team2, target):
        if target == 0:
            key = self.groups[0][2]
            op1 = self.groups[0][0]
            op2 = self.groups[0][1]
            self.target1 += 1
        elif target == 1:
            key = self.groups[1][2]
            op1 = self.groups[1][0]
            op2 = self.groups[1][1]
            self.target1 += 1
        elif target == 2:
            key = self.groups[2][2]
            op1 = self.groups[2][0]
            op2 = self.groups[2][1]
            self.target1 += 1
        elif target == 3:
            key = self.groups[3][2]
            op1 = self.groups[3][0]
            op2 = self.groups[3][1]
            self.target1 += 1
        else:
            t.semi_final()
            exit()

        t.Round1(op1, op2, key, score_team1, score_team2)

    def Round1(self, op1, op2, name, op1_score, op2_score):
        print(f"Ok this is the {name} Game:\n{op1} Vs {op2}")
        if op1_score > op2_score:
            self.win_round1[self.num1].append(op1)
            input("Press enter to see the result of the game!: ")
            print(f"Ok the game ended {op1_score} - {op2_score} To {op1}")
            self.num1 += 1
            t.Game_score()
        elif op1_score < op2_score:
            self.win_round1[self.num1].append(op2)
            input("Press enter to see the result of the game!: ")
            print(f"Ok the game ended {op1_score} - {op2_score} To {op2}")
            self.num1 += 1
            t.Game_score()
        elif op1_score == op2_score:
            input("Press enter to see the result of the game!: ")
            print(f"Ok the game ended {op1_score} - {op2_score} in a draw So a rematch is called!")
            self.target1 -= 1
            t.Game_score()
        else:
            print("Start Game problem!==================================")
            exit()

    def game_number(self):
        game_number = ["First", "Second", "Third", "Forth"]
        self.groups[0].append(game_number[0])
        self.groups[1].append(game_number[1])
        self.groups[2].append(game_number[2])
        self.groups[3].append(game_number[3])

    def semi_final(self):
        r1 = random.randint(0, 4)
        r2 = random.randint(0, 4)
        r3 = random.randint(0, 4)
        r4 = random.randint(0, 4)
        print(f"Ok the club that pass the first round are:\n{self.win_round1}\n")
        input("Press enter to continue: ")
        print(f"The next two game are:\nFirst: {self.win_round1[0]} Vs {self.win_round1[1]}\nSecond: {self.win_round1[2]} Vs {self.win_round1[3]}")
        t.semi_final1(r1, r2)
        t.semi_final2(r3, r4)
        t.the_big_winner()

    def semi_final1(self, r1, r2):
        global key
        if r1 > r2:
            print(f"The score in the first game is: {r1} - {r2} To {self.win_round1[0]}")
            key = self.win_round1[0]
        elif r1 < r2:
            print(f"The score in the first game is: {r1} - {r2} To {self.win_round1[1]}")
            key = self.win_round1[1]
        elif r1 == r2:
            r1 = random.randint(0, 5)
            r2 = random.randint(0, 5)
            t.semi_final1(r1, r2)
        else:
            print("We have a problem is semi_final1 ================================")

        self.sami_final_win[0].append(key)
        input("press enter to continue")

    def semi_final2(self, r3, r4):
        global key
        if r3 > r4:
            print(f"The score in the second game is: {r3} - {r4} To {self.win_round1[2]}")
            key = self.win_round1[2]
        elif r3 < r4:
            print(f"The score in the second game is: {r3} - {r4} To {self.win_round1[3]}")
            key = self.win_round1[3]
        elif r3 == r4:
            print(f"The score in the second game is: {r3} - {r4} so its a draw Remath is called!")
            r3 = random.randint(0, 5)
            r4 = random.randint(0, 5)
            t.semi_final2(r3, r4)
        else:
            print("We have a problem is semi_final1 ================================")
        self.sami_final_win[1].append(key)

    def the_big_winner(self):
        global winner, lose, r1, r2
        r1 = random.randint(1, 4)
        r2 = random.randint(1, 4)
        input("\nPress enter to go to the final!\n\n")

        print(f"This is the last game\nThe game is between: {self.sami_final_win[0][0]} Vs {self.sami_final_win[1][0]}")
        input("Press enter to see the result!: \n\n")
        while True:
            if r1 > r2:
                winner = self.sami_final_win[0][0]
                lose = self.sami_final_win[1][0]
                break
            elif r1 > r2:
                winner = self.sami_final_win[1][0]
                lose = self.sami_final_win[0][0]
                break
            elif r1 == r2:
                r1 = random.randint(1, 3)
                r2 = random.randint(1, 3)
                continue

        t.print_winner()

    def print_winner(self):
        print(
            f"So to the result of this tournament is:\n{winner} Beat {lose}\nThe score is: {r1} - {r2} To {winner}\nGood bey!")
        exit()


t = tournament()
t.Team_Sort()
