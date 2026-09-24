"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_per_tutorial_data(user_id):
    content = request.json
    per_tut = PerTutorialData()
    per_tut.prolificID      = str(content.get('prolificID'))
    per_tut.studyID      = str(content.get('studyID'))
    per_tut.sessionID      = str(content.get('sessionID'))
    per_tut.userID      = str(content.get('userID'))
    per_tut.condition      = str(content.get('condition'))
    per_tut.date        = str(content.get('date'))
    per_tut.startTime   = str(content.get('startTime'))
    per_tut.section    = str(content.get('section'))
    per_tut.sectionTime    = str(content.get('sectionTime'))
    per_tut.tutorialTry    = str(content.get('tutorialTry'))
    per_tut.blockCond    = str(content.get('blockCond'))
    per_tut.trialNum = str(content.get('trialNum'))
    per_tut.trialTime  = str(content.get('trialTime'))
    per_tut.fixTime   = str(content.get('fixTime'))
    per_tut.stimTime    = str(content.get('stimTime'))
    per_tut.stimPos    = str(content.get('stimPos'))
    per_tut.dotDiffLeft = str(content.get('dotDiffLeft'))
    per_tut.dotDiffRight  = str(content.get('dotDiffRight'))
    per_tut.dotDiffStim1 = str(content.get('dotDiffStim1'))
    per_tut.dotDiffStim2     = str(content.get('dotDiffStim2'))
    per_tut.responseKey    = str(content.get('responseKey'))
    per_tut.respTime  = str(content.get('respTime'))
    per_tut.respFbTime     = str(content.get('respFbTime'))
    per_tut.rewFbTime  = str(content.get('rewFbTime'))
    per_tut.choice = str(content.get('choice'))
    per_tut.confLevel  = str(content.get('confLevel'))
    per_tut.confTime    = str(content.get('confTime'))
    per_tut.correct = str(content.get('correct'))
    per_tut.correctMat = str(content.get('correctMat'))
    per_tut.correctPer = str(content.get('correctPer'))
    per_tut.responseMatrix  = str(content.get('responseMatrix'))
    per_tut.reversals = str(content.get('reversals'))
    per_tut.stairDir     = str(content.get('stairDir'))
    per_tut.dotStair    = str(content.get('dotStair'))

    per_tut.correctMatEasy = str(content.get('correctMatEasy'))
    per_tut.correctPerEasy  = str(content.get('correctPerEasy'))
    per_tut.responseMatrixEasy    = str(content.get('responseMatrixEasy'))
    per_tut.stairDirEasy = str(content.get('stairDirEasy'))
    per_tut.dotStairEasy = str(content.get('dotStairEasy'))

    per_tut.correctMatHard = str(content.get('correctMatHard'))
    per_tut.correctPerHard  = str(content.get('correctPerHard'))
    per_tut.responseMatrixHard = str(content.get('responseMatrixHard'))
    per_tut.stairDirHard     = str(content.get('stairDirHard'))
    per_tut.dotStairHard     = str(content.get('dotStairHard'))

    per_tut.dotStairLeft     = str(content.get('dotStairLeft'))
    per_tut.dotStairRight  = str(content.get('dotStairRight'))


    BaseObject.check_and_save(per_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
