import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1"),
        pytest.param(6, [1, 1, 0, 0], id="6"),
        pytest.param(17, [2, 1, 1, 0], id="17"),
        pytest.param(50, [0, 0, 0, 2], id="50")
    ]
)
def test_coin_combination(coin: int, result: list) -> None:
    test_result = get_coin_combination(coin)
    assert isinstance(test_result, list)
    assert all(isinstance(number, int) for number in test_result)
    assert test_result == result


@pytest.mark.parametrize(
    "coin",
    [
        pytest.param("10", id="String number"),
        pytest.param([1, 2, 3], id="List input"),
        pytest.param(None, id="None input")
    ]
)
def test_coin_combination_type_error(coin: int) -> None :
    with pytest.raises(TypeError):
        get_coin_combination(coin)


@pytest.mark.parametrize(
    "coin, expected_coin",
    [
        pytest.param(1, [1, 0, 0, 0], id="Should return 1 cent"),
        pytest.param(5, [0, 1, 0, 0], id="Should return 1 nickel"),
        pytest.param(10, [0, 0, 1, 0], id="Should return 1 dime"),
        pytest.param(25, [0, 0, 0, 1], id="Should return 1 quarter")
    ]
)
def test_coin_combination_coin_sorting(coin: int,
                                       expected_coin: list
                                       ) -> None :
    assert get_coin_combination(coin) == expected_coin
