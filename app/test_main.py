import pytest
from app.main import get_coin_combination

@pytest.mark.parametrize(
    "coin, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(coin, expected):
    assert get_coin_combination(coin) == expected


@pytest.mark.parametrize(
    "coin, expected_error",
    [
        pytest.param(-1, ValueError, id="ValueError"),
        pytest.param("1", TypeError, id="TypeError"),
    ]
)
def test_get_coin_combination_error(coin, expected_error):
    with pytest.raises(expected_error):
        get_coin_combination(coin)

def test_get_coin_combination_should_return_len_result_4():
    assert len(get_coin_combination(1)) == 4