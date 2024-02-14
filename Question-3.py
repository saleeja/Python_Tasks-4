"""3.Write a Python code to remove all characters except a           
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e)
"""

def character(sample_string, target_character):
    result = ''.join(char for char in sample_string if char == target_character)
    return result

sample_string = 'exercises'

target_character = 's'

result = character(sample_string, target_character)

print(f"Expected Result: '{result}'")
