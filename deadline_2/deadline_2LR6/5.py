import re
def is_palindrome(text):
    """
    Проверяет, является ли строка палиндромом, игнорируя регистр и знаки препинания.
    """
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', cleaned_text)
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False
word1 = "волонтёр"
print(f"'{word1}' является палиндромом? {is_palindrome(word1)}") 
word2 = "Гасилов"
print(f"'{word2}' является палиндромом? {is_palindrome(word2)}")
word3 = "Волонтёр"
print(f"'{word3}' является палиндромом? {is_palindrome(word3)}")
phrase1 = "А роза упала на лапу Азора"
print(f"'{phrase1}' является палиндромом? {is_palindrome(phrase1)}")
phrase2 = "Do geese see God"
print(f"'{phrase2}' является палиндромом? {is_palindrome(phrase2)}")