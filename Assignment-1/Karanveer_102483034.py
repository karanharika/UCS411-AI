""" Written by: Karanveer Singh Harika
    Roll No: 102483034
   Assignment 1"""

import re
import random
from interest_calc import calculate_compound_interest


def student_marks():
    """ Solution for 1st question in the assignment """
    math_marks = [42, 35, 76, 84, 32, 78, 95, 93, 14, 85]
    science_marks = [45, 67, 52, 86, 79, 99, 42, 97, 43, 60]
    english_marks = [87, 42, 37, 45, 67, 52, 95, 93, 14, 78]
    it_marks = [76, 84, 32, 78, 37, 45, 67, 94, 42, 96]

    overall_marks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(math_marks)):
        overall_marks[i] += math_marks[i]
        overall_marks[i] += science_marks[i]
        overall_marks[i] += english_marks[i]
        overall_marks[i] += it_marks[i]

    avg_math = sum(math_marks) / len(math_marks)
    avg_science = sum(science_marks) / len(science_marks)
    avg_english = sum(english_marks) / len(english_marks)
    avg_it = sum(it_marks) / len(it_marks)

    print(f"Max marks in Maths: {max(math_marks)} \n"
          f"Max marks in Science: {max(science_marks)} \n"
          f"Max marks in English: {max(english_marks)} \n"
          f"Max marks in It: {max(it_marks)}\n")

    print(f"Lowest marks in Maths: {min(math_marks)} \n"
          f"Lowest marks in Science: {min(science_marks)} \n"
          f"Lowest marks in English: {min(english_marks)} \n"
          f"Lowest marks in It: {min(it_marks)}\n")

    print(f"Average marks in Maths: {avg_math}\n"
          f"Average marks in Science: {avg_science}\n"
          f"Average marks in English: {avg_english}\n"
          f"Average marks in It: {avg_it}\n")

    print(f"Highest Overall Marks: {max(overall_marks)} \n"
          f"Lowest Overall Marks: {min(overall_marks)} \n"
          f"Average Overall Marks: {(sum(overall_marks) / len(overall_marks))}\n")


def calculate_salary(salary):
    """ Solution to 2nd question in the assignment """
    if salary <= 10000:
        gross_salary = salary + salary * 0.20 + salary * 0.80
    elif 10000 < salary <= 20000:
        gross_salary = salary + salary * 0.25 + salary * 0.90
    else:
        gross_salary = salary + salary * 0.30 + salary * 0.95

    print(f"Gross Salary: {gross_salary}")
    return gross_salary


def validate_password_input(str_value):
    """ Solution to 3rd question in the assignment """

    if len(str_value) <= 6:
        raise ValueError("Password must be at least 6 characters.")
    if len(str_value) >= 16:
        raise ValueError("Password must be less than 16 characters.")
    if not re.search("[a-z]", str_value):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search("[A-Z]", str_value):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search("[0-9]", str_value):
        raise ValueError("Password must contain at least one number from 0 to 9.")
    if not re.search("[$#@]", str_value):
        raise ValueError("Password must contain at least one special character from $ # @")


def list_manipulation():
    """ Solution to 4th question in the assignment """
    L = [10, 20, 30, 40, 50, 60, 70, 80]

    L.append(200)
    L.append(300)
    print(f"L: {L}")
    L.remove(10)
    L.remove(30)
    print(f"L: {L}")
    L.sort()
    print(f"L: {L}")
    L.sort(reverse=True)
    print(f"L: {L}")


def dictionary_manipulation():
    """ Solution to 5th question in the assignment """
    D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

    D[6] = "Six"

    D.pop(2)
    print(f"D: {D}")

    if 6 in D:
        print("6 key is present\n")

    print(f"Number of elements in dictionary: {len(D)}")

    """We should use D.values() but the values are strings. So utilizing keys, which will also give the same result."""
    print(f"Sum of all values in dictionary: {sum((D.keys()))}")


def check_prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def random_numbers():
    """ Solution to 6th question in the assignment """
    random_numbers_list = [random.randint(100, 900) for _ in range(100)]
    even_numbers_list=[]
    odd_numbers_list=[]
    prime_numbers_list=[]
    for number in random_numbers_list:
        if check_prime_number(number):
            prime_numbers_list.append(number)
        if number % 2 == 0:
            even_numbers_list.append(number)
        else:
            odd_numbers_list.append(number)

    print(f"Count of even numbers: {len(even_numbers_list)}\n"
          f"Even numbers: {even_numbers_list}\n")

    print(f"Count of odd numbers: {len(odd_numbers_list)}\n"
          f"Odd numbers: {odd_numbers_list}\n")

    print(f"Count of prime numbers: {len(prime_numbers_list)}\n"
          f"Prime numbers: {prime_numbers_list}\n")



if __name__ == '__main__':
    student_marks()  # Solution for 1st question in the assignment

    salary_input = input("Enter Basic Salary: ")
    calculate_salary(int(salary_input))

    password = "Ak6hf@fsA"
    validate_password_input(password)

    list_manipulation()

    dictionary_manipulation()

    random_numbers()

    principal = 10000
    rate = 10
    years = 2
    compound_interest = calculate_compound_interest(principal, rate, years) # function for CI is imported from second file
    print(f"Compound interest: {compound_interest}")