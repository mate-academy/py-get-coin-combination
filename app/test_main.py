from pytest import mark, param
from app.main import get_coin_combination


class TestModify:
    @mark.parametrize(
        "cents, result",
        [
            param(
                1,
                [1, 0, 0, 0],
                id="Test result != [1, 0, 0, 0]"
            ),
            param(
                6,
                [1, 1, 0, 0],
                id="Test result != [1, 1, 0, 0]"
            ),
            param(
                17,
                [2, 1, 1, 0],
                id="Test result != [2, 1, 1, 0]"
            ),
            param(
                50,
                [0, 0, 0, 2],
                id="Test result != [0, 0, 0, 2]"
            ),

        ]
    )
    def test_modify(self, cents, result) -> None:
        assert isinstance(cents, int), "Please enter an integer"
        assert cents > 0, "Please enter a positive number"
        assert get_coin_combination(cents) == result