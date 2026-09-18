"""users routes"""
from flask import current_app as app, jsonify, request
from models import Feedback, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/feedback/<user_id>', methods=['POST'])
def create_feedback(user_id):
    content = json_body()
    feedback = Feedback()
    feedback.prolificID  = field(content, 'prolificID')
    feedback.userID     = field(content, 'userID')
    feedback.condition     = field(content, 'condition')
    feedback.date        = field(content, 'date')
    feedback.startTime   = field(content, 'startTime')
    feedback.section        = field(content, 'section')
    feedback.sectionTime   = field(content, 'sectionTime')
    feedback.perBonus    = field(content, 'perBonus')
    feedback.memBonus    = field(content, 'memBonus')
    feedback.totalBonus    = field(content, 'totalBonus')
    feedback.feedback    = field(content, 'feedback')
    feedback.textTime    = field(content, 'textTime')
    feedback.selfKnowledge    = field(content, 'selfKnowledge')

    BaseObject.check_and_save(feedback)
    result = dict({"success": "yes"})
    return jsonify(result)
