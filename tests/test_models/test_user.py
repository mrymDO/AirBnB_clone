#!/user/bin/python3
"""Unittest User class"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """test class User"""
    def setUp(self):
        """setUp users"""
        self.user1 = User()
        self.user1.first_name = "Betty"
        self.user1.last_name = "Bar"
        self.user1.email = "airbnb@mail.com"
        self.user1.password = "root"
        self.user1.save()

        self.user2 = User()
        self.user2.first_name = "John"
        self.user2.email = "airbnb2@mail.com"
        self.user2.password = "root"
        self.user2.save()

    def test_user_creation(self):
        """test user creation"""
        all_objs = storage.all()
        user = User()

        self.assertIn(f"User.{self.user1.id}", all_objs.keys())
        self.assertIn(f"User.{self.user2.id}", all_objs.keys())

        self.assertNotEqual(self.user1.id, self.user2.id)

        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

        expected_attributes = ["email", "password", "first_name", "last_name"]
        for attribute in expected_attributes:
            self.assertTrue(hasattr(user, attribute))
            self.assertEqual(getattr(user, attribute), "")

    def test_user_str_repre(self):
        """test string representation"""
        user_str = str(self.user1)

        expected_output = "[User] ({}) {}".format(
                self.user1.id, self.user1.__dict__)
        self.assertEqual(user_str, expected_output)

    def test_user_to_dict(self):
        """test to_dict method"""
        user = User()
        new_dict = user.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

        expected_attributes = ["email", "password", "first_name", "last_name"]
        for attribute in expected_attributes:
            self.assertTrue(attribute in User.__dict__)

        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], user.created_at.isoformat())


if __name__ == "__main__":
    unittest.main()
