from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PsychQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)
    prolificID           = Column(Text(length=10000))
    userID           = Column(Text(length=10000))
    condition           = Column(Text(length=10000))
    date             = Column(Text(length=10000))
    startTime        = Column(Text(length=10000))
    section         = Column(Text(length=10000))
    sectionTime     = Column(Text(length=10000))
    qnTimeStart      = Column(Text(length=10000))
    qnTimeEnd        = Column(Text(length=10000))
    PgFinish_demo    = Column(Text(length=10000))
    PgFinish_PHQ    = Column(Text(length=10000))
    PgFinish_GAD   = Column(Text(length=10000))
    PgRT_demo    = Column(Text(length=10000))
    PgRT_PHQ    = Column(Text(length=10000))
    PgRT_GAD    = Column(Text(length=10000))
    age              = Column(Text(length=10000))
    gender           = Column(Text(length=10000))
    PHQ    = Column(Text(length=10000))
    GAD    = Column(Text(length=10000))
    windowWidth = Column(Text(length=10000))
    windowHeight = Column(Text(length=10000))
    mouseMovements= Column(Text(length=10000)) 

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

    def get_start_time(self):
        return str(self.startTime)

    def get_section(self):
        return str(self.section)

    def get_section_time(self):
        return str(self.sectionTime)

    def get_qn_start(self):
        return str(self.qnTimeStart)

    def get_qn_end(self):
        return str(self.qnTimeEnd)

    def get_pg0_finish(self):
        return str(self.PgFinish_demo)

    def get_pg1_finish(self):
        return str(self.PgFinish_PHQ)

    def get_pg2_finish(self):
        return str(self.PgFinish_GAD)

    def get_pg0_rt(self):
        return str(self.PgRT_demo)

    def get_pg1_rt(self):
        return str(self.PgRT_PHQ)

    def get_pg2_rt(self):
        return str(self.PgRT_GAD)

    def get_age(self):
        return str(self.age)

    def get_gender(self):
        return str(self.gender)

    def get_phq(self):
        return str(self.PHQ)

    def get_gad(self):
        return str(self.GAD)

    def get_windowWidth(self):
        return str(self.windowWidth)

    def get_windowHeight(self):
        return str(self.windowHeight)
    
    def get_mouseMovements(self):
        return str(self.mouseMovements)

    def errors(self):
        errors = super(PsychQuiz, self).errors()
        return errors
