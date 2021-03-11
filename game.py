from tkinter import *
from constructs import check_for_winner, Player, Board
from tkinter import messagebox
from functools import partial


class BoardTile:
    def __init__(self, row, column, game_instance):
        self.row = row
        self.column = column
        self.command = partial(game.click, self)
        self.button = Button(game_instance.root, text='', font=('Helvetica', 20), height=3, width=6,
                             bg='SystemButtonFace',
                             command=self.command)
        self.clicked = False

    def reset(self):
        self.button['text'] = ''
        self.clicked = False


class Game:
    def __init__(self):
        # interface elements - add stuff to the interface here

        self.root = Tk()
        self.root.title('Tic-Tac-Toe')

        self.new_game_button = Button(self.root, text='New game', font=('Helvetica', 12), height=2, width=10,
                                      bg='SystemButtonFace',
                                      command=self.reset_ui)
        self.p1_score = Label(self.root, text='P1 (X) : 0', font=('Helvetica', 10), height=2, width=10,
                              bg='SystemButtonFace')
        self.p2_score = Label(self.root, text='P2 (O) : 0', font=('Helvetica', 10), height=2, width=10,
                              bg='SystemButtonFace')
        self.current_player_label = Label(self.root, text='Next move : X', font=('Helvetica', 10),
                                          bg='SystemButtonFace')

        # game variables - add game variables here

        self.tiles = []
        self.current_player, self.next_player = Player(1, 'X'), Player(2, 'O')
        self.board = Board()

    def __setup_game(self):
        for x in range(3):
            for y in range(3):
                temp = BoardTile(x, y, self)
                temp.button.grid(row=x, column=y)
                self.tiles.append(temp)

    def __switch_player(self):
        self.current_player, self.next_player = self.next_player, self.current_player

    def __update_scoreboard(self, player):
        if player.nr == 1:
            self.p1_score['text'] = player.verbose_name + str(player.score)
        else:
            self.p2_score['text'] = player.verbose_name + str(player.score)

    def __update_current_player(self, player):
        self.current_player_label['text'] = f'Next move : {player.symbol}'

    def __place_ui_elements(self):
        self.new_game_button.grid(row=4, column=1)
        self.p1_score.grid(row=4, column=0)
        self.p2_score.grid(row=4, column=2)
        self.current_player_label.grid(row=5, column=1)

    def click(self, tile):
        if not tile.clicked:
            tile.clicked = True
            self.board.matrix[tile.row, tile.column] = self.current_player.nr
            tile.button['text'] = self.current_player.symbol
            if check_for_winner(self.board.matrix):
                messagebox.showinfo(title='Game over', message=f'{self.current_player.symbol} won !')
                self.current_player.score += 1
                self.__update_scoreboard(self.current_player)
                self.reset_ui()
                self.__switch_player()
                self.__update_current_player(self.current_player)
                return
            self.__switch_player()
            self.__update_current_player(self.current_player)
        return

    def reset_ui(self):
        for tile in self.tiles:
            tile.reset()
        self.board.reset_matrix()

    def start_game(self):
        self.__setup_game()
        self.__place_ui_elements()
        self.root.mainloop()


game = Game()
game.start_game()
