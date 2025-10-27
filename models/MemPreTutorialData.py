"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class MemPreTutorialData(BaseObject, Model):

    id = Column(Integer, primary_key=True)
    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    section         = Column(Text(length=10000))
    sectionTime         = Column(Text(length=10000))
    trialNum      = Column(Text(length=10000))
    stimNumLeft = Column(Text(length=10000))
    choiceCor = Column(Text(length=10000))
    choicePos = Column(Text(length=10000))

    trialTime            = Column(Text(length=10000))
    fixTime            = Column(Text(length=10000))
    respTime      = Column(Text(length=10000))
    respFbTime      = Column(Text(length=10000))
    rewFbTime       = Column(Text(length=10000))
    responseKey   = Column(Text(length=10000))
    choice     = Column(Text(length=10000))
    correct     = Column(Text(length=10000))

    statePicArray            = Column(Text(length=10000))
    stateWordArray            = Column(Text(length=10000))
    stimPick         = Column(Text(length=10000))
    stimWordPick         = Column(Text(length=10000))
    stimShown      = Column(Text(length=10000))
    stimWordShown      = Column(Text(length=10000))
    choiceShownWordLeft       = Column(Text(length=10000))
    choiceShownWordRight   = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_prolific_id(self):
        return str(self.prolificID)

    def get_user_id(self):
        return str(self.userID)

    def get_condition(self):
        return str(self.condition)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_section(self):
        return str(self.section)

    def get_sectionTime(self):
        return str(self.sectionTime)

    def get_trialNum(self):
        return str(self.trialNum)

    def get_stiNumLeft(self):
        return str(self.stimNumLeft)

    def get_choiceOCr(self):
        return str(self.choiceCor)

    def get_choicePos(self):
        return str(self.choicePos)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_fixTime(self):
        return str(self.fixTime)

    def get_respTime(self):
        return str(self.respTime)

    def get_respFbTime(self):
        return str(self.respFbTime)

    def get_rewFbTime(self):
        return str(self.rewFbTime)

    def get_responseKey(self):
        return str(self.responseKey)

    def get_choice(self):
        return str(self.choice)

    def get_correct(self):
        return str(self.correct)

    def get_statePicArray(self):
        return str(self.statePicArray)

    def get_stateWordArray(self):
        return str(self.stateWordArray)

    def get_stimPick(self):
        return str(self.stimPick)

    def get_stimWwordPick(self):
        return str(self.stimWordPick)

    def get_stimShown(self):
        return str(self.stimShown)

    def get_stimWordShown(self):
        return str(self.stimWordShown)

    def get_choiceShownWordRight(self):
        return str(self.choiceShownWordRight)

    def get_choiceShownWordRight(self):
        return str(self.choiceShownWordRight)


    def errors(self):
        errors = super(MemPreTutorialData, self).errors()
        return errors
