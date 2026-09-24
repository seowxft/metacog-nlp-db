"""users routes"""
from flask import current_app as app, jsonify, request
from models import PrePostConf, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/pre_post_conf/<user_id>', methods=['POST', 'GET'])
def create_pre_post_conf(user_id):
    content = request.json
    prepost_conf = PrePostConf()
    prepost_conf.prolificID = str(content['prolificID'])
    prepost_conf.userID = str(content['userID'])
    prepost_conf.condition = str(content['condition'])
    prepost_conf.task = str(content['task'])
    prepost_conf.date        = str(content['date'])
    prepost_conf.startTime   = str(content['startTime'])
    prepost_conf.section   = str(content['section'])
    prepost_conf.sectionTime = str(content['sectionTime'])
    prepost_conf.blockNum = str(content['blockNum'])
    prepost_conf.quizState = str(content['quizState'])
    prepost_conf.confInitial = str(content['confInitial'])
    prepost_conf.confLevel = str(content['confLevel'])
    prepost_conf.textTime = str(content['textTime'])
    prepost_conf.selfKnowledge = str(content['selfKnowledge'])
    prepost_conf.windowWidth = str(content['windowWidth'])
    prepost_conf.windowHeight = str(content['windowHeight'])
    prepost_conf.mouseMovements = str(content['mouseMovements'])
    # Signals about how the text box was filled in (see clientFlags.jsx in the
    # front-end). Older front-ends do not send it, so it may be missing.
    prepost_conf.clientFlags = str(content.get('clientFlags'))
    # Cloud-hosted AI browser agents (e.g. ChatGPT agent) sign their requests
    # with this header; ordinary browsers never send it.
    prepost_conf.signatureAgent = str(request.headers.get('Signature-Agent'))

    BaseObject.check_and_save(prepost_conf)
    result = dict({"success": "yes"})
    return jsonify(result)
