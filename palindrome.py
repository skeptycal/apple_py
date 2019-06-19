class Palindrome:
    @staticmethod
    def is_palindrome(word: str) -> bool:
        word = word.lower()
        if word == word[::-1]:
            return True
        else:
            return False


l = ['Deleveled', 'adam']

for word in l:
    print(Palindrome.is_palindrome(word))
