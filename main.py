"""
Digital Permit & License Management System
PROG211 - Object-Oriented Programming 1
Educational government-service prototype. Demonstration records are fictional.
The program stores multiple Permit objects in ONE collection: a dictionary.
"""

class Applicant:
    """Represents an applicant using a privacy-friendly reference code."""

    def __init__(self, applicant_id, display_name):
        self.applicant_id = applicant_id
        self.display_name = display_name

    def identify(self):
        """Return a display-safe applicant reference."""
        return f"{self.display_name} ({self.applicant_id})"

    @classmethod
    def from_reference(cls, applicant_id, display_name):
        """Alternative constructor for an Applicant object."""
        return cls(applicant_id, display_name)


class Permit:
    """Represents an application for a government permit or licence."""

    VALID_STATUSES = ("Submitted", "Under Review", "Approved", "Rejected", "Expired")
    VALID_TYPES = ("Business Permit", "Driving Licence", "Building Permit", "Trading Licence")

    def __init__(self, permit_id, permit_type, purpose, applicant):
        self.permit_id = permit_id
        self.permit_type = permit_type
        self.purpose = purpose
        self.applicant = applicant
        self.status = "Submitted"

    def update_status(self, new_status):
        """Update the application status only when the value is supported."""
        if new_status not in self.VALID_STATUSES:
            raise ValueError(
                "Invalid status. Choose Submitted, Under Review, Approved, Rejected, or Expired."
            )
        self.status = new_status

    def summary(self):
        """Return a readable summary of the permit application."""
        return (
            f"{self.permit_id} | {self.permit_type} | {self.status} | "
            f"{self.applicant.identify()} | {self.purpose}"
        )


class PermitManagementSystem:
    """Manages permit and licence applications for a government service desk."""

    ALLOWED_TYPES = Permit.VALID_TYPES

    def __init__(self, office_name):
        self.office_name = office_name
        # The program's only collection for storing multiple Permit objects.
        # Permit ID is the dictionary key; the value is a Permit object.
        self.permits = {}

    @staticmethod
    def valid_permit_type(permit_type):
        """Return True when the permit type is supported."""
        return permit_type in PermitManagementSystem.ALLOWED_TYPES

    def add_application(self, permit):
        """Validate and add a Permit object to the dictionary."""
        if not self.valid_permit_type(permit.permit_type):
            raise ValueError("Unsupported permit or licence type.")
        if permit.permit_id in self.permits:
            raise ValueError("Permit ID already exists.")
        self.permits[permit.permit_id] = permit

    def update_application(self, permit_id, new_status):
        """Find an application by ID and update its status."""
        if permit_id not in self.permits:
            raise KeyError("Permit ID was not found.")
        self.permits[permit_id].update_status(new_status)

    def display_applications(self):
        """Display all stored permit applications."""
        print(f"\n--- {self.office_name}: Permit & Licence Register ---")
        if not self.permits:
            print("No applications have been recorded.")
            return
        for permit in self.permits.values():
            print(permit.summary())

    @classmethod
    def create_demo_system(cls):
        """Create a system preloaded with fictional demonstration applications."""
        system = cls("Public Permits and Licensing Desk")
        applicant1 = Applicant.from_reference("APP-104", "Aminata Koroma")
        applicant2 = Applicant.from_reference("APP-219", "Daniel Bangura")
        permit1 = Permit(
            "PER-301", "Business Permit",
            "Application for a small community grocery shop.", applicant1
        )
        permit1.update_status("Under Review")
        permit2 = Permit(
            "PER-302", "Building Permit",
            "Application for a one-storey residential extension.", applicant2
        )
        system.add_application(permit1)
        system.add_application(permit2)
        return system


def interactive_mode():
    """Simple console interface for demonstrating the OOP classes."""
    system = PermitManagementSystem.create_demo_system()
    print("Digital Permit & Licence Management System")
    print("Commands: demo, add, show, update, exit")
    while True:
        choice = input("\nCommand (demo/add/show/update/exit): ").strip().lower()
        if choice == "demo":
            system = PermitManagementSystem.create_demo_system()
            system.display_applications()
        elif choice == "add":
            applicant_id = input("Applicant reference (e.g., APP-401): ").strip()
            display_name = input("Display name or alias: ").strip()
            permit_type = input(
                "Type (Business Permit/Driving Licence/Building Permit/Trading Licence): "
            ).strip()
            purpose = input("Application purpose: ").strip()
            permit_id = input("Permit ID (e.g., PER-401): ").strip()
            applicant = Applicant.from_reference(applicant_id, display_name)
            permit = Permit(permit_id, permit_type, purpose, applicant)
            try:
                system.add_application(permit)
                print("Application submitted successfully.")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "show":
            system.display_applications()
        elif choice == "update":
            permit_id = input("Permit ID: ").strip()
            status = input(
                "New status (Submitted/Under Review/Approved/Rejected/Expired): "
            ).strip()
            try:
                system.update_application(permit_id, status)
                print("Application status updated.")
            except (KeyError, ValueError) as error:
                print(f"Error: {error}")
        elif choice == "exit":
            print("Goodbye.")
            break
        else:
            print("Unknown command. Use demo, add, show, update, or exit.")


if __name__ == "__main__":
    interactive_mode()
