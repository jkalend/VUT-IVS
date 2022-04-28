#!usr/bin/python


import os
# import kivy module
import kivy
# import calculator math library
import calc
import webbrowser

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# for arranging widgets in a grid
from kivy.uix.gridlayout import GridLayout

# for the size of window
from kivy.config import Config
from kivy.lang import Builder

kivy.require('2.1.0')

# Setting size to resizable
Config.set('graphics', 'resizable', 1)
Config.set('kivy', 'window_icon', os.path.dirname(os.path.abspath(__file__)) + 'button.png')


# Creating Layout class
class CalcGridLayout(GridLayout):
    # variable indicating whether to clear the display or not
    ERR = False

    path = os.path.dirname(os.path.abspath(__file__)) + '/../dokumentace.pdf'

    # Function called when "=" is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(calc.eval_str(calculation))
            except TypeError:
                self.display.text = "INVALID INPUT"
                self.ERR = True
            except ValueError:
                self.display.text = "MATH ERROR"
                self.ERR = True
            except IndexError:
                self.display.text = "INVALID INPUT"
                self.ERR = True

    # Function called when "AC" button is pressed
    def clear(self):
        self.display.text = ""
        self.ERR = False

    # Function called when "HELP" button is pressed
    def help(self):
        self.clear()
        webbrowser.open(self.path)

    # Function called when "DEL" button is pressed
    def delete(self):
        if self.ERR:
            self.clear()
        else:
            self.display.text = self.display.text[:-1]

    # Function handling the input of numbers and operators
    def enter(self, text):
        if self.ERR:
            self.display.text = text
            self.ERR = False
        else:
            self.display.text += text


# background_color: 0.851, 0.48627, 0, 1
# Creating App class
class CalculatorApp(App):
    title = "Supreme Calc"

    def build(self):
        self.icon = "button.png"
        file = Builder.load_string("""
# Custom button
<CalcButton@Button>:
    background_color: 0, 0.5411, 0.847, 0.7
    font_size: 36

    # Defining id of the grid layout
    # Display points to the entry widget
<CalcGridLayout>:
    id: calculator
    display: entry
    rows: 6
    padding: 10
    spacing: 10



    # Where input is displayed
    BoxLayout:
        TextInput:
            cursor_width: 2 
            background_color: 0, 0.48627, 0.489, 1
            id: entry
            font_size: 56
            multiline: False
            on_text_validate: calculator.calculate(entry.text)
            text_validate_unfocus: False
            focus: True

    # First row of buttons          
    BoxLayout:
        spacing: 10
        CalcButton:
            background_color: 1, 0, 0, 0.85
            text: "AC"
            on_press: calculator.clear()
            on_release: entry.focus = True
        CalcButton:
            background_color: 1, 0, 0, 0.85
            text: "DEL"
            on_press: calculator.delete()
            on_release: entry.focus = True
        CalcButton:
            text: "("
            on_press: calculator.enter("(")
            on_release: entry.focus = True
        CalcButton:
            text: ")"
            on_press: calculator.enter(")")
            on_release: entry.focus = True
        CalcButton:
            text: "%"
            on_press: calculator.enter("%")
            on_release: entry.focus = True

    # Second row of buttons
    BoxLayout:
        spacing: 10
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "7"
            on_press: calculator.enter("7")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "8"
            on_press: calculator.enter("8")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "9"
            on_press: calculator.enter("9")
            on_release: entry.focus = True
        CalcButton:
            text: "+"
            on_press: calculator.enter("+")
            on_release: entry.focus = True
        CalcButton:
            text: "-"
            on_press: calculator.enter("-")
            on_release: entry.focus = True

    # Third row of buttons
    BoxLayout:
        spacing: 10
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "4"
            on_press: calculator.enter("4")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "5"
            on_press: calculator.enter("5")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "6"
            on_press: calculator.enter("6")
            on_release: entry.focus = True
        CalcButton:
            text: "*"
            on_press: calculator.enter("*")
            on_release: entry.focus = True
        CalcButton:
            text: "/"
            on_press: calculator.enter("/")
            on_release: entry.focus = True

    # Fourth row of buttons
    BoxLayout:
        spacing: 10
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "1"
            on_press: calculator.enter("1")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "2"
            on_press: calculator.enter("2")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "3"
            on_press: calculator.enter("3")
            on_release: entry.focus = True
        CalcButton:
            text: "^"
            on_press: calculator.enter("^")
            on_release: entry.focus = True
        CalcButton:
            text: "√"
            on_press: calculator.enter("√")
            on_release: entry.focus = True

    # Fifth row of buttons
    # When equals is pressed pass text in the entry
    # to the calculate function
    BoxLayout:
        spacing: 10
        CalcButton:
            text: "!"
            on_press: calculator.enter("!")
            on_release: entry.focus = True
        CalcButton:
            background_color: 0, 0.5411, 0.847, 0.9
            text: "0"
            on_press: calculator.enter("0")
            on_release: entry.focus = True
        CalcButton:
            text: "="
            on_press: calculator.calculate(entry.text)
            on_release: entry.focus = True
        CalcButton:
            text: "."
            on_press: calculator.enter(".")
            on_release: entry.focus = True
        CalcButton:
            background_color: 1, 1, 1, 0.5
            text: "HELP"
            on_press: calculator.help()
            on_release: entry.focus = True

""")
        return CalcGridLayout()


# Create the App and load the kv file
# The kv file is a python file that contains the
# definition of the widgets and the layout of the app
# The kv file is loaded by the Builder.
# The Builder loads the kv file and creates the widgets
# and the layout of the app.


# GUI is run only if this file is run directly
if __name__ == '__main__':
    # creating object and running it
    calcApp = CalculatorApp()
    calcApp.run()
