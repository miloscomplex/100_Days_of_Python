#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()


print(names)

for name in names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_text = letter.read()
        file = open(f"./Output/ReadyToSend/letter_{name.strip()}.txt", mode="w")
        file.write(letter_text.replace("[name]", name.strip()))
        file.close()
