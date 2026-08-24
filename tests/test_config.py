import json
import os
import unittest
from unittest.mock import patch

from utils import config


class UserDataConfigTests(unittest.TestCase):
    def setUp(self):
        config.userData = None

    def tearDown(self):
        config.userData = None

    def test_accepts_a_single_task_object(self):
        task = {
            "username": "account",
            "unique_id": "123",
            "targets": ["456"],
        }
        cookies = json.dumps([{"name": "sessionid", "value": "value"}])

        with patch.dict(
            os.environ,
            {"TASKS": json.dumps(task), "COOKIES_123": cookies},
            clear=False,
        ):
            self.assertEqual(
                config.get_userData(),
                [
                    {
                        "unique_id": "123",
                        "username": "account",
                        "cookies": json.loads(cookies),
                        "targets": ["456"],
                    }
                ],
            )


if __name__ == "__main__":
    unittest.main()
