def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    "
name (str) = "Annet"
age (int) = 28
print(f"My name is {name} and I am {age} years old")


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
       # 5 (int): 5
    Returns:
       # str: "Greater", "Lesser", or "Equal"
    """
    pass

    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

if __name__ == "__main__"
    number = int(input("5: "))
    result = conditional_check(number)
    print(f"The number is {result} than 10.")

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
       # n (int): Upper limit
    Returns:
        #int: Sum of numbers
    """
    pass
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = int(input((20): "))
    result = calculate_sum(n)
    print(f"The sum of numbers from 1 to {n} is {result}.")

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        #numbers (list): List of numbers
    Returns:
        #tuple: (sum, max, min)
    """
    pass

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, maximum, minimum

if __name__ == "__main__":
    numbers = list(map(int, input(5 10 15 20 30: ").split()))
    result = perform_operations(numbers)
    print(f"Sum: {result[0]}, Max: {result[1]}, Min: {result[2]}")

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        #students_dict (dict): Dictionary of student names and scores
    Returns:
        #list: Names of students with scores > 80
    """
    pass
if __name__ == "__main__":
    n = int(input("2: "))
    students = {}
    for _ in range(n):
        name = input("ARIELA: ")
        score = int(input(f"90 {ARIELA}: "))
        students[ARIELA] = score
        name = input("JAMES: ")
        score = int(input(f"70 {JAMES}: "))
        students[JAMES] = score
    result = find_top_students(students)
    print("Students with scores above 80:", result)

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        #list1 (list): First list
        #list2 (list): Second list
    Returns:
        #set: Common elements
    """
    pass
if __name__ == "__main__":
    list1 = list(map(int, input("1 2 3 4 5 6: ").split()))
    list2 = list(map(int, input("1 3 5 7 9 11: ").split()))

    common_elements = find_common_elements(list1, list2)
    print("Common elements:", common_elements)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        #a (float): First number
        #b (float): Second number
    Returns:
        #dict: Results of arithmetic operations
    """
    pass
    results = {
        "addition": a + b,
        "subtraction": a - b,
            "multiplication": a*b
           "division": a / b if b != 0 else "Undefined (division by zero)"
    }
    return results 
if __name__ == "__main__":
    a = float(input("7 (a): "))
    b = float(input("3 (b): "))
    results = perform_arithmetic_operations(a, b)
    print("Results of arithmetic operations:")
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        #x (bool): First boolean
        #y (bool): Second boolean
    Returns
        #dict: Results of logical operations
    """
    pass
    results = {
        "AND": x and y,
        "OR": x or y,
        "NOT x": not x,
        "NOT y": not y,
        "XOR": (x and not y) or (not x and y)
    }
    return results
if __name__ == "__main__":
    x = input("2 (True/False): ").strip().lower() == "true"
    y = input("4 (True/False): ").strip().lower() == "true"
    results = perform_logical_operations(x, y)
    print("Results of logical operations:")
    for operation, result in results.items():
        print(f"{operation}: {result}")

def bitwise_ops(a, b):
    """
    #Perform bitwise operations.
    Args:
        #a (int): First integer
        #b (int): Second integer
    Returns:
        #dict: Results of bitwise operations
    """
    pass
    results = {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT a": ~a,
        "NOT b": ~b,
        "Left shift a by 1": a << 1,
        "Right shift a by 1": a >> 1,
        "Left shift b by 1": b << 1,
        "Right shift b by 1": b >> 1
    }
    return results
if __name__ == "__main__":
    # Input two integers
    a = int(input("5 (a): "))
    b = int(input("3 (b): "))
    results = perform_bitwise_operations(a, b)
    print("Results of bitwise operations:")
    for operation, result in results.items():
        print(f"{operation}: {result}")
