import os
import sys
from collections import deque

import requests as requests


def readfile(name):
    if os.access(os.getcwd() + "/{}".format(name), os.F_OK):
        with open(os.getcwd() + "/{}".format(name), "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
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
            if r.status_code == 200:
                with open(os.path.join(os.getcwd(), "{}".format(website[:website.find(".")])), "w",
                          encoding="UTF-8") as file:  # First, create a file to store the GET data
                    file.writelines(r.text)  # Then write the text of the page to it
                stack.append(website[:website.find(".")])  # Append it to our "back stack
                readfile(website[:website.find(".")])  # And now read the content to the screen
        except requests.exceptions.ConnectionError:
            print("URL does not exist!")
