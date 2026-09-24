"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTaskData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/per_task_data/<user_id>', methods=['POST', 'GET'])
def create_per_task_data(user_id):
    content = request.json
    per_task = PerTaskData()
    per_task.prolificID      = str(content.get('prolificID'))
    per_task.studyID      = str(content.get('studyID'))
    per_task.sessionID      = str(content.get('sessionID'))
    per_task.userID      = str(content.get('userID'))
    per_task.condition      = str(content.get('condition'))
    per_task.date        = str(content.get('date'))
    per_task.startTime   = str(content.get('startTime'))
    per_task.section    = str(content.get('section'))
    per_task.sectionTime    = str(content.get('sectionTime'))
    per_task.trialNum = str(content.get('trialNum'))
    per_task.blockNum    = str(content.get('blockNum'))
    per_task.blockCond    = str(content.get('blockCond'))
    per_task.condEasyTrialNum = str(content.get('condEasyTrialNum'))
    per_task.condHardTrialNum = str(content.get('condHardTrialNum'))
    per_task.trialNumInBlock = str(content.get('trialNumInBlock'))
    
    per_task.stimPos = str(content.get('stimPos'))
    per_task.dotDiffLeft = str(content.get('dotDiffLeft'))
    per_task.dotDiffRight  = str(content.get('dotDiffRight'))
    per_task.dotDiffStim1 = str(content.get('dotDiffStim1'))
    per_task.dotDiffStim2     = str(content.get('dotDiffStim2'))

    per_task.trialTime  = str(content.get('trialTime'))
    per_task.fixTime   = str(content.get('fixTime'))
    per_task.stimTime    = str(content.get('stimTime'))
    per_task.responseKey    = str(content.get('responseKey'))
    per_task.respTime  = str(content.get('respTime'))
    per_task.respFbTime     = str(content.get('respFbTime'))
    per_task.choice = str(content.get('choice'))
    per_task.confInitial = str(content.get('confInitial'))
    per_task.confLevel  = str(content.get('confLevel'))
    per_task.confTime    = str(content.get('confTime'))
    per_task.correct = str(content.get('correct'))
    per_task.correctMat = str(content.get('correctMat'))
    per_task.correctPer = str(content.get('correctPer'))

    per_task.responseMatrix  = str(content.get('responseMatrix'))
    per_task.reversals = str(content.get('reversals'))
    per_task.stairDir     = str(content.get('stairDir'))
    per_task.dotStair    = str(content.get('dotStair'))

    per_task.dotStairEasy    = str(content.get('dotStairEasy'))
    per_task.correctMatEasy  = str(content.get('correctMatEasy'))
    per_task.correctPerEasy     = str(content.get('correctPerEasy'))
    per_task.responseMatrixEasy = str(content.get('responseMatrixEasy'))
    per_task.stairDirEasy = str(content.get('stairDirEasy'))

    per_task.dotStairHard  = str(content.get('dotStairHard'))
    per_task.correctMatHard    = str(content.get('correctMatHard'))
    per_task.correctPerHard = str(content.get('correctPerHard'))
    per_task.responseMatrixHard = str(content.get('responseMatrixHard'))
    per_task.stairDirHard = str(content.get('stairDirHard'))

    per_task.dotStairLeft     = str(content.get('dotStairLeft'))
    per_task.dotStairRight  = str(content.get('dotStairRight'))

    per_task.leftDotsArray     = str(content.get('leftDotsArray'))
    per_task.rightDotsArray  = str(content.get('rightDotsArray'))

    per_task.windowWidth = str(content.get('windowWidth'))
    per_task.windowHeight = str(content.get('windowHeight'))
    per_task.mouseMovements  = str(content.get('mouseMovements'))

    BaseObject.check_and_save(per_task)
    result = dict({"success": "yes"})
    return jsonify(result)
