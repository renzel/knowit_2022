import time

start = time.time()

with open("dict.txt", "r") as f:
    dictionary = f.read()
letter = ""
with open("letter.txt", "r") as f:
    letter = f.read()

list_of_tuples = []
dict_dictionary = {}
for item in dictionary.split("\n"):
    key, value = item.split(",")
    dict_dictionary[key] = value

translation = ""

max_length = len(max(dict_dictionary.keys(), key=len))
words = []
while len(letter) > 0:
    words = []
    word = ""
    for char in letter:
        word += char
        if len(word) > max_length:
            break
        if word in dict_dictionary:
          
            words.append(word)
    longest_string = max(words, key=len)
    translation += dict_dictionary[longest_string] + " "
    letter = letter[len(longest_string):]

print(len(translation))
end = time.time()
print(end - start)