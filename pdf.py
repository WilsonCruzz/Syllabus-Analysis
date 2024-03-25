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
1. get pdf info
2. 從捕捉到第一個week開始 往後確認所有的week assignment %
3. 如果都有就把他整個段落變成新obj
4. 以y座標為基準分組
5. key value配對
6. output 到table
'''