import unittest
from patient_record import build_linked_list, linked_list_to_list, merge_patient_records


class TestMergePatientRecords(unittest.TestCase):

    def test_normal_case_1(self):
        list1 = build_linked_list([
            (111, 25, "Alice"),
            (333, 40, "Charlie")
        ])

        list2 = build_linked_list([
            (222, 30, "Bob"),
            (444, 50, "David")
        ])

        merged = merge_patient_records(list1, list2)

        self.assertEqual(linked_list_to_list(merged), [
            (111, 25, "Alice"),
            (222, 30, "Bob"),
            (333, 40, "Charlie"),
            (444, 50, "David")
        ])

    def test_normal_case_2(self):
        list1 = build_linked_list([
            (100, 21, "A"),
            (200, 22, "B")
        ])

        list2 = build_linked_list([
            (150, 24, "C")
        ])

        merged = merge_patient_records(list1, list2)

        self.assertEqual(linked_list_to_list(merged), [
            (100, 21, "A"),
            (150, 24, "C"),
            (200, 22, "B")
        ])

    def test_normal_case_duplicate(self):
        list1 = build_linked_list([
            (111, 25, "Alice")
        ])

        list2 = build_linked_list([
            (111, 30, "Duplicate Alice")
        ])

        merged = merge_patient_records(list1, list2)

        self.assertEqual(linked_list_to_list(merged), [
            (111, 25, "Alice"),
            (111, 30, "Duplicate Alice")
        ])

    def test_edge_case_both_empty(self):
        merged = merge_patient_records(None, None)
        self.assertEqual(linked_list_to_list(merged), [])

    def test_edge_case_first_empty(self):
        list2 = build_linked_list([
            (500, 40, "Only Patient")
        ])

        merged = merge_patient_records(None, list2)

        self.assertEqual(linked_list_to_list(merged), [
            (500, 40, "Only Patient")
        ])

    def test_edge_case_second_empty(self):
        list1 = build_linked_list([
            (900, 60, "Single Patient")
        ])

        merged = merge_patient_records(list1, None)

        self.assertEqual(linked_list_to_list(merged), [
            (900, 60, "Single Patient")
        ])


if __name__ == "__main__":
    unittest.main()
