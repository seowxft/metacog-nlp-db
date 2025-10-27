"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_quiz_test/<user_id>', methods=['POST', 'GET'])
def create_per_quiz_test(user_id):
    content = request.json
    per_quiz = PerQuizTest()
    per_quiz.prolificID      = str(content['prolificID'])
    per_quiz.userID      = str(content['userID'])
    per_quiz.condition      = str(content['condition'])
    per_quiz.date        = str(content['date'])
    per_quiz.startTime   = str(content['startTime'])
    per_quiz.section   = str(content['section'])
    per_quiz.sectionTime   = str(content['sectionTime'])
    per_quiz.quizTry   = str(content['quizTry'])
    per_quiz.quizNumTotal = str(content['quizNumTotal'])
    per_quiz.quizNum = str(content['quizNum'])
    per_quiz.quizTime = str(content['quizTime'])
    per_quiz.quizResp = str(content['quizResp'])
    per_quiz.quizRT = str(content['quizRT'])
    per_quiz.quizAns = str(content['quizAns'])
    per_quiz.quizCor = str(content['quizCor'])
    per_quiz.quizCorTotal = str(content['quizCorTotal'])


    BaseObject.check_and_save(per_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
