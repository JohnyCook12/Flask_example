from flask import Flask, render_template
from admin.second import second_blue                                  # import BLUEPRINT - just like a FUNCTION from MODULE

app = Flask(__name__)
app.register_blueprint(second_blue, url_prefix="/admin")              # REGISTER blueprint. URLs with prefix /admin will get page from BLUEPRINT
                                                                      # (and you can have multiple BLUEPRINTS)

@app.route('/')
def home():                                                            # page without blueprint
    return '<h1>Home page without blueprints.</h1> <br> now put "/admin/" or "/admin/home" into url and you will see it! '

@app.route('/test/')
def test():
    return '<h1>Basic TEST page without blueprints.</h1>'



if __name__ == '__main__':
    app.run(debug=True)