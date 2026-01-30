# utils/assessment.py

def get_questions(domain):
    """
    Return questions based on selected domain
    """

    if domain == "python":
        return [
            {
                "question": "What is the output of print(5+2)?",
                "options": ["52", "7", "Error", "None"],
                "answer": "7"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": "def"
            }
        ]

    elif domain == "sql":
        return [
            {
                "question": "Which SQL command is used to fetch data?",
                "options": ["GET", "SELECT", "FETCH", "OPEN"],
                "answer": "SELECT"
            },
            {
                "question": "Which clause is used to filter rows?",
                "options": ["ORDER BY", "GROUP BY", "WHERE", "FROM"],
                "answer": "WHERE"
            }
        ]

    return []


def calculate_score(questions, user_answers):
    score = 0
    for i in range(len(questions)):
        if user_answers[i] == questions[i]["answer"]:
            score += 1
    return score
