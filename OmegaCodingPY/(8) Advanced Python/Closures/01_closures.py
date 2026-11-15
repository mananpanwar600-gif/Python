def main_welcome(msg):
    # msg = "Welcome"
    def sub_welcome():
        print("Welcome to python")
        print(msg)
        print("These are advance concepts...")
    return sub_welcome()

main_welcome("Welcome")