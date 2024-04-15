from function import gui

"""Main function to run the application."""
def main():
    # Create the GUI and get the progress bar
    root, progress_bar = gui.createGui()
    # Create a button to select the Word files for analysis.
    btn = gui.tk.Button(root, text="Upload file(s)", command=lambda: gui.processMultipleFiles(gui.selectFiles(), progress_bar))
    btn.pack()
    # Run the main loop of the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
    print("Done")