
def reverse_string(str):

    word = str
    reverse_word = []
    i = len(word)
    while i > 0:
        reverse_word += word[i-1]
        i -= 1

    return reverse_word


if __name__ == '__main__':
    plv = input("Digite uma palavra: ")
    print(reverse_string(plv))


