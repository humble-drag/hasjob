from datetime import timedelta

from hasjob.views.display import *
from hasjob.views.error_handling import *
from hasjob.views.stats import *
from hasjob.views.helper import *
from hasjob.views.update import *

@app.route('/type/')
@app.route('/category/')
@app.route('/view/')
@app.route('/edit/')
@app.route('/confirm/')
@app.route('/withdraw/')
def root_paths():
    return redirect(url_for('index'), code=302)

ALLOWED_TAGS = [
    'strong',
    'em',
    'p',
    'ol',
    'ul',
    'li',
    'br',
    'a',
]


newlimit = timedelta(days=1)