from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "inputt, expected",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return empty list when no data"
            ),
            pytest.param(
                68,
                [3, 1, 1, 2],
                id="should be list with all numbers"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should fulfill req. for indexes"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="check zero index"
            ),
            pytest.param(
                15,
                [0, 1, 1, 0],
                id="check first and second index"
            ),
            pytest.param(
                1000,
                [0, 0, 0, 40],
                id="pile of money"
            ),
            pytest.param(
                -10,
                [0, 1, 1, -1],
                id="correct list when negative number"
            ),
            pytest.param(
                -1000,
                [0, 0, 0, -40],
                id="huge debt"
            ),
            pytest.param(
                0.5,
                [0.0, 0.0, 0.0, 0.0],
                id="input is float"
            ),
            pytest.param(
                360.5,
                [0.0, 0.0, 1.0, 14.0],
                id="big float"
            ),
            pytest.param(
                True,
                [1, 0, 0, 0],
                id="hmmm"
            ),
            pytest.param(
                2**32,
                [1, 0, 2, 171798691],
                id="calculate the USA debt"
            ),
            pytest.param(
                68.0,
                [3.0, 1.0, 1.0, 2.0],
                id="everything is float"
            )
        ]
    )
    def test_get_combinations_correctly(
            self,
            inputt: int,
            expected: list
    ) -> None:
        assert get_coin_combination(inputt) == expected

    @pytest.mark.parametrize(
        "inputt, expected_error",
        [
            pytest.param(
                None,
                TypeError,
                id="error when int is None"
            ),
            pytest.param(
                {"s": 123},
                TypeError,
                id="errr when dict"
            ),
            pytest.param(
                "str",
                TypeError,
                id="dwedwe"
            ),
            pytest.param(
                [1, 2, 3],
                TypeError,
                id="gwrtt"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            inputt: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(inputt)
