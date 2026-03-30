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
    PgFinish_AES    = Column(Text(length=10000))
    PgFinish_GSE    = Column(Text(length=10000))
    PgFinish_RSE    = Column(Text(length=10000))
    PgFinish_STAIY2  = Column(Text(length=10000))
    PgFinish_SDS      = Column(Text(length=10000))
    PgRT_demo    = Column(Text(length=10000))
    PgRT_AES    = Column(Text(length=10000))
    PgRT_GSE    = Column(Text(length=10000))
    PgRT_RSE    = Column(Text(length=10000))
    PgRT_STAIY2  = Column(Text(length=10000))
    PgRT_SDS      = Column(Text(length=10000))
    age              = Column(Text(length=10000))
    gender           = Column(Text(length=10000))
    AES    = Column(Text(length=10000))
    GSE    = Column(Text(length=10000))
    RSE    = Column(Text(length=10000))
    STAIY2  = Column(Text(length=10000))
    SDS      = Column(Text(length=10000))

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
        return str(self.PgFinish_AES)

    def get_pg7_finish(self):
        return str(self.PgFinish_SDS)

    def get_pg9_finish(self):
        return str(self.PgFinish_STAIY2)

    def get_pg10_finish(self):
        return str(self.PgFinish_RSE)

    def get_pg11_finish(self):
        return str(self.PgFinish_GSE)

    def get_pg0_rt(self):
        return str(self.PgRT_demo)

    def get_pg1_rt(self):
        return str(self.PgRT_AES)

    def get_pg7_rt(self):
        return str(self.PgRT_SDS)

    def get_pg9_rt(self):
        return str(self.PgRT_STAIY2)

    def get_pg10_rt(self):
        return str(self.PgRT_RSE)

    def get_pg11_rt(self):
        return str(self.PgRT_GSE)

    def get_age(self):
        return str(self.age)

    def get_gender(self):
        return str(self.gender)

    def get_aes(self):
        return str(self.AES)

    def get_gse(self):
        return str(self.GSE)

    def get_rse(self):
        return str(self.RSE)

    def get_staiTwo(self):
        return str(self.STAIY2)

    def get_sds(self):
        return str(self.SDS)


    def errors(self):
        errors = super(PsychQuiz, self).errors()
        return errors
