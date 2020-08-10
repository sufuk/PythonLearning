"""import tkinter
window = tkinter.Tk()
window.title("Recipe App PROSMH")
button_widget = tkinter.Button(window,text="Welcome to DataCamp's Tutorial on Tkinter")
button_widget.pack()
window.mainloop()
"""

class recipe:
  def __init__(self, partyname, partytype, wirenumber, yarnNE, yarntype,tub1tension, tub1temprature, tub1elangationrate, tub2tension, tub2temprature,tub2elangationrate,machinespeed):
    self.partyname = partyname
    self.partytype = partytype
    self.wirenumber = wirenumber
    self.yarnNE = yarnNE
    self.yarntype = yarntype
    self.tub1tension = tub1tension
    self.tub1temprature = tub1temprature
    self.tub1elangationrate = tub1elangationrate
    self.tub2tension = tub2tension
    self.tub2temprature = tub2temprature
    self.tub2elangationrate = tub2elangationrate
    self.machinespeed = machinespeed

p1 = recipe("John", "mehler", 3, "4/5", "cotton", 40, 32, 5.06, 50, 42, 3.006, 65)

f = open("demofile.txt", "r")
print(f.read())

"""
print(p1.partyname)
print(p1.partytype)
print(p1.wirenumber)
print(p1.yarnNE)
print(p1.yarntype)
print(p1.tub1tension)
print(p1.tub1temprature)
print(p1.tub1elangationrate)
print(p1.tub2tension)
print(p1.tub2temprature)
print(p1.tub2elangationrate)
print(p1.machinespeed)
"""
