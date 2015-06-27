from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
#app.config['DEBUG_TB_PANELS'] = (
#    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
#    'flask_debugtoolbar.panels.logger.LoggingPanel',
#    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
#)
#app.config['DEBUG_TB_HOSTS'] = ('127.0.0.1', '::1' )
app.config['SECRET_KEY'] = 'admin'
app.config['DEBUG'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
	app.logger.info("Hello there")
	return render_template('index.html')


@app.route('/redirect')
def redirect_example():
    response = redirect(url_for('index'))
    response.set_cookie('test_cookie', '1')
    return response


if __name__ == "__main__":
    app.run()