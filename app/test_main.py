import pytest

from app.main import get_coin_combination


def test_get_coin_combination_should_return_list_with_four_element() -> None:
    assert isinstance(get_coin_combination(42), list)


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "amount, expected_result",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="shouldn't return any coins when '0' was passed"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return '1' penny when '1' was passed"
            ),
            pytest.param(
                4, [4, 0, 0, 0],
                id="should return '4' pennies when '4' was passed"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should return '1' penny and '1' nickel when '6' was passed"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="should return '1' dime when '10' was passed"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should return '2' pennies, '1' nickel "
                   "and '1' dime when '17' was passed"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="should return '1' quarter when '25' was passed"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="should return '1' penny, '1' nickel, '1' dime "
                   "and '1' quarter when '41' was passed"
            ),
            pytest.param(
                72, [2, 0, 2, 2],
                id="should return '2' penny, '2' dime "
                   "and '2' quarter when '72' was passed"
            ),
            pytest.param(
                75, [0, 0, 0, 3],
                id="should return '3' quarters when '75' was passed"
            ),
            pytest.param(
                104, [4, 0, 0, 4],
                id="should return '4' pennies and '4' quarters "
                   "when '104' was passed"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            amount: int,
            expected_result: list,
    ) -> None:
        assert get_coin_combination(amount) == expected_result
