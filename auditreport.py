import os
import utility
import data_access
import start_screen
import program_sites
import program_auditinfo
import program_subjects
import program_auditresult
import program_targets

"""
TODO: Funktio joka tarkastaa käyttäjän syötettä (vai sisällytetäänkö tämä suoraan)
        = validointifunktiot???
"""

def main():
    start_screen.main()

    data_access.check_for_dir()

    site = None
    targets = []
    audit_info = None
    subjects = []
    results = []
    deviations = []

    while True:
        main_menu()
        command = utility.menu_choice()

        if command == "exit":
            break
        elif command == "site":
            site = program_sites.site_menu(site)
        elif command == "targets":
            if site != None:
                targets = program_targets.targets_menu(site.id)
            else:
                print("---------- You need to choose site first! ----------")
                print()
                input("---------- Press ENTER to return ----------")
        elif command == "info":
            if site != None:
                audit_info = program_auditinfo.audit_info_menu(audit_info, site.id)
            else:
                print("---------- You need to choose site first! ----------")
                print()
                input("---------- Press ENTER to return ----------")
        elif command == "subjects":
            subjects = program_subjects.subject_menu(subjects)
        elif command == "result":
            if site != None and len(targets) != 0 and audit_info != None and len(subjects) != 0:
                results = program_auditresult.get_audit_data(site.id, targets, audit_info.id, subjects)
            else:
                input("---------- You are missing needed information ----------")
        elif command == "show":
            show_report(audit_info, site, subjects, results)
        elif command == "save":
            input("---------- NOT IMPLEMENTED! ----------")
        elif command == "load":
            input("---------- NOT IMPLEMENTED! ----------")
        elif command == "print":
            input("---------- NOT IMPLEMENTED! ----------")
        else:
            input("---------- Invalid value ----------")

    input("Close the program by pressing ENTER")


def main_menu():
    os.system("cls")
    start_screen.print_logo()

    print("~~~~~~~~~~ Main Menu ~~~~~~~~~~")
    print()
    print("[site] - Auditable site")
    print("[trgt] - Manage audit targets")
    print("[info] - Audit Info")
    print("[subj] - Choose audit subjects")
    print("[rslt] - Add audit result")
    print("[show] - Show report")
    print("[save] - Save audit")
    print("[load] - Load audit")
    print("[prnt] - Print report")
    print("[exit] - Close the program")
    print()


def show_report(info, site, subjects, results):
    print("~~~~~~~~~~ Site info ~~~~~~~~~~")
    print()
    if site == None:
        print("No site info added")
    else:
        print(site.site_name)
        print(site.site_address)
        print(site.site_manager)
        print(site.manager_contact)
    print()
    
    print("~~~~~~~~~~ Audit info ~~~~~~~~~~")
    print()
    if info == None:
        print("No audit info added")
    else:
        print(info.description)
        print(info.schedule)
        print(info.auditer)
    print()

    print("~~~~~~~~~~ Auditable subjects ~~~~~~~~~~")
    print()
    if len(subjects) == 0:
        print("No audit subjects chosen")
        print()
    else:
        for subject in subjects:
            print(subject.subject)
            print(subject.description)
            print()

    print("~~~~~~~~~~ Audit results ~~~~~~~~~~")
    print()
    if len(results) == 0:
        print("No audit results added")
        print()
    else:
        for audit in results:
            print(audit.target)

            for i in range(len(subjects)):
                print(subjects[i].subject + ": " + audit.results[i])
            print()

    input("---------- Press ENTER to return ----------")


if __name__ == "__main__":
    main()