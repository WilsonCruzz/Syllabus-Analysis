import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from function import forDocxFile, PDFConvert
import os
import webbrowser

def openLinkedinSebastian(event):
    webbrowser.open('https://www.linkedin.com/in/sebastian-bruce/')

def openLinkedinChunwei(event):
    webbrowser.open('https://www.linkedin.com/in/chun-wei-wang-9ab9981a2/')
"""Create and configure the GUI."""
def createGui():
    # Create the root window
    root = tk.Tk()
    # Set the title, size, and resizability of the window
    root.title("Syllabus-Analysis")
    root.minsize(650, 650)
    root.resizable(True, True)

    # Add the background image, greeting message, content message, and instruction message to the GUI
    addBackgroundImage(root)

    # Create a frame to hold the labels
    frame = tk.Frame(root)
    frame.pack(pady=10)
    # Create a label to display the creators of the program
    textLabel = tk.Label(frame, text="Created by: ", font=("Arial", 10, "bold"))
    textLabel.grid(row=0, column=0)
    # Create a label to display the names
    sebastianLabel = tk.Label(frame, text="Sebastian Bruce", font=("Arial", 10, "underline"), fg="blue",
                              cursor="hand2")
    sebastianLabel.bind("<Button-1>", openLinkedinSebastian)
    sebastianLabel.grid(row=0, column=1)
    # Create a label to display the word "and"
    andLabel = tk.Label(frame, text=" & ", font=("Arial", 10, "bold"))
    andLabel.grid(row=0, column=2)
    # Create a label to display the names
    chunweiLabel = tk.Label(frame, text="Chun-Wei Wang", font=("Arial", 10, "underline"), fg="blue",
                            cursor="hand2")
    chunweiLabel.bind("<Button-1>", openLinkedinChunwei)
    chunweiLabel.grid(row=0, column=3)

    addGreetingMessage(root)
    addContentMessage(root)
    addInstructionMessage(root)

    # Create a progress bar
    progressBar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progressBar.pack(pady=10)

    # Return the root window and progress bar
    return root, progressBar

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
    greeting.pack(pady=0)


"""Add a content message to the GUI."""
def addContentMessage(root):
    # Create a label to display the content message
    content = tk.Label(root, text="This program analyzes class syllabus files\n "
                                  "and generates week-by-week schedules for students.", font=("Arial", 16))
    # Set the position of the label
    content.pack(pady=15)


"""Add an instruction message to the GUI."""
def addInstructionMessage(root):
    # Create a label to display the instruction message
    instruction = tk.Label(root, text="Please click the button below to select "
                                      "word or pdf files for analysis,\n" 
                                      "then select a directory for output.", font=("Arial", 14))
    # Set the position of the label
    instruction.pack(pady=0)

    # Create disclaimer
    textLabel = tk.Label(root, text=r"*100% accuracy cannot be guaranteed, be sure to double check results*", font=("Arial", 10, "bold"))
    textLabel.pack(pady=10)


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
    # Return the result of the last function
    return inputData


"""Open a file dialog and return the selected file path."""
def selectFiles():
    # Open a file dialog to select multiple files
    return filedialog.askopenfilenames()

"""Process multiple files."""
def processFiles(filePaths, progressBar):

    # Declare column variable to be changed for each file
    column = 0

    # Determine how many files were uploaded
    totalFiles = len(filePaths)

    # Set the output path for the processed file
    outputPath = filedialog.asksaveasfilename(defaultextension=".docx")

    # Iterate over each selected file path
    for idx, filePath in enumerate(filePaths, 1):

        # Increment column count so that each files contents is written to a separate one
        column += 1

        # Process each file
        processDocxFile(filePath, outputPath, column, filePath)

        # Update progress bar value based on the current file index
        progressValue = (idx / totalFiles) * 100
        progressBar["value"] = progressValue
        # Update the GUI to reflect the changes
        progressBar.update()

    # Open the file for the user if they have word installed and a license to use it
    try:
        os.startfile(outputPath)

    # If not open a window displaying the error
    except FileNotFoundError:
        messagebox.showerror("Error", "Failed to open the file. It appears you don't have Microsoft Word installed or don't have a license to use it. Consider installing a compatible application to open .docx files, or try opening the file with a different program.")
