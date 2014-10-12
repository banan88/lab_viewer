from app.shared import db

# many-to-many labs/tags support
labs_tags = db.Table('labs_tags', \
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                     db.Column('lab_id', db.Integer, db.ForeignKey('lab.id'))
)


class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    tags = db.relationship('Tag', secondary=labs_tags, backref=db.backref('labs'), lazy='joined')
    parent_id = db.Column(db.Integer, db.ForeignKey('lab.id'), index=True)
    parent = db.relationship('Lab', remote_side=id, backref=db.backref('child_nodes'))

    def __init__(self, name, parent_id = None):
        self.name = name
        self.parent_id = parent_id