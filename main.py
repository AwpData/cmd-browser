import os
import re
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
if len(sys.argv) == 2:
    try:
        os.makedirs(sys.argv[1])
    except FileExistsError:
        pass
else:
    print("Error: please only input desired directory")
    exit(-1)

os.chdir(os.getcwd() + "/{}".format(sys.argv[1]))
websites = {"nytimes.com": nytimes_com, "bloomberg.com": bloomberg_com}
while True:
    website = str(input())
    if website == "exit":
        break
    else:
        if website in list(websites.keys()) and re.match(r"[\w]+\.[\w]+", website) is not None:
            print(websites[website])
            with open(os.path.join(os.getcwd(), "{}".format(website[:website.find(".")])), "w+") as file:
                file.writelines(websites[website])
        else:
            if os.access(os.getcwd() + "/{}".format(website), os.F_OK):
                with open(os.getcwd() + "/{}".format(website), "r") as file:
                    for line in file:
                        print(line.strip())
            else:
                print("Error: Incorrect URL")
