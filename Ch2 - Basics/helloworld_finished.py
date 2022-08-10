#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#


def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

if __name__ == "__main__":
    main()
print(__name__) #main  in own program run code  otherwise not run ✅
#Python assign the '__main__' to the __name__ variable when you run the script directly and the module name if you import the script as a module.
#https://www.pythontutorial.net/python-basics/python-__name__/