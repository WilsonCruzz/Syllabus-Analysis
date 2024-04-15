import tkinter as tk
from tkinter import filedialog, ttk
from function import forDocxFile, PDFConvert
import time


"""Create and configure the GUI."""
def createGui():
    # Create the root window
    root = tk.Tk()
    # Set the title, size, and resizability of the window
    root.title("Syllabus-Analysis")
    root.minsize(600, 600)
    root.resizable(True, True)

    # Add the background image, greeting message, content message, and instruction message to the GUI
    addBackgroundImage(root)
    addGreetingMessage(root)
    addContentMessage(root)
    addInstructionMessage(root)

    # Create a progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    # Return the root window and progress bar
    return root, progress_bar

"""Add a background image to the GUI."""
def addBackgroundImage(root):
    # Load the background image
    root.bgImage = tk.PhotoImage(file="static/georgianc.png")
    # Create a label to display the background image
    bgLabel = tk.Label(root, image=root.bgImage)
    # Set the position and size of the label
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1.5)


"""Add a greeting message to the GUI."""
def addGreetingMessage(root):
    # Create a label to display the greeting message
    greeting = tk.Label(root, text="Welcome to Syllabus-Analysis.", font=("Arial", 22))
    # Set the position of the label
    greeting.pack(pady=25)


"""Add a content message to the GUI."""
def addContentMessage(root):
    # Create a label to display the content message
    content = tk.Label(root, text="This program analyzes Microsoft Word syllabus files\n "
                                  "and generates weekly schedules for students.", font=("Arial", 16))
    # Set the position of the label
    content.pack(pady=15)


"""Add an instruction message to the GUI."""
def addInstructionMessage(root):
    # Create a label to display the instruction message
    instruction = tk.Label(root, text="Please click the button below to select "
                                      "the Word file for analysis.", font=("Arial", 14))
    # Set the position of the label
    instruction.pack(pady=20)


"""Process a DOCX file and return the result."""
def processDocxFile(docxFilePath, outputPath, column, filePath):

    # If the user selects a PDF file, convert it to a docx file
    if docxFilePath.lower().endswith('.pdf'):
        docxFilePath = PDFConvert.convertToDocx(docxFilePath)
    
    # Set the input path for the DOCX file
    inputData = docxFilePath

    # Set the list of functions to be applied to the input data
    functionsList = [forDocxFile.weekFinder, forDocxFile.dupCheck,
                     forDocxFile.targetWordsChecker, forDocxFile.concatList,
                     # ref.https://www.w3schools.com/python/python_lambda.asp
                     lambda x: forDocxFile.insertToTable(x, outputPath, column, filePath)]

    # Apply the functions to the input data
    for function in functionsList:
        # Update the input data with the result of the current function
        inputData = function(inputData)

    # Convert the generated schedule to a PDF
    PDFConvert.convertToPdf(outputPath)

    # Return the result of the last function
    return inputData


"""Open a file dialog and return the selected file path."""
def selectFiles():
    # Open a file dialog to select multiple files
    return filedialog.askopenfilenames()

"""Process multiple files."""
def processMultipleFiles(filePaths, progress_bar):

    # Declare column variable to be changed for each file
    column = 0

    # Determine how many files were uploaded
    total_files = len(filePaths)

    # Set the output path for the processed file
    outputPath = filedialog.asksaveasfilename(defaultextension=".docx")

    # Iterate over each selected file path
    for idx, filePath in enumerate(filePaths, 1):

        # Increment column count so that each files contents is written to a separate one
        column += 1

        # Process each file
        processDocxFile(filePath, outputPath, column, filePath)

        # Update progress bar value based on the current file index
        progress_value = (idx / total_files) * 100
        progress_bar["value"] = progress_value
        # Update the GUI to reflect the changes
        progress_bar.update()

    # Reset progress bar after processing all files
    progress_bar["value"] = 0
