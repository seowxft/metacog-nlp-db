'''
	Script qui lance le backend (database)
'''
import os
import warnings

# Flask: interagit avec la base de donnees
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message

from models.db import db
from models.install import install_models

from config import config

warnings.filterwarnings("ignore")

# mail = Mail()
app  = Flask(__name__)

# -------------------------
# --- DB configuration ----
# -------------------------

# 1. Try to get the production (Scalingo) DATABASE_URL
database_url = os.environ.get('DATABASE_URL')

# 2. If the variable is NOT found (we are running locally), 
#    then fall back to your local config file.
if not database_url:
    print("INFO: DATABASE_URL environment variable not set. Falling back to local config.txt.")
    database_url = config.get('Database Parameters','database_url')
else:
    # 3. If the variable IS found (we are on Scalingo),
    #    make sure it uses the 'mysql+pymysql' driver.
    print("INFO: Found DATABASE_URL. Configuring for production.")
    if database_url.startswith('mysql://'):
        database_url = database_url.replace('mysql://', 'mysql+pymysql://', 1)

# 4. Finally, set the configuration using whichever URL was chosen
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db.init_app(app)
CORS(app)

with app.app_context():
    install_models()
    import routes


# --- TESTING THE SERVER IS WORKING -----------
@app.route('/testmethod', methods=['GET', 'POST'])
def mytest():
    result = dict()
    result['test'] = 'ok'
    return jsonify(result), 200


###########################################################
# let's start
###########################################################

if __name__ == '__main__':
    print("Starting webserver.")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=False)
