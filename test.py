from tkinter import *

# --- functions ---

def on_click():
    # change image on canvas
    canvas.itemconfig(image_id, image=image2)

# --- main ---

root = Tk()

# canvas for image
canvas = Canvas(root, width=60, height=60)
canvas.pack()

# button to change image
button = Button(root, text="Change", command=on_click)
button.pack()

# images
image1 = PhotoImage(file="/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")
image2 = PhotoImage(file="/Users/bradpaiva/Documents/Python/CNN/tmp/image2.jpg")

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=image1)

root.mainloop()