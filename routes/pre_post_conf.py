"""users routes"""
from flask import current_app as app, jsonify, request
from models import PrePostConf, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/pre_post_conf/<user_id>', methods=['POST', 'GET'])
def create_pre_post_conf(user_id):
    content = request.json
    prepost_conf = PrePostConf()
    prepost_conf.prolificID = str(content.get('prolificID'))
    prepost_conf.studyID      = str(content.get('studyID'))
    prepost_conf.sessionID      = str(content.get('sessionID'))
    prepost_conf.userID = str(content.get('userID'))
    prepost_conf.condition = str(content.get('condition'))
    prepost_conf.task = str(content.get('task'))
    prepost_conf.date        = str(content.get('date'))
    prepost_conf.startTime   = str(content.get('startTime'))
    prepost_conf.section   = str(content.get('section'))
    prepost_conf.sectionTime = str(content.get('sectionTime'))
    prepost_conf.blockNum = str(content.get('blockNum'))
    prepost_conf.quizState = str(content.get('quizState'))
    prepost_conf.confInitial = str(content.get('confInitial'))
    prepost_conf.confLevel = str(content.get('confLevel'))
    prepost_conf.textTime = str(content.get('textTime'))
    prepost_conf.selfKnowledge = str(content.get('selfKnowledge'))
    prepost_conf.windowWidth = str(content.get('windowWidth'))
    prepost_conf.windowHeight = str(content.get('windowHeight'))
    prepost_conf.mouseMovements = str(content.get('mouseMovements'))
    prepost_conf.clientFlags = str(content.get.get('clientFlags'))
    prepost_conf.signatureAgent = str(request.headers.get('Signature-Agent'))

    BaseObject.check_and_save(prepost_conf)
    result = dict({"success": "yes"})
    return jsonify(result)
