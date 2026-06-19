"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTaskData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_task_data/<user_id>', methods=['POST', 'GET'])
def create_per_task_data(user_id):
    content = request.json
    per_task = PerTaskData()
    per_task.prolificID      = str(content['prolificID'])
    per_task.userID      = str(content['userID'])
    per_task.condition      = str(content['condition'])
    per_task.date        = str(content['date'])
    per_task.startTime   = str(content['startTime'])
    per_task.section    = str(content['section'])
    per_task.sectionTime    = str(content['sectionTime'])
    per_task.trialNum = str(content['trialNum'])
    per_task.blockNum    = str(content['blockNum'])
    per_task.blockCond    = str(content['blockCond'])
    per_task.condEasyTrialNum = str(content['condEasyTrialNum'])
    per_task.condHardTrialNum = str(content['condHardTrialNum'])
    per_task.trialNumInBlock = str(content['trialNumInBlock'])
    
    per_task.stimPos = str(content['stimPos'])
    per_task.dotDiffLeft = str(content['dotDiffLeft'])
    per_task.dotDiffRight  = str(content['dotDiffRight'])
    per_task.dotDiffStim1 = str(content['dotDiffStim1'])
    per_task.dotDiffStim2     = str(content['dotDiffStim2'])

    per_task.trialTime  = str(content['trialTime'])
    per_task.fixTime   = str(content['fixTime'])
    per_task.stimTime    = str(content['stimTime'])
    per_task.responseKey    = str(content['responseKey'])
    per_task.respTime  = str(content['respTime'])
    per_task.respFbTime     = str(content['respFbTime'])
    per_task.choice = str(content['choice'])
    per_task.confInitial = str(content['confInitial'])
    per_task.confLevel  = str(content['confLevel'])
    per_task.confTime    = str(content['confTime'])
    per_task.correct = str(content['correct'])
    per_task.correctMat = str(content['correctMat'])
    per_task.correctPer = str(content['correctPer'])

    per_task.responseMatrix  = str(content['responseMatrix'])
    per_task.reversals = str(content['reversals'])
    per_task.stairDir     = str(content['stairDir'])
    per_task.dotStair    = str(content['dotStair'])

    per_task.dotStairEasy    = str(content['dotStairEasy'])
    per_task.correctMatEasy  = str(content['correctMatEasy'])
    per_task.correctPerEasy     = str(content['correctPerEasy'])
    per_task.responseMatrixEasy = str(content['responseMatrixEasy'])
    per_task.stairDirEasy = str(content['stairDirEasy'])

    per_task.dotStairHard  = str(content['dotStairHard'])
    per_task.correctMatHard    = str(content['correctMatHard'])
    per_task.correctPerHard = str(content['correctPerHard'])
    per_task.responseMatrixHard = str(content['responseMatrixHard'])
    per_task.stairDirHard = str(content['stairDirHard'])

    per_task.dotStairLeft     = str(content['dotStairLeft'])
    per_task.dotStairRight  = str(content['dotStairRight'])

    per_task.mouseMovements  = str(content['mouseMovements'])

    BaseObject.check_and_save(per_task)
    result = dict({"success": "yes"})
    return jsonify(result)
