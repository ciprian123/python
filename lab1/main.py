# EX 1 =====================================================================
def cmmdc_helper(a, b):
    """ return the cmmdc of a and b usic euclidean algorithm """
    while b:
        r, a, b = a % b, b, a % b
    return a


def cmmdc_of_list(numbers):
    """ return cmmdc of all numbers from list """ 
    if numbers == []:
        return

    result = numbers[0]
    for number in numbers[1:]:
        result = cmmdc_helper(result, number)
    
    return result



# EX2 ======================================================================
def vowels_counter(string):
    """ return number of vowels in the string """
    counter = 0
    for char in string:
        if char in "aeiouAEIOU":
            counter += 1
    return counter



# EX 3 =====================================================================
def count_occurences(source, target):
    """ return the number of times source is containing target """
    counter, n, m = 0, len(source), len(target)
    for i in range(n - m + 1):
        if source[i:i + m] == target:
            counter += 1
    return counter



# EX 4 =====================================================================
def transform_case(string):
    """ return the transformation of UpperCamelCase into lowercase_with_underscores """
    result = ""
    for i in range(len(string) - 1):
        if string[i].islower() and string[i + 1].isupper():
            result += string[i] + "_"
        elif string[i].isupper():
            result += string[i].lower()
        else:
            result += string[i]
    result += string[-1]
    return result



# EX 5 =====================================================================
def traverse_matrix(matrix):
    """ traverse matrix and print contents in spiral order """
    n = len(matrix)
    k = n // 2

    for i in range(k):
        r = n - i - 2
        p = i + 1

        # top line
        j = i
        while j <= r:
            print(f'{matrix[i][j]} ')
            j += 1

        # right line
        j = i
        while j <= r:
            print(f'{matrix[j][r + 1]} ')
            j += 1

        # bottom line
        j = r + 1
        while j >= p:
            print(f'{matrix[r + 1][j]} ')
            j -= 1

        # left line
        j = r + 1
        while j >= p:
            print(f'{matrix[j][i]} ')
            j -= 1

    if n % 2 == 1:
        print(matrix[k][k])



# EX6 ======================================================================
def is_palindrome(number):
    """ check if the number is a palindrome (is equal with it's reverse value) """
    return str(number) == str(number)[::-1]



# EX 7 =====================================================================
def extract_number(string):
    """ return the first number found in a sentence, None otherwise """
    for idx, char in enumerate(string):
        if char.isdigit():
            result = ""
            start_idx = tmp_idx = idx
            while tmp_idx < len(string) and string[tmp_idx].isdigit():
                result += string[tmp_idx]
                tmp_idx += 1
            if start_idx > 0 and string[start_idx - 1] == '-':
                return int(result) * (-1)
            return int(result)
    return None



# EX 8 =====================================================================
def count_set_bits(number):
    """ return number of set bits python """
    counter = 0
    while number:
        if number % 2 == 1:
            counter += 1
        number //= 2
    return counter



# EX 9 =====================================================================
def most_common_letter(string):
    """ return the letter with the max frequency no matter the case """
    max_counter, max_letter = 0, ''
    for char in string.lower():
        if char.isalpha():
            counter_lower = string.count(char)
            counter_upper = string.count(char.upper())
            if counter_lower + counter_upper > max_counter:
                max_counter = counter_lower + counter_upper
                max_letter = char if counter_lower > 0 else char.upper()
    return max_letter



# EX 10 ====================================================================
def count_words(string):
    """  return number of words, words being delimited by a single space """
    return string.count(' ') + 1