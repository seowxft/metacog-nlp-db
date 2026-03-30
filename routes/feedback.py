"""users routes"""
from flask import current_app as app, jsonify, request
from models import Feedback, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/feedback/<user_id>', methods=['POST', 'GET'])
def create_feedback(user_id):
    content = request.json
    feedback = Feedback()
    feedback.prolificID  = str(content['prolificID'])
    feedback.userID     = str(content['userID'])
    feedback.condition     = str(content['condition'])
    feedback.date        = str(content['date'])
    feedback.startTime   = str(content['startTime'])
    feedback.section        = str(content['section'])
    feedback.sectionTime   = str(content['sectionTime'])
    feedback.perBonus    = str(content['perBonus'])
    feedback.memBonus    = str(content['memBonus'])
    feedback.totalBonus    = str(content['totalBonus'])
    feedback.feedback    = str(content['feedback'])
    feedback.textTime    = str(content['textTime'])
    feedback.selfKnowledge    = str(content['selfKnowledge'])

    BaseObject.check_and_save(feedback)
    result = dict({"success": "yes"})
    return jsonify(result)
