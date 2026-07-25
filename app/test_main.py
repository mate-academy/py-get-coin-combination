import pytest

from app.main import get_coin_combination


class TestCorrectValues:
    @pytest.mark.parametrize(
        "expected_input,expected_output",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="must be only pennies"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="must be only pennies"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="must be exchange to nickels"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="must be have pennies and nickels"
            ),
            pytest.param(
                15,
                [0, 1, 1, 0],
                id="must be have nickels and dimes"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="must be have pennies, nickels and dimes"
            ),
            pytest.param(
                24,
                [4, 0, 2, 0],
                id="must be have pennies and dimes"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="must be have only quarters"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="must be have all kind of money"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="must be have more one quarters"
            ),
        ]
    )
    def test_correct_input(
            self,
            expected_input: int,
            expected_output: list
    ) -> None:
        assert get_coin_combination(expected_input) == expected_output


class TestExpectedError:
    @pytest.mark.parametrize(
        "expected_input,expected_error",
        [
            pytest.param(-1, ValueError, id="argument should be positive"),
            pytest.param("1", TypeError, id="argument should be type int"),
        ]
    )
    def test_expected_error(
            self,
            expected_input: (int, str),
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            assert get_coin_combination(expected_input)
