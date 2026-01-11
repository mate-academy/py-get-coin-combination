from app.main import get_coin_combination
import pytest


class TestValues:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Test should return 1 penny"),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Test should return 1 penny + 1 nicke;"),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Test should return 2 pennies + 1 nickel + 1 dime"),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="Test should return 2 quarters"),
        ]
    )
    def test_correct_values(self, cents: int, expected_result: list) -> None:
        assert get_coin_combination(cents) == expected_result

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            pytest.param(
                "string",
                TypeError,
                id="Test should raise TypeError for string value"),
        ]
    )
    def test_correct_type_of_values(self,
                                    cents: int,
                                    expected_error: Exception) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)
