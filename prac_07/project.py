"""
CP1404/CP5632 Practical
Class for project management program
time estimate: 10 minutes
actual time: 15 minutes
"""

import datetime

class Project:
    """Represent a single project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if project is completed."""
        return self.completion_percentage == 100
