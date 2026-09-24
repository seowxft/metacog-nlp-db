"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_quiz_test/<user_id>', methods=['POST', 'GET'])
def create_per_quiz_test(user_id):
    content = request.json
    per_quiz = PerQuizTest()
    per_quiz.prolificID      = str(content.get('prolificID'))
    per_quiz.studyID      = str(content.get('studyID'))
    per_quiz.sessionID      = str(content.get('sessionID'))
    per_quiz.userID      = str(content.get('userID'))
    per_quiz.condition      = str(content.get('condition'))
    per_quiz.date        = str(content.get('date'))
    per_quiz.startTime   = str(content.get('startTime'))
    per_quiz.section   = str(content.get('section'))
    per_quiz.sectionTime   = str(content.get('sectionTime'))
    per_quiz.quizTry   = str(content.get('quizTry'))
    per_quiz.quizNumTotal = str(content.get('quizNumTotal'))
    per_quiz.quizNum = str(content.get('quizNum'))
    per_quiz.quizTime = str(content.get('quizTime'))
    per_quiz.quizResp = str(content.get('quizResp'))
    per_quiz.quizRT = str(content.get('quizRT'))
    per_quiz.quizAns = str(content.get('quizAns'))
    per_quiz.quizCor = str(content.get('quizCor'))
    per_quiz.quizCorTotal = str(content.get('quizCorTotal'))


    BaseObject.check_and_save(per_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
