import re

def hi(list_input):
    return print("How can I help you?")

def add(list_input):
    if len(list_input)<3:
        return print("Please enter a space after the add command ""name"", and phone number (or other information)")
    if len(list_input)>=3:
        list_input[1] = list_input[1]
        if list_input[1] in phone_book.keys():
            list_input[1] += "_copy"    
            phone_book.update({list_input[1]: list_input[2]})
            return  print("Contact exists. I saved his as:",list_input[1])
        phone_book.update({list_input[1]: list_input[2]})
        return print("Your contact has been saved")

def change(list_input):
    if len(list_input)<3:
        return print("Please enter a space after the command ""change""  name, and phone number (or other information)")
    if len(list_input)>=3:
        list_input[1] = list_input[1]
        if list_input[1] in phone_book.keys():
            phone_book.update({list_input[1]: list_input[2]})
            return print("The number your contact ",list_input[1],", has been changed.")
        else:
            phone_book.update({list_input[1]: list_input[2]})
            return print("Contact ",list_input[1],"not found, but i saved his for you.")
    
def phone(list_input):
    if len(list_input)<2:
        return print("Please enter a space after the command ""phone"" name.")
    str_out = "List of requested contacts " + list_input[1]+":"
    for key, value in phone_book.items():
        if key.lower() == list_input[1].lower():
            str_out += "\n"+"Name: "+str(key)+".  Phone number: "+str(value)  
    if str_out == "List of requested contacts:":
        str_out = "The requested contact was not found."
    return print(str_out)

def show_all(list_input):
    if len(phone_book):
        str_out = "List of your contacts:"
        for key, value in phone_book.items():
            str_out += "\n"+"Name: "+str(key)+".  Phone number: "+ str(value)
        return print(str_out)    
    else:
        return print("Your contact list is empty.")

def  double_commands(list):
    if (len(list)>1) and ((list[0] == "show") and (list[1].lower() == "all")):
        return "show all" 
    else:
        return list[0]
    
def not_know():
    str_out = "Сommands not recognized.\nEnter commands that I know: "
    for i in list_out:
        str_out += (str(i) + ", ")
    str_out += "if you want me to finish working.\nOr one of the commands: "
    for i in dict_def.keys():
        str_out += (i + ", ")
    str_out += "if you want me to help you."
    return print(str_out)

phone_book = {}

list_out = ["good bye","close","exit"]
dict_def = {"hello": hi, "add": add, "change": change, "phone": phone, "show all": show_all }

def bot_assistant(): #bot assistant))) 
    print("Hi, I'm a helper bot))). How can I help you?")
    list_command = []
    while True:
        input_text = input("Waiting for commands: ")
        list_command = re.split(r"[ ]+",input_text)
        list_command[0] = list_command[0].lower()
        list_command[0] = double_commands(list_command)
        if list_command[0] in dict_def.keys():
            dict_def[list_command[0]](list_command)
        elif input_text in list_out:
            print("Good bye!")
            break
        else:
            not_know()

bot_assistant()