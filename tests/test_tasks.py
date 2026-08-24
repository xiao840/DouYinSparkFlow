import unittest

import core.tasks as tasks


class FriendListScanTests(unittest.TestCase):
    def test_resets_empty_scroll_count_when_scroll_position_moves(self):
        self.assertTrue(hasattr(tasks, "next_empty_scroll_count"))
        self.assertEqual(tasks.next_empty_scroll_count(9, scroll_moved=True), 0)

    def test_increments_empty_scroll_count_when_scroll_position_stops(self):
        self.assertTrue(hasattr(tasks, "next_empty_scroll_count"))
        self.assertEqual(tasks.next_empty_scroll_count(2, scroll_moved=False), 3)


class SendMessageTests(unittest.TestCase):
    def test_send_message_confirms_enter_clears_composer(self):
        class FakePage:
            def wait_for_timeout(self, _):
                return None

            def locator(self, _):
                raise AssertionError("send button fallback should not be needed")

        class FakeInput:
            def __init__(self):
                self.value = ""
                self.pressed = []

            def click(self):
                return None

            def inner_text(self, timeout=1000):
                return self.value

            def text_content(self, timeout=1000):
                return self.value

            def type(self, value):
                self.value += value

            def press(self, key):
                self.pressed.append(key)
                if key == "Enter":
                    self.value = ""

        chat_input = FakeInput()
        tasks.send_message(FakePage(), chat_input, "🔥")
        self.assertIn("Enter", chat_input.pressed)

    def test_send_message_raises_when_composer_never_clears(self):
        class FakePage:
            def wait_for_timeout(self, _):
                return None

            def locator(self, _):
                return self

            def count(self):
                return 0

        class FakeInput:
            def click(self):
                return None

            def inner_text(self, timeout=1000):
                return "stuck"

            def text_content(self, timeout=1000):
                return "stuck"

            def type(self, _):
                return None

            def press(self, _):
                return None

        original_retries = tasks.config["taskRetryTimes"]
        tasks.config["taskRetryTimes"] = 1
        try:
            with self.assertRaises(RuntimeError):
                tasks.send_message(FakePage(), FakeInput(), "🔥")
        finally:
            tasks.config["taskRetryTimes"] = original_retries


if __name__ == "__main__":
    unittest.main()
