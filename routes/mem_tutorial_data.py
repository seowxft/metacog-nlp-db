"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_mem_tutorial_data(user_id):
    content = request.json
    mem_tut = MemTutorialData()
    mem_tut.prolificID      = str(content['prolificID'])
    mem_tut.userID      = str(content['userID'])
    mem_tut.condition      = str(content['condition'])
    mem_tut.date        = str(content['date'])
    mem_tut.startTime   = str(content['startTime'])
    mem_tut.section    = str(content['section'])
    mem_tut.sectionTime    = str(content['sectionTime'])
    mem_tut.trialNum = str(content['trialNum'])
    mem_tut.tutorialTry = str(content['tutorialTry'])
    mem_tut.blockCond    = str(content['blockCond'])
    mem_tut.choicePos    = str(content['choicePos'])
    mem_tut.choiceCor    = str(content['choiceCor'])
    
    mem_tut.trialTime  = str(content['trialTime'])
    mem_tut.fixTime   = str(content['fixTime'])
    mem_tut.stimTime    = str(content['stimTime'])
    mem_tut.encodeTime    = str(content['encodeTime'])
    mem_tut.respTime  = str(content['respTime'])
    mem_tut.respFbTime     = str(content['respFbTime'])
    mem_tut.rewFbTime  = str(content['rewFbTime'])
    mem_tut.confTime    = str(content['confTime'])
    mem_tut.responseKey    = str(content['responseKey'])
    mem_tut.choice = str(content['choice'])
    mem_tut.correct = str(content['correct'])
    mem_tut.correctMat = str(content['correctMat'])
    mem_tut.correctPer = str(content['correctPer'])
    mem_tut.confLevel  = str(content['confLevel'])

    mem_tut.stimNum  = str(content['stimNum'])
    mem_tut.responseMatrix  = str(content['responseMatrix'])
    mem_tut.reversals = str(content['reversals'])
    mem_tut.stairDir     = str(content['stairDir'])

    mem_tut.stimNumEasy = str(content['stimNumEasy'])
    mem_tut.correctMatEasy = str(content['correctMatEasy'])
    mem_tut.correctPerEasy = str(content['correctPerEasy'])
    mem_tut.responseMatrixEasy  = str(content['responseMatrixEasy'])
    mem_tut.stairDirEasy  = str(content['stairDirEasy'])

    mem_tut.stimNumHard  = str(content['stimNumHard'])
    mem_tut.correctMatHard  = str(content['correctMatHard'])
    mem_tut.correctPerHard = str(content['correctPerHard'])
    mem_tut.responseMatrixHard     = str(content['responseMatrixHard'])
    mem_tut.stairDirHard     = str(content['stairDirHard'])

    mem_tut.stimPick  = str(content['stimPick'])
    mem_tut.stimWordPick  = str(content['stimWordPick'])
    mem_tut.stimShown     = str(content['stimShown'])
    mem_tut.stimWordShown  = str(content['stimWordShown'])
    mem_tut.choiceShownWordStim1 = str(content['choiceShownWordStim1'])
    mem_tut.choiceShownWordStim2     = str(content['choiceShownWordStim2'])
    mem_tut.choiceShownWordLeft = str(content['choiceShownWordLeft'])
    mem_tut.choiceShownWordRight     = str(content['choiceShownWordRight'])

    BaseObject.check_and_save(mem_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
