"""2.Print even length words in a string.
Sample String : ''I love coding"
Expected Result : “love, coding”
"""


# even length words in a string 
 
def EvenWords(string): 
    even_length_words = [word for word in string.split(' ') if len(word) % 2 == 0]
    return even_length_words

string = "I love coding "
words = EvenWords(string)
print(", ".join(words))
