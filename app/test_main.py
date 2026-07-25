import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("number", [(1), (5), (23)])
def test_return_obj_is_list(number: int) -> None:
    assert isinstance(
        get_coin_combination(number), list), "Function must return list"


@pytest.mark.parametrize("number", [(15), (53), (213)])
def test_list_has_positive_int(number: int) -> None:
    check_list = [
        isinstance(number, int) and number >= 0
        for number in get_coin_combination(number)
    ]
    assert all(check_list), "List must contain only positive integers"


@pytest.mark.parametrize("number", [("a"), (["world"])])
def test_raise_typeerror(number: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(number)


@pytest.mark.parametrize(
    "number, result",
    [
        pytest.param(6, [1, 1, 0, 0], id="6 coins"),
        pytest.param(17, [2, 1, 1, 0], id="17 coins"),
        pytest.param(53, [3, 0, 0, 2], id="53 coins"),
    ],
)
def test_get_coin_result(number: int, result: list[int]) -> None:
    assert (
        get_coin_combination(number) == result
    ), f"get_coin_combination must return {result}"
