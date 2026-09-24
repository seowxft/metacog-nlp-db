"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemPreTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_pre_tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_mem_pre_tutorial_data(user_id):
    content = request.json
    mem_pre_tut = MemPreTutorialData()
    mem_pre_tut.prolificID      = str(content.get('prolificID'))
    mem_pre_tut.studyID      = str(content.get('studyID'))
    mem_pre_tut.sessionID      = str(content.get('sessionID'))
    mem_pre_tut.userID      = str(content.get('userID'))
    mem_pre_tut.condition      = str(content.get('condition'))    
    mem_pre_tut.date        = str(content.get('date'))
    mem_pre_tut.startTime   = str(content.get('startTime'))
    mem_pre_tut.section    = str(content.get('section'))
    mem_pre_tut.sectionTime    = str(content.get('sectionTime'))
    mem_pre_tut.trialNum = str(content.get('trialNum'))
    mem_pre_tut.stimNumLeft = str(content.get('stimNumLeft'))
    mem_pre_tut.choiceCor = str(content.get('choiceCor'))
    mem_pre_tut.choicePos = str(content.get('choicePos'))

    mem_pre_tut.trialTime  = str(content.get('trialTime'))
    mem_pre_tut.fixTime   = str(content.get('fixTime'))
    mem_pre_tut.respTime  = str(content.get('respTime'))
    mem_pre_tut.respFbTime     = str(content.get('respFbTime'))
    mem_pre_tut.rewFbTime  = str(content.get('rewFbTime'))
    mem_pre_tut.responseKey    = str(content.get('responseKey'))
    mem_pre_tut.choice = str(content.get('choice'))
    mem_pre_tut.correct = str(content.get('correct'))

    mem_pre_tut.statePicArray   = str(content.get('statePicArray'))
    mem_pre_tut.stateWordArray  = str(content.get('stateWordArray'))
    mem_pre_tut.stimPick     = str(content.get('stimPick'))
    mem_pre_tut.stimWordPick  = str(content.get('stimWordPick'))
    mem_pre_tut.stimShown  = str(content.get('stimShown'))
    mem_pre_tut.stimWordShown    = str(content.get('stimWordShown'))
    mem_pre_tut.choiceShownWordLeft = str(content.get('choiceShownWordLeft'))
    mem_pre_tut.choiceShownWordRight = str(content.get('choiceShownWordRight'))

    BaseObject.check_and_save(mem_pre_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
