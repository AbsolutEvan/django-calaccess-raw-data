from __future__ import unicode_literals
from django.db import models
from .base import CalAccessBaseModel


class FilerFilingsCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'FILING_DATE',
        'RPT_START',
        'RPT_END',
        'RPT_DATE'
    ]
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    period_id = models.IntegerField(
        null=True, db_column='PERIOD_ID', blank=True
    )
    form_id = models.CharField(max_length=7L, db_column='FORM_ID')
    filing_sequence = models.IntegerField(
        db_column='FILING_SEQUENCE', db_index=True
    )
    filing_date = models.DateField(db_column='FILING_DATE')
    stmnt_type = models.IntegerField(db_column='STMNT_TYPE')
    stmnt_status = models.IntegerField(db_column='STMNT_STATUS')
    session_id = models.IntegerField(db_column='SESSION_ID')
    user_id = models.CharField(max_length=12L, db_column='USER_ID')
    special_audit = models.IntegerField(
        null=True, db_column='SPECIAL_AUDIT', blank=True
    )
    fine_audit = models.IntegerField(
        null=True, db_column='FINE_AUDIT', blank=True
    )
    rpt_start = models.DateField(null=True, db_column='RPT_START', blank=True)
    rpt_end = models.DateField(null=True, db_column='RPT_END', blank=True)
    rpt_date = models.DateField(null=True, db_column='RPT_DATE', blank=True)
    filing_type = models.IntegerField(
        null=True, db_column='FILING_TYPE', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_FILINGS_CD'


class FilingsCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    filing_type = models.IntegerField(db_column='FILING_TYPE')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILINGS_CD'


class SmryCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'ELEC_DT'
    ]
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    line_item = models.CharField(max_length=8L, db_column='LINE_ITEM')
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    form_type = models.CharField(max_length=8L, db_column='FORM_TYPE')
    amount_a = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_A', blank=True
    )
    amount_b = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_B', blank=True
    )
    amount_c = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_C', blank=True
    )
    elec_dt = models.DateField(null=True, db_column='ELEC_DT', blank=True)
    current_filing = models.CharField(max_length=1L, blank=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'SMRY_CD'


class CvrE530Cd(CalAccessBaseModel):
    DATE_FIELDS = (
        "RPT_DATE",
        "PMNT_DT",
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=3)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    entity_cd = models.CharField(
        db_column='ENTITY_CD', max_length=32, blank=True
    )
    filer_naml = models.CharField(db_column='FILER_NAML', max_length=200)
    filer_namf = models.CharField(
        db_column='FILER_NAMF', max_length=4, blank=True
    )
    filer_namt = models.CharField(
        db_column='FILER_NAMT', max_length=32, blank=True
    )
    filer_nams = models.CharField(
        db_column='FILER_NAMS', max_length=32, blank=True
    )
    report_num = models.CharField(
        db_column='REPORT_NUM', max_length=32, blank=True
    )
    rpt_date = models.DateField(db_column='RPT_DATE')
    filer_city = models.CharField(
        db_column='FILER_CITY', max_length=16, blank=True
    )
    filer_st = models.CharField(db_column='FILER_ST', max_length=4, blank=True)
    filer_zip4 = models.CharField(
        db_column='FILER_ZIP4', max_length=10, blank=True
    )
    occupation = models.CharField(
        db_column='OCCUPATION', max_length=15, blank=True
    )
    employer = models.CharField(
        db_column='EMPLOYER', max_length=13, blank=True
    )
    cand_naml = models.CharField(db_column='CAND_NAML', max_length=46)
    cand_namf = models.CharField(
        db_column='CAND_NAMF', max_length=21, blank=True
    )
    cand_namt = models.CharField(
        db_column='CAND_NAMT', max_length=32, blank=True
    )
    cand_nams = models.CharField(
        db_column='CAND_NAMS', max_length=32, blank=True
    )
    district_cd = models.IntegerField(db_column='DISTRICT_CD')
    office_cd = models.IntegerField(db_column='OFFICE_CD')
    pmnt_dt = models.DateField(db_column='PMNT_DT')
    pmnt_amount = models.FloatField(db_column='PMNT_AMOUNT')
    type_literature = models.IntegerField(db_column='TYPE_LITERATURE')
    type_printads = models.IntegerField(db_column='TYPE_PRINTADS')
    type_radio = models.IntegerField(db_column='TYPE_RADIO')
    type_tv = models.IntegerField(db_column='TYPE_TV')
    type_it = models.IntegerField(db_column='TYPE_IT')
    type_billboards = models.IntegerField(db_column='TYPE_BILLBOARDS')
    type_other = models.IntegerField(db_column='TYPE_OTHER')
    other_desc = models.CharField(db_column='OTHER_DESC', max_length=49)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_E530_CD'


class TextMemoCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=8)
    ref_no = models.CharField(db_column='REF_NO', max_length=20, blank=True)
    text4000 = models.CharField(
        db_column='TEXT4000',
        max_length=4000, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'TEXT_MEMO_CD'