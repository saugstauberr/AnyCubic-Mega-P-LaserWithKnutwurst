import src.bcolors as bcolors
import src.config_parser as config_parser

def check_requirements(content):
    remove_before_line = config_parser.read('remove_before_line')


    # Remove before line - Check
    if remove_before_line in content:
            print("[ " + bcolors.OKGREEN + bcolors.BOLD + "✓" + bcolors.ENDC + " ] - " + 
                  '"' + remove_before_line + '" wurde gefunden.' + bcolors.ENDC)
    else:
        print("[ " + bcolors.FAIL + bcolors.BOLD + "X" + bcolors.ENDC + " ] - " + 
                  '"' + remove_before_line + '" wurde nicht gefunden. Prozess wird abgebrochen.' + bcolors.ENDC)
        quit()