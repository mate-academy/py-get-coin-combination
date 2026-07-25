import pytest

from app.main import get_coin_combination


class TestCombination:

    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(0, [0, 0, 0, 0], id="should list with zerow"),
            pytest.param(1, [1, 0, 0, 0], id="should list with pennies"),
            pytest.param(6, [1, 1, 0, 0], id="should list with nickels"),
            pytest.param(17, [2, 1, 1, 0], id="should list with dimes"),
            pytest.param(56, [1, 1, 0, 2], id="should list with quarters"),
            pytest.param(121, [1, 0, 2, 4], id="should list with dollars"),
        ]
    )
    def test_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected


class TestCombinationError:

    @pytest.mark.parametrize(
        "cents, expected_errors",
        [
            pytest.param("121", TypeError,
                         id="should ValueError if argument Not int"),
            pytest.param(12.1, TypeError,
                         id="should ValueError if argument Float"),
            pytest.param(-12, TypeError,
                         id="should ValueError if argument Negative"),
        ]
    )
    def test_raise_errors(
            self, cents: int, expected_errors: type[TypeError]
    ) -> None:
        with pytest.raises(expected_errors):
            get_coin_combination(cents)
