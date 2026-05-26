from app.your_module import get_coin_combination


@pytest.mark.parametrize(
   "cents","values",
   [
      (1, [1, 0, 0, 0]),
      (6, [1, 1, 0, 0]),
      (17, [2, 1, 1, 0]),
      (50, [0, 0, 0, 2])
      
   ]
)
