"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/psych_quiz/<user_id>', methods=['POST', 'GET'])
def create_psych_data(user_id):
    content = request.json
    psych_quiz = PsychQuiz()
    psych_quiz.prolificID = str(content.get('prolificID'))
    psych_quiz.studyID      = str(content.get('studyID'))
    psych_quiz.sessionID      = str(content.get('sessionID'))
    psych_quiz.userID = str(content.get('userID'))
    psych_quiz.condition = str(content.get('condition'))
    psych_quiz.date = str(content.get('date'))
    psych_quiz.startTime = str(content.get('startTime'))
    psych_quiz.section = str(content.get('section'))
    psych_quiz.sectionTime = str(content.get('sectionTime'))
    psych_quiz.qnTimeStart = str(content.get('qnTimeStart'))
    psych_quiz.qnTimeEnd = str(content.get('qnTimeEnd'))
    psych_quiz.PgFinish_demo = str(content.get('PgFinish_demo'))
    psych_quiz.PgFinish_PHQ = str(content.get('PgFinish_PHQ'))
    psych_quiz.PgFinish_GAD = str(content.get('PgFinish_GAD'))
    psych_quiz.PgRT_demo = str(content.get('PgRT_demo'))
    psych_quiz.PgRT_PHQ = str(content.get('PgRT_PHQ'))
    psych_quiz.PgRT_GAD = str(content.get('PgRT_GAD'))
    psych_quiz.age = str(content.get('age'))
    psych_quiz.gender = str(content.get('gender'))
    psych_quiz.PHQ = str(content.get('PHQ'))
    psych_quiz.GAD = str(content.get('GAD'))
    psych_quiz.windowWidth = str(content.get('windowWidth'))
    psych_quiz.windowHeight = str(content.get('windowHeight'))
    psych_quiz.mouseMovements = str(content.get('mouseMovements'))

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
