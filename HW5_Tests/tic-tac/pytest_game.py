import pytest
import game

game_instance = game.TicTacToe()
game_instance.board[4] = 'X'


def test_available_moves():
    assert 4 not in game_instance.available_moves()
    assert 3 in game_instance.available_moves()


def test_make_move():
    assert game_instance.make_move(square=4, letter='X') is False
    assert game_instance.make_move(square=5, letter='X') is True
    assert (game_instance.board[5] != " ") is True


if __name__ == "__main__":
    test_available_moves()
    test_make_move()

