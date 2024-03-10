from flask import Flask, redirect


# Creates a flask application.
app = Flask(__name__)


@app.route("/")
def index():
    """Redirects to upload page.

    Redirects to upload page.

    Args:
        None.

    Returns:
        A response for the redirected upload page.
    """
    return redirect("/upload")
