import os
import pathlib

headerName = "../../ORBIS_Skeleton/GNM_Framework/basic_quad/FileNames.h"

def CreateHeader(data):
   try:
      headerFile = open(headerName, "x")
      headerFile.write("#include <string>\n\n")
      headerFile.write("namespace ImportFileNames{\n")
      headerFile.write("std::string files[]{\n")
      headerFile.write("}};")
      headerFile.close()
   except FileExistsError:
      pass

   headerFile = open(headerName, "r")

   listOfLines = headerFile.readlines()

   listOfLines[len(listOfLines) - 1] = data
   listOfLines.append("};}")

   headerFile = open(headerName, "w")
   headerFile.writelines(listOfLines)
   headerFile.close()

def FindFiles():
   path = pathlib.Path().resolve()
   files = os.listdir(path)

   for f in files:
      if f[-3:].lower() == "png" or f[-3:].lower() == "jpg":
         command = "orbis-image2gnf.exe -i {fileName:}.{fileType:} -f BC1Unorm -o {fileName}.gnf"
         os.system(command.format(fileName = f[:-4], fileType = f[-3:].lower()))
         data = "\t\"{fileName}.gnf\"\n\t\"{fileName}.xml\"\n"
         CreateHeader(data.format(fileName = f[:-4] ))
         print(f[:-4])

if __name__ == '__main__':
    FindFiles()
