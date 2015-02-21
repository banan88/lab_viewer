from flask.ext.restless import ProcessingException
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.schema import UniqueConstraint
from app.models.lab import Lab
from app.utils.text_utils import camelcase_to_underscore

def check_master_node_assign(instance_id, **kw):
    if kw['data'].get('parent_id') and Lab.query.filter_by(parent_id=instance_id).count() > 0:
        raise ProcessingException(
            description="This lab is a master node, can't assign it to another node.",
            code=400)


#TODO make this validator generic!
def check_lab_unique(data, **kw):
    for k, v in data.iteritems() :
        print camelcase_to_underscore(k)


    for c in Lab.__table__.constraints:
        if type(c) is UniqueConstraint or type(c) is PrimaryKeyConstraint:
            print c.columns


    name = data.get('name') #chain filters to make one sql query for all constraints + relevant msg
    if Lab.query.filter_by(name=name).count() > 0:
        raise ProcessingException(
            description="Field '%s' already exists." % name,
            code=400)