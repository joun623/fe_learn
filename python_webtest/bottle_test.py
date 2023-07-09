from bottle import route, run

@route('/')
def home():
    return "It isn't nancy, but it's my home page"

@route('/echo/<thing>')
def echo(thing):
    return  "say hello to my little friend: %s!" % thing

run(host="localhost", port=9999, reloader=True)
