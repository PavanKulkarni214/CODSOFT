import tkinter as tk
from tkinter import messagebox
import random
import time

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.scores = {"Player": 0, "AI": 0, "Draw": 0}
        self.current_player = PLAYER_O  # Player starts

    def reset_board(self):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.current_player = PLAYER_O

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return self.board[i][0], [(i, 0), (i, 1), (i, 2)]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                return self.board[0][i], [(0, i), (1, i), (2, i)]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return self.board[0][0], [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return self.board[0][2], [(0, 2), (1, 1), (2, 0)]
        if all(cell != EMPTY for row in self.board for cell in row):
            return 'Draw', []
        return None, []

    def minimax(self, board, depth, is_maximizing):
        winner, _ = self.check_winner()
        if winner == PLAYER_X:
            return 1
        elif winner == PLAYER_O:
            return -1
        elif winner == 'Draw':
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_X
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = EMPTY
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_O
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = EMPTY
                        best_score = min(best_score, score)
            return best_score

    def best_move(self, difficulty="Hard"):
        if difficulty == "Easy":
            # Random move
            empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]
            return random.choice(empty_cells) if empty_cells else None

        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_X
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play_move(self, row, col, player):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player
            return True
        return False


class TicTacToeApp:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.scoreboard = None
        self.difficulty = "Hard"  # Default difficulty
        self.create_widgets()

    def create_widgets(self):
        # Create settings menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        settings_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Easy", command=lambda: self.set_difficulty("Easy"))
        settings_menu.add_command(label="Hard", command=lambda: self.set_difficulty("Hard"))
        settings_menu.add_command(label="Reset Scores", command=self.reset_scores)

        # Create a 3x3 grid of buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        for i in range(3):
            for j in range(3):
                button = tk.Button(frame, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Create a scoreboard
        self.scoreboard = tk.Label(self.root, text=self.get_score_text(), font=('Arial', 14))
        self.scoreboard.pack(pady=10)

        # Create a reset button
        reset_button = tk.Button(self.root, text="Reset Game", font=('Arial', 12), command=self.reset_game)
        reset_button.pack(pady=5)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        messagebox.showinfo("Difficulty Set", f"Difficulty changed to {difficulty}.")

    def reset_scores(self):
        self.game.scores = {"Player": 0, "AI": 0, "Draw": 0}
        self.update_scoreboard()

    def on_button_click(self, row, col):
        if self.game.play_move(row, col, PLAYER_O):  # Player's move
            self.buttons[row][col].config(text=PLAYER_O, state=tk.DISABLED)
            winner, positions = self.game.check_winner()
            if winner:
                self.end_game(winner, positions)
                return
            self.root.after(500, self.ai_move)  # Delay AI move for better experience

    def ai_move(self):
        move = self.game.best_move(self.difficulty)
        if move:
            row, col = move
            self.game.play_move(row, col, PLAYER_X)
            self.buttons[row][col].config(text=PLAYER_X, state=tk.DISABLED)
            winner, positions = self.game.check_winner()
            if winner:
                self.end_game(winner, positions)

    def end_game(self, winner, positions):
        if winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game.scores["Draw"] += 1
        else:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            if winner == PLAYER_X:
                self.game.scores["AI"] += 1
            else:
                self.game.scores["Player"] += 1

        self.update_scoreboard()
        self.highlight_winner(positions)
        self.disable_all_buttons()

    def highlight_winner(self, positions):
        for row, col in positions:
            self.buttons[row][col].config(bg="lightgreen")

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset_game(self):
        self.game.reset_board()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=tk.NORMAL, bg="SystemButtonFace")

    def update_scoreboard(self):
        self.scoreboard.config(text=self.get_score_text())

    def get_score_text(self):
        return f"Player: {self.game.scores['Player']} | AI: {self.game.scores['AI']} | Draws: {self.game.scores['Draw']}"


def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
