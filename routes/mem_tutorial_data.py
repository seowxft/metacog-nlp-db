"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/mem_tutorial_data/<user_id>', methods=['POST'])
def create_mem_tutorial_data(user_id):
    content = json_body()
    mem_tut = MemTutorialData()
    mem_tut.prolificID      = field(content, 'prolificID')
    mem_tut.userID      = field(content, 'userID')
    mem_tut.condition      = field(content, 'condition')
    mem_tut.date        = field(content, 'date')
    mem_tut.startTime   = field(content, 'startTime')
    mem_tut.section    = field(content, 'section')
    mem_tut.sectionTime    = field(content, 'sectionTime')
    mem_tut.trialNum = field(content, 'trialNum')
    mem_tut.tutorialTry = field(content, 'tutorialTry')
    mem_tut.blockCond    = field(content, 'blockCond')
    mem_tut.choicePos    = field(content, 'choicePos')
    mem_tut.choiceCor    = field(content, 'choiceCor')
    
    mem_tut.trialTime  = field(content, 'trialTime')
    mem_tut.fixTime   = field(content, 'fixTime')
    mem_tut.stimTime    = field(content, 'stimTime')
    mem_tut.encodeTime    = field(content, 'encodeTime')
    mem_tut.respTime  = field(content, 'respTime')
    mem_tut.respFbTime     = field(content, 'respFbTime')
    mem_tut.rewFbTime  = field(content, 'rewFbTime')
    mem_tut.confTime    = field(content, 'confTime')
    mem_tut.responseKey    = field(content, 'responseKey')
    mem_tut.choice = field(content, 'choice')
    mem_tut.correct = field(content, 'correct')
    mem_tut.correctMat = field(content, 'correctMat')
    mem_tut.correctPer = field(content, 'correctPer')
    mem_tut.confLevel  = field(content, 'confLevel')

    mem_tut.stimNum  = field(content, 'stimNum')
    mem_tut.responseMatrix  = field(content, 'responseMatrix')
    mem_tut.reversals = field(content, 'reversals')
    mem_tut.stairDir     = field(content, 'stairDir')

    mem_tut.stimNumEasy = field(content, 'stimNumEasy')
    mem_tut.correctMatEasy = field(content, 'correctMatEasy')
    mem_tut.correctPerEasy = field(content, 'correctPerEasy')
    mem_tut.responseMatrixEasy  = field(content, 'responseMatrixEasy')
    mem_tut.stairDirEasy  = field(content, 'stairDirEasy')

    mem_tut.stimNumHard  = field(content, 'stimNumHard')
    mem_tut.correctMatHard  = field(content, 'correctMatHard')
    mem_tut.correctPerHard = field(content, 'correctPerHard')
    mem_tut.responseMatrixHard     = field(content, 'responseMatrixHard')
    mem_tut.stairDirHard     = field(content, 'stairDirHard')

    mem_tut.stimPick  = field(content, 'stimPick')
    mem_tut.stimWordPick  = field(content, 'stimWordPick')
    mem_tut.stimShown     = field(content, 'stimShown')
    mem_tut.stimWordShown  = field(content, 'stimWordShown')
    mem_tut.choiceShownWordStim1 = field(content, 'choiceShownWordStim1')
    mem_tut.choiceShownWordStim2     = field(content, 'choiceShownWordStim2')
    mem_tut.choiceShownWordLeft = field(content, 'choiceShownWordLeft')
    mem_tut.choiceShownWordRight     = field(content, 'choiceShownWordRight')

    BaseObject.check_and_save(mem_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
