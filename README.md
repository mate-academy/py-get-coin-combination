# Coin combination

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start.


Write tests for `get_coin_combination` function that takes a non-negative integer
`cents` (a specific amount in cents) and returns a combination of the smallest
possible number of coins, giving the same amount.

The function should return a list where:
- `coins[0]` = number of pennies (1 penny = 1 cent);
- `coins[1]` = number of nickels (1 nickel = 5 cents);
- `coins[2]` = number of dimes (1 dime = 10 cents);
- `coins[3]` = number of quarters (1 quarter = 25 cents).

**Please note:** you have to use `pytest` for writing tests.

Examples:
```python
get_coin_combination(1) == [1, 0, 0, 0]  # 1 penny
get_coin_combination(6) == [1, 1, 0, 0]  # 1 penny + 1 nickel
get_coin_combination(17) == [2, 1, 1, 0]   # 2 pennies + 1 nickel + 1 dime
get_coin_combination(50) == [0, 0, 0, 2]   # 2 quarters
```

Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.
