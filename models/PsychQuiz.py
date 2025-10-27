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
    PgFinish_AUDIT    = Column(Text(length=10000))
    PgFinish_BIS11    = Column(Text(length=10000))
    PgFinish_EAT26    = Column(Text(length=10000))
    PgFinish_GSE    = Column(Text(length=10000))
    PgFinish_LSAS    = Column(Text(length=10000))
    PgFinish_OCIR    = Column(Text(length=10000))
    PgFinish_RSE    = Column(Text(length=10000))
    PgFinish_STAIY2  = Column(Text(length=10000))
    PgFinish_SDS      = Column(Text(length=10000))
    PgFinish_SSMS    = Column(Text(length=10000))
    PgFinish_IQ_text     = Column(Text(length=10000))
    PgFinish_IQ_image      = Column(Text(length=10000))
    PgRT_demo    = Column(Text(length=10000))
    PgRT_AES    = Column(Text(length=10000))
    PgRT_AUDIT    = Column(Text(length=10000))
    PgRT_BIS11    = Column(Text(length=10000))
    PgRT_EAT26    = Column(Text(length=10000))
    PgRT_GSE    = Column(Text(length=10000))
    PgRT_LSAS    = Column(Text(length=10000))
    PgRT_OCIR    = Column(Text(length=10000))
    PgRT_RSE    = Column(Text(length=10000))
    PgRT_STAIY2  = Column(Text(length=10000))
    PgRT_SDS      = Column(Text(length=10000))
    PgRT_SSMS    = Column(Text(length=10000))
    PgRT_IQ_text     = Column(Text(length=10000))
    PgRT_IQ_image      = Column(Text(length=10000))
    age              = Column(Text(length=10000))
    gender           = Column(Text(length=10000))
    AES    = Column(Text(length=10000))
    BIS11    = Column(Text(length=10000))
    EAT26    = Column(Text(length=10000))
    GSE    = Column(Text(length=10000))
    LSAS    = Column(Text(length=10000))
    OCIR    = Column(Text(length=10000))
    RSE    = Column(Text(length=10000))
    STAIY2  = Column(Text(length=10000))
    SDS      = Column(Text(length=10000))
    SSMS    = Column(Text(length=10000))
    AUDIT_1    = Column(Text(length=10000))
    AUDIT_2    = Column(Text(length=10000))
    AUDIT_3    = Column(Text(length=10000))
    AUDIT_4    = Column(Text(length=10000))
    AUDIT_5    = Column(Text(length=10000))
    AUDIT_6    = Column(Text(length=10000))
    AUDIT_7    = Column(Text(length=10000))
    AUDIT_8    = Column(Text(length=10000))
    AUDIT_9    = Column(Text(length=10000))
    AUDIT_10    = Column(Text(length=10000))
    AUDIT_11    = Column(Text(length=10000))
    AUDIT_12    = Column(Text(length=10000))
    AUDIT_13    = Column(Text(length=10000))
    IQ_1              = Column(Text(length=10000))
    IQ_2              = Column(Text(length=10000))
    IQ_3              = Column(Text(length=10000))
    IQ_4              = Column(Text(length=10000))
    IQ_5              = Column(Text(length=10000))
    IQ_6              = Column(Text(length=10000))
    IQ_7              = Column(Text(length=10000))
    IQ_8              = Column(Text(length=10000))
    IQimage_1              = Column(Text(length=10000))
    IQimage_2              = Column(Text(length=10000))
    IQimage_3              = Column(Text(length=10000))
    IQimage_4              = Column(Text(length=10000))
    IQimage_5              = Column(Text(length=10000))
    IQimage_6              = Column(Text(length=10000))
    IQimage_7              = Column(Text(length=10000))
    IQimage_8              = Column(Text(length=10000))

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

    def get_pg2_finish(self):
        return str(self.PgFinish_AUDIT)

    def get_pg3_finish(self):
        return str(self.PgFinish_BIS11)

    def get_pg4_finish(self):
        return str(self.PgFinish_EAT26)

    def get_pg5_finish(self):
        return str(self.PgFinish_LSAS)

    def get_pg6_finish(self):
        return str(self.PgFinish_OCIR)

    def get_pg7_finish(self):
        return str(self.PgFinish_SDS)

    def get_pg8_finish(self):
        return str(self.PgFinish_SSMS)

    def get_pg9_finish(self):
        return str(self.PgFinish_STAIY2)

    def get_pg10_finish(self):
        return str(self.PgFinish_RSE)

    def get_pg11_finish(self):
        return str(self.PgFinish_GSE)

    def get_pg12_finish(self):
        return str(self.PgFinish_IQ_text)

    def get_pg13_finish(self):
        return str(self.PgFinish_IQ_image)

    def get_pg0_rt(self):
        return str(self.PgRT_demo)

    def get_pg1_rt(self):
        return str(self.PgRT_AES)

    def get_pg2_rt(self):
        return str(self.PgRT_AUDIT)

    def get_pg3_rt(self):
        return str(self.PgRT_BIS11)

    def get_pg4_rt(self):
        return str(self.PgRT_EAT26)

    def get_pg5_rt(self):
        return str(self.PgRT_LSAS)

    def get_pg6_rt(self):
        return str(self.PgRT_OCIR)

    def get_pg7_rt(self):
        return str(self.PgRT_SDS)

    def get_pg8_rt(self):
        return str(self.PgRT_SSMS)

    def get_pg9_rt(self):
        return str(self.PgRT_STAIY2)

    def get_pg10_rt(self):
        return str(self.PgRT_RSE)

    def get_pg11_rt(self):
        return str(self.PgRT_GSE)

    def get_pg12_rt(self):
        return str(self.PgRT_IQ_text)

    def get_pg13_rt(self):
        return str(self.PgRT_IQ_image)

    def get_age(self):
        return str(self.age)

    def get_gender(self):
        return str(self.gender)

    def get_aes(self):
        return str(self.AES)

    def get_audit1(self):
        return str(self.AUDIT_1)

    def get_audit2(self):
        return str(self.AUDIT_2)

    def get_audit3(self):
        return str(self.AUDIT_3)

    def get_audit4(self):
        return str(self.AUDIT_4)

    def get_audit5(self):
        return str(self.AUDIT_5)

    def get_audit6(self):
        return str(self.AUDIT_6)

    def get_audit7(self):
        return str(self.AUDIT_7)

    def get_audit8(self):
        return str(self.AUDIT_8)

    def get_audit9(self):
        return str(self.AUDIT_9)

    def get_audit10(self):
        return str(self.AUDIT_10)

    def get_audit11(self):
        return str(self.AUDIT_11)

    def get_audit12(self):
        return str(self.AUDIT_12)

    def get_audit13(self):
        return str(self.AUDIT_13)

    def get_eat(self):
        return str(self.EAT26)

    def get_gse(self):
        return str(self.GSE)

    def get_rse(self):
        return str(self.RSE)

    def get_lsas(self):
        return str(self.LSAS)

    def get_SSMS(self):
        return str(self.SSMS)

    def get_ocir(self):
        return str(self.OCIR)

    def get_staiTwo(self):
        return str(self.STAIY2)

    def get_bis(self):
        return str(self.BIS11)

    def get_sds(self):
        return str(self.SDS)

    def get_iq1(self):
        return str(self.IQ_1)

    def get_iq3(self):
        return str(self.IQ_3)

    def get_iq4(self):
        return str(self.IQ_4)

    def get_iq5(self):
        return str(self.IQ_5)

    def get_iq6(self):
        return str(self.IQ_6)

    def get_iq7(self):
        return str(self.IQ_7)

    def get_iq8(self):
        return str(self.IQ_8)

    def get_iqimage1(self):
        return str(self.IQimage_1)

    def get_iqimage3(self):
        return str(self.IQimage_3)

    def get_iqimage4(self):
        return str(self.IQimage_4)

    def get_iqimage5(self):
        return str(self.IQimage_5)

    def get_iqimage6(self):
        return str(self.IQimage_6)

    def get_iqimage7(self):
        return str(self.IQimage_7)

    def get_iqimage8(self):
        return str(self.IQimage_8)


    def errors(self):
        errors = super(PsychQuiz, self).errors()
        return errors
