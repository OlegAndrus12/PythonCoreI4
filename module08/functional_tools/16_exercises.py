# 17 list comprehension exercises (+ bonus)
# Solutions: 16_exercises_solutions.py — try on your own first!

fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example: a for loop that adds 1 to each number
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# The same with a list comprehension
numbers_plus_one = [number + 1 for number in numbers]

# Example: a for loop that uppercases every fruit
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the example above as a list comprehension.
# Name the variable uppercased_fruits. Output: ['MANGO', 'KIWI', ...]

# Exercise 2 - capitalized_fruits: ['Mango', 'Kiwi', 'Strawberry', ...]

# Exercise 3 - fruits_with_more_than_two_vowels.
# Hint: you'll need a way to check if a letter is a vowel.

# Exercise 4 - fruits_with_only_two_vowels. Result: ['mango', 'kiwi', 'strawberry']

# Exercise 5 - fruits with more than 5 characters

# Exercise 6 - fruits with exactly 5 characters

# Exercise 7 - fruits with less than 5 characters

# Exercise 8 - number of characters in each fruit. Output: [5, 4, 10, ...]

# Exercise 9 - fruits_with_letter_a: only the fruits that contain the letter "a"

# Exercise 10 - even_numbers

# Exercise 11 - odd_numbers

# Exercise 12 - positive_numbers

# Exercise 13 - negative_numbers

# Exercise 14 - numbers with 2 or more digits (e.g. 10, 256, -9 is not, -10 would be)

# Exercise 15 - numbers_squared: [4, 9, 16, ...]

# Exercise 16 - odd_negative_numbers: numbers that are both odd and negative

# Exercise 17 - numbers_plus_5: each number plus five

# BONUS - primes: the prime numbers from the numbers list.
# Hint: write a helper function is_prime(n).
