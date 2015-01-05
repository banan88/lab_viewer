from flask.ext.restless import APIManager
from flask.ext.restless import ProcessingException
from app.models.lab import Lab
from app.models.tag import Tag
from app.shared import db

rest_api_prefix = '/api/v1'
all_http_verbs = ['GET', 'DELETE', 'POST', 'PUT']


def pre_put_single(instance_id, **kw):
    if kw['data'].get('parent_id') and Lab.query.filter_by(parent_id=instance_id).count() > 0:
        raise ProcessingException(
            description="This lab is a master node, can't assign it to another node.",
            code=400)


def create_api_manager(application):
    """
    Creates & configures flask-restless api manager providing rest api for db model classes.
    """
    manager = APIManager(application, flask_sqlalchemy_db=db)
    configure_labs_api(manager)
    configure_tags_api(manager)


def configure_labs_api(manager):
    manager.create_api(Lab, url_prefix=rest_api_prefix, methods=all_http_verbs,
                       include_columns=['id', 'name', 'mpp_name', 'ip', 'credentials', 'description', 'parent_id',
                                        'child_nodes', 'tags'],
                       preprocessors={'PUT_SINGLE': [pre_put_single]})


def configure_tags_api(manager):
    manager.create_api(Tag, url_prefix=rest_api_prefix, methods=all_http_verbs, include_columns=['id', 'name', 'labs'])