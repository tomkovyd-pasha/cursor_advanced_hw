import unittest
from unittest.mock import patch
from game import TicTacToe


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.game.board[4] = "X"

    def test_available_moves(self):
        self.assertTrue(4 not in self.game.available_moves())

    def test_make_move(self):
        self.assertFalse(self.game.make_move(4, "X"))
        self.assertTrue(self.game.make_move(5, "X"))
        self.assertTrue(self.game.board[5] != " ")

    def test_winner(self):
        """
        у функції test_winner є три інші функції columns_check, rows_check, diagonal_check
        у кожній  функції створюється всі можливі варіанти заповнення дошки для виграшу (але тільки одна лінія, всі інші клітинки дошки пусті)
        :return:
        """

        def columns_check(letter):
            for columns in range(3):
                for rows in range(3):
                    self.game.board = [" " for i in range(9)]
                    row = [letter] * 3
                    self.game.board[rows * 3: (rows + 1) * 3] = row
                    # print(self.game.board)
                    self.assertTrue(self.game.winner(columns + rows * 3, letter))

        def rows_check(letter):
            for columns in range(3):
                for rows in range(3):
                    self.game.board = [" " for i in range(9)]
                    self.game.board[columns], self.game.board[columns + 3], self.game.board[columns + 6] = letter * 3
                    # print(self.game.board)
                    self.assertTrue(self.game.winner(rows * 3 + columns, letter))

        def diagonal_check(letter):
            a = [0, 4, 8]
            b = [2, 4, 6]
            for i in (a, b):
                for x in i:
                    self.game.board = [" " for i in range(9)]
                    for m in range(3):
                        self.game.board[i[m]] = letter
                    # print(self.game.board)
                    self.assertTrue(self.game.winner(x, letter))

        for l in ("X", "O"):
            columns_check(l)
            rows_check(l)
            diagonal_check(l)


if __name__ == '__main__':
    unittest.main()
