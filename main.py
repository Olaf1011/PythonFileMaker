import os
import pathlib

headerName = "../../ORBIS_Skeleton/GNM_Framework/basic_quad/FileNames.h"



def CreateHeader(name):

    data = "\t\t\"/app0/{fileName}.gnf\",\n\t\t\"/app0/{fileName}.xml\"\n"
    data = data.format(fileName=name)

    enum = "\tenum class TextureKeys : unsigned int\n"

    try:
        # Write the boiler plate if the file doesn't exist yet
        headerFile = open(headerName, "x")
        headerFile.write("#pragma once\n\n")
        headerFile.write("#include <string>\n\n")
        headerFile.write("//DO NOT TOUCH THIS FILE!\n\n")
        headerFile.write("namespace ImportFileNames{\n\n")
        headerFile.write(enum)
        headerFile.write("\t{\n")
        headerFile.write("\t\tDEFAULT = 0,\n")
        headerFile.write("\t}\n")
        headerFile.write("\tinline const std::string FILES_LOC[]\n\t{\n")
        headerFile.write("\t\t\"/app0/Default.gnf\",\n")
        headerFile.write("\t\t\"/app0/Default.xml\"\n")
        headerFile.write("\t}\n};")
        headerFile.close()
    except FileExistsError:
        pass

    headerFile = open(headerName, "r")

    listOfLines = headerFile.readlines()

    if enum in listOfLines:
        start = listOfLines.index(enum)
        counter = start
        while listOfLines[counter].find('}') != 1:
            counter += 1
            enumInput = "\t\t{0} = {1}, \n\t{2}\n".format(name.upper(), (counter - (start + 2)) * 2, "};")
            if listOfLines[counter].find(name.upper()) > 0:
                print("!! This entry name already exist!!\nPlease contact the programmer")
                assert False

        listOfLines[counter] = enumInput


    # Check if there are already existing lines. If so add a comma to them.
    if listOfLines[-3].find('{') != 1:
        # Get the last character (\n) and replace it with with a , and add the \n back
        tempLine = listOfLines[-3][:-1]
        tempLine += ",\n"
        listOfLines[-3] = tempLine

    # Override the last the character (} };) we add them back on later
    listOfLines[-2:] = data

    listOfLines.append("\t};\n}")

    headerFile = open(headerName, "w")
    headerFile.writelines(listOfLines)
    headerFile.close()


def FindFiles():
    path = pathlib.Path().resolve()
    files = os.listdir(path)

    for f in files:
        if f[-3:].lower() == "png" or f[-3:].lower() == "jpg":
            command = "orbis-image2gnf.exe -i {fileName:}.{fileType:} -f BC1Unorm -o {fileName}.gnf"
            os.system(command.format(fileName=f[:-4], fileType=f[-3:].lower()))
            CreateHeader(f[:-4])
            print(f[:-4])


if __name__ == '__main__':
    FindFiles()
    print("Done")
