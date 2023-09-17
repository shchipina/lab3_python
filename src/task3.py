def min_length_word(sentence):
    # перетворення речення на масив
    words = sentence.split()
    # присвоєння змінній перше значення
    min_word = words[0]
    # перебір через цикл масива та знаходження слова з найменшою довжиною
    for word in words:
        if len(min_word) > len(word):
            min_word = word

    return min_word

result = min_length_word('The shortest word in this sentence')
print(f"Найкоротше слово в реченні - {result}")