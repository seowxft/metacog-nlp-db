"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class Feedback(BaseObject, Model):

    id = Column(Integer, primary_key=True)
    prolificID               = Column(Text(length=10000))
    userID               = Column(Text(length=10000))
    condition               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    section               = Column(Text(length=10000))
    sectionTime           = Column(Text(length=10000))
    ratingValue           = Column(Text(length=10000))
    perBonus = Column(Text(length=10000))
    memBonus = Column(Text(length=10000))
    totalBonus            = Column(Text(length=10000))
    feedback             = Column(Text(length=10000))


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

    def get_ratingValue(self):
        return str(self.ratingValue)

    def get_perBonus(self):
        return str(self.perBonus)

    def get_memBonus(self):
        return str(self.memBonus)

    def get_totalBonus(self):
        return str(self.totalBonus)

    def get_feedback(self):
        return str(self.feedback)


    def errors(self):
        errors = super(Feedback, self).errors()
        return errors
