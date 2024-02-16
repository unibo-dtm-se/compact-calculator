from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


BUTTONS_NAMES = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+'],
]


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        grid = BoxLayout(orientation='vertical')

        self.display = Label(text='0', font_size=24, size_hint=(1, 0.75))
        grid.add_widget(self.display)

        for button_names_row in BUTTONS_NAMES:
            grid_row = BoxLayout()
            for button_name in button_names_row:
                button = Button(text=button_name, font_size=24, on_press=self.on_button_press)
                grid_row.add_widget(button)
            grid.add_widget(grid_row)

        return grid

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
