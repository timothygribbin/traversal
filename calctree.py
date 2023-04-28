import os.path
def get_input():
    while True:
        user_input = input("Enter the path to your directory: ")
        if os.path.isdir(user_input):
            return user_input
        else:
            print("There is no directory at the address " + user_input + ".")

def polish_notation(path):
    print(path)
    if os.path.isdir(path) == True:
        file_list = os.listdir(path)
        for name in file_list:
            child_path = os.path.join(path,name)
            polish_notation(child_path)


def reverse_polish_notation(path):
    if os.path.isdir(path) == True:
        file_list = os.listdir(path)
        for name in file_list:
            child_path = os.path.join(path,name)
            reverse_polish_notation(child_path)
    print(path)

def main():
    x = get_input()
    
    print("Polish Notation: ")
    
    polish_notation(x)

    print("-----------------")

    print("Reverse Polish Notation: ")

    reverse_polish_notation(x)


main()