#1st test
def return_10():
    return 10

#2nd test
def add(num1, num2):
    sum = num1 + num2
    return sum

#3rd test
def subtract(num1, num2):
    result = num1 - num2
    return result

#4th test
def multiply(num1, num2):
    result = num1 * num2
    return result

#5th test
def divide(num1, num2):
    result = num1 / num2
    return result

#6th test
def length_of_string(string):
    return len(string)

#7th test
def join_string(string_1, string_2):
    result = string_1 + string_2
    return result

#8th test
def add_string_as_number(num1, num2):
    result = int(num1) + int(num2)
    return result

#9th, 10th and 11th test - I have realised that this function will work across all three tests, so commenting out the two below
def number_to_full_month_name(num1):
    import calendar
    return calendar.month_name[num1]

# #10th test
# def number_to_full_month_name(num1):
#     import calendar
#     return calendar.month_name[num1]

#11th test
# def number_to_full_month_name(num1):
#     import calendar
#     return calendar.month_name[num1]

#12th, 13th and 14th test  - I have reaalised that this function will work across all three tests, so commenting out the two below
def number_to_short_month_name(num1):
    import calendar
    return calendar.month_abbr[num1]

# #13th test
# def number_to_short_month_name(num1):
#     import calendar
#     return calendar.month_abbr[num1]

#14th test
# def number_to_short_month_name(num1):
#     import calendar
#     return calendar.month_abbr[num1]

#15th test
def cube_side_length(num1):
    result = num1 ** 3
    return result

#16th test
def reverse_string(string1):
    return string1[::-1]

#17th test
def fahrenheit_to_celsius(num1):
    return (num1 - 32) / 1.8
