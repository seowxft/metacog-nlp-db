"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemPreTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func
from routes.common import field, json_body

@app.route('/mem_pre_tutorial_data/<user_id>', methods=['POST'])
def create_mem_pre_tutorial_data(user_id):
    content = json_body()
    mem_pre_tut = MemPreTutorialData()
    mem_pre_tut.prolificID      = field(content, 'prolificID')
    mem_pre_tut.userID      = field(content, 'userID')
    mem_pre_tut.condition      = field(content, 'condition')    
    mem_pre_tut.date        = field(content, 'date')
    mem_pre_tut.startTime   = field(content, 'startTime')
    mem_pre_tut.section    = field(content, 'section')
    mem_pre_tut.sectionTime    = field(content, 'sectionTime')
    mem_pre_tut.trialNum = field(content, 'trialNum')
    mem_pre_tut.stimNumLeft = field(content, 'stimNumLeft')
    mem_pre_tut.choiceCor = field(content, 'choiceCor')
    mem_pre_tut.choicePos = field(content, 'choicePos')

    mem_pre_tut.trialTime  = field(content, 'trialTime')
    mem_pre_tut.fixTime   = field(content, 'fixTime')
    mem_pre_tut.respTime  = field(content, 'respTime')
    mem_pre_tut.respFbTime     = field(content, 'respFbTime')
    mem_pre_tut.rewFbTime  = field(content, 'rewFbTime')
    mem_pre_tut.responseKey    = field(content, 'responseKey')
    mem_pre_tut.choice = field(content, 'choice')
    mem_pre_tut.correct = field(content, 'correct')

    mem_pre_tut.statePicArray   = field(content, 'statePicArray')
    mem_pre_tut.stateWordArray  = field(content, 'stateWordArray')
    mem_pre_tut.stimPick     = field(content, 'stimPick')
    mem_pre_tut.stimWordPick  = field(content, 'stimWordPick')
    mem_pre_tut.stimShown  = field(content, 'stimShown')
    mem_pre_tut.stimWordShown    = field(content, 'stimWordShown')
    mem_pre_tut.choiceShownWordLeft = field(content, 'choiceShownWordLeft')
    mem_pre_tut.choiceShownWordRight = field(content, 'choiceShownWordRight')

    BaseObject.check_and_save(mem_pre_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
