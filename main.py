import tkinter as tk
from tkinter import filedialog
from function import forDocxFile


"""Create and configure the GUI."""
def createGui():
    root = tk.Tk()
    root.title("Syllabus-Analysis")
    root.minsize(600, 600)
    root.resizable(True, True)

    addBackgroundImage(root)
    addGreetingMessage(root)
    addContentMessage(root)
    addInstructionMessage(root)

    return root


"""Add a background image to the GUI."""
def addBackgroundImage(root):
    bgImage = tk.PhotoImage(file="static/georgianc.png")
    bgLabel = tk.Label(root, image=bgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1.5)


"""Add a greeting message to the GUI."""
def addGreetingMessage(root):
    greeting = tk.Label(root, text="Welcome to Syllabus-Analysis.", font=("Arial", 22))
    greeting.pack(pady=25)


"""Add a content message to the GUI."""
def addContentMessage(root):
    content = tk.Label(root, text="This program analyzes Microsoft Word syllabus files\n "
                                  "and generates weekly schedules for students.", font=("Arial", 16))
    content.pack(pady=15)


"""Add an instruction message to the GUI."""
def addInstructionMessage(root):
    instruction = tk.Label(root, text="Please click the button below to select "
                                      "the Word file for analysis.", font=("Arial", 14))
    instruction.pack(pady=20)


"""Process a DOCX file and return the result."""
def processDocxFile(docxFilePath):
    inputData = docxFilePath
    functionsList = [forDocxFile.weekFinder, forDocxFile.dupCheck,
                     forDocxFile.targetWordsChecker, forDocxFile.concatList,
                     forDocxFile.insertTable]

    for function in functionsList:
        inputData = function(inputData)

    return inputData


"""Open a file dialog and return the selected file path."""
def selectFile():
    return filedialog.askopenfilename()


"""Main function to run the application."""
def main():
    root = createGui()

    btn = tk.Button(root, text="Click me", command=lambda: processDocxFile(selectFile()))
    btn.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
