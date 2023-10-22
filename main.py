from parser_src import AntlrParser


if __name__ == '__main__':
    # create a parser
    parser = AntlrParser()
    # specific to calculator implementation: keep asking input as long as user does not input 'quit'
    quit_p = False
    while not quit_p:
        user_input = input()
        if user_input.lower() == 'quit':
            quit_p = True
        # don't raise errors if empty input
        elif user_input == '':
            continue
        else:
            parser.parse(user_input)
