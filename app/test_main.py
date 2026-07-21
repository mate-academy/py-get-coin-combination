import pytest
from app.main import get_coin_combination


def test_should_return_list_of_int() -> None:
    result = get_coin_combination(15)
    assert all(isinstance(val, int) for val in result)


class TestCheckNumberCases:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [

            (
                1, [1, 0, 0, 0]
            ),

            (
                6, [1, 1, 0, 0]
            ),

            (
                17, [2, 1, 1, 0]
            ),

            (
                50, [0, 0, 0, 2]
            ),

        ]
    )
    def test_should_return_correct_values(
            self,
            cents: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_result

    @pytest.mark.parametrize(
        "cents,error",
        [
            ([1], TypeError),
            ({1}, TypeError),
            ("1", TypeError),
            (2.1, TypeError),
            (-1, ValueError)

        ]
    )
    def test_should_accept_correct_types(
            self, cents: int, error: tuple
    ) -> None:
        with pytest.raises(error):
            get_coin_combination(cents)
