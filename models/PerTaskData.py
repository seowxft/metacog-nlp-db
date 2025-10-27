"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PerTaskData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    section         = Column(Text(length=10000))
    sectionTime    = Column(Text(length=10000))
    trialNum = Column(Text(length=10000))
    trialTime  = Column(Text(length=10000))
    fixTime   = Column(Text(length=10000))
    stimTime    = Column(Text(length=10000))
    stimPos =Column(Text(length=10000))
    dotDiffLeft = Column(Text(length=10000))
    dotDiffRight  = Column(Text(length=10000))
    dotDiffStim1 = Column(Text(length=10000))
    dotDiffStim2     = Column(Text(length=10000))
    responseKey    = Column(Text(length=10000))
    respTime  = Column(Text(length=10000))
    respFbTime     = Column(Text(length=10000))
    choice = Column(Text(length=10000))
    confInitial =Column(Text(length=10000))
    confLevel  = Column(Text(length=10000))
    confTime    = Column(Text(length=10000))
    correct = Column(Text(length=10000))
    correctMat = Column(Text(length=10000))
    correctPer = Column(Text(length=10000))
    responseMatrix  = Column(Text(length=10000))
    reversals = Column(Text(length=10000))
    stairDir     = Column(Text(length=10000))
    dotStair    = Column(Text(length=10000))
    dotStairLeft     = Column(Text(length=10000))
    dotStairRight  = Column(Text(length=10000))

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

    def get_trialPic(self):
        return str(self.trialPic)

    def get_trialWord(self):
        return str(self.trialWord)

    def get_trialCat(self):
        return str(self.trialCat)

    def get_ratingTime(self):
        return str(self.ratingTime)

    def get_ratingRT(self):
        return str(self.ratingRT)

    def get_ratingRT(self):
        return str(self.ratingRT)

    def get_itemText(self):
        return str(self.itemText)

    def get_harmIni(self):
        return str(self.harmIni)

    def get_harmLevel(self):
        return str(self.harmLevel)

    def get_anxIni(self):
        return str(self.anxIni)

    def get_anxLevel(self):
        return str(self.anxLevel)


    def errors(self):
        errors = super(PerTaskData, self).errors()
        return errors
