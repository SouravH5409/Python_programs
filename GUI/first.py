from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        '''Sets up the window and the widget'''
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",row =0, column =0, sticky = "NSEW")
        textLabel = self.addLabel(text = "A new day", row = 1, column = 0, sticky = "NSEW")

        self.image = PhotoImage(file = "download (1).png")
        imageLabel["image"] = self.image

        font = Font(family = "Helvetica", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["background"] = "yellow"