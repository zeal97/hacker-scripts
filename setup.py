# Setup for installing hacker-scripts
import os, sys, shutil
from sys import argv

script, arguement = argv

# Gets the root directory (Drive letter for Windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
#os.chdir(rootDirectory)

# mainDirectory = C:\hacker-scripts (Windows)
mainDirectory = os.path.join(rootDirectory + "\\hacker-scripts")

# binDirectory = C:\hacker-scripts\bin (Windows)
binDirectory = os.path.join(mainDirectory + "\\bin")

def main():
    # If the directory hacker-scripts already exists in the root directory then ...
    if (os.path.exists(mainDirectory)):
        # Asks the user whether to overrite the directory 
        print("A directory named \"hacker-scripts\" already exists in {}, do you want to replace it? (y/N)".format(rootDirectory))

        # Changes user provided input to upper case
        choice = input().upper()

        if(choice == "Y" or choice == "YES"):
            # Removes the entire directory tree
            shutil.rmtree(mainDirectory)
            # Proceed with the installation
            install()
        else:
            sys.exit()
    
    # If hacker-scripts does not exist in the root directory then proceed with installation
    else:
        install()

def install():
    # Creates the directories hacker-scripts and hacker-scripts\bin in the root directory
    os.mkdir(mainDirectory)
    os.mkdir(binDirectory)

    # Scripts to be installed are in the "src" directory of the downloaded package os.listdir() returns the list
    scripts = os.listdir("src")

    for script in scripts:
        script = os.path.join("src", script)

        if (not os.path.isdir(script)):
            if(script != "src\\hs-config.py"):
                shutil.copy(script, binDirectory)
            else:
                shutil.copy(script, mainDirectory)

    # Add C:\hacker-scripts and C:\hacker-scripts\bin to PATH
    path = os.environ['PATH']

    os.system("setx PATH \"\"")
    os.system("setx PATH \"{};{};{}\"".format(path, mainDirectory, binDirectory))

    print("""
    The installation was successful, you can use the command \"hs-help\" in a new terminal to view the help documentation
    Please open an new terminal session and run hs-config to configure hacker-scripts
    If you face any problems after installation please check the documentation at github.com/areeb-beigh/hacker-scripts 
    """)

    choice = input()

if arguement == "install":
    main()
else:
    print("Error: Invalid arguement, pass arguement \"install\" to install hacker-scripts")