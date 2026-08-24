import unittest

import core.tasks as tasks


class FriendListScanTests(unittest.TestCase):
    def test_resets_empty_scroll_count_when_scroll_position_moves(self):
        self.assertTrue(hasattr(tasks, "next_empty_scroll_count"))
        self.assertEqual(tasks.next_empty_scroll_count(9, scroll_moved=True), 0)

    def test_increments_empty_scroll_count_when_scroll_position_stops(self):
        self.assertTrue(hasattr(tasks, "next_empty_scroll_count"))
        self.assertEqual(tasks.next_empty_scroll_count(2, scroll_moved=False), 3)


if __name__ == "__main__":
    unittest.main()
