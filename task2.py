import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
required_money_capital = 0
spend = 6000
for month in range(months):
    deficit = max(0, spend - salary)
    required_money_capital += deficit
    spend *= (1 + increase)

required_money_capital = int(required_money_capital)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital)
