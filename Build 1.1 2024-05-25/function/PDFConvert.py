import comtypes.client
import os
from pdf2docx import Converter

# Convert a docx file to a PDF
def convertToPdf(inputFile):

    # Create the output path (same as input path, but .pdf)
    outputPath = os.path.splitext(inputFile)[0] + ".pdf"

    try:
        # Create a new instance of word
        word = comtypes.client.CreateObject('Word.Application')

        # Open the provided word file
        doc = word.Documents.Open(inputFile)

        # Check if the output file already exists, and if so, delete it
        if os.path.exists(outputPath):
            os.remove(outputPath)

        # Save the file to the output path as a PDF (17)
        doc.SaveAs(outputPath, FileFormat=17)

        # Close document
        doc.Close()

        # Quit the instance of word
        word.Quit()

    except Exception as e:
        print("Error occurred while converting to PDF:", e)

    return outputPath

def convertToDocx(inputFile):

    # Create the output path (same as input path, but .docx)
    outputFile = os.path.splitext(inputFile)[0] + ".docx"

    try:
        # Check if the output file already exists, and if so, delete it
        if os.path.exists(outputFile):
            os.remove(outputFile)

        # Create a converter object
        cv = Converter(inputFile)

        # Convert the PDF file to DOCX
        cv.convert(outputFile, start=0, end=None)

        # Close the converter
        cv.close()
    except Exception as e:
        print("Error occurred while converting to DOCX:", e)
    
    return outputFile
