"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/per_tutorial_data/<user_id>', methods=['POST'])
def create_per_tutorial_data(user_id):
    content = json_body()
    per_tut = PerTutorialData()
    per_tut.prolificID      = field(content, 'prolificID')
    per_tut.userID      = field(content, 'userID')
    per_tut.condition      = field(content, 'condition')
    per_tut.date        = field(content, 'date')
    per_tut.startTime   = field(content, 'startTime')
    per_tut.section    = field(content, 'section')
    per_tut.sectionTime    = field(content, 'sectionTime')
    per_tut.tutorialTry    = field(content, 'tutorialTry')
    per_tut.blockCond    = field(content, 'blockCond')
    per_tut.trialNum = field(content, 'trialNum')
    per_tut.trialTime  = field(content, 'trialTime')
    per_tut.fixTime   = field(content, 'fixTime')
    per_tut.stimTime    = field(content, 'stimTime')
    per_tut.stimPos    = field(content, 'stimPos')
    per_tut.dotDiffLeft = field(content, 'dotDiffLeft')
    per_tut.dotDiffRight  = field(content, 'dotDiffRight')
    per_tut.dotDiffStim1 = field(content, 'dotDiffStim1')
    per_tut.dotDiffStim2     = field(content, 'dotDiffStim2')
    per_tut.responseKey    = field(content, 'responseKey')
    per_tut.respTime  = field(content, 'respTime')
    per_tut.respFbTime     = field(content, 'respFbTime')
    per_tut.rewFbTime  = field(content, 'rewFbTime')
    per_tut.choice = field(content, 'choice')
    per_tut.confLevel  = field(content, 'confLevel')
    per_tut.confTime    = field(content, 'confTime')
    per_tut.correct = field(content, 'correct')
    per_tut.correctMat = field(content, 'correctMat')
    per_tut.correctPer = field(content, 'correctPer')
    per_tut.responseMatrix  = field(content, 'responseMatrix')
    per_tut.reversals = field(content, 'reversals')
    per_tut.stairDir     = field(content, 'stairDir')
    per_tut.dotStair    = field(content, 'dotStair')

    per_tut.correctMatEasy = field(content, 'correctMatEasy')
    per_tut.correctPerEasy  = field(content, 'correctPerEasy')
    per_tut.responseMatrixEasy    = field(content, 'responseMatrixEasy')
    per_tut.stairDirEasy = field(content, 'stairDirEasy')
    per_tut.dotStairEasy = field(content, 'dotStairEasy')

    per_tut.correctMatHard = field(content, 'correctMatHard')
    per_tut.correctPerHard  = field(content, 'correctPerHard')
    per_tut.responseMatrixHard = field(content, 'responseMatrixHard')
    per_tut.stairDirHard     = field(content, 'stairDirHard')
    per_tut.dotStairHard     = field(content, 'dotStairHard')

    per_tut.dotStairLeft     = field(content, 'dotStairLeft')
    per_tut.dotStairRight  = field(content, 'dotStairRight')


    BaseObject.check_and_save(per_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
