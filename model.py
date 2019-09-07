from .app import db


class SamplesMetaData(db.Model):
    __tablename__ = 'samplesMeta'

    Sample = db.Column(db.Integer, primary_key=True)
    Ethnicity = db.Column(db.String(64))
    Gender = db.Column(db.Float)
    Age = db.Column(db.Float)
    Location = db.Column(db.Float)
    BBtype = db.Column(db.Float)
    WFREG = db.Column(db.Float)
    def __repr__(self):
        return '<Sample %r>' % (self.name)

class SampleMetaData(db.model):
    __tablename__ = "sampleMeta"

    Sample = db.Column(db.Integer)
    Ethnicity = db.Column(db.Integer)
    Gender = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Location = db.Column(db.Integer)
    BBtype = db.column(db.Integer)
    WFREG  = db.Column(db.Integer)
    def __repr__(self):
        return '<Sample %r' % (self.name)
