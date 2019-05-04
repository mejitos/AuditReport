import data_access
import utility
from classes import Site_Info


def site_menu(site):

    while True:
        if site != None:
            site = site
        print_menu(site)
        
        command = utility.menu_choice()

        if command == "back":
            return site
        elif command == "existing":
            site = choose_site()
        elif command == "add":
            site = get_site_info()
        else:
            input("---------- Invalid value ----------")


def print_menu(site):
    print("~~~~~~~~~~ Site Menu ~~~~~~~~~~")
    print()

    if site == None:
        print("You haven't chosen site yet")
    else:
        print(f"Site name: {site.site_name}")
        print(f"Site address: {site.site_address}")
        print(f"Site manager: {site.site_manager}")
        print(f"Manager contact: {site.manager_contact}")

    print()
    print("[exst] - Choose existing site")
    print("[add] - Create new site")
    print()
    print("[back] - Go back")
    print()


def get_site_info():
    print("~~~~~~~~~~ Add New Site ~~~~~~~~~~")
    print()

    question_pattern_info = ["Site name", "Site address", "Site manager", "Manager contact"]
    sep = " > "

    id = utility.get_id()
    name = get_result(question_pattern_info[0] + sep)
    address = get_result(question_pattern_info[1] + sep)
    manager = get_result(question_pattern_info[2] + sep)
    contact = get_result(question_pattern_info[3] + sep)
    site = Site_Info(id, name, address, manager, contact)

    data_access.create_site(site)

    print()
    print("---------- Site created! ----------")

    return site


def choose_site():
    print("~~~~~~~~~~ Existing sites ~~~~~~~~~~")
    print()

    sites = data_access.convert_to_sites()

    for site in sites:
        print("[ID] " + site.id)
        print("Site: " + site.site_name)
        print()

    choice = input("Choose existing site by inputting the site name > ")

    for i in range(len(sites)):
        if choice == sites[i].site_name:
            return sites[i]


def get_result(question):
    result = input(question)

    while result.strip() == "":
        print("Invalid value")
        result = input(question)

    return result