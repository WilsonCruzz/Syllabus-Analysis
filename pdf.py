import PyPDF2
from docx import Document

'''
Target List
'''

dueDateList = [
    "deadline", "hand in",
    "submission", "turn in",
    "d-day", "deliverable",
    "task date"
]

gradesList = [
    "grades", "marks",
    "score", "percentage", "weightage",
    "evaluation", "performance"
]

assignmentsList = [
    "assignment 1", "assignment 2", "homework",
    "project", "task", "exercise",
    "problem set", "report"
]

examsList = [
    "exam", "quiz",
    "test", "mid-term",
    "final", "assessment", 'test 1', 'test 2', 'test 3', 'test 4', 'test 5'
]

'''
weekList
'''
weekList = ['week 1', 'week 2', 'week 3', 'week 4', 'week 5', 'week 6',
            'week 7', 'study week', 'week 8', 'week 9', 'week 10',
            'week 11', 'week 12', 'week 13', 'week 14', 'week']


tableContentList = []

targetList = dueDateList + gradesList + assignmentsList + examsList
catchList = []


# pdf
def processPdfFile(filePath):
    #open file
    pdfFileObj = open(filePath, 'rb')
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

finalList = []








'''
1. get pdf info
2. 從捕捉到第一個week開始 往後確認所有的week assignment %
3. 如果都有就把他整個段落變成新obj
4. 以y座標為基準分組
5. key value配對
6. output 到table
'''
