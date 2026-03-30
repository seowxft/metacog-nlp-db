"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemTaskData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_task_data/<user_id>', methods=['POST', 'GET'])
def create_mem_task_data(user_id):
    content = request.json
    mem_task = MemTaskData()
    mem_task.prolificID      = str(content['prolificID'])
    mem_task.userID      = str(content['userID'])
    mem_task.condition      = str(content['condition'])
    mem_task.date        = str(content['date'])
    mem_task.startTime   = str(content['startTime'])
    mem_task.section    = str(content['section'])
    mem_task.sectionTime    = str(content['sectionTime'])
    mem_task.trialNum = str(content['trialNum'])
    mem_task.blockNum    = str(content['blockNum'])
    mem_task.blockCond    = str(content['blockCond'])
    mem_task.condEasyTrialNum    = str(content['condEasyTrialNum'])
    mem_task.condHardTrialNum = str(content['condHardTrialNum'])

    mem_task.trialNumInBlock = str(content['trialNumInBlock'])
    mem_task.choicePos = str(content['choicePos'])
    mem_task.choiceCor = str(content['choiceCor'])

    mem_task.trialTime  = str(content['trialTime'])
    mem_task.fixTime   = str(content['fixTime'])
    mem_task.stimTime    = str(content['stimTime'])
    mem_task.encodeTime = str(content['encodeTime'])
    mem_task.respTime  = str(content['respTime'])
    mem_task.respFbTime     = str(content['respFbTime'])
    mem_task.confTime    = str(content['confTime'])
    mem_task.responseKey    = str(content['responseKey'])
    mem_task.choice = str(content['choice'])

    mem_task.correct = str(content['correct'])
    mem_task.correctMat = str(content['correctMat'])
    mem_task.correctPer = str(content['correctPer'])
    mem_task.confInitial = str(content['confInitial'])
    mem_task.confLevel  = str(content['confLevel'])

    mem_task.stimNum  = str(content['stimNum'])
    mem_task.responseMatrix  = str(content['responseMatrix'])
    mem_task.reversals = str(content['reversals'])
    mem_task.stairDir     = str(content['stairDir'])

    mem_task.stimNumEasy = str(content['stimNumEasy'])
    mem_task.correctMatEasy = str(content['correctMatEasy'])
    mem_task.correctPerEasy = str(content['correctPerEasy'])
    mem_task.responseMatrixEasy  = str(content['responseMatrixEasy'])
    mem_task.stairDirEasy  = str(content['stairDirEasy'])

    mem_task.stimNumHard  = str(content['stimNumHard'])
    mem_task.correctMatHard  = str(content['correctMatHard'])
    mem_task.correctPerHard = str(content['correctPerHard'])
    mem_task.responseMatrixHard     = str(content['responseMatrixHard'])
    mem_task.stairDirHard     = str(content['stairDirHard'])
  
    mem_task.stimPick    = str(content['stimPick'])
    mem_task.stimWordPick     = str(content['stimWordPick'])
    mem_task.stimShown  = str(content['stimShown'])
    mem_task.stimWordShown     = str(content['stimWordShown'])

    mem_task.choiceShownWordStim1    = str(content['choiceShownWordStim1'])
    mem_task.choiceShownWordStim2     = str(content['choiceShownWordStim2'])
    mem_task.choiceShownWordLeft  = str(content['choiceShownWordLeft'])
    mem_task.choiceShownWordRight     = str(content['choiceShownWordRight'])

    BaseObject.check_and_save(mem_task)
    result = dict({"success": "yes"})
    return jsonify(result)
