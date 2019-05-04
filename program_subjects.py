import utility
import data_access
from classes import Subject


def subject_menu(subjects):
    all_subjects = data_access.convert_to_subjects()
    chosen_subjects = subjects

    while True:
        print_menu(chosen_subjects)
        command = utility.menu_choice()

        if command == "back":
            return chosen_subjects
        elif command == "subjects":
            chosen_subject = choose_subjects(all_subjects)
            if chosen_subject != None:
                chosen_subjects.append(chosen_subject)
        elif command == "add":
            get_subject()
        elif command == "remove":
            input("---------- NOT IMPLEMENTED! ----------")
        else:
            input("---------- Invalid value ----------")


def print_menu(subjects):
    print("~~~~~~~~~~ Chosen audit subjects ~~~~~~~~~~")
    print()

    if len(subjects) == 0:
        print("You haven't chosen any subjects")
        print()
    else:
        for subject in subjects:
            print(f"Subject: {subject.subject}")
            print(f"Description: {subject.description}")
            print()

    print("[subj] - Choose subject(s)")
    print("[add] - Add new subject")
    print("[rmv] - Remove subject")
    print("[back] - Go back")
    print()


def choose_subjects(subjects):
    print("~~~~~~~~~~ Subjects ~~~~~~~~~~")
    print()

    for subject in subjects:
       print(f"Subject: {subject.subject}")
       print(f"Description: {subject.description}")
       print()

    #TODO: While-loop for as long as valid input is given

    print("[back] - Go back")
    choice = input("Choose existing subject by inputting the subject name > ").strip().lower()

    if choice == "back":
        return

    for i in range(len(subjects)):
        if choice == subjects[i].subject.lower():
            return subjects[i]

    input("---------- Invalid input ----------")


def get_result(question):
    result = input(question)

    while result.strip() == "":
        print("Invalid value")
        result = input(question)

    return result


def get_subject():
    print("~~~~~~~~~~ Add New Subject ~~~~~~~~~~")
    print()

    question_pattern_subject = ["Subject", "Description"]
    sep = " > "

    id = utility.get_id()
    category = get_result(question_pattern_subject[0] + sep)
    description = get_result(question_pattern_subject[1] + sep)
    subject = Subject(id, category, description)

    data_access.create_subject(subject)

    print()
    print("---------- New subject created! ----------")