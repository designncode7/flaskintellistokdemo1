from flask import render_template
from IntellistokDemoFlaskWeb2018Jul264 import app

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

#@app.errorhandler(Exception)
#def unhandled_exception(e):
#    errormsg = 'Unhandled Exception: ' + str(e)
#    app.logger.error(errormsg)
#    return render_template('errors.html', errormsg), e.code 
