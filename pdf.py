import PyPDF2

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
'''
weekList
'''
weekList = ['week1', 'week2', 'week3', 'week4', 'week5', 'week6',
            'week7', 'study week', 'week8', 'week9', 'week10',
            'week11', 'week12', 'week13', 'week14']
tableContentList = []

targetList = dueDateList + gradesList + assignmentsList + examsList
catchList = []
# pdf
pdfFileObj = open(r"C:\Users\wilso\Desktop\Syllabus-COMP1054-2024W.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

numContextWords = 10
pagesWithKeywords = {}

for pageNum, page in enumerate(pdfReader.pages):
    pageText = page.extract_text()
    words = pageText.split()
    for target in targetList:
        if target in words:
            targetIndex = words.index(target)

            startIndex = max(0, targetIndex - numContextWords)
            endIndex = min(len(words), targetIndex + numContextWords + 1)
            context = ''
            for i in range(startIndex, endIndex):
                context += words[i] + ' '
            if pageNum in pagesWithKeywords:
                pagesWithKeywords[pageNum].append((target, context))
            else:
                pagesWithKeywords[pageNum] = [(target, context)]
            print(target, context)

pdfFileObj.close()

'''
print(len(pdfReader.pages))
page0Obj = pdfReader.pages[0]
page0Text = page0Obj.extract_text()
page1Obj = pdfReader.pages[1]
page1Text = page1Obj.extract_text()
page2Obj = pdfReader.pages[2]
page2Text = page2Obj.extract_text()
page3Obj = pdfReader.pages[3]
page3Text = page3Obj.extract_text()

print(page0Text)
print(page1Text)
print(page2Text)
print(page3Text)
'''
'''
1. get pdf info
2. 從捕捉到第一個week開始 往後確認所有的week assignment %
3. 如果都有就把他整個段落變成新obj
4. 以y座標為基準分組
5. key value配對
6. output 到table
'''