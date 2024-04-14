"""
The targetList is a list that combines several other lists. These lists include:

1. dueDateList: Contains phrases related to due dates.
2. gradesList: Contains percentages from 1% to 100%. These represent possible grades or weights for assignments.
3. assignmentsList: Contains phrases related to assignments.
4. examsList: Contains phrases related to exams.

The targetList is used to filter words in a document. Any word that matches an item in the targetList is considered a "target word". These target words are used for further processing, such as generating a weekly schedule for students.
"""
dueDateList = [
    "deadline ", "hand in ",
    "submission ", "turn in",
    "d-day ", "deliverable ",
    "task date "
]

gradesList = ['1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%',
              '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%',
              '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%',
              '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%',
              '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%',
              '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%',
              '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '70%',
              '71%', '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%',
              '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%',
              '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%']


assignmentsList = [
    "assignment", "homework ", "assignment 1", "assignment 2", "assignment 3", "assignment 4", "assignment 5",
    "project ", "task ", "exercise ",
    "problem set ", "report ", "lab "
]

examsList = [
    "exam", "quiz",
    "test", "mid-term",
    "final", "assessment", 'test 1', 'test 2', 'test 3',
    'test 4', 'test 5'
]
'''
weekList
'''
weekList = ['week 1', 'week 2', 'week 3', 'week 4', 'week 5',
            'week 6', 'week 7', 'week 8', 'week 9', 'week 10',
            'week 11', 'week 12', 'week 13', 'week 14', 'week 15', 'study week']

targetList = dueDateList + gradesList + assignmentsList + examsList
