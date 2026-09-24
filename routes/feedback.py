"""users routes"""
from flask import current_app as app, jsonify, request
from models import Feedback, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/feedback/<user_id>', methods=['POST', 'GET'])
def create_feedback(user_id):
    content = request.json
    feedback = Feedback()
    feedback.prolificID  = str(content.get('prolificID'))
    feedback.studyID      = str(content.get('studyID'))
    feedback.sessionID      = str(content.get('sessionID'))
    feedback.userID     = str(content.get('userID'))
    feedback.condition     = str(content.get('condition'))
    feedback.date        = str(content.get('date'))
    feedback.startTime   = str(content.get('startTime'))
    feedback.section        = str(content.get('section'))
    feedback.sectionTime   = str(content.get('sectionTime'))
    feedback.perBonus    = str(content.get('perBonus'))
    feedback.memBonus    = str(content.get('memBonus'))
    feedback.totalBonus    = str(content.get('totalBonus'))
    feedback.feedback    = str(content.get('feedback'))

    BaseObject.check_and_save(feedback)
    result = dict({"success": "yes"})
    return jsonify(result)
