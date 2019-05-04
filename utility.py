import random
import os.path
"""
This part is for some global functions and shit that every module can use
"""

def menu_choice():
    """ Dictionary for all the menu commands """

    choice = input("Input your command and press ENTER > ")
    print()

    #TODO: Somekind of validation part here?

    return {
        "site" : "site",
        "exst" : "existing",
        "add" : "add",
        "back" : "back",
        "trgt" : "targets",
        "info" : "info",
        "subj" : "subjects",
        "rslt" : "result",
        "show" : "show",
        "save" : "save",
        "load" : "load",
        "prnt" : "print",
        "edit" : "edit",
        "rmv"  : "remove",
        "exit" : "exit"
    }.get(choice, "Invalid value")


def get_id():
    """ Primitive ID-generator for starters """

    return random.randint(10000, 99999) * random.randint(10000, 99999)