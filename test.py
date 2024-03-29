import PyPDF2
import re
import targetList

def weekFinder(filePath):
    pdfFileObj = open(filePath, 'rb')
    reader = PyPDF2.PdfReader(pdfFileObj)
    relatedList = []

    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum]
        text = page.extract_text()
        words = re.findall(r'\b[^\W\d_]+ \d+\b', text)  # 使用正则表达式将文本按单词分割

        for index, word in enumerate(words):
            if word.lower() in targetList.weekList:
                print(word)
                relatedText = words[max(0, index - 1): min(len(words), index + 1)]  # 提取单词周围的相关文本
                relatedList.append({
                    str(word): relatedText,
                })
    pdfFileObj.close()
    return relatedList

'''
    pdf_file = r"C:\Users\wilso\Desktop\syllabus\Syllabus - Winter 2024 - Relational Databases.pdf"  # 替换为你的PDF文件路径


    results = weekFinder(pdf_file)
    for result in results:
        print(result)
        
        for text in result['relatedText']:
            if text.lower() in keyword.targetList:
                print(result['relatedText'],result['y'])
'''
