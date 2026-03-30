"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class MemTaskData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    section         = Column(Text(length=10000))
    sectionTime    = Column(Text(length=10000))
    trialNum = Column(Text(length=10000))
    blockNum                = Column(Text(length=10000))
    blockCond           = Column(Text(length=10000))
    condEasyTrialNum         = Column(Text(length=10000))
    condHardTrialNum    = Column(Text(length=10000))
    trialNumInBlock = Column(Text(length=10000))
    choicePos =Column(Text(length=10000))
    choiceCor =Column(Text(length=10000))
    trialTime  = Column(Text(length=10000))
    fixTime   = Column(Text(length=10000))
    stimTime    = Column(Text(length=10000))
    encodeTime    = Column(Text(length=10000))
    respTime  = Column(Text(length=10000))
    respFbTime     = Column(Text(length=10000))
    confTime    = Column(Text(length=10000))

    responseKey    = Column(Text(length=10000))
    choice = Column(Text(length=10000))
    correct = Column(Text(length=10000))
    correctMat = Column(Text(length=10000))
    correctPer = Column(Text(length=10000))
    confInitial =Column(Text(length=10000))
    confLevel  = Column(Text(length=10000))

    stimNum  = Column(Text(length=10000))
    responseMatrix  = Column(Text(length=10000))
    reversals = Column(Text(length=10000))
    stairDir     = Column(Text(length=10000))

    stimNumEasy = Column(Text(length=10000))
    correctMatEasy     = Column(Text(length=10000))
    correctPerEasy    = Column(Text(length=10000))
    responseMatrixEasy  = Column(Text(length=10000))
    stairDirEasy     = Column(Text(length=10000))

    stimNumHard = Column(Text(length=10000))
    correctMatHard =Column(Text(length=10000))
    correctPerHard  = Column(Text(length=10000))
    responseMatrixHard    = Column(Text(length=10000))
    stairDirHard = Column(Text(length=10000))

    stimPick= Column(Text(length=10000))
    stimWordPick= Column(Text(length=10000))
    stimShown= Column(Text(length=10000))
    stimWordShown= Column(Text(length=10000))

    choiceShownWordStim1= Column(Text(length=10000))
    choiceShownWordStim2= Column(Text(length=10000))
    choiceShownWordLeft= Column(Text(length=10000))
    choiceShownWordRight= Column(Text(length=10000))

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

    def get_blockNum(self):
        return str(self.blockNum)

    def get_blockCond(self):
        return str(self.blockCond)

    def get_condEasyTrialNum(self):
        return str(self.condEasyTrialNum)

    def get_condHardTrialNum(self):
        return str(self.condHardTrialNum)

    def get_choicePos(self):
        return str(self.choicePos)

    def get_choiceCor(self):
        return str(self.choiceCor)

    def get_trialTime(self):
        return str(self.trialTime)

    def get_fixTime(self):
        return str(self.fixTime)

    def get_stimTime(self):
        return str(self.stimTime)

    def get_encodeTime(self):
        return str(self.encodeTime)

    def get_respTime(self):
        return str(self.respTime)

    def get_respFbTime(self):
        return str(self.respFbTime)

    def get_confTime(self):
        return str(self.confTime)

    def get_responseKey(self):
        return str(self.responseKey)

    def get_choice(self):
        return str(self.choice)

    def get_correct(self):
        return str(self.correct)

    def get_correctMat(self):
        return str(self.correctMat)

    def get_correctPer(self):
        return str(self.correctPer)

    def get_confInitial(self):
        return str(self.confInitial)

    def get_confLevel(self):
        return str(self.confLevel)

    def get_stimNum(self):
        return str(self.stimNum)

    def get_responseMatrix(self):
        return str(self.responseMatrix)

    def get_reversals(self):
        return str(self.reversals)

    def get_stairDir(self):
        return str(self.stairDir)
    
    def get_correctMatEasy(self):
        return str(self.correctMatEasy)

    def get_correctPerEasy(self):
        return str(self.correctPerEasy)

    def get_responseMatrixEasy(self):
        return str(self.responseMatrixEasy)

    def get_stairDirEasy(self):
        return str(self.stairDirEasy)

    def get_stimNumEasy(self):
        return str(self.stimNumEasy)

    def get_correctMatHard(self):
        return str(self.correctMatHard)

    def get_correctPerHard(self):
        return str(self.correctPerHard)

    def get_responseMatrixHard(self):
        return str(self.responseMatrixHard)

    def get_stairDirHard(self):
        return str(self.stairDirHard)

    def get_stimNumHard(self):
        return str(self.stimNumHard)

    def get_stimPick(self):
        return str(self.stimPick)

    def get_stimWordPick(self):
        return str(self.stimWordPick)

    def get_stimShown(self):
        return str(self.stimShown)

    def get_stimWordShown(self):
        return str(self.stimWordShown)

    def get_choiceShownWordStim1(self):
        return str(self.choiceShownWordStim1)

    def get_choiceShownWordStim2(self):
        return str(self.choiceShownWordStim2)

    def get_choiceShownWordRight(self):
        return str(self.choiceShownWordLeft)

    def get_choiceShownWordRight(self):
        return str(self.choiceShownWordRight)


    def errors(self):
        errors = super(MemTaskData, self).errors()
        return errors
