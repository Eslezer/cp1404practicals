from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        user_name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {user_name}"
        print(f"Greeting: Hello {user_name}")

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''
        print("Cleared input and label.")

BoxLayoutDemo().run()
