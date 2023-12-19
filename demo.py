def is_valid_word(word):
    if len(word) < 3 or any(char.isdigit() for char in word):
        return False

    has_vowel = any(char.lower() in "aeiou" for char in word)
    has_consonant = any(char.isalpha() and char.lower() not in "aeiou" for char in word)

    return has_vowel and has_consonant

def countValidWords(s):
    words = s.split()
    valid_word_count = sum(1 for word in words if is_valid_word(word))
    return valid_word_count

# Sample Case 0
s1 = "This is Form16 submission date"
output1 = countValidWords(s1)
print(output1)  # Output: 3

# Sample Case 1
s2 = "Bob wins the game"
output2 = countValidWords(s2)
print(output2)  # Output: 4









# def is_valid_word(word):
#     if len(word) < 3 or any(char.isdigit() for char in word):
#         return False

#     has_vowel = any(char.lower() in "aeiou" for char in word)
#     has_consonant = any(char.isalpha() and char.lower() not in "aeiou" for char in word)

#     return has_vowel and has_consonant

# def countValidWords(s):
#     words = s.split()
#     valid_word_count = sum(1 for word in words if is_valid_word(word))

#     return valid_word_count

# # Sample Input
# s = "This is Form16 submission date"

# # Sample Output
# result = countValidWords(s)
# print(result)  # Output: 3




