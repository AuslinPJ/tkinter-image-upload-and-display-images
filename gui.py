
from tkinter import *
from tkinter import filedialog
# loading Python Imaging Library 
from PIL import ImageTk, Image 


class MyWindow:
	def __init__(self,win):
		self.button1=Button(win, text = "Browse Input Image",fg = "Black", padx=5, pady=5, bd=4, bg="Light Blue", command =self.display)
		self.button1.place(x=200,y=50)
		self.exitbutton=Button(win, text = "Exit",fg = "White", padx=5, pady=5, bd=4, bg="Red", command =win.quit)
		self.exitbutton.place(x=400,y=50)
		self.y_value=100
		self.x_value=100
		self.count=1

	def display(self):
		img,panel = self.fileopen()
	    
		# set the image as img  
		panel.image = img 

		# If number of images more than 4 exit the program
		if self.count == 5:
			exit()

		# x,y value for placing image in second row
		if self.x_value ==700:
			self.x_value=100
			self.y_value=300

		panel.place(x=self.x_value,y=self.y_value)
		self.x_value=self.x_value+300
		self.count=self.count+1

	def fileopen(self):
		# Select the Imagename  from a folder  
	    filename = filedialog.askopenfilename(title ='open', filetypes=(("PNGs", "*.png"),("JPGs", "*.jpg"), ("GIFs", "*.gif"), ("All Files", "*.")))
	  
	    # opens the image 
	    img = Image.open(filename) 
	      
	    # resize the image and apply a high-quality down sampling filter 
	    img = img.resize((150, 150), Image.ANTIALIAS) 
	  
	    # PhotoImage class is used to add image to widgets, icons etc 
	    img = ImageTk.PhotoImage(img) 
	   
	    # create a label 
	    panel = Label(window, image = img) 

	    return img,panel


window = Tk()
mywin=MyWindow(window)
window.title("Image upload")
window.configure(background="Grey")
window.geometry("800x600")
window.mainloop()
