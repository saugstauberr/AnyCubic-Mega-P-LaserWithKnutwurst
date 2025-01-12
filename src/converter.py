import bcolors as bcolors
import requirements as requirements
import config_parser as config_parser

def convert_gcode(file):
    remove_before_line = config_parser.read("remove_before_line")

    with open(file, 'r') as textfile:
        content = textfile.read().splitlines()

        requirements.check_remove_before_line(content)

        layer_pos = content.index(remove_before_line) - 1
        layer_pos_i = 0
        while layer_pos_i <= layer_pos:
            content.pop(0)
            layer_pos_i = layer_pos_i + 1
        
        with open("custom.gcode", "r") as custom_file:
            gcode_append = custom_file.read().splitlines()
            for x in gcode_append:
                content.insert(0, x)

        for i in range(len(content)):
            content[i] = content[i].replace("M106", "M3")
            content[i] = content[i].replace("S255", "S254")
            
        new_filename = 'output/CONVERTED_' + file[6:]
        with open(new_filename, 'w') as output:
            for x in content:
                output.write(f"{x}\n")
        print(bcolors.OKGREEN + "Die Konvertierung wurde beendet. Du findest die fertige Datei unter dem output-Ordner.")
