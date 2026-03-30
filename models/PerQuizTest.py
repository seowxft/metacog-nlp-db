"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PerQuizTest(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    section          = Column(Text(length=10000))
    sectionTime          = Column(Text(length=10000))
    quizTry        =  Column(Text(length=10000))
    quizNumTotal         = Column(Text(length=10000))
    quizNum          = Column(Text(length=10000))
    quizTime         = Column(Text(length=10000))
    quizResp    = Column(Text(length=10000))
    quizRT     = Column(Text(length=10000))
    quizAns     = Column(Text(length=10000))
    quizCor     = Column(Text(length=10000))
    quizCorTotal      = Column(Text(length=10000))

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

    def get_quizTry(self):
        return str(self.quizTry)

    def get_quizNumTotal(self):
        return str(self.quizNumTotal)

    def get_quizNum(self):
        return str(self.quizNum)

    def get_quizTime(self):
        return str(self.quizTime)

    def get_quizResp(self):
        return str(self.quizResp)

    def get_quizRT(self):
        return str(self.quizRT)

    def get_quizAns(self):
        return str(self.quizAns)

    def get_quizCor(self):
        return str(self.quizCor)

    def get_quizCorTotal(self):
        return str(self.quizCorTotal)

    def errors(self):
        errors = super(PerQuizTest, self).errors()
        return errors
