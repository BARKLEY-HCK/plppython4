#File =open("samuel.pdf", "w")
#File.write("This is a samuel's PDF file content.")

#File =open("samuel.txt", "w")
#File.write("This is a samuel's Documentation content.")

#File =open("samuel.docx", "w")
#File.write("This is a samuel's Word file content.")

#File =open("samuel.txt", "r")
#data=File.read()
#print(data)

#File = open("samuel.csv", "w")
#content = "Samuel is at the party.\n"
#File.write(content.upper())

#File = open("samuel.csv", "a")
#content = "Invite professor to the party also\n"
#File.write(content)

#File = open("samuel.csv", "r")
#data = File.read()
#print(data)

FileName = input("Enter the file name: ")

try:
    File = open(FileName, "r")
    content = File.read()
    print(content)
except FileNotFoundError:
    print(f"The file {FileName} not found.")
finally:
    File.close()
    print("File closed successfully.")
    