import os
import time
import msvcrt
import auditreport

def main():
    loop = True
    while loop is True:
        
        start_time = time.time()
        os.system('cls')
        print_logo()
        print_start_by()

        while time.time() - start_time < 0.7 and loop is True:
            if msvcrt.kbhit():
                msvcrt.getch()
                loop = False
                break

        start_time = time.time()
        os.system('cls')
        print_blank()
        print_start_by()

        while time.time() - start_time < 0.5 and loop is True:
            if msvcrt.kbhit():
                msvcrt.getch()
                loop = False
                break


def print_logo():
    print("""                                    (                                         """)
    print("""   (                (            ) )\ )                                  )    """)
    print("""   )\               )\ )  (   ( /((()/(                                 ( /(  """)
    print("""((((_)(   (        (()/(  )\  )\())/(_)_)     (               (          )\())""")
    print(""" )\ _ )\ ))\       ((_))((_)(_))/| (_)_\ /     ))\ `  )    (   )   )    (_))/ """)
    print("""(_)_ \(_)/((_)      | | (_) | |   | ___ \/   ((_)/(/(    )\ (()\  ()(   | |_  """)
    print("""/ /_\ \ (_))(_)   __| |  _  | |_  | |_/ /   (_)) ((_)_\   ((_)  ((___)  | |_  """)
    print("""|  _  | | | | |  / _` | | | | __| |    /   / _ \ | '_ \   / _ \  | '__| | __| """)
    print("""| | | | | |_| | | (_| | | | | |_  | |\ \  |  __/ | |_) | | (_) | | |    | |_  """)
    print("""\_| |_/  \__,_|  \__,_| |_|  \__| \_| \_|  \___| | .__/   \___/  |_|     \__| """)
    print("""                                                 | |                          """)
    print("""                                                 |_|                          """)


def print_blank():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


def print_start_by():
    print()
    print("               ~~~~~~~~~~ Start by pressing ENTER ~~~~~~~~~~")