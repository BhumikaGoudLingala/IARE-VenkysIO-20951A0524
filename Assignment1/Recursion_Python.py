def rev(para):
    if len(para)==0:
        return ""
    else:
        return para[-1]+rev(para[:-1])
def rev_s(para):
    word=para.split()
    r_word=[rev(i) for i in word]
    return " ".join(r_word)
paragraph=input()
print("Original Paragraph:\n",paragraph)
print("Reversal of each string in a paragraph:\n",rev_s(paragraph))
