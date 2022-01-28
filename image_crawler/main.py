import logging
import os
from multiprocessing import Pool
from time import time
from typing import List, Optional

import face_recognition
import numpy as np

from exceptions import NoUriProviden

logging.basicConfig(level=logging.INFO)


def obtain_image_face_encodings(img_uri: str) -> List[np.ndarray]:
    """
    Calculates the face encoding from a given URI image.
    :param img_uri: path to the image
    :return: return the 128-dimension face encoding for each face in the image
    """
    if not img_uri:
        raise NoUriProviden()

    img = face_recognition.load_image_file(img_uri)
    return face_recognition.face_encodings(img)


IMAGE_DIRECTORY = "image_set/full/"
RESULT_FILENAME = "average_face_encodings.txt"


def parallelize_face_encodings() -> List[List[np.ndarray]]:
    """
    Parallelize the face encoding calculation in order to speed up the process.

    Extracting the face encoding is CPU heavy so multiprocessing is one way to
    speed up the process and a work around the GIL.

    :return: encoding lists
    """
    with Pool() as p:
        encodings = p.map(
            obtain_image_face_encodings,
            [IMAGE_DIRECTORY + directory for directory in os.listdir(IMAGE_DIRECTORY)],
        )

    return encodings


def calculate_average_face_encoding(
    face_encodings: List[List[np.ndarray]],
) -> Optional[np.ndarray]:
    """
    Calculates the average face encodings with numpy.mean() method.
    :param face_encodings: List of image face encodings
    """
    if not face_encodings:
        return None

    average_face_encodings = np.mean(np.array(face_encodings, dtype=object), axis=0)
    logging.info(f"Average face encodings:\n {average_face_encodings}")

    np.savetxt(RESULT_FILENAME, average_face_encodings)
    logging.info(f"Results stored at: {RESULT_FILENAME}")

    return average_face_encodings


if __name__ == "__main__":
    ts = time()
    encodings = parallelize_face_encodings()
    calculate_average_face_encoding(encodings)
    te = time()
    logging.info(f"Average face encoding calculated in: {te - ts:.2f} seconds")
