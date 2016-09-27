import Image
import ImageTk
from Tkinter import Tk, Label
import thread
import threading

class ImageHandler(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def exit(self):
        self.root.quit()
        
    def showImage(self, path):
        i = Image.open(path)
        photo = ImageTk.PhotoImage(i)
        self.label.configure(image = photo)
        self.label.image = photo

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.label = Label(self.root)
        self.label.pack()

        self.label.mainloop()


# app = ImageHandler()
# print('Now we can continue running code while mainloop runs!')
# 
# for i in range(4):
#     print(i)
#     app.showImage(raw_input("nextImage..."))
# 
# app.exit()