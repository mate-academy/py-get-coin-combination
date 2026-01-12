from app.main import get_coin_combination
import pytest

# 0, 1, 5, 10, 25, 41, 64536834617

# [1], (1,), {"1": 1}, "1", None, 1.15


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            pytest.param(64536834617, [2, 1, 1, 2581473384],
                         id="should work with very big values as well")
        ]
    )
    def test_int_args_should_return_expected_result(
            self,
            cents: int,
            expected: list) -> None:
        assert get_coin_combination(cents) == expected

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            ([1], TypeError),
            ((1, ), TypeError),
            ({"1": 1}, TypeError),
            ("1", TypeError),
            (None, TypeError)
        ],
        ids=["list is not expected",
             "tuple is not expected",
             "dict is not expected",
             "str is not expected",
             "NoneType is not expected"]
    )
    def should_raise_type_error_if_cents_wrong_type(
            self,
            cents: int,
            expected_error: type[TypeError]) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)
