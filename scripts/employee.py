class Employee:
    def __init__(self, first_name, last_name, role, email, salary_per_hour, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.email = email
        self.salary_per_hour = salary_per_hour
        self.job_title = job_title

    def __repr__(self):
        return f"{self.first_name} {self.last_name} - {self.role} ({self.email})"

    def calculate_pay(self, hours_worked):
        """
        This method takes in the number of hours worked and returns the amount the employee should be paid.
        """
        return self.salary_per_hour * hours_worked

    def full_name(self):
        return self.first_name + " " + self.last_name
