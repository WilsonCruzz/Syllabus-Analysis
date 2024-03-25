from docx import Document

'''
Target List
'''
dueDateList = [
    "Deadline", "Hand in",
    "Submission", "Turn in",
    "D-day", "Deliverable",
    "Task Date"
]

gradesList = [
    "Grades", "Marks",
    "Score", "Percentage", "Weightage",
    "Evaluation", "Performance"
]

assignmentsList = [
    "Assignment", "Homework",
    "Project", "Task", "Exercise",
    "Problem Set", "Report"
]

examsList = [
    "Exam", "Quiz",
    "Test", "Mid-term",
    "Final", "Assessment"
]



docxFilePath = r"C:\Users\wilso\Desktop\Syllabus - Winter 2024 - Relational Databases.docx"

doc = Document(docxFilePath)

table = doc.tables[0]

for paragraph in doc.paragraphs:
    print(paragraph.text)

for row in table.rows:
    for cell in row.cells:
        print(cell.text)

finalList=[]

doc = Document()
table = doc.add_table(rows=15, columns=1)
for i in range(len(finalList)):
    table.cell(i,0).text = finalList[i]