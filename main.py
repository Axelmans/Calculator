from parser_src import AntlrParser


if __name__ == '__main__':
    parser = AntlrParser()
    quit_p = False
    while not quit_p:
        print("Enter a number (or type \"quit\" to end program): ")
        user_input = input()
        if user_input.lower() == 'quit':
            quit_p = True
        else:
            parser.parse(user_input)

