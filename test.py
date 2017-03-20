words = {"Yeet":"Diabetes","Neap":"A type of spring tide"}
word=""
definition=""
choice=""
while True:
    print("enter quit to quit")
    choice=input()
    if choice=="new":
        print("Please enter the word you'd wish to add.")
        word=input()
        print("Please enter the definition for "+word)
        definition=input()
        words[word]=definition
    elif choice=="print":
        for i in words:
            print(i)
    elif choice=="definition":
        print("Which word would you like the definition of")
        word=input()
        definition=words[word]
        print(definition)
    elif choice=="quit":
        break
    else:
        print("Invalid option")

