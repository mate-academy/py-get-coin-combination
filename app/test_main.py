import pytest
from app.main import get_coin_combination


class TestGetCoinCombinationClass():
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(0, [0, 0, 0, 0],
                         id="zero values should return result 0"),
            pytest.param(1, [1, 0, 0, 0],
                         id="combination with penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="combination with penny, nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="combination with penny, nickel, dime"),
            pytest.param(50, [0, 0, 0, 2],
                         id="combination with penny, nickel, dime, quarter"),
            pytest.param(9999, [4, 0, 2, 399],
                         id="should return correct values for large numbers")
        ]
    )
    def test_return_values_correctly(
            self,
            cents: int,
            expected_result: list[int]
    ) -> None:
        result = get_coin_combination(cents)
        assert result == expected_result

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "0", TypeError,
                id="should raise exception when cents is not integer"
            ),
            pytest.param(
                [], TypeError,
                id="should raise exception when cents is not integer"
            ),
        ]
    )
    def test_raise_exception_correctly(
            self,
            cents: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
