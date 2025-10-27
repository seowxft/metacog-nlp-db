"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_quiz_test/<user_id>', methods=['POST', 'GET'])
def create_mem_quiz_test(user_id):
    content = request.json
    mem_quiz = MemQuizTest()

    mem_quiz.prolificID      = str(content['prolificID'])
    mem_quiz.userID      = str(content['userID'])
    mem_quiz.condition      = str(content['condition'])
    mem_quiz.date        = str(content['date'])
    mem_quiz.startTime   = str(content['startTime'])
    mem_quiz.section   = str(content['section'])
    mem_quiz.sectionTime   = str(content['sectionTime'])
    mem_quiz.quizTry   = str(content['quizTry'])
    mem_quiz.quizNumTotal = str(content['quizNumTotal'])
    mem_quiz.quizNum = str(content['quizNum'])
    mem_quiz.quizTime = str(content['quizTime'])
    mem_quiz.quizResp = str(content['quizResp'])
    mem_quiz.quizRT = str(content['quizRT'])
    mem_quiz.quizAns = str(content['quizAns'])
    mem_quiz.quizCor = str(content['quizCor'])
    mem_quiz.quizCorTotal = str(content['quizCorTotal'])


    BaseObject.check_and_save(mem_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
