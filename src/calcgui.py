# usr/bin/python

# priority = [["("], ["!"],["^", "√"], ['-'], ["%", "/", "*"], ["-", "+"], [")"]]

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

kivy.require('2.1.0')

# for arranging widgets in a grid
from kivy.uix.gridlayout import GridLayout

# for the size of window
from kivy.config import Config

from kivy.lang import Builder

import calc

# Setting size to resizable
Config.set('graphics', 'resizable', 1)


# Creating Layout class
class CalcGridLayout(GridLayout):
    ERR = False

    # Function called when "=" is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(calc.eval_str(calculation))
            except Exception:
                self.display.text = "MATH ERROR"

    def help(self):
        self.display.text = "HELP"


# Creating App class
class CalculatorApp(App):

    def build(self):
        file = Builder.load_string("""
        # Custom button
<CustButton@Button>:
	font_size: 32

# Define id so I can refer to the CalcGridLayout
# class functions
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
			id: entry
			font_size: 32
			multiline: False
			focus: True
    
    BoxLayout:
		spacing: 10
		CustButton:
			text: "AC"
			on_press: entry.text = ""
			on_release: entry.focus = True
		CustButton:
			text: "DEL"
			on_press: entry.text = entry.text[:-1]
			on_release: entry.focus = True
		CustButton:
			text: "("
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: ")"
			on_press: calculator.calculate(entry.text)
			on_release: entry.focus = True
		CustButton:
			text: "%"
			on_press: entry.text += self.text
			on_release: entry.focus = True
			

	# When buttons are pressed update the entry
	BoxLayout:
		spacing: 10
		CustButton:
			text: "7"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "8"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "9"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "+"
			on_press: entry.text += self.text
			on_release: entry.focus = True
        CustButton:
			text: "-"
			on_press: entry.text += self.text
			on_release: entry.focus = True

	BoxLayout:
		spacing: 10
		CustButton:
			text: "4"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "5"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "6"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "*"
			on_press: entry.text += self.text
			on_release: entry.focus = True
        CustButton:
			text: "/"
			on_press: entry.text += self.text
			on_release: entry.focus = True

	BoxLayout:
		spacing: 10
		CustButton:
			text: "1"
			on_press: ifentry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "2"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "3"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "^"
			on_press: entry.text += self.text
			on_release: entry.focus = True
        CustButton:
			text: "√"
			on_press: entry.text += self.text
			on_release: entry.focus = True

	# When equals is pressed pass text in the entry
	# to the calculate function
	BoxLayout:
		spacing: 10
		CustButton:
			text: "!"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "0"
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "="
			on_press: calculator.calculate(entry.text)
			on_release: entry.focus = True
		CustButton:
			text: "."
			on_press: entry.text += self.text
			on_release: entry.focus = True
		CustButton:
			text: "HELP"
			on_press: calculator.help()
			on_release: entry.focus = True

""")
        return CalcGridLayout()


# creating object and running it
calcApp = CalculatorApp()
calcApp.run()
