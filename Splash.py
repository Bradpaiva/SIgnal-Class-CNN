from SignalGen import *
# from SignalRCNN import *
from SignalCNN import *
from SignalNN import *
from SpecDatasetFolders import *
from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
from PIL import ImageTk,Image  


Height =500
Width =400


# creating a new tkinter window
master = Tk()

# assigning a title
master.title("Singal Modulation CNN")

# specifying geometry for window size
master.geometry(str(Width)+"x"+str(Height))


# function to display the total subject
# credits total credits and SGPA according
# to grades entered
def roundHZ(value):
	if value>100:
		value=round(value,-1)
	if value>1000:
		value=round(value,-2)
	if value>10000:
		value=round(value,-3)
	if value>100000:
		value=round(value,-4)
	if value>1000000:
		value=round(value,-5)
	return value

def displayHZ(value):
	if (value>=1000000):
		return (str(value/1000000)+"MHz")
	if (value>=1000):
		return (str(value/1000)+"kHz")
	else:
		return (str(value)+"Hz")

def display():
	print("CNN")

def Exit():
	master.destroy()
	return

def NoiseSet(value):
	value = (float(value))
	selection = "Value = " + str(round(value,3))
	label2.config(text = selection)
	c.NoiseRatio=round(value,3)
	noiseratio.set(value)

def FminSet(value):
	value = int(float(value))
	value = roundHZ(value)
	if(value>c.CarrierFreqMax):
		FmaxSet(value)
	hertz=displayHZ(value)
	selection = "Value = " + str(hertz)
	label4.config(text = selection)
	c.CarrierFreqMin=value
	Fmin.set(value)

def FmaxSet(value):
	value = int(float(value))
	value= roundHZ(value)
	if value*2>c.SamplingFrequency:
		#value = c.SamplingFrequency/2
		SampFset(value*2)
	if(value<c.CarrierFreqMin):
		# value=c.CarrierFreqMin
		FminSet(value)
	hertz=displayHZ(value)
	selection = "Value = " + str(hertz)
	label6.config(text = selection)
	c.CarrierFreqMax=int(value)
	Fmax.set(value)

def totaltset(value):
	value = int(float(value))
	selection = "Value = " + str(value) +"s"
	label8.config(text = selection)
	c.TotalTime=int(value)
	totalt.set(value)

def SampFset(value):
	value = int(float(value))
	if value-value%c.BinaryFrequency >c.BinaryFrequency:
		value = value-value%c.BinaryFrequency
	else:
		value = c.BinaryFrequency
	if (c.CarrierFreqMax*2>value):
		FmaxSet(value/2)
	hertz=displayHZ(value)
	selection = "Value = " + str(hertz)
	label10.config(text = selection)
	c.SamplingFrequency=value
	SampF.set(value)

def BinFset(value):
	value = int(float(value))
	if(value>c.SamplingFrequency):
		value=c.SamplingFrequency
	while (c.SamplingFrequency/value%1>0):
		value=value-1
	hertz=displayHZ(value)
	selection = "Value = " + str(hertz)
	label12.config(text = selection)
	c.BinaryFrequency=value
	BinF.set(value)

def reset():
	FminSet(500)
	FmaxSet(1500)
	NoiseSet(.15)
	totaltset(2)
	SampFset(3000)
	BinFset(100)



SpecOption = IntVar() 
global img
def SpecOpt1():
	SpecOption.set(1)
def SpecOpt2():
	SpecOption.set(2)
def Test():
	def GenAM():
		plot.clf()
		Signal ,t, SamplingFrequency= RanAMSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenFM():
		plot.clf()
		Signal ,t, SamplingFrequency= RanFMSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenASK():
		plot.clf()
		Signal ,t, SamplingFrequency= RanASKSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenFSK():
		plot.clf()
		Signal ,t, SamplingFrequency= RanFSKSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenPSK():
		plot.clf()
		Signal ,t, SamplingFrequency= RanPSKSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenQPSK():
		plot.clf()
		Signal ,t, SamplingFrequency= RanQPSKSignal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img
	def GenQAM16():
		plot.clf()
		Signal ,t, SamplingFrequency= RanQAM16Signal()
		if (int(SpecOption.get()) ==1):
			plot.plot(t,Signal)
			plot.savefig('tmp/image.jpg')
		elif (int(SpecOption.get()) ==2):
			plot.specgram(Signal,c.SamplingFrequency)
			plot.savefig('tmp/image.jpg')
		img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/image.jpg")) 
		imglabel.configure(image=img)
		imglabel.image=img

	spacing = 3
	test = Toplevel()
	test.title("Signal Generator")
	
	imglabel = Label(test)  
	imglabel.pack(fill="both", expand=True)
	img = ImageTk.PhotoImage(Image.open("/Users/bradpaiva/Documents/Python/CNN/tmp/Home.png")) 
	imglabel.configure(image=img)


	frame1 = Frame(test)
	frame1.pack()

	RBttn = Radiobutton(frame1, text = "X and Y Plot", value = 1, variable = SpecOption,command=SpecOpt1)
	RBttn.pack(side="left", fill="x")

	RBttn2 = Radiobutton(frame1, text = "Specotgram", value = 2, variable = SpecOption,command=SpecOpt2)
	RBttn2.pack(side="left", fill="both", expand=True)

	frame2 = Frame(test)
	frame2.pack()

	button1=Button(frame2, text="AM", style='W.TButton', command=GenAM)
	button1.pack(side="left", fill="both", expand=True)

	button1=Button(frame2, text="FM", style='W.TButton', command=GenFM)
	button1.pack(side="left", fill="both", expand=True)

	button1=Button(frame2, text="ASK", style='W.TButton', command=GenASK)
	button1.pack(side="left",fill="both", expand=True)

	frame3 = Frame(test)
	frame3.pack()

	button1=Button(frame3, text="FSK", style='W.TButton', command=GenFSK)
	button1.pack(side="left", fill="both", expand=True)

	button1=Button(frame3, text="PSK", style='W.TButton', command=GenPSK)
	button1.pack(side="left", fill="both", expand=True)

	button1=Button(frame3, text="QPSK", style='W.TButton', command=GenQPSK)
	button1.pack(side="left", fill="both", expand=True)

	button1=Button(frame3, text="QAM16", style='W.TButton', command=GenQAM16)
	button1.pack(side="left", fill="both", expand=True)

	test.mainloop()


#Create style object
#Create style object
# sto = Style()

#configure style
# sto.configure('W.TButton', font= ('Helvetica', 18),foreground='Blue')

	
button1=Button(master, text="Run Neural Network", style='W.TButton', command=RunNN)
button1.grid(row=0, column=0,sticky="nsew")

button1=Button(master, text="Run Convolution NN", style='W.TButton', command=RunCNN)
button1.grid(row=3, column=0,sticky="nsew")

button1=Button(master, text="Generate Sample Frames", style='W.TButton', command=SpecDatasetGen)
button1.grid(row=6, column=0,sticky="nsew")

button1=Button(master, text="Concurrent Sample Frames", style='W.TButton', command=display)
button1.grid(row=9, column=0,sticky="nsew")

button1=Button(master, text="Test Signal Generator", style='W.TButton', command=Test)
button1.grid(row=12, column=0,sticky="nsew")

button1=Button(master, text="Exit", style='W.TButton', command=Exit)
button1.grid(row=80, column=0,sticky="nsew")

# 
# 
sliderstart = 20
spacing = 3
noiseratio = DoubleVar()


reset = Button(master, text="reset", command=reset)
reset.grid(row=sliderstart, column=2)


label1 = Label(master, text="NoiseRatio")
label1.grid(row=sliderstart, column=0)
scale1 = Scale(master, from_=0, to=1,variable = noiseratio ,orient=HORIZONTAL, command= NoiseSet)
scale1.grid(row=sliderstart+spacing, column=0)
label2 = Label(master)
label2.grid(row=sliderstart+spacing, column=2)
noiseratio.set(.15)
selection = "Value = " + str((noiseratio.get()))
label2.config(text = selection)


Fmin = IntVar()

label3 = Label(master, text="Minimum Frequency")
label3.grid(row=sliderstart+2*spacing, column=0)
scale2 = Scale(master, from_=50, to=50000000,variable = Fmin,orient=HORIZONTAL, command=FminSet)
scale2.grid(row=sliderstart+3*spacing, column=0)
label4 = Label(master)
label4.grid(row=sliderstart+3*spacing, column=2)
Fmin.set(500)
selection = "Value = " + str(int(Fmin.get()))+"hz"
label4.config(text = selection)

Fmax = DoubleVar()

label5 = Label(master, text="Maximum Frequency")
label5.grid(row=sliderstart+4*spacing, column=0)
scale3 = Scale(master, from_=50, to=50000000,variable = Fmax,orient=HORIZONTAL, command=FmaxSet)
scale3.grid(row=sliderstart+5*spacing, column=0)
label6 = Label(master)
label6.grid(row=sliderstart+5*spacing, column=2)
Fmax.set(1500)
selection = "Value = " + str(int(Fmax.get()))+"hz"
label6.config(text = selection)


totalt = DoubleVar()

label7 = Label(master, text="Total Time")
label7.grid(row=sliderstart+6*spacing, column=0)
scale4 = Scale(master, from_=1, to=30,variable = totalt,orient=HORIZONTAL, command=totaltset)
scale4.grid(row=sliderstart+7*spacing, column=0)
label8 = Label(master)
label8.grid(row=sliderstart+7*spacing, column=2)
totalt.set(2)
selection = "Value = " + str(int(totalt.get()))+"s"
label8.config(text = selection)

SampF = IntVar()

label9 = Label(master, text="Sampling Frequency")
label9.grid(row=sliderstart+8*spacing, column=0)
scale5 = Scale(master, from_=1000, to=100000000,variable = SampF,orient=HORIZONTAL, command = SampFset)
scale5.grid(row=sliderstart+9*spacing, column=0)
label10 = Label(master)
label10.grid(row=sliderstart+9*spacing, column=2)
SampF.set(3000)
selection = "Value = " + str(int(SampF.get()))+"hz"
label10.config(text = selection)

BinF = IntVar()

label11 = Label(master, text="Binary Frequency")
label11.grid(row=sliderstart+10*spacing, column=0)
scale6 = Scale(master, from_=1, to=10000,variable = BinF,orient=HORIZONTAL, command = BinFset)
scale6.grid(row=sliderstart+11*spacing, column=0)
label12 = Label(master)
label12.grid(row=sliderstart+11*spacing, column=2)
BinF.set(100)
selection = "Value = " + str(int(BinF.get()))+"hz"
label12.config(text = selection)


master.mainloop()


