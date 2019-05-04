import data_access
import utility
from classes import Audit_Info


def audit_info_menu(audit_info, site_id):

    while True:
        print_menu(audit_info)
        command = utility.menu_choice()

        if command == "back":
            return audit_info
        elif command == "add":
            audit_info = get_audit_info(site_id)
        elif command == "edit":
            input("---------- NOT IMPLEMENTED! ----------")
        else:
            input("---------- Invalid value ----------")


def print_menu(info):
    print("~~~~~~~~~~ Audit Info ~~~~~~~~~~")
    print()
    
    if info == None:
        print("You haven't added any info yet")
    else:
        print(f"Description: {info.description}")
        print(f"Schedule: {info.schedule}")
        print(f"Auditer: {info.auditer}")
        print()

    print()
    print("[add] - Add new audit")
    print("[edit] - Edit audit info")
    print("[back] - Go back")
    print()


def get_audit_info(site_id):
    print("~~~~~~~~~~ Change Audit Info ~~~~~~~~~~")
    print()

    question_pattern_audit = ["Description", "Audit schedule", "Auditer"]
    sep = " > "

    id = utility.get_id()
    description = get_result(question_pattern_audit[0] + sep)
    auditer = get_result(question_pattern_audit[1] + sep)
    schedule = get_result(question_pattern_audit[2] + sep)

    info = Audit_Info(id, description, auditer, schedule)
    info.site_id = site_id
    data_access.create_audit_info(info)

    print()
    print("---------- Updated! ----------")

    return info


def get_result(q):
    result = input(q)

    while result.strip() == "":
        print("Invalid value")
        result = input(q)

    return result