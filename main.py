from function import gui

"""Main function to run the application."""
def main():
    # Create the GUI
    root = gui.createGui()
    # Create a button to select the Word file for analysis. Use a lambda function to ensure that gui.processDocxFile(
    # gui.selectFile()) executes when the button is clicked, rather than when the button is created.
    btn = gui.tk.Button(root, text="Click me", command=lambda: gui.processDocxFile(gui.selectFile()))
    # Set the position of the button
    btn.pack()
    # Run the main loop of the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
