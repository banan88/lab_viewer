from app.shared import db

# many-to-many labs/tags support
labs_tags = db.Table('labs_tags', \
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                     db.Column('lab_id', db.Integer, db.ForeignKey('lab.id'))
)


class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    mpp_name = db.Column(db.String(120), unique=True)
    ip = db.Column(db.String(45), unique=True)
    credentials=db.Column(db.String(120), unique=False)
    tags = db.relationship('Tag', secondary=labs_tags, backref=db.backref('labs'), lazy='joined')
    parent_id = db.Column(db.Integer, db.ForeignKey('lab.id'), index=True)
    parent = db.relationship('Lab', remote_side=id, backref=db.backref('child_nodes'))
    description = db.Column(db.String(300), unique=True)

    def __init__(self, name, mpp_name=None, ip=None, parent_id=None, description=None):
        self.name = name
        self.mpp_name = mpp_name
        self.ip = ip
        self.parent_id = parent_id
        self.description = description