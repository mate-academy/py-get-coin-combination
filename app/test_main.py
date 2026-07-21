import pytest

from app.main import get_coin_combination


class TestCombination:
    @pytest.mark.parametrize(

        "combination,expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            ("", TypeError)
        ]

    )
    def test_coin_combination(self, combination: int, expected: list) -> None:
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                get_coin_combination(combination)
        else:
            assert get_coin_combination(combination) == expected
