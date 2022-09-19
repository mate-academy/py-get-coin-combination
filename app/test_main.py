from app.main import get_coin_combination


def test_result_should_is_list():
    assert isinstance(get_coin_combination(25), list), (
        "Result should be type 'list'"
    )


def test_equal_right_result():
    args = (
        {"cents": 0, "result": [0, 0, 0, 0]},
        {"cents": 1, "result": [1, 0, 0, 0]},
        {"cents": 7, "result": [2, 1, 0, 0]},
        {"cents": 47, "result": [2, 0, 2, 1]},
        {"cents": 67, "result": [2, 1, 1, 2]}
    )
    for i in range(len(args)):
        assert get_coin_combination(args[i]["cents"]) == args[i]["result"], (
            "Result not equal right."
        )
