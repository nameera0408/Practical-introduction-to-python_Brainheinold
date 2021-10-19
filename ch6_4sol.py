vowels =['a','e','i','o','u']
count =0
word =input("Enter Word: ")
for i in range(len(word)):
    for j in range(5):
        if vowels[j] in word[i]:
            count += 1
print(count)
