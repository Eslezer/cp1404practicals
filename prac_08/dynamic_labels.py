"""
Dynamic Labels
A Kivy app that creates labels dynamically from a list of strings
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """main class"""

    def __init__(self, **kwargs):
        """initializing"""
        super().__init__(**kwargs)
        # list of strings
        self.names = ["Bob Blue", "Cat Cyan", "Oren Ochre", "Eduardo Eraser of worlds Eater of souls",
                      "Gina Green", "Samuel Sepia", "Yuri Yellow", "Zara Zinc"]

    def build(self):
        """Build the Kivy app from the kv file and add labels dynamically"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        # create and add labels
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


# running the app
if __name__ == '__main__':
    DynamicLabelsApp().run()