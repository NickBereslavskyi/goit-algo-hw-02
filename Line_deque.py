from collections import deque

def is_palindrome(input_string):
    # Попередня обробка: видалити пробіли, перевести в нижній регістр
    cleaned = ''.join(char.lower() for char in input_string if char.isalnum())
    
    d = deque(cleaned)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклади тестування
test_strings = [
    "A man a plan a canal Panama",
    "Racecar",
    "Hello world",
    "Was it a car or a cat I saw"
]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' -> {'Паліндром' if result else 'Не паліндром'}")