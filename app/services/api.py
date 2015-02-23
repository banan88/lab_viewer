from flask.ext.restless import APIManager
from app.models.lab import Lab
from app.models.tag import Tag
from app.shared import db
from app.services.validators import check_master_node_assign
from app.services.validators import unique_validator_for_model

rest_api_prefix = '/api/v1'
all_http_verbs = ['GET', 'DELETE', 'POST', 'PUT']




def create_api_manager(application):
    """
    Creates & configures flask-restless api manager providing rest api for db model classes.
    """
    manager = APIManager(application, flask_sqlalchemy_db=db)
    configure_labs_api(manager)
    configure_tags_api(manager)


def configure_labs_api(manager):
    unique_field_validator= unique_validator_for_model(Lab)

    manager.create_api(Lab, url_prefix=rest_api_prefix, methods=all_http_verbs,
                       include_columns=['id', 'name', 'mpp_name', 'ip', 'credentials', 'description', 'parent_id',
                                        'child_nodes', 'tags'],
                       preprocessors={'PUT_SINGLE': [check_master_node_assign],
                                      'POST': [unique_field_validator]})


def configure_tags_api(manager):
    manager.create_api(Tag, url_prefix=rest_api_prefix, methods=all_http_verbs, include_columns=['id', 'name', 'labs'])