import pytest
from tictactoe.tictactoe import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["deck", "expected_result"],
    [
        ([["-", "-", "x"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
        ([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
        ([["x", "x", "x"], ["-", "-", "o"], ["x", "o", "x"]], "x wins!"),
        ([["-", "-", "o"], ["x", "x", "x"], ["x", "o", "o"]], "x wins!"),
        (
            [
                ["-", "-", "o"],
                ["x", "o", "o"],
                ["x", "x", "x"],
            ],
            "x wins!",
        ),
        (
            [
                ["x", "-", "o"],
                ["x", "o", "o"],
                ["x", "o", "-"],
            ],
            "x wins!",
        ),
        (
            [
                ["-", "x", "o"],
                ["o", "x", "o"],
                ["-", "x", "-"],
            ],
            "x wins!",
        ),
        (
            [
                ["-", "-", "x"],
                ["o", "o", "x"],
                ["-", "-", "x"],
            ],
            "x wins!",
        ),
    ],
)
def test_tic_tac_toe_checker_x_wins(deck, expected_result):
    assert tic_tac_toe_checker(deck) == expected_result


@pytest.mark.parametrize(
    ["deck", "expected_result"],
    [
        ([["-", "-", "o"], ["-", "o", "x"], ["o", "x", "x"]], "o wins!"),
        ([["o", "-", "x"], ["-", "o", "x"], ["x", "o", "o"]], "o wins!"),
        ([["o", "o", "o"], ["-", "-", "o"], ["x", "o", "x"]], "o wins!"),
        ([["-", "-", "o"], ["o", "o", "o"], ["x", "o", "x"]], "o wins!"),
        (
            [
                ["-", "-", "x"],
                ["x", "o", "x"],
                ["o", "o", "o"],
            ],
            "o wins!",
        ),
        (
            [
                ["o", "-", "o"],
                ["o", "x", "x"],
                ["o", "o", "-"],
            ],
            "o wins!",
        ),
        (
            [
                ["-", "o", "x"],
                ["o", "o", "x"],
                ["-", "o", "-"],
            ],
            "o wins!",
        ),
        (
            [
                ["-", "-", "o"],
                ["o", "x", "o"],
                ["-", "-", "o"],
            ],
            "o wins!",
        ),
    ],
)
def test_tic_tac_toe_checker_o_wins(deck, expected_result):
    assert tic_tac_toe_checker(deck) == expected_result


@pytest.mark.parametrize(
    ["deck", "expected_result"],
    [
        (
            [
                ["-", "-", "o"],
                ["-", "x", "o"],
                ["x", "o", "x"],
            ],
            "unfinished!",
        ),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished!"),
    ],
)
def test_tic_tac_toe_checker_unfinished(deck, expected_result):
    assert tic_tac_toe_checker(deck) == expected_result


@pytest.mark.parametrize(
    ["deck", "expected_result"],
    [
        (
            [
                ["x", "x", "o"],
                ["o", "o", "x"],
                ["x", "o", "x"],
            ],
            "draw!",
        ),
        ([["x", "o", "x"], ["x", "x", "o"], ["o", "x", "o"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker_unfinished(deck, expected_result):
    assert tic_tac_toe_checker(deck) == expected_result
