import os
import bcolors as bcolors
import config_parser as config_parser

def check_requirements():
    if not os.path.isdir('gcode'):
        os.makedirs("gcode")

    if not os.path.isdir('output'):
        os.makedirs("output")


    

def check_remove_before_line(content):
    remove_before_line = config_parser.read('remove_before_line')


    # Remove before line - Check
    if remove_before_line in content:
            print("[ " + bcolors.OKGREEN + bcolors.BOLD + "✓" + bcolors.ENDC + " ] - " + 
                  '"' + remove_before_line + '" wurde gefunden.' + bcolors.ENDC)
    else:
        print("[ " + bcolors.FAIL + bcolors.BOLD + "X" + bcolors.ENDC + " ] - " + 
                  '"' + remove_before_line + '" wurde nicht gefunden. Prozess wird abgebrochen.' + bcolors.ENDC)
        quit()