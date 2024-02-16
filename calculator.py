from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        # Define the layout
        layout = BoxLayout(orientation='vertical')

        # Add the display
        self.display = Button(text='0', font_size=24, size_hint=(1, 0.75))
        layout.add_widget(self.display)

        # Add buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=24, on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.display.text = str(eval(self.expression))
            except SyntaxError:
                self.display.text = 'Error'
            self.expression = ""
        else:
            self.expression += instance.text
            self.display.text = self.expression


if __name__ == '__main__':
    CalculatorApp().run()
