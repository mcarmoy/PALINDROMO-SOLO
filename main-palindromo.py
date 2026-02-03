def is_palindrome(word):
    # 1. Ponemos todo en minúsculas para que 'Radar' y 'radar' sean iguales
    word = word.lower()
    
    # 2. Creamos la palabra al revés
    word_reversed = word[::-1]
    
    # 3. Comparamos si son iguales
    if word == word_reversed:
        return True
    else:
        return False

# Prueba básica
print(is_palindrome("radar"))  # Debería devolver True
print(is_palindrome("casa"))   # Debería devolver False