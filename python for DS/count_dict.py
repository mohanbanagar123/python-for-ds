def char_count():
    count={}
    for char in count:
        if char:
            count+=[char]
        else:
            count=[char]
    return count

str1=input("enter the words:")
str2=char_count(str1)

for key, values in sorted(str2.items()):
    print(f"{key}:{values}")