import PyPDF2
import re
import pdf
from pdfminer.high_level import extract_text

def weekFinder(filePath):
    pdfFileObj = open(filePath, 'rb')
    reader = PyPDF2.PdfReader(pdfFileObj)
    relatedList = []
    relatedText=''

    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum]
        text = page.extract_text()
        words = re.findall(r'\b[^\W\d_]+ \d+\b', text)  # 使用正则表达式将文本按单词分割

        for index, word in enumerate(words):
            if word.lower() in pdf.weekList:
                yCoordinate = page.mediabox[3] - (page.mediabox[3] - page.mediabox[1]) * index / len(text)  # 使用单词在文本中的索引作为y坐标
                relatedText = words[max(0, index - 5): min(len(words), index + 6)]  # 提取单词周围的相关文本
                relatedList.append({
                    'Week': word,
                    'y': yCoordinate,
                    'relatedText': relatedText,
                })
    pdfFileObj.close()
    return relatedList

def finder(filePath):
    relatedList = []
    pdfFileObj = open(filePath, 'rb')
    text = extract_text(filePath)

    lines = text.split('\n')
    for line in lines:
        for match in re.finditer(r'\b[^\W\d_]+ \d+\b', line):
            word = match.group()  # 获取匹配到的单词
            if word.lower() in pdf.weekList:
                relatedList.append({
                    'Week': word,
                    'relatedText': line,  # 将包含单词的行添加到字典中
                })

    for i in range(len(relatedList)):
        relatedList[i]['relatedText'] = [word for word in relatedList[i]['relatedText'].split() if word.lower() not in pdf.targetList]

    for item in relatedList:
        print(f"Week: {item['Week']}, Related Text: {item['relatedText']}")
    pdfFileObj.close()

if __name__ == "__main__":
    pdf_file = r"C:\Users\wilso\Desktop\syllabus\Syllabus-COMP1054-2024W.pdf"  # 替换为你的PDF文件路径

    keyword=pdf.weekList
    finder(pdf_file)
    '''
    results = weekFinder(pdf_file)
    for result in results:
        print(f"{result['Week']}: ")
        for text in result['relatedText']:
            if text.lower() in pdf.targetList:
                print(text,result['y'])
                '''
