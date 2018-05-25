# -*- coding: UTF-8 -*-


def guide(description, code=None, start=False, show_instruction=True):
    """Print guide in example.

    Args:
        description      (str)     : The description.
        code             (str/list): The code of the guide. If multiple lines needed, use list.
        start            (bool)    : If the guide is a start, it will not promote user input at the beginning.
        show_instruction (bool)    : False will hide all instructions.
    """

    # if not show instruction, skip
    if not show_instruction:
        return

    # if is not start, promote a user input for making steps effect.
    if not start:
        raw_input()

    # separate description to 80 char per line.
    length = len(description)
    descriptions = []
    while description:
        descriptions.append(description[:80])
        description = description[80:]

    # print the upper box
    print "┌───────────────────────────────────────────────────────────────────────────────────┐"

    # print the description
    for d in descriptions:
        print "│", d, (80 - len(d)) * ' ', "│"

    # print the lower box
    print "└───────────────────────────────────────────────────────────────────────────────────┘"

    # print code
    if code:
        # one line code
        if type(code) == str:
            print ">>>", code
        # multi line code
        elif type(code) == list:
            for line in code:
                print ">>>", line

    print
