"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PrePostConf(BaseObject, Model):

    id = Column(Integer, primary_key=True)
    
    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    task               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    section          = Column(Text(length=10000))
    sectionTime          = Column(Text(length=10000))
    blockNum   = Column(Text(length=10000))
    quizState       = Column(Text(length=10000))
    confInitial            = Column(Text(length=10000))
    confLevel             = Column(Text(length=10000))
    textTime            = Column(Text(length=10000))
    selfKnowledge             = Column(Text(length=10000))
    mouseMovements =   Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_prolific_id(self):
        return str(self.prolificID)

    def get_user_id(self):
        return str(self.userID)

    def get_condition(self):
        return str(self.condition)

    def get_task(self):
        return str(self.task)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_section(self):
        return str(self.section)

    def get_sectionTime(self):
        return str(self.sectionTime)

    def get_blockNum(self):
        return str(self.blockNum)

    def get_quizState(self):
        return str(self.quizState)

    def get_confInitial(self):
        return str(self.confInitial)

    def get_confLevel(self):
        return str(self.confLevel)

    def get_textTime(self):
        return str(self.textTime)

    def get_selfKnowledge(self):
        return str(self.selfKnowledge)
    
    def get_mouseMovements(self):
        return str(self.mouseMovements)
    
    def errors(self):
        errors = super(PrePostConf, self).errors()
        return errors
