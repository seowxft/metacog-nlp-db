"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemTaskData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_task_data/<user_id>', methods=['POST', 'GET'])
def create_mem_task_data(user_id):
    content = request.json
    mem_task = MemTaskData()
    mem_task.prolificID      = str(content.get('prolificID'))
    mem_task.studyID      = str(content.get('studyID'))
    mem_task.sessionID      = str(content.get('sessionID'))
    mem_task.userID      = str(content.get('userID'))
    mem_task.condition      = str(content.get('condition'))
    mem_task.date        = str(content.get('date'))
    mem_task.startTime   = str(content.get('startTime'))
    mem_task.section    = str(content.get('section'))
    mem_task.sectionTime    = str(content.get('sectionTime'))
    mem_task.trialNum = str(content.get('trialNum'))
    mem_task.blockNum    = str(content.get('blockNum'))
    mem_task.blockCond    = str(content.get('blockCond'))
    mem_task.condEasyTrialNum    = str(content.get('condEasyTrialNum'))
    mem_task.condHardTrialNum = str(content.get('condHardTrialNum'))

    mem_task.trialNumInBlock = str(content.get('trialNumInBlock'))
    mem_task.choicePos = str(content.get('choicePos'))
    mem_task.choiceCor = str(content.get('choiceCor'))

    mem_task.trialTime  = str(content.get('trialTime'))
    mem_task.fixTime   = str(content.get('fixTime'))
    mem_task.stimTime    = str(content.get('stimTime'))
    mem_task.encodeTime = str(content.get('encodeTime'))
    mem_task.respTime  = str(content.get('respTime'))
    mem_task.respFbTime     = str(content.get('respFbTime'))
    mem_task.confTime    = str(content.get('confTime'))
    mem_task.responseKey    = str(content.get('responseKey'))
    mem_task.choice = str(content.get('choice'))

    mem_task.correct = str(content.get('correct'))
    mem_task.correctMat = str(content.get('correctMat'))
    mem_task.correctPer = str(content.get('correctPer'))
    mem_task.confInitial = str(content.get('confInitial'))
    mem_task.confLevel  = str(content.get('confLevel'))

    mem_task.stimNum  = str(content.get('stimNum'))
    mem_task.responseMatrix  = str(content.get('responseMatrix'))
    mem_task.reversals = str(content.get('reversals'))
    mem_task.stairDir     = str(content.get('stairDir'))

    mem_task.stimNumEasy = str(content.get('stimNumEasy'))
    mem_task.correctMatEasy = str(content.get('correctMatEasy'))
    mem_task.correctPerEasy = str(content.get('correctPerEasy'))
    mem_task.responseMatrixEasy  = str(content.get('responseMatrixEasy'))
    mem_task.stairCountEasy  = str(content.get('stairCountEasy'))
    mem_task.stairDirEasy  = str(content.get('stairDirEasy'))

    mem_task.stimNumHard  = str(content.get('stimNumHard'))
    mem_task.correctMatHard  = str(content.get('correctMatHard'))
    mem_task.correctPerHard = str(content.get('correctPerHard'))
    mem_task.responseMatrixHard     = str(content.get('responseMatrixHard'))
    mem_task.stairCountHard  = str(content.get('stairCountHard'))
    mem_task.stairDirHard     = str(content.get('stairDirHard'))
  
    mem_task.stimPick    = str(content.get('stimPick'))
    mem_task.stimWordPick     = str(content.get('stimWordPick'))
    mem_task.stimShown  = str(content.get('stimShown'))
    mem_task.stimWordShown     = str(content.get('stimWordShown'))

    mem_task.choiceShownWordStim1    = str(content.get('choiceShownWordStim1'))
    mem_task.choiceShownWordStim2     = str(content.get('choiceShownWordStim2'))
    mem_task.choiceShownWordLeft  = str(content.get('choiceShownWordLeft'))
    mem_task.choiceShownWordRight     = str(content.get('choiceShownWordRight'))

    mem_task.windowWidth = str(content.get('windowWidth'))
    mem_task.windowHeight = str(content.get('windowHeight'))
    mem_task.mouseMovements     = str(content.get('mouseMovements'))

    BaseObject.check_and_save(mem_task)
    result = dict({"success": "yes"})
    return jsonify(result)
