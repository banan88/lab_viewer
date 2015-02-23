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


def unique_validator_for_model(model):
    unique_fields = []

    for constraint in model.__table__.constraints:
        if type(constraint) is UniqueConstraint or type(constraint) is PrimaryKeyConstraint:
            for column in  constraint.columns.items():
                unique_fields.append(column[0])

    def check_constraints(data, **kw):
        field_names_to_check = []
        for k, v in data.iteritems() :
            if camelcase_to_underscore(k) in unique_fields:
                field_names_to_check.append(k)
        print field_names_to_check

    return check_constraints




#TODO make this validator generic!
def check_constraints(data, **kw):
    print data
    for k, v in data.iteritems() :
        print camelcase_to_underscore(k)

    name = data.get('name') #chain filters to make one sql query for all constraints + relevant msg
    if Lab.query.filter_by(name=name).count() > 0:
        raise ProcessingException(
            description="Field '%s' already exists." % name,
            code=400)