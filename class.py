def find_vowels(input_string):
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}
    found_vowels = []

    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1
            found_vowels.append(char)
    
    return found_vowels, vowel_count

# Example usage
input_string = "Hello, World!"
found_vowels, vowel_count = find_vowels(input_string)

print("Vowels found in the string:", found_vowels)
print("Count of each vowel:", vowel_count)
