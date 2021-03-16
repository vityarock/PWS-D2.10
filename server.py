
import sentry_sdk
import os
from bottle import route, run, error
from sentry_sdk.integrations.bottle import BottleIntegration
from sentry_sdk import capture_exception, capture_message

sentry_sdk.init(dsn="https://8658c9f1ce404fb28fd7c01a9dd66897@o552959.ingest.sentry.io/5679508", integrations = [BottleIntegration()])

@route("/")
def default_page():
    pass

@route("/success")
def success():
    pass

@route("/fail")
def fail():
    capture_message("something error")
    return RuntimeError

@route("/raise")
def crash():
    raise Exception


@error(404)
def error404(error):
    capture_message("NonExistPage request")
    return 'Nothing interesting here'


try:
    if os.environ.get("APP_LOCATION") == "heroku":
        run(
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
            server="gunicorn",
            workers=3,
        )
    else:
        run(host="localhost", port=8080, debug=True)
except Exception as e:
    capture_exception(e)
