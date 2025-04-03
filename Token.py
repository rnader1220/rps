
import tkinter as tk

class Token:
    def __init__(this, keystroke, label, beats, image):
        this.keystroke = keystroke
        this.label = label
        this.beats = beats
        this.prompt = str(f"({keystroke}):{label}")
        this.image = tk.PhotoImage(file=image)
        
    def test(this, compare):
        return compare == this.beats