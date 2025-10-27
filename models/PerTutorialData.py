"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PerTutorialData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    section         = Column(Text(length=10000))
    sectionTime         = Column(Text(length=10000))
    tutorialTry = Column(Text(length=10000))
    trialNum      = Column(Text(length=10000))
    trialTime            = Column(Text(length=10000))
    fixTime            = Column(Text(length=10000))
    stimTime         = Column(Text(length=10000))
    stimPos         = Column(Text(length=10000))
    dotDiffLeft     = Column(Text(length=10000))
    dotDiffRight        = Column(Text(length=10000))
    dotDiffStim1     = Column(Text(length=10000))
    dotDiffStim2     = Column(Text(length=10000))
    responseKey   = Column(Text(length=10000))
    respTime      = Column(Text(length=10000))
    respFbTime      = Column(Text(length=10000))
    rewFbTime       = Column(Text(length=10000))
    choice     = Column(Text(length=10000))
    confLevel     = Column(Text(length=10000))
    confTime         = Column(Text(length=10000))
    correct     = Column(Text(length=10000))
    correctMat     = Column(Text(length=10000))
    correctPer     = Column(Text(length=10000))
    responseMatrix        = Column(Text(length=10000))
    reversals     = Column(Text(length=10000))
    stairDir     = Column(Text(length=10000))
    dotStair   = Column(Text(length=10000))
    dotStairLeft      = Column(Text(length=10000))
    dotStairRight       = Column(Text(length=10000))



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

    def get_tutorialTry(self):
        return str(self.tutorialTry)

    def get_trialNum(self):
        return str(self.trialNum)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_fixTime(self):
        return str(self.fixTime)

    def get_stimTime(self):
        return str(self.stimTime)

    def get_stimPos(self):
        return str(self.stimPos)

    def get_dotDiffLeft(self):
        return str(self.dotDiffLeft)

    def get_dotDiffRight(self):
        return str(self.dotDiffRight)

    def get_dotDiffStim1(self):
        return str(self.dotDiffStim1)

    def get_dotDiffStim2(self):
        return str(self.dotDiffStim2)

    def get_responseKey(self):
        return str(self.responseKey)

    def get_respTime(self):
        return str(self.respTime)

    def get_respFbTime(self):
        return str(self.respFbTime)

    def get_rewFbTime(self):
        return str(self.rewFbTime)

    def get_choice(self):
        return str(self.choice)

    def get_confLevel(self):
        return str(self.confLevel)

    def get_confTime(self):
        return str(self.confTime)

    def get_correct(self):
        return str(self.correct)

    def get_correctMat(self):
        return str(self.correctMat)

    def get_correctPer(self):
        return str(self.correctPer)

    def get_responseMatrix(self):
        return str(self.responseMatrix)

    def get_reversals(self):
        return str(self.reversals)

    def get_stairDir(self):
        return str(self.stairDir)

    def get_dotStair(self):
        return str(self.dotStair)

    def get_dotStairLeft(self):
        return str(self.dotStairLeft)

    def get_dotStairRight(self):
        return str(self.dotStairRight)

    def errors(self):
        errors = super(PerTutorialData, self).errors()
        return errors
