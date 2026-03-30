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
    psych_quiz.PgFinish_AES = str(content['PgFinish_AES'])
    psych_quiz.PgFinish_GSE = str(content['PgFinish_GSE'])
    psych_quiz.PgFinish_RSE = str(content['PgFinish_RSE'])
    psych_quiz.PgFinish_STAIY2 = str(content['PgFinish_STAIY2'])
    psych_quiz.PgFinish_SDS = str(content['PgFinish_SDS'])
    psych_quiz.PgRT_demo = str(content['PgRT_demo'])
    psych_quiz.PgRT_AES = str(content['PgRT_AES'])
    psych_quiz.PgRT_GSE = str(content['PgRT_GSE'])
    psych_quiz.PgRT_RSE = str(content['PgRT_RSE'])
    psych_quiz.PgRT_STAIY2 = str(content['PgRT_STAIY2'])
    psych_quiz.PgRT_SDS = str(content['PgRT_SDS'])
    psych_quiz.PgRT_SSMS = str(content['PgRT_SSMS'])
    psych_quiz.age = str(content['age'])
    psych_quiz.gender = str(content['gender'])
    psych_quiz.AES = str(content['AES'])
    psych_quiz.GSE = str(content['GSE'])
    psych_quiz.RSE = str(content['RSE'])
    psych_quiz.STAIY2 = str(content['STAIY2'])
    psych_quiz.SDS = str(content['SDS'])

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
