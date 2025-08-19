Important Notes
The code creates text files with different extensions (.pdf, .docx), but these are not actual PDF or Word documents.

For creating real PDF files, you would need a library like ReportLab or FPDF.

For creating real Word documents, you would need a library like python-docx.

The CSV file operations are basic and don't use Python's csv module for proper CSV formatting.

The error handling section demonstrates good practice for file operations.

How to Run
Save the code to a Python file (open_File.py)

Run the script: python open_File.py

When prompted, enter a filename to read

Learning Points
File opening modes: 'w' (write), 'r' (read), 'a' (append)

The importance of closing files (or using context managers with with)

Basic error handling for file operations

String manipulation before writing to files
This README provides a comprehensive explanation of the file handling code, including what it does, limitations, and suggestions for improvement. It's written in clear language that would be appropriate for someone with basic Python knowledge.

