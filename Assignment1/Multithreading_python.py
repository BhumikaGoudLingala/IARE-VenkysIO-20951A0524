import threading
def reverse_string(string):
    return string[::-1]
def reverse_words(para):
    words = para.split()
    threads = []
    reversed_words = [''] * len(words)
    for i, word in enumerate(words):
        t = threading.Thread(target=lambda i, word: reversed_words.__setitem__(i, reverse_string(word)), args=(i, word))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return ' '.join(reversed_words)

para = input()
reversed_paragraph = reverse_words(para)
print(reversed_paragraph)
