#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Day 24/Input/Names/invited_names.txt") as name_list:
    list_of_names = name_list.readlines()
#Replace the [name] placeholder with the actual name.
with open("./Day 24/Input/Letters/starting_letter.txt") as template_mail:
    template_content = template_mail.read()

#Save the letters in the folder "ReadyToSend".
    for name in list_of_names:
        cleaned_name = name.strip()
        copy_letter = template_content
        template_content = template_content.replace("[name]", cleaned_name)
        with open(f"./Day 24/Output/ReadyToSend/letter_to_{cleaned_name}.txt", "w") as files:
            files.write(copy_letter)