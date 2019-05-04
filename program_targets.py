import utility
import data_access
from classes import Target


def targets_menu(site_id):
    chosen_targets = data_access.get_targets_by_site_id(site_id)

    while True:
        print_menu(chosen_targets)
        command = utility.menu_choice()

        if command == "back":
            return chosen_targets
        elif command == "add":
            chosen_targets.append(get_target(site_id))
        elif command == "edit":
            input("---------- NOT IMPLEMENTED! ----------")
        elif command == "remove":
            input("---------- NOT IMPLEMENTED! ----------")
        else:
            input("---------- Invalid value ----------")


def print_menu(targets):
    print("~~~~~~~~~~ Manage audit targets ~~~~~~~~~~")
    print()

    if len(targets) == 0:
        print("You have not chosen any targets")
    else:
        for target in targets:
            print(f"{target.id}: {target.name}")
    print()
    
    print("[add] - Add new target")
    print("[edit] - Edit target")
    print("[rmv] - Remove target")
    print("[back] - Return")
    print()


def get_target(site_id):
    print("~~~~~~~~~~ Add new target ~~~~~~~~~~")
    print()

    question_pattern = ["Name"]
    sep = " > "

    id = utility.get_id()
    name = get_result(question_pattern[0] + sep)
    target = Target(id, name)
    target.site_id = site_id
    data_access.create_target(target)

    print()
    print("---------- New target created! ----------")

    return target


def get_result(question):
    result = input(question)

    while result.strip() == "":
        print("Invalid value")
        result = input(question)

    return result