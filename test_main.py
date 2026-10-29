import unittest
from main import Applicant, Permit, PermitManagementSystem


class PermitManagementSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = PermitManagementSystem.create_demo_system()
        self.applicant = Applicant.from_reference("APP-900", "Test Applicant")
        self.permit = Permit(
            "PER-900", "Driving Licence", "Sample licence application.", self.applicant
        )

    def test_object_creation_and_interaction(self):
        self.system.add_application(self.permit)
        self.assertIn("PER-900", self.system.permits)
        self.assertIs(self.system.permits["PER-900"].applicant, self.applicant)

    def test_dictionary_is_the_record_collection(self):
        self.system.add_application(self.permit)
        self.assertIsInstance(self.system.permits, dict)
        self.assertEqual(len(self.system.permits), 3)

    def test_status_update(self):
        self.system.add_application(self.permit)
        self.system.update_application("PER-900", "Approved")
        self.assertEqual(self.permit.status, "Approved")

    def test_invalid_permit_type(self):
        bad = Permit("PER-901", "Passport", "Unsupported type.", self.applicant)
        with self.assertRaises(ValueError):
            self.system.add_application(bad)

    def test_duplicate_permit_id(self):
        self.system.add_application(self.permit)
        duplicate = Permit("PER-900", "Building Permit", "Duplicate.", self.applicant)
        with self.assertRaises(ValueError):
            self.system.add_application(duplicate)

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.permit.update_status("In Progress")


if __name__ == "__main__":
    unittest.main()
