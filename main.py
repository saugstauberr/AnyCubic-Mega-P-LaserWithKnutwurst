import os
import src.converter as converter
import src.bcolors as bcolors
import src.config_parser as config_parser
import time


gcode_files = []
selected_gcode_file = ""

# ggf. notwendige Ordner erstellen und alle gcode Dateien auflisten
if not os.path.isdir('gcode'):
    os.makedirs("gcode")

if not os.path.isdir('output'):
    os.makedirs("output")

for file in os.listdir("gcode"):
    if file.endswith(".gcode"):
        gcode_files.append("gcode/" + file)

# Begrüßung
print(bcolors.HEADER + "Willkommen im GCode-Converter!")
print("Hier kannst Du Deine exportierten GCodes aus bspw. LightBurn in M3-kompatible Befehle " + 
      "für die Firmware von Knutwurst umwandeln.")
print("Folgende Konfiguration ist eingestellt:\n" + bcolors.ENDC)
print(bcolors.OKBLUE + "Vor dieser Zeile entfernen" + bcolors.ENDC + "\n" + config_parser.read("remove_before_line") + "\n")
print(bcolors.OKBLUE + "Start-GCode" + bcolors.ENDC + "\n" + "Siehe custom.gcode ..." + "\n")

# Bestätigung zum Start des Programms
input(bcolors.OKGREEN + "Drücke die ENTER-Taste, um das Programm zu starten ..." + bcolors.ENDC)

# gcode Ordner überprüfen
# keine gcode Dateien
if(len(gcode_files) == 0):
    print(bcolors.FAIL + "Keine .gcode-Datei(en) gefunden. Bitte verschiebe Deine .gcode-Datei(en) in den gcode-Ordner.")
    quit()

# eine gcode Datei
if(len(gcode_files) == 1):
    selected_gcode_file = gcode_files[0]
    print(bcolors.OKCYAN + "Es wurde eine .gcode-Datei gefunden: " + selected_gcode_file)
    print("Diese Datei wird nun konvertiert..." + bcolors.ENDC)
    converter.convert_gcode(selected_gcode_file)

# mehr als eine gcode Datei
if len(gcode_files) >= 2:
    print(bcolors.WARNING + "Es wurden mehrere .gcode-Dateien gefunden. Welche möchtest Du konvertieren?" + bcolors.ENDC)
    i = 1
    for file in gcode_files:
        print(bcolors.OKBLUE + str(i) + bcolors.ENDC + ") " + file)
        i = i+1
    print("Um eine Datei auszuwählen, schreibe die Zahl vor der Datei in die Konsole:")
    selected_gcode_file = gcode_files[int(input("> ")) - 1]
    print(bcolors.OKCYAN + "Folgende Datei wurde erfolgreich ausgewählt und wird konvertiert: " + selected_gcode_file + bcolors.ENDC)
    converter.convert_gcode(selected_gcode_file)