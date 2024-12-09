def count_char(word):
    count={}
    for char in word:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count

str1=input("enter the string:")
str2=count_char(str1)

for key,values in sorted(str2.items()):
    print(f"{key}:{values}")