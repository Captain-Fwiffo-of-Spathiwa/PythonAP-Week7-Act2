import unittest
from unittest.mock import patch
from src.tasks import(
    add_task,
    mark_task_completed,
    delete_task,
    list_tasks,
    sort_tasks,
    binary_search
)


class TestTasks(unittest.TestCase):

    def setUp(self):
        """Create mock tasks list."""
        self.tasks = [("Walk dogs", False), ("Handmade Hero", False)]

    def tearDown(self):
        """Delete mock tasks list."""
        del self.tasks

    def test_add_task(self):
        """Test adding a task."""
        new_task_name = "Practice piano"
        expected_list = [("Walk dogs", False),
                         ("Handmade Hero", False),
                         ("Practice piano", False)]
        add_task(self.tasks, new_task_name)
        self.assertEqual(expected_list, self.tasks)

    # def test_add_invalid_task
    # def test_add_to_invalid_tasks

    # def test_mark_task_completed(self):
    #     """Test marking a task as completed."""
    #     expected_list = [("Walk dogs", True), ("Handmade Hero", True)]
    #     mark_task_completed(self.tasks, 0)
    #     mark_task_completed(self.tasks, 1)
    #     self.assertEqual(expected_list, self.tasks)

    # def test_mark_invalid_task_completed
    # def test_mark_task_completed_in_invalid_list
    # def text_mark_invalid_indexed_task_completed


if __name__ == ' __main__':
    unittest.main()