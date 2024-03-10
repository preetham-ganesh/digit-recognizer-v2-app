import os
import numpy as np
import cv2

from src.utils import load_json_file


class DigitRecognizer(object):
    """Recognizes digit in an image."""

    def __init__(self, model_version: str, model_api_url: str) -> None:
        """Creates object attributes for DigitRecognizer class.

        Creates object attributes for DigitRecognizer class.

        Args:
            model_version: A string for the version of the model.
            model_api_url: A string for the URL of the model's API.

        Returns:
            None.
        """
        # Asserts type of input arguments.
        assert isinstance(
            model_version, str
        ), "Variable model_version should be of type 'str'."
        assert isinstance(
            model_api_url, str
        ), "Variable model_api_url should be of type 'str'."

        # Initializes class variables.
        self.model_version = model_version
        self.model_api_url = model_api_url

    def load_model_configuration(self) -> None:
        """Loads the model configuration file for current version.

        Loads the model configuration file for current version.

        Args:
            None.

        Returns:
            None.
        """
        self.home_directory_path = os.getcwd()
        model_configuration_directory_path = (
            "{}/configs/models/digit_recognizer".format(self.home_directory_path)
        )
        self.model_configuration = load_json_file(
            "v{}".format(self.model_version), model_configuration_directory_path
        )

    def resize_image(self, image: np.ndarray) -> np.ndarray:
        """Resizes image based on final image height & width.

        Resizes image to (final_image_height, final_image_width, n_channels) shape.

        Args:
            image: A NumPy array for the input image.

        Returns:
            A NumPy array for the resized version of the input image.
        """
        # Checks type & values of arguments.
        assert isinstance(
            image, np.ndarray
        ), "Variable image should be of type 'np.ndarray'."

        # Resizes image based on final image height & width.
        resized_image = cv2.resize(
            image,
            (
                self.model_configuration["model"]["final_image_width"],
                self.model_configuration["model"]["final_image_height"],
            ),
        )
        return resized_image

    def load_preprocess_image(self, image_file_path: str) -> np.ndarray:
        """Loads & preprocesses image based on model requirements.

        Loads & preprocesses image based on model requirements.

        Args:
            image_file_path: A string for the location of the image.

        Returns: A NumPy array for the fully processed version of the image.
        """
        # Asserts type & value of the arguments.
        assert isinstance(
            image_file_path, str
        ), "Variable image_file_path should be of type 'str'."

        # Loads the image for the current image path.
        image = cv2.imread(image_file_path)

        # Gray scales image.
        gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resizes image to (final_image_height, final_image_width, n_channels).
        model_input_image = self.resize_image(gray_scale_image)

        # Casts input image to float32 and normalizes the image from [0, 255] range to [0, 1] range.
        model_input_image = model_input_image.astype(np.float32)
        model_input_image = model_input_image / 255.0

        # Adds extra dimension in axis 0 & 3.
        model_input_image = np.expand_dims(model_input_image, axis=0)
        model_input_image = np.expand_dims(model_input_image, axis=3)
        return model_input_image
