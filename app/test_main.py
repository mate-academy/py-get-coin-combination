from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, combination",
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="Should return [1, 0, 0, 0] when 1"
                         ),
            pytest.param(6, [1, 1, 0, 0],
                         id="Should return [1, 1, 0, 0] when 6"
                         ),
            pytest.param(17, [2, 1, 1, 0],
                         id="Should return [2, 1, 1, 0] when 17"
                         ),
            pytest.param(50, [0, 0, 0, 2],
                         id="Should return [0, 0, 0, 2] when 50"
                         )
        ]
    )
    def test_get_coin_combination(self, cents, combination):
        assert get_coin_combination(cents) == combination


if __name__ == '__main__':
    pytest.main()
