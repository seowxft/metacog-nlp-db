"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/per_quiz_test/<user_id>', methods=['POST'])
def create_per_quiz_test(user_id):
    content = json_body()
    per_quiz = PerQuizTest()
    per_quiz.prolificID      = field(content, 'prolificID')
    per_quiz.userID      = field(content, 'userID')
    per_quiz.condition      = field(content, 'condition')
    per_quiz.date        = field(content, 'date')
    per_quiz.startTime   = field(content, 'startTime')
    per_quiz.section   = field(content, 'section')
    per_quiz.sectionTime   = field(content, 'sectionTime')
    per_quiz.quizTry   = field(content, 'quizTry')
    per_quiz.quizNumTotal = field(content, 'quizNumTotal')
    per_quiz.quizNum = field(content, 'quizNum')
    per_quiz.quizTime = field(content, 'quizTime')
    per_quiz.quizResp = field(content, 'quizResp')
    per_quiz.quizRT = field(content, 'quizRT')
    per_quiz.quizAns = field(content, 'quizAns')
    per_quiz.quizCor = field(content, 'quizCor')
    per_quiz.quizCorTotal = field(content, 'quizCorTotal')


    BaseObject.check_and_save(per_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
