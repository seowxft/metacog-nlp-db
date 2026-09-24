"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemQuizTest, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_quiz_test/<user_id>', methods=['POST', 'GET'])
def create_mem_quiz_test(user_id):
    content = request.json
    mem_quiz = MemQuizTest()

    mem_quiz.prolificID      = str(content.get('prolificID'))
    mem_quiz.studyID      = str(content.get('studyID'))
    mem_quiz.sessionID      = str(content.get('sessionID'))
    mem_quiz.userID      = str(content.get('userID'))
    mem_quiz.condition      = str(content.get('condition'))
    mem_quiz.date        = str(content.get('date'))
    mem_quiz.startTime   = str(content.get('startTime'))
    mem_quiz.section   = str(content.get('section'))
    mem_quiz.sectionTime   = str(content.get('sectionTime'))
    mem_quiz.quizTry   = str(content.get('quizTry'))
    mem_quiz.quizNumTotal = str(content.get('quizNumTotal'))
    mem_quiz.quizNum = str(content.get('quizNum'))
    mem_quiz.quizTime = str(content.get('quizTime'))
    mem_quiz.quizResp = str(content.get('quizResp'))
    mem_quiz.quizRT = str(content.get('quizRT'))
    mem_quiz.quizAns = str(content.get('quizAns'))
    mem_quiz.quizCor = str(content.get('quizCor'))
    mem_quiz.quizCorTotal = str(content.get('quizCorTotal'))


    BaseObject.check_and_save(mem_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
