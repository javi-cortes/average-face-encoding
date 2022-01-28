from unittest import TestCase
from unittest.mock import patch

import numpy as np
from exceptions import NoUriProviden
from main import calculate_average_face_encoding
from main import obtain_image_face_encodings
from main import parallelize_face_encodings


class TryTesting(TestCase):
    def test_obtain_image_face_encodings_empty_uri(self):
        with self.assertRaises(NoUriProviden):
            obtain_image_face_encodings("")

    def test_obtain_image_face_encodings_uri_not_found(self):
        with self.assertRaises(FileNotFoundError):
            obtain_image_face_encodings("uri/that/doesnt/exists")

    @patch("main.IMAGE_DIRECTORY", "/path/that/doesnt/exist")
    def test_parallelize_face_encodings_directory_not_found(self):
        # this is not checked on the actual code but the actual
        # face_recognition library is raising the exception
        with self.assertRaises(FileNotFoundError):
            parallelize_face_encodings()

    @patch("main.obtain_image_face_encodings", return_value=[])
    @patch("os.listdir", return_value=[])
    def test_parallelize_face_encodings_empty_directory_encoding_not_called(
        self, listdir_mock, obtain_mock
    ):
        self.assertFalse(obtain_mock.called)

    def test_calculate_average_face_encoding_with_empty_encodings(self):
        self.assertIsNone(calculate_average_face_encoding([]))

    @patch("main.np.savetxt")
    def test_calculate_average_face_encoding_ensure_file_creation_called(
        self, mocked_np
    ):
        calculate_average_face_encoding(np.ndarray([1]))
        self.assertTrue(mocked_np.called)
