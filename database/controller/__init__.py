from flask import Blueprint

bp = Blueprint('controller', __name__)

from controller import (history_controller)