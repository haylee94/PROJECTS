from flask import Blueprint
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/', methods=['POST', 'GET'])
def values():
    return render_template('main.html')