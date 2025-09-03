from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "value, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (22, [2, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination_examples(value: int, result: list[int]) -> None:
    out = get_coin_combination(value)
    assert isinstance(out, list), "Return type must be list"
    assert len(out) == 4, "Return list must habe exactly four elements"
    assert all(isinstance(x, int) for x in out), "All elements must be ints"
    assert out == result, f"Output {out} should be equeal {result}"


@pytest.mark.parametrize(
    "value, before, after",
    [
        (0, [0, 0, 0, 0], [1, 0, 0, 0]),
        (5, [0, 1, 0, 0], [1, 1, 0, 0]),
        (6, [1, 1, 0, 0], [2, 1, 0, 0]),
        (9, [4, 1, 0, 0], [0, 0, 1, 0]),
        (10, [0, 0, 1, 0], [1, 0, 1, 0]),
        (14, [4, 0, 1, 0], [0, 1, 1, 0]),
        (15, [0, 1, 1, 0], [1, 1, 1, 0]),
        (19, [4, 1, 1, 0], [0, 0, 2, 0]),
        (20, [0, 0, 2, 0], [1, 0, 2, 0]),
        (25, [0, 0, 0, 1], [1, 0, 0, 1]),
        (29, [4, 0, 0, 1], [0, 1, 0, 1]),
        (30, [0, 1, 0, 1], [1, 1, 0, 1]),
        (35, [0, 0, 1, 1], [1, 0, 1, 1]),
        (39, [4, 0, 1, 1], [0, 1, 1, 1]),
        (40, [0, 1, 1, 1], [1, 1, 1, 1]),
        (45, [0, 0, 2, 1], [1, 0, 2, 1]),
        (49, [4, 0, 2, 1], [0, 0, 0, 2]),
        (50, [0, 0, 0, 2], [1, 0, 0, 2]),
        (55, [0, 1, 0, 2], [1, 1, 0, 2]),
        (59, [4, 1, 0, 2], [0, 0, 1, 2]),
    ]
)
def test_boundaries_change(value: int, before: list[int], after: list[int]) -> None:
    assert get_coin_combination(value) == before
    assert get_coin_combination(value + 1) == after


# @pytest.mark.parametrize("value", [(-1), (-2), (-9)])
# def test_negative_values_raise_value_error(value):
#     with pytest.raises(ValueError):
#         get_coin_combination(value)


# @pytest.mark.parametrize("value", [(5.0), (17.0), (25.0)])
# def test_non_integer_inputs_raise_type_error(value):
#     with pytest.raises(TypeError):
#         get_coin_combination(value)


@pytest.mark.parametrize("value", [(10**6), (10**9)])
def test_very_large_values(value: int) -> None:
    out = get_coin_combination(value)
    assert (
        isinstance(out, list)
        and len(out) == 4
        and all(isinstance(x, int) for x in out)
    )
    out_prev = get_coin_combination(value - 1)
    assert out[0] < out_prev[0]
