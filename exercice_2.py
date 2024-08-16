from random import randrange

def get_numbers_ticket(min, max, quantity):

  if(min < 1 or max > 1000 or min > max or max - min < quantity):
    return []

  numbers = []

  i = 0

  while i < quantity:

    num = randrange(min, max)

    if(num in numbers):
      i -= 1
    else:
      numbers.append(num)

    i += 1

  numbers.sort()

  return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
lottery_numbers = get_numbers_ticket(1, 15, 10)
print("Ваші лотерейні числа:", lottery_numbers)
