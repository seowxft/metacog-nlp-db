"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_per_tutorial_data(user_id):
    content = request.json
    per_tut = PerTutorialData()
    per_tut.prolificID      = str(content['prolificID'])
    per_tut.userID      = str(content['userID'])
    per_tut.condition      = str(content['condition'])
    per_tut.date        = str(content['date'])
    per_tut.startTime   = str(content['startTime'])
    per_tut.section    = str(content['section'])
    per_tut.sectionTime    = str(content['sectionTime'])
    per_tut.tutorialTry    = str(content['tutorialTry'])
    per_tut.blockCond    = str(content['blockCond'])
    per_tut.trialNum = str(content['trialNum'])
    per_tut.trialTime  = str(content['trialTime'])
    per_tut.fixTime   = str(content['fixTime'])
    per_tut.stimTime    = str(content['stimTime'])
    per_tut.stimPos    = str(content['stimPos'])
    per_tut.dotDiffLeft = str(content['dotDiffLeft'])
    per_tut.dotDiffRight  = str(content['dotDiffRight'])
    per_tut.dotDiffStim1 = str(content['dotDiffStim1'])
    per_tut.dotDiffStim2     = str(content['dotDiffStim2'])
    per_tut.responseKey    = str(content['responseKey'])
    per_tut.respTime  = str(content['respTime'])
    per_tut.respFbTime     = str(content['respFbTime'])
    per_tut.rewFbTime  = str(content['rewFbTime'])
    per_tut.choice = str(content['choice'])
    per_tut.confLevel  = str(content['confLevel'])
    per_tut.confTime    = str(content['confTime'])
    per_tut.correct = str(content['correct'])
    per_tut.correctMat = str(content['correctMat'])
    per_tut.correctPer = str(content['correctPer'])
    per_tut.responseMatrix  = str(content['responseMatrix'])
    per_tut.reversals = str(content['reversals'])
    per_tut.stairDir     = str(content['stairDir'])
    per_tut.dotStair    = str(content['dotStair'])

    per_tut.correctMatEasy = str(content['correctMatEasy'])
    per_tut.correctPerEasy  = str(content['correctPerEasy'])
    per_tut.responseMatrixEasy    = str(content['responseMatrixEasy'])
    per_tut.stairDirEasy = str(content['stairDirEasy'])
    per_tut.dotStairEasy = str(content['dotStairEasy'])

    per_tut.correctMatHard = str(content['correctMatHard'])
    per_tut.correctPerHard  = str(content['correctPerHard'])
    per_tut.responseMatrixHard = str(content['responseMatrixHard'])
    per_tut.stairDirHard     = str(content['stairDirHard'])
    per_tut.dotStairHard     = str(content['dotStairHard'])

    per_tut.dotStairLeft     = str(content['dotStairLeft'])
    per_tut.dotStairRight  = str(content['dotStairRight'])


    BaseObject.check_and_save(per_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
