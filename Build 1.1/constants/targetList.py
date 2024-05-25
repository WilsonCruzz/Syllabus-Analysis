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

gradesList = [f'{i}%' for i in range(1, 101)]+[f'({i}%)' for i in range(1, 101)]

labGradeList = [f'lab {i} ({j}%)' for i in range(1, 20) for j in range(1, 101)]
assignmentGradeList = [f'assignment {i} ({j}%)' for i in range(1, 20) for j in range(1, 101)]

assignmentsList = [
    "homework",
    "project", "task", "exercise", "introduction email", "structured topic paragraph", "research project",
    "research skills quiz", "evaluating sources", "plagiarism quiz", "apa references (research project)",
    "draft thesis and outline", "thesis and outline (research project)", "apa reference list",
    "draft research project", "linkedin post", "thesis and outline", "presentation assigned"
    "problem set", "report", "giving feedback (presentation)", "final research project",
    "final course reflection", "introduction",
]+[f'assignment {i}' for i in range(1, 20)]+[f'lab {i}' for i in range(1, 20)]

examsList = [
    "exam", "quiz", "midterm quiz",
    "test", "mid-term", 'mid-semester test'
] + [f'test {i}' for i in range(1, 20)]
'''
weekList
'''
weekList = ['study week'] + [f'week {i}' for i in range(1, 20)]

targetList = dueDateList + gradesList + assignmentsList + examsList + assignmentGradeList + labGradeList
