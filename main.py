import forDocxFile
import tkinter as tk
from tkinter import filedialog
'''
gui setting
'''
# creat screen obj
root = tk.Tk()
# name title
root.title("Syllabus-Analysis")
# size
# resizable
root.minsize(600, 600)
root.resizable(True, True)

def main(docxFilePath):
    # Initialize input data with the provided argument.
    inputData = docxFilePath

    # Define a list of functions to be executed sequentially.
    functionsList = [forDocxFile.weekFinder, forDocxFile.dupCheck,
                      forDocxFile.targetWordsChecker, forDocxFile.concatList,
                      forDocxFile.insertTable]

    # Iterate through the list of functions and execute each one with input data.
    for function in functionsList:
        # Execute the current function with input data and obtain the output.
        outputData = function(inputData)

        # Update the input data with the output for the next iteration.
        inputData = outputData


def show():
    # Open a file dialog to select a file.
    filePath = filedialog.askopenfilename()
    # Call the main function with the selected file path.
    main(filePath)


# Create a button widget with the text "Open" and the command to call the show function.
btn = tk.Button(root, text="Open", command=show)

# Pack the button widget onto the Tkinter root window.
btn.pack()

# Keep running the Tkinter main event loop to display the GUI and handle events.
root.mainloop()

