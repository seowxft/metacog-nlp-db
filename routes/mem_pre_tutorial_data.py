"""users routes"""
from flask import current_app as app, jsonify, request
from models import MemPreTutorialData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/mem_pre_tutorial_data/<user_id>', methods=['POST', 'GET'])
def create_mem_pre_tutorial_data(user_id):
    content = request.json
    mem_pre_tut = MemPreTutorialData()
    mem_pre_tut.prolificID      = str(content['prolificID'])
    mem_pre_tut.userID      = str(content['userID'])
    mem_pre_tut.condition      = str(content['condition'])    
    mem_pre_tut.date        = str(content['date'])
    mem_pre_tut.startTime   = str(content['startTime'])
    mem_pre_tut.section    = str(content['section'])
    mem_pre_tut.sectionTime    = str(content['sectionTime'])
    mem_pre_tut.trialNum = str(content['trialNum'])
    mem_pre_tut.stimNumLeft = str(content['stimNumLeft'])
    mem_pre_tut.choiceCor = str(content['choiceCor'])
    mem_pre_tut.choicePos = str(content['choicePos'])

    mem_pre_tut.trialTime  = str(content['trialTime'])
    mem_pre_tut.fixTime   = str(content['fixTime'])
    mem_pre_tut.respTime  = str(content['respTime'])
    mem_pre_tut.respFbTime     = str(content['respFbTime'])
    mem_pre_tut.rewFbTime  = str(content['rewFbTime'])
    mem_pre_tut.responseKey    = str(content['responseKey'])
    mem_pre_tut.choice = str(content['choice'])
    mem_pre_tut.correct = str(content['correct'])

    mem_pre_tut.statePicArray   = str(content['statePicArray'])
    mem_pre_tut.stateWordArray  = str(content['stateWordArray'])
    mem_pre_tut.stimPick     = str(content['stimPick'])
    mem_pre_tut.stimWordPick  = str(content['stimWordPick'])
    mem_pre_tut.stimShown  = str(content['stimShown'])
    mem_pre_tut.stimWordShown    = str(content['stimWordShown'])
    mem_pre_tut.choiceShownWordLeft = str(content['choiceShownWordLeft'])
    mem_pre_tut.choiceShownWordRight = str(content['choiceShownWordRight'])

    BaseObject.check_and_save(mem_pre_tut)
    result = dict({"success": "yes"})
    return jsonify(result)
