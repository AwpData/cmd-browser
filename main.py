import os
import sys
from collections import deque
from colorama import Fore

import requests
from bs4 import BeautifulSoup


def readfile(name):
    if os.access(os.getcwd() + "/{}".format(name), os.F_OK):
        with open(os.getcwd() + "/{}".format(name), "r", encoding="utf-8") as r_file:
            for line in r_file:
                print(line.strip("\n"))
    else:
        print("Error: Incorrect URL")


if len(sys.argv) == 2:
    try:
        os.makedirs(sys.argv[1])
    except FileExistsError:
        pass
else:
    print("Error: please only input desired directory")
    exit(-1)

os.chdir(os.getcwd() + "/{}".format(sys.argv[1]))

stack = deque()

while True:
    website = str(input())
    if website == "exit":
        break
    elif website == "back":
        try:
            if len(stack) != 1:  # len(stack) = 1 = we are on the current page
                readfile(stack[len(stack) - 2])  # If there are more pages though, then we return the previous page
                stack.pop()  # Pop the page we just visited and move to the previous page
        except IndexError:
            pass
    else:
        try:
            r = requests.get("https://{}".format(website))  # Attempt to first get info from website
            with open(os.path.join(os.getcwd(), "{}".format(website[:website.rfind(".")])), "w+",
                      encoding="UTF-8") as file:  # First, create a file to store the GET data

                soup = BeautifulSoup(r.content, "html.parser")
                tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
                data = list()
                for tag in tags:
                    spec = soup.find_all(tag)
                    for text in spec:
                        if tag == "a":
                            data.append(Fore.BLUE + text.get_text(" ", strip=True) + "\n")
                        else:
                            data.append(text.get_text(" ", strip=True) + "\n")

                file.writelines(data)  # Then write the text of the page to it

            stack.append(website[:website.rfind(".")])  # Append it to our "back stack
            readfile(website[:website.rfind(".")])  # And now read the content to the screen
        except requests.exceptions.ConnectionError:
            print("Error: Incorrect URL")
