# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    sort_word = sorted(word)
    sort_anagram = sorted(anagram)
    if sort_word == sort_anagram:
        return True
    return False

print(find_anagram("yam", "may"))