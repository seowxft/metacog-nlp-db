"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/psych_quiz/<user_id>', methods=['POST'])
def create_psych_data(user_id):
    content = json_body()
    psych_quiz = PsychQuiz()
    psych_quiz.prolificID = field(content, 'prolificID')
    psych_quiz.userID = field(content, 'userID')
    psych_quiz.condition = field(content, 'condition')
    psych_quiz.date = field(content, 'date')
    psych_quiz.startTime = field(content, 'startTime')
    psych_quiz.section = field(content, 'section')
    psych_quiz.sectionTime = field(content, 'sectionTime')
    psych_quiz.qnTimeStart = field(content, 'qnTimeStart')
    psych_quiz.qnTimeEnd = field(content, 'qnTimeEnd')
    psych_quiz.PgFinish_demo = field(content, 'PgFinish_demo')
    psych_quiz.PgFinish_AES = field(content, 'PgFinish_AES')
    psych_quiz.PgFinish_GSE = field(content, 'PgFinish_GSE')
    psych_quiz.PgFinish_RSE = field(content, 'PgFinish_RSE')
    psych_quiz.PgFinish_STAIY2 = field(content, 'PgFinish_STAIY2')
    psych_quiz.PgFinish_SDS = field(content, 'PgFinish_SDS')
    psych_quiz.PgRT_demo = field(content, 'PgRT_demo')
    psych_quiz.PgRT_AES = field(content, 'PgRT_AES')
    psych_quiz.PgRT_GSE = field(content, 'PgRT_GSE')
    psych_quiz.PgRT_RSE = field(content, 'PgRT_RSE')
    psych_quiz.PgRT_STAIY2 = field(content, 'PgRT_STAIY2')
    psych_quiz.PgRT_SDS = field(content, 'PgRT_SDS')
    psych_quiz.age = field(content, 'age')
    psych_quiz.gender = field(content, 'gender')
    psych_quiz.AES = field(content, 'AES')
    psych_quiz.GSE = field(content, 'GSE')
    psych_quiz.RSE = field(content, 'RSE')
    psych_quiz.STAIY2 = field(content, 'STAIY2')
    psych_quiz.SDS = field(content, 'SDS')
    psych_quiz.mouseMovements = field(content, 'mouseMovements')

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
