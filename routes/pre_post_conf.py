"""users routes"""
from flask import current_app as app, jsonify, request
from models import PrePostConf, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/pre_post_conf/<user_id>', methods=['POST'])
def create_pre_post_conf(user_id):
    content = json_body()
    prepost_conf = PrePostConf()
    prepost_conf.prolificID = field(content, 'prolificID')
    prepost_conf.userID = field(content, 'userID')
    prepost_conf.condition = field(content, 'condition')
    prepost_conf.task = field(content, 'task')
    prepost_conf.date        = field(content, 'date')
    prepost_conf.startTime   = field(content, 'startTime')
    prepost_conf.section   = field(content, 'section')
    prepost_conf.sectionTime = field(content, 'sectionTime')
    prepost_conf.blockNum = field(content, 'blockNum')
    prepost_conf.quizState = field(content, 'quizState')
    prepost_conf.confInitial = field(content, 'confInitial')
    prepost_conf.confLevel = field(content, 'confLevel')
    prepost_conf.textTime = field(content, 'textTime')
    prepost_conf.selfKnowledge = field(content, 'selfKnowledge')
    prepost_conf.mouseMovements = field(content, 'mouseMovements')

    BaseObject.check_and_save(prepost_conf)
    result = dict({"success": "yes"})
    return jsonify(result)
