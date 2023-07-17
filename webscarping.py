import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore
import time


def DisplayElement(all_element) -> None:
    for i in all_element:
        print(Fore.YELLOW + f"{i}" + Fore.RED + "\n\n========================================================================================\n")


def Search(soup, all_element, element_to_search) -> None:
    elements = soup.findAll(str(element_to_search))
    for element in elements:
        all_element.append(element)


def SaveInFile(all_element, name) -> None:
    with open(f"{name}.txt", "w") as file:
        for line in all_element:
            file.write(str(line) + "\n")
    print(Fore.RED + "File Saved")


def main() -> None:
    try:
        print("\n")
        print(Fore.RED + "========================================================================================")
        print("\n")

        print(Fore.BLUE + """
         __      __      ___.       _________                          .__                
        /  \    /  \ ____\_ |__    /   _____/ ____ _____ _____________ |__| ____    ____  
        \   \/\/   // __ \| __ \   \_____  \_/ ___| \__  \_  __ \____ \|  |/    \  / ___\ 
         \        /\  ___/| \_\ \  /        \  \___ / __ \|  | \/  |_> >  |   |  \/ /_/  >
          \__/\  /  \___  >___  / /_______  /\___  >____  /__|  |   __/|__|___|  /\___  / 
               \/       \/    \/          \/     \/     \/      |__|           \//_____/   
                                """)

        print(Fore.RED + "\n                            https://github.com/Silme94")

        print("\n")
        print(Fore.RED + "========================================================================================")

        url = input(Fore.GREEN + "\nEnter a Url : ")
        element_to_search = input("\nWhat Element You Want To Search ? : ")
        save = input("\nWanna Save Element In a File ? (Y/N) : ")

        name = None

        if save.lower() == "y":
            name = input(Fore.GREEN + "\nPut a Name For Your File : ")

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        print("\n")
        print(Fore.RED + "========================================================================================")
        print("\n")

        all_element = []

        Search(soup, all_element, element_to_search)

        DisplayElement(all_element)

        if name != None:
            SaveInFile(all_element, name)

        print(Fore.RED + "\n========================================================================================\n")

    except Exception as ex:
        print(Fore.RED + ex)


if __name__ == "__main__":
    os.system("cls")
    main()
    print(Fore.RESET)
    os.system("pause")
