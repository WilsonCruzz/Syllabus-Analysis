import tkinter as tk
from tkinter import filedialog
from function import forDocxFile


"""Create and configure the GUI."""
def createGui():
    # Create the root window
    root = tk.Tk()
    # Set the title, size, and resizability of the window
    root.title("Syllabus-Analysis")
    # Set the title, size, and resizability of the window
    root.minsize(600, 600)
    # Set the title, size, and resizability of the window
    root.resizable(True, True)

    # Add the background image, greeting message, content message, and instruction message to the GUI
    addBackgroundImage(root)
    addGreetingMessage(root)
    addContentMessage(root)
    addInstructionMessage(root)

    # Return the root window
    return root


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
def processDocxFile(docxFilePath):
    # Set the input path for the DOCX file
    inputData = docxFilePath
    # Set the output path for the processed file
    outputPath = filedialog.asksaveasfilename(defaultextension=".docx")
    # Set the list of functions to be applied to the input data
    functionsList = [forDocxFile.weekFinder, forDocxFile.dupCheck,
                     forDocxFile.targetWordsChecker, forDocxFile.concatList,
                     # ref.https://www.w3schools.com/python/python_lambda.asp
                     lambda x: forDocxFile.insertToTable(x, outputPath)]

    # Apply the functions to the input data
    for function in functionsList:
        # Update the input data with the result of the current function
        inputData = function(inputData)

    # Return the result of the last function
    return inputData


"""Open a file dialog and return the selected file path."""
def selectFile():
    # Open a file dialog to select a file
    return filedialog.askopenfilename()