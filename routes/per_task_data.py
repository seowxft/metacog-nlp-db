"""users routes"""
from flask import current_app as app, jsonify, request
from models import PerTaskData, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/per_task_data/<user_id>', methods=['POST'])
def create_per_task_data(user_id):
    content = json_body()
    per_task = PerTaskData()
    per_task.prolificID      = field(content, 'prolificID')
    per_task.userID      = field(content, 'userID')
    per_task.condition      = field(content, 'condition')
    per_task.date        = field(content, 'date')
    per_task.startTime   = field(content, 'startTime')
    per_task.section    = field(content, 'section')
    per_task.sectionTime    = field(content, 'sectionTime')
    per_task.trialNum = field(content, 'trialNum')
    per_task.blockNum    = field(content, 'blockNum')
    per_task.blockCond    = field(content, 'blockCond')
    per_task.condEasyTrialNum = field(content, 'condEasyTrialNum')
    per_task.condHardTrialNum = field(content, 'condHardTrialNum')
    per_task.trialNumInBlock = field(content, 'trialNumInBlock')
    
    per_task.stimPos = field(content, 'stimPos')
    per_task.dotDiffLeft = field(content, 'dotDiffLeft')
    per_task.dotDiffRight  = field(content, 'dotDiffRight')
    per_task.dotDiffStim1 = field(content, 'dotDiffStim1')
    per_task.dotDiffStim2     = field(content, 'dotDiffStim2')

    per_task.trialTime  = field(content, 'trialTime')
    per_task.fixTime   = field(content, 'fixTime')
    per_task.stimTime    = field(content, 'stimTime')
    per_task.responseKey    = field(content, 'responseKey')
    per_task.respTime  = field(content, 'respTime')
    per_task.respFbTime     = field(content, 'respFbTime')
    per_task.choice = field(content, 'choice')
    per_task.confInitial = field(content, 'confInitial')
    per_task.confLevel  = field(content, 'confLevel')
    per_task.confTime    = field(content, 'confTime')
    per_task.correct = field(content, 'correct')
    per_task.correctMat = field(content, 'correctMat')
    per_task.correctPer = field(content, 'correctPer')

    per_task.responseMatrix  = field(content, 'responseMatrix')
    per_task.reversals = field(content, 'reversals')
    per_task.stairDir     = field(content, 'stairDir')
    per_task.dotStair    = field(content, 'dotStair')

    per_task.dotStairEasy    = field(content, 'dotStairEasy')
    per_task.correctMatEasy  = field(content, 'correctMatEasy')
    per_task.correctPerEasy     = field(content, 'correctPerEasy')
    per_task.responseMatrixEasy = field(content, 'responseMatrixEasy')
    per_task.stairDirEasy = field(content, 'stairDirEasy')

    per_task.dotStairHard  = field(content, 'dotStairHard')
    per_task.correctMatHard    = field(content, 'correctMatHard')
    per_task.correctPerHard = field(content, 'correctPerHard')
    per_task.responseMatrixHard = field(content, 'responseMatrixHard')
    per_task.stairDirHard = field(content, 'stairDirHard')

    per_task.dotStairLeft     = field(content, 'dotStairLeft')
    per_task.dotStairRight  = field(content, 'dotStairRight')

    per_task.mouseMovements  = field(content, 'mouseMovements')

    BaseObject.check_and_save(per_task)
    result = dict({"success": "yes"})
    return jsonify(result)
