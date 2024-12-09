def create_dictionary(words):
    dict={}
    for word in words:
        if word:
            first_char=word[0].upper()
            if first_char not in dict:
                dict[first_char]=[]
            dict[first_char].append(word)
    return dict

words=input("enter the words:").split()
result=create_dictionary(words)

for key,values in sorted(result.items()):
    print(f"{key}:{values}")
