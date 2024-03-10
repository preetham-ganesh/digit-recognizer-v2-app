from flask import Flask, redirect, send_from_directory


# Creates a flask application.
app = Flask(__name__)


@app.route("/send_image/")
def send_image():
    """Sends saved image from the directory using the filename.

    Args:
        None.

    Returns:
        A file based on the directory path & the file name.
    """
    return send_from_directory("data/in", "temp.png")


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
