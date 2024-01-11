import datetime

import config
import pydantic_models
import models
import bit

wallet = bit.Key()  # наш кошелек готов и содержится в переменной wallet
print(f"Баланс: {wallet.get_balance()}")
print(f"Адрес: {wallet.address}")
print(f"Приватный ключ: {wallet.to_wif()}")
print(f"Транзакции: {wallet.get_transactions()}")
