"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/mem_quiz_test/<user_id>', methods=['POST'])
def create_mem_quiz_test(user_id):
    content = json_body()
    mem_quiz = MemQuizTest()

    mem_quiz.prolificID      = field(content, 'prolificID')
    mem_quiz.userID      = field(content, 'userID')
    mem_quiz.condition      = field(content, 'condition')
    mem_quiz.date        = field(content, 'date')
    mem_quiz.startTime   = field(content, 'startTime')
    mem_quiz.section   = field(content, 'section')
    mem_quiz.sectionTime   = field(content, 'sectionTime')
    mem_quiz.quizTry   = field(content, 'quizTry')
    mem_quiz.quizNumTotal = field(content, 'quizNumTotal')
    mem_quiz.quizNum = field(content, 'quizNum')
    mem_quiz.quizTime = field(content, 'quizTime')
    mem_quiz.quizResp = field(content, 'quizResp')
    mem_quiz.quizRT = field(content, 'quizRT')
    mem_quiz.quizAns = field(content, 'quizAns')
    mem_quiz.quizCor = field(content, 'quizCor')
    mem_quiz.quizCorTotal = field(content, 'quizCorTotal')


    BaseObject.check_and_save(mem_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
