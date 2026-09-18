"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemTaskData, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/mem_task_data/<user_id>', methods=['POST'])
def create_mem_task_data(user_id):
    content = json_body()
    mem_task = MemTaskData()
    mem_task.prolificID      = field(content, 'prolificID')
    mem_task.userID      = field(content, 'userID')
    mem_task.condition      = field(content, 'condition')
    mem_task.date        = field(content, 'date')
    mem_task.startTime   = field(content, 'startTime')
    mem_task.section    = field(content, 'section')
    mem_task.sectionTime    = field(content, 'sectionTime')
    mem_task.trialNum = field(content, 'trialNum')
    mem_task.blockNum    = field(content, 'blockNum')
    mem_task.blockCond    = field(content, 'blockCond')
    mem_task.condEasyTrialNum    = field(content, 'condEasyTrialNum')
    mem_task.condHardTrialNum = field(content, 'condHardTrialNum')

    mem_task.trialNumInBlock = field(content, 'trialNumInBlock')
    mem_task.choicePos = field(content, 'choicePos')
    mem_task.choiceCor = field(content, 'choiceCor')

    mem_task.trialTime  = field(content, 'trialTime')
    mem_task.fixTime   = field(content, 'fixTime')
    mem_task.stimTime    = field(content, 'stimTime')
    mem_task.encodeTime = field(content, 'encodeTime')
    mem_task.respTime  = field(content, 'respTime')
    mem_task.respFbTime     = field(content, 'respFbTime')
    mem_task.confTime    = field(content, 'confTime')
    mem_task.responseKey    = field(content, 'responseKey')
    mem_task.choice = field(content, 'choice')

    mem_task.correct = field(content, 'correct')
    mem_task.correctMat = field(content, 'correctMat')
    mem_task.correctPer = field(content, 'correctPer')
    mem_task.confInitial = field(content, 'confInitial')
    mem_task.confLevel  = field(content, 'confLevel')

    mem_task.stimNum  = field(content, 'stimNum')
    mem_task.responseMatrix  = field(content, 'responseMatrix')
    mem_task.reversals = field(content, 'reversals')
    mem_task.stairDir     = field(content, 'stairDir')

    mem_task.stimNumEasy = field(content, 'stimNumEasy')
    mem_task.correctMatEasy = field(content, 'correctMatEasy')
    mem_task.correctPerEasy = field(content, 'correctPerEasy')
    mem_task.responseMatrixEasy  = field(content, 'responseMatrixEasy')
    mem_task.stairDirEasy  = field(content, 'stairDirEasy')

    mem_task.stimNumHard  = field(content, 'stimNumHard')
    mem_task.correctMatHard  = field(content, 'correctMatHard')
    mem_task.correctPerHard = field(content, 'correctPerHard')
    mem_task.responseMatrixHard     = field(content, 'responseMatrixHard')
    mem_task.stairDirHard     = field(content, 'stairDirHard')
  
    mem_task.stimPick    = field(content, 'stimPick')
    mem_task.stimWordPick     = field(content, 'stimWordPick')
    mem_task.stimShown  = field(content, 'stimShown')
    mem_task.stimWordShown     = field(content, 'stimWordShown')

    mem_task.choiceShownWordStim1    = field(content, 'choiceShownWordStim1')
    mem_task.choiceShownWordStim2     = field(content, 'choiceShownWordStim2')
    mem_task.choiceShownWordLeft  = field(content, 'choiceShownWordLeft')
    mem_task.choiceShownWordRight     = field(content, 'choiceShownWordRight')

    mem_task.mouseMovements     = field(content, 'mouseMovements')

    BaseObject.check_and_save(mem_task)
    result = dict({"success": "yes"})
    return jsonify(result)
