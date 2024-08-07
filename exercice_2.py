from random import randrange

def get_numbers_ticket(min, max, quantity):

  if(min < 1 or max > 1000):
    return []

  numbers = []

  for i in range(quantity):

    num = randrange(min, max)

    if(num in numbers):
      i -= 1
    else:
      numbers.append(num)

  numbers.sort()

  return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)