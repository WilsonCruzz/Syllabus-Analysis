import PyPDF2

tableContentList = []
catchList = []


'''
1. get pdf info
2. 從捕捉到第一個week開始 往後確認所有的week assignment %
3. 如果都有就把他整個段落變成新obj
4. 以y座標為基準分組
5. key value配對
6. output 到table
'''
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
        for target in keyword.targetList:
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


