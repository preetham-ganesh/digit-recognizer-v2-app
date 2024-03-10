from PIL import Image
import io

from flask import Flask, redirect, send_from_directory, request, render_template
import requests

from src.digit_recognizer import DigitRecognizer


# Creates a flask application.
app = Flask(__name__)

# Model Base URL for TF serving container.
models_base_url = "https://digit-recognizer-v2-serving-62b7e8d7d147.herokuapp.com"


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


@app.route("/upload", methods=["GET", "POST"])
def upload() -> str:
    """Renders template for upload. Predicts digit for uploaded image.

    Renders template for upload. Predicts digit for uploaded image.

    Args:
        None.

    Returns:
        A string for the rendered template for upload or complete.
    """
    # Checks if request method is POST, then predicts digit for uploaded image.
    if request.method == "POST":

        # Extract image from request.
        image_file = request.files["image"]

        # Read the content in the image as bytes.
        image_content = image_file.read()

        # Convert bytes to PIL images, & saves it as a PNG file.
        image = Image.open(io.BytesIO(image_content))
        image.save("data/in/temp.png")

        # Creates an object for the DigitRecognizer class.
        digit_recognition = DigitRecognizer(
            "1.0.0",
            "{}/v1/models/digit_recognizer_v1.0.0:predict".format(models_base_url),
        )

        # Loads & preprocesses image based on model requirements. Predicts digit recognized from image.
        output = digit_recognition.predict_digit("data/in/temp.png")

        # If status is success, then return the output to user.
        if output["status"] == "Success":
            return render_template(
                "output.html",
                digit=output["digit"],
                score=round(output["score"] * 100, 3),
            )

        else:
            return render_template("error.html", message=output["message"])

    # Else, renders the upload template.
    else:
        return render_template("upload.html")
