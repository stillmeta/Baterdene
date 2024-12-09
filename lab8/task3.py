def assign_bikes(students, bikes):
    num_students = len(students)
    num_bikes = len(bikes)

    assignments = [-1] * num_students
    is_bike_assigned = [False] * num_bikes
    is_student_assigned = [False] * num_students
    distance_list = []

    for student_index in range(num_students):
        student_x, student_y = students[student_index]
        for bike_index in range(num_bikes):
            bike_x, bike_y = bikes[bike_index]
            manhattan_distance = abs(student_x - bike_x) + abs(student_y - bike_y)
            distance_list.append((manhattan_distance, student_index, bike_index))

    distance_list.sort()

    for distance, student_index, bike_index in distance_list:
        if not is_student_assigned[student_index] and not is_bike_assigned[bike_index]:
            assignments[student_index] = bike_index
            is_student_assigned[student_index] = True
            is_bike_assigned[bike_index] = True

            if all(is_student_assigned):
                break

    return assignments


import unittest

class TestAssignBikes(unittest.TestCase):
    def test_example(self):
        students = [(0, 0), (1, 1)]
        bikes = [(0, 1), (4, 3), (2, 1)]
        expected = [0, 2]
        self.assertEqual(assign_bikes(students, bikes), expected)

    def test_same_distance(self):
        students = [(0, 0), (0, 0)]
        bikes = [(1, 0), (2, 0)]
        expected = [0, 1]
        self.assertEqual(assign_bikes(students, bikes), expected)

    def test_more_bikes(self):
        students = [(0, 0)]
        bikes = [(1, 0), (2, 0), (3, 0)]
        expected = [0]
        self.assertEqual(assign_bikes(students, bikes), expected)

    def test_more_students(self):
        students = [(0, 0), (1, 1), (2, 0)]
        bikes = [(1, 0), (2, 2)]
        expected = [0, 1, -1]
        self.assertEqual(assign_bikes(students, bikes), expected)

    def test_no_students(self):
        students = []
        bikes = [(1, 0), (2, 0)]
        expected = []
        self.assertEqual(assign_bikes(students, bikes), expected)

if __name__ == "__main__":
    unittest.main()