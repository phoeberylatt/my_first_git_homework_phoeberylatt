print('hello')

def is_even(num)
    return num % 2 == 0

def is_within_range(num, _min, _max)
    if _min <= num <= _max:
        return True
    return False

def red_or_blue(num):
    if is_even(num) and (not is_even(num) or not is_within_range(num, 6, 20)):
          return "Red"

    if (is_even(num) and num > 20) or num in [2,4]:
        return 'Blue'
