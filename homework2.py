import os
import socket

def printInfo():
    totalWords = 0
    mostText = ""
    maxWordCount = 0

    a = open(outFilePath + outFile, "a")
    a.write("Text files in folder: ")
    for file in os.listdir(fileDir):
        if file.endswith(".txt"):
            a.write(file + ", ")
    a.write("\nTotal Words:\n")

    for file in os.listdir(fileDir):
        if file.endswith(".txt"):
            txtFile = open(fileDir + file, "r")
            wordCount = len(txtFile.read().split())

            if wordCount > maxWordCount:
                maxWordCount = wordCount
                mostText = file

            totalWords += wordCount
            a.write(file + ": " + str(wordCount) + "\n")
            txtFile.close()

    a.write("Total number of words in all text files: " + str(totalWords) + "\n")
    a.write("Text file with the most words: " + mostText + "\n")

    computerIP = socket.gethostbyname(socket.gethostname())
    a.write("Your machine's IP: " + computerIP + "\n")
    a.close()


fileDir = "/home/data/"
outFilePath = "/home/output/"
outFile = "result.txt"

printInfo()
output = open(outFilePath + outFile, "r")
for line in output.readlines():
    print(line)
