from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
db = SQLAlchemy()

class Officer(db.Model):
    # __tablename__ = 'officers'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(80), index=True)
    county = db.Column(db.String(80), index=True)
    case_num = db.Column(db.String(60), index=True)
    first_name = db.Column(db.String(80), index=True)
    middle_name = db.Column(db.String(80), index=True)
    last_name = db.Column(db.String(80), index=True)
    suffix = db.Column(db.String(60))
    dob = db.Column(db.String(80), index=True)
    race = db.Column(db.String(60), index=True)
    sex = db.Column(db.String(60), index=True)
    arrest_date = db.Column(db.String(80), index=True)
    filing_date = db.Column(db.String(80), index=True)
    offense_date = db.Column(db.String(80))
    division_name = db.Column(db.String(120))
    case_status = db.Column(db.String(60))
    defense_attorney = db.Column(db.String(120))
    public_defender = db.Column(db.String(120))
    judge = db.Column(db.String(120))
    charge_count = db.Column(db.String(60))
    charge_statute = db.Column(db.String(120))
    charge_description = db.Column(db.String(120))
    charge_disposition = db.Column(db.String(120))
    charge_disposition_date = db.Column(db.String(80))
    charge_offense_date = db.Column(db.String(80))
    charge_citation_num = db.Column(db.Integer)
    charge_plea = db.Column(db.String(60), index=True)
    charge_plea_date = db.Column(db.String(80), index=True)
    arresting_officer = db.Column(db.String(120), index=True)
    arresting_officer_badge_number = db.Column(db.Integer, index=True)

    def __init__(self, state=None, county=None, case_num=None, first_name=None, middle_name=None, last_name=None,
                     suffix=None, dob=None, race=None, sex=None, arrest_date=None, filing_date=None, offense_date=None,
                     division_name=None, case_status=None, defense_attorney=None, public_defender=None, judge=None,
                     charge_count=None, charge_statute=None, charge_description=None, charge_disposition=None,
                     charge_disposition_date=None, charge_offense_date=None, charge_citation_num=None, charge_plea=None,
                     charge_plea_date=None, arresting_officer=None, arresting_officer_badge_number=None):
         self.state = state
         self.county = county
         self.case_num = case_num
         self.first_name = first_name
         self.middle_name = middle_name
         self.last_name = last_name
         self.suffix = suffix
         self.dob = dob
         self.race = race
         self.sex = sex
         self.arrest_date = arrest_date
         self.filing_date = filing_date
         self.offense_date = offense_date
         self.division_name = division_name
         self.case_status = case_status
         self.defense_attorney = defense_attorney
         self.public_defender = public_defender
         self.judge = judge
         self.charge_count = charge_count
         self.charge_statute = charge_statute
         self.charge_description = charge_description
         self.charge_disposition = charge_disposition
         self.charge_disposition_date = charge_disposition_date
         self.charge_offense_date = charge_offense_date
         self.charge_citation_num = charge_citation_num
         self.charge_plea = charge_plea
         self.charge_plea_date = charge_plea_date
         self.arresting_officer = arresting_officer
         self.arresting_officer_badge_number = arresting_officer_badge_number


class OfficerSchema(Schema):
    id = fields.Int()
    state = fields.Str()
    county = fields.Str()
    case_num = fields.Str()
    first_name = fields.Str()
    middle_name = fields.Str()
    last_name = fields.Str()
    suffix = fields.Str()
    dob = fields.Str()
    race = fields.Str()
    sex = fields.Str()
    arrest_date = fields.Str()
    filing_date = fields.Str()
    offense_date = fields.Str()
    division_name = fields.Str()
    case_status = fields.Str()
    defense_attorney = fields.Str()
    public_defender = fields.Str()
    judge = fields.Str()
    charge_count = fields.Str()
    charge_statute = fields.Str()
    charge_description = fields.Str()
    charge_disposition = fields.Str()
    charge_disposition_date = fields.Str()
    charge_offense_date = fields.Str()
    charge_citation_num = fields.Int()
    charge_plea = fields.Str()
    charge_plea_date = fields.Str()
    arresting_officer = fields.Str()
    arresting_officer_badge_number = fields.Int()
