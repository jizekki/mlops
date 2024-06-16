import unittest
from boddle import boddle
from main import *
import json


class TestModel(unittest.TestCase):
    def test_supported_languages(self):
        with boddle():
            response = supported_languages()
            self.assertEqual(json.loads(response)[0], "fr-FR")

    def test_health_check(self):
        with boddle():
            response = health_check_endpoint()
            self.assertEqual(
                response.status_code, 200, "Error on returned status code"
            )

    def test_intent_inference(self):
        with boddle():
            self.assertRaises(KeyError, intent_inference)
        with boddle(query={"sentence": "Suggest a close hotel"}):
            response = intent_inference()
            values = json.loads(response)
            self.assertTupleEqual(
                tuple(values.keys()),
                (
                    "purchase",
                    "find-restaurant",
                    "irrelevant",
                    "find-hotel",
                    "provide-showtimes",
                    "find-around-me",
                    "find-train",
                    "find-flight",
                ),
            )


if __name__ == "__main__":
    unittest.main()
