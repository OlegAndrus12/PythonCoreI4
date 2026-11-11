# Solutions for 16_exercises.py

fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

VOWELS = "aeiou"


def count_vowels(word):
    return sum(1 for char in word if char in VOWELS)


def is_prime(n):
    if n < 2:
        return False
    return all(n % divisor != 0 for divisor in range(2, int(n**0.5) + 1))


# 1
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(1, uppercased_fruits)

# 2
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(2, capitalized_fruits)

# 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
print(3, fruits_with_more_than_two_vowels)

# 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]
print(4, fruits_with_only_two_vowels)

# 5
print(5, [fruit for fruit in fruits if len(fruit) > 5])

# 6
print(6, [fruit for fruit in fruits if len(fruit) == 5])

# 7
print(7, [fruit for fruit in fruits if len(fruit) < 5])

# 8
print(8, [len(fruit) for fruit in fruits])

# 9
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(9, fruits_with_letter_a)

# 10
even_numbers = [n for n in numbers if n % 2 == 0]
print(10, even_numbers)

# 11
odd_numbers = [n for n in numbers if n % 2 != 0]
print(11, odd_numbers)

# 12
positive_numbers = [n for n in numbers if n > 0]
print(12, positive_numbers)

# 13
negative_numbers = [n for n in numbers if n < 0]
print(13, negative_numbers)

# 14
two_or_more_digits = [n for n in numbers if abs(n) >= 10]
print(14, two_or_more_digits)

# 15
numbers_squared = [n**2 for n in numbers]
print(15, numbers_squared)

# 16
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]
print(16, odd_negative_numbers)

# 17
numbers_plus_5 = [n + 5 for n in numbers]
print(17, numbers_plus_5)

# BONUS
primes = [n for n in numbers if is_prime(n)]
print("bonus", primes)
