from ImageHandler import ImageHandler

gui = ImageHandler()
print('Now we can continue running code while gui runs!')
 
for i in range(4):
    print(i)
    gui.showImage(raw_input("nextImage..."))
 
gui.exit()