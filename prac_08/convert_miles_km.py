"""
Miles to Kilometers Converter
A Kivy app that converts miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometresApp(App):
    """ MilesToKilometresApp is a Kivy App for converting miles to kilometres """

    # StringProperty for the output label, will update automatically when changed
    output_km = StringProperty('0.0')

    # Conversion constant
    MILES_TO_KM = 1.60934

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ Calculate miles to km conversion based on input text """
        try:
            miles = float(text)
            self.output_km = str(miles * self.MILES_TO_KM)
        except ValueError:
            # Handle invalid input
            self.output_km = '0.0'

    def handle_increment(self, text, change):
        """ Handle up/down button press, changing the input value """
        try:
            # Try to convert the current value to a float
            value = float(text) + change
        except ValueError:
            # If the text isn't a valid number, start from 0
            value = 0 + change

        # Update the input field with the new value
        self.root.ids.input_miles.text = str(value)
        # Also update the result (instead of waiting for button press)
        self.handle_calculate(str(value))


# Create and run the app
if __name__ == '__main__':
    MilesToKilometresApp().run()