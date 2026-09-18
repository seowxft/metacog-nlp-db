"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/psych_quiz/<user_id>', methods=['POST', 'GET'])
def create_psych_data(user_id):
    content = request.json
    psych_quiz = PsychQuiz()
    psych_quiz.prolificID = str(content['prolificID'])
    psych_quiz.userID = str(content['userID'])
    psych_quiz.condition = str(content['condition'])
    psych_quiz.date = str(content['date'])
    psych_quiz.startTime = str(content['startTime'])
    psych_quiz.section = str(content['section'])
    psych_quiz.sectionTime = str(content['sectionTime'])
    psych_quiz.qnTimeStart = str(content['qnTimeStart'])
    psych_quiz.qnTimeEnd = str(content['qnTimeEnd'])
    psych_quiz.PgFinish_demo = str(content['PgFinish_demo'])
    psych_quiz.PgFinish_PHQ = str(content['PgFinish_PHQ'])
    psych_quiz.PgFinish_GAD = str(content['PgFinish_GAD'])
    psych_quiz.PgRT_demo = str(content['PgRT_demo'])
    psych_quiz.PgRT_PHQ = str(content['PgRT_PHQ'])
    psych_quiz.PgRT_GAD = str(content['PgRT_GAD'])
    psych_quiz.age = str(content['age'])
    psych_quiz.gender = str(content['gender'])
    psych_quiz.PHQ = str(content['PHQ'])
    psych_quiz.GAD = str(content['GAD'])
    psych_quiz.mouseMovements = str(content['mouseMovements'])

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
