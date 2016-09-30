from PIL import Image
from PIL import ImageTk
from Tkinter import Tk, Label
import threading


class ImageHandler(threading.Thread):
    """Class in charge of displaying images on the screen in a presentation-like fashion

    Inherits from threading.Thread

    """

    def __init__(self):
        """ Initiates a new instance of the ImageHandler type.

        This method automatically starts the instance as a new thread.
        """

        threading.Thread.__init__(self)
        self.start()

    def exit(self):
        """ Closes the thread and the window with the images.

        """

        self.root.quit()
        
    def showImage(self, path):
        """ Shows an image in the predefined window of the instance

        Args:
            path: The path to the image to be displayed.
        """
        i = Image.open(path)
        photo = ImageTk.PhotoImage(i)
        self.label.configure(image = photo)
        self.label.image = photo

    def run(self):
        """ Runs the thread and the window for the images.

        """
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.label = Label(self.root)
        self.label.pack()

        self.label.mainloop()
