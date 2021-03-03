import sys
from os import path


inFile = open(sys.argv[1], "r")
outFile = open("formattedLatex.txt", "w")

if len(sys.argv) == 3:

    outFile.write("\\usepackage{tcolorbox}")
    outFile.write("\\def\code#1{\\texttt{#1}}")

outFile.write("\\begin{tcolorbox}" + "\n")

for line in inFile:
    writeLine = line.replace("\\", "\\textbackslash").replace(" ", "\\ ").replace("\n", "")
    writeLine = writeLine.replace("&", "\\&").replace("$", "\\$").replace("\t", "\\ \\ \\ \\ ")
    writeLine = writeLine.replace("#", "\\#").replace("%", "\\%").replace("{", "\\{").replace("}", "\\}")

    outFile.write("\\code{-")
    outFile.write(writeLine)
    outFile.write("}\\\\" + "\n")


outFile.write("\\end{tcolorbox}" + "\n")

inFile.close()
outFile.close()
