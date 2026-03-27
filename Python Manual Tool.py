import time

# Creator: Good123453\Neo
# Creator roles : system & structure desginer , ux & ui designer ,  arhitechiture designer , developer

# Credit: Chatgpt roles: code analyzer , bug fixer , assistant coder  

# topics and display block : topics cheatsheet display on computer
python_cheatsheet = {
    1: "\nPrint & Comments:\n# print function shows text on screen\nprint('Hello World')\n# this is a single-line comment\n",
    2: "\nVariables:\n# store information in variables\nname = 'Ali'  # text\nage = 20      # number\nheight = 5.9  # decimal\nis_student = True  # True/False\n",
    3: "\nInput:\n# ask user for input\nname = input('Enter your name: ')\nage = input('Enter your age: ')\nprint('Hello', name, 'you are', age, 'years old')\n",
    4: "\nNumbers & Math:\na = 10\nb = 3\nprint(a + b)  # addition\nprint(a - b)  # subtraction\nprint(a * b)  # multiplication\nprint(a / b)  # division\nprint(a % b)  # remainder\n",
    5: "\nConditions:\n# make decisions\nage = 18\nif age >= 18:\n    print('You are an adult')\nelse:\n    print('You are a minor')\n",
    6: "\nLoops:\n# for loop\nfor i in range(5):\n    print(i)\n\n# while loop\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n",
    7: "\nLists:\n# store multiple items\nfruits = ['apple', 'banana', 'mango']\nprint(fruits)\nprint(fruits[0])\nfruits.append('orange')\nprint(fruits)\n",
    8: "\nStrings:\ntext = 'Hello Python'\nprint(text)\nprint(text[0])  # first letter\nprint(len(text))  # length of text\n",
    9: "\nFunctions:\n# group code together\ndef greet():\n    print('Hello! Welcome')\n\ngreet()  # call the function\n",
    10: "\nDictionaries:\n# store key-value pairs\nperson = {'name': 'Ali', 'age': 20}\nprint(person['name'])\nprint(person['age'])\n",
    11: "\nFiles:\n# write to file\nfile = open('myfile.txt', 'w')\nfile.write('Hello World\\n')\nfile.close()\n\n# read from file\nfile = open('myfile.txt', 'r')\ntext = file.read()\nprint(text)\nfile.close()\n",
    12: "\nError Handling:\n# handle errors safely\ntry:\n    num = int(input('Enter a number: '))\n    print('You entered:', num)\nexcept ValueError:\n    print('Invalid input! Please enter a number.')\n"
}

# topics display block: numbers and topics display 
Python_topics = {1:"Print & Comments",
                 2:"Variables",
                 3:"Input",
                 4:"Numbers & Math",
                 5:"Conditions",
                 6:"Loops",
                 7:"Lists",
                 8:"Strings",
                 9:"Functions",
                 10:"Dictionaries",
                 11:"Files",
                 12:"Error Handling",
                 13: "All Topics on Display",
                 14: "Instruction Manual about this Tool",
                 0: "Press 0 to exit"}
                 
                 
                 
                 
                 
# basics instruction block : this tool instructions tells how to use tool and what do not to do                 
def basic_instructions() -> None:
    print("\n\n---  Python Manual Tool  ---\n\n")

    print("How Use: you need to select the topic and you need to give input 1 - 12 others giving numbers are not allowed.\n ")
    print("\npress 14 to open instructions manual\n")
    


# full instructions block : if users give input 14 then computer shows instructions
def instruction() -> None:
    print("\n\n---  Python Manual Tool  ---\n\n")
    time.sleep(0.02)
    print("========  INSTRUCTIONS  ========\n\n")
    time.sleep(0.02)
    print("Creator: Good123453/Neo\n")
    print("Creator roles : system & structure desginer , ux & ui designer ,  arhitechiture designer , developer\n")
    time.sleep(0.02)
    print("Credit: Chatgpt roles: code analyzer , bug fixer , assistant coder\n")
    print("About: This tool helps you to learn fastly Python syntax and basics method foundations.\n\n")
    time.sleep(0.02)
    print("Topics: This Tool have 12 Topics very basic syxtax and readable.\n\n")
    time.sleep(0.02)
    print("Advantages: The advantages about this tool ->  The Tool is giving simple syxtax and Truely readable code with instructions.\n\n  ")
    time.sleep(0.02)
    print("Covering Topics: \n\n1 -> Print & Comments\n \
        \n2 -> Variables\n  \
        \n3 -> Input\n \
        \n4 -> Numbers & Math\n \
        \n5 -> Conditions\n \
        \n6 -> Loops\n \
        \n7 -> Lists\n \
        \n8 -> Strings\n \
        \n9 -> Functions\n \
        \n10 -> Dictionaries\n \
        \n11 -> Files\n \
        \n12 -> Error Handling\n")
    time.sleep(0.02)
    print("\nHow Use: you need to select the topic and you need to give input 1 - 12 others giving numbers are not allowed.\n\n ")
    time.sleep(0.02)
    
    input("Press Enter Key To Continue...")


basic_instructions()
# user decisions block: if user press 14 then open instructions otherwise skip the instructions

once_instructions = input("\n\n\nPress 14 to open instructions panel or Enter Key To Skip instructions...\n\n")
    
if once_instructions == "14":
        instruction()
        
else: 
    print("skip instructions panel")    
while True:
    
    time.sleep(0.5)
    print("\n\n\nPython Manual Menu\n")
    
    for Key , Value in Python_topics.items():
        print(f"{Key} : {Value}")
        time.sleep(0.005)
    try:
        user = int(input("\n\nSelect The Topic: "))

    except ValueError:
        print("Invalid Select Number!\n Please select 1 - 13 and 0 only!\n")
        continue
    except NameError:
        print("Invalid Select Number!\n Please select 1 - 13 and 0 only!\n")
        continue
    
    
    
    if user in [1,2,3,4,5,6,7,8,9,10,11,12]:
        python_cheatsheet_display = python_cheatsheet.get(user)
        time.sleep(0.2)
        print(python_cheatsheet_display)
        input("\n\n\n\nPress Enter Key To Continue...\n\n")

    elif user in [14]:
        instruction()
        input("\n\n\n\nPress Enter Key To Continue...\n\n")
        
    elif user in [13]:
        print("\n\nAll Python Topics on Displying\n")
        
        for key , value in python_cheatsheet.items():
            print(value)
            time.sleep(0.05)
            
        input("\n\n\n\nPress Enter Key To Continue...\n\n")
        
    elif user in [0]:
        print("\n\nTHANKS FOR USING MY PYTHON MANUAL TOOL)\n\n ")
        break

    else:
        print("\n\nInvalid selected number!\n please choose 1 - 14 number\n\n")
        continue
