import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("input_cents,expected_output,exception", [
    pytest.param(1, [1, 0, 0, 0], None, id="Should return [1, 0, 0, 0] if "
                                           "input_cents is 1"),
    pytest.param(6, [1, 1, 0, 0], None, id="Should return [1, 1, 0, 0] if "
                                           "input_cents is 6"),
    pytest.param(17, [2, 1, 1, 0], None, id="Should return [2, 1, 1, 0] if "
                                           "input_cents is 17"),
    pytest.param(50, [0, 0, 0, 2], None, id="Should return [0, 0, 0, 2] if "
                                           "input_cents is 50"),
    pytest.param("a", None, TypeError, id="Should return None if "
                                          "input_cents are not integer"),
])
def test_get_coin_combination(input_cents: int,
                              expected_output: list,
                              exception: type) -> None:

    if exception:
        with pytest.raises(exception):
            get_coin_combination(input_cents)
    else:
        assert get_coin_combination(input_cents) == expected_output
