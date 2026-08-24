import unittest

from core.tasks import resolve_target_symbol


class TargetMatchingTests(unittest.TestCase):
    def test_matches_short_id_from_nickname(self):
        self.assertEqual(
            resolve_target_symbol(
                "好友昵称",
                ["904201732"],
                {"904201732": {"nickname": "好友昵称"}},
            ),
            "904201732",
        )

    def test_matches_short_id_from_remark_name(self):
        self.assertEqual(
            resolve_target_symbol(
                "聊天备注",
                ["1027821990"],
                {"1027821990": {"nickname": "原始昵称", "remark_name": "聊天备注"}},
            ),
            "1027821990",
        )

    def test_accepts_short_id_field_variants(self):
        self.assertEqual(
            resolve_target_symbol(
                "好友昵称",
                ["904201732"],
                {"internal-key": {"nickname": "好友昵称", "short_id": "904201732"}},
            ),
            "904201732",
        )


if __name__ == "__main__":
    unittest.main()
