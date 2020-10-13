# EX1 ======================================================================
def get_n_fibo(n):
    ''' 
        function to return a list containing first n fibbonaci numbers
    '''
    if n < 0:
        return []
    if n <= 1:
        return [1]
    a = b = 1
    result = [1, 1]
    for _ in range(3, n + 1):
        c = a + b
        a = b
        b = c
        result.append(b)
    return result


# EX2 ======================================================================
def is_prime(number):
    '''
        function thats return the primality of a number
    '''
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    idx = 3
    while idx * idx <= number:
        if number % idx == 0:
            return False
        idx += 2
    return True


def filter_primes(numbers):
    ''' 
        function to return a list of prime numbers from numbers list
    '''
    primes = [number for number in numbers if is_prime(number)]
    return primes


# EX3 ======================================================================
def set_operations(list1, list2):
    ''' 
        return a list containing intersection, reunion and set differences of list1 and list2
    '''
    result = []
    list1, list2 = set(list1), set(list2)
    result.append(list1 & list2) # intersection
    result.append(list1 | list2) # union
    result.append(list1 - list2) # difference
    result.append(list2 - list1)
    return result


# EX4 ======================================================================
def compose(notes, moves, start_idx):
    '''
        function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer).
    '''
    result = []
    result.append(notes[start_idx])

    for move in moves:
        start_idx = start_idx + move
        result.append(notes[start_idx])
        print(start_idx)
    
    return result


# EX6 ======================================================================
def replace_in_matrix(matrix):
    ''' 
        function that receives as parameter a matrix and will return the
        matrix obtained by replacing all the elements under the main diagonal with 0
    '''
    if matrix == [] or matrix[0] == []:
        return
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i > j:
                matrix[i][j] = 0
    return matrix
    

# EX7 ======================================================================
def is_palindrome(number):
    '''
        check if number is palindrome
    '''
    return str(number) == str(number[::-1])


def get_palindrome_results(numbers):
    '''
        function that receives as parameter a list of numbers (integers) and
        will return a tuple with 2 elements. The first element of the tuple 
        will be the number of palindrome numbers found in the list and the 
        second element will be the greatest palindrome number
    '''
    tmp = [number for number in numbers if is_palindrome(number)]
    return (len(tmp), max(tmp))

