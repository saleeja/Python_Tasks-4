"""3.Write a Python code to remove all characters except a           
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e)
"""

def character(sample_string, target_character):
    # result is a string that contains only characters matching the target_character
    result = ''.join(filter(lambda char: char == target_character, sample_string))
    return result

sample_string = 'exercises'

target_character = 'e'

result = character(sample_string, target_character)

print(f"Expected Result: '{result}'")
