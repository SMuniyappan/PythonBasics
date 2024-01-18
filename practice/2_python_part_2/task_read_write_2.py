"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def write_to_file(file_path, content, encoding, separator='\n'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(separator.join(content))

def reverse_order(words):
    return list(reversed(words))


word_list = generate_words()

write_to_file('file1.txt', word_list, 'utf-8')

reversed_word_list = reverse_order(word_list)

write_to_file('file2.txt', reversed_word_list, 'cp1252', separator=',')

print("Original words:", word_list)
print("Reversed order:", reversed_word_list)
