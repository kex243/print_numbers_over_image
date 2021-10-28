import os
import csv
import random

print ("Enter first number to print:")
first_number = int(input())
print ("Enter last number to print:")
last_number = int(input())
print ("Font size:")
font_size = int(input())
print ("Font: default will be 'arial', test any other that your system supports. Use '-' for two-words names: 'Courier-New' eg.")
font = input()
if font =="":
    font ='arial'
print ("Color: default will be 'random', - it will be all colors from the 'color_dictionary.csv' file. You can pick and add your colors from the link (bottom scrolling list): https://imagemagick.org/script/color.php ")
color = input()
if color =="":
    color ='random'
if color == "random":
    with open('color_dictionary.csv',encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        color_dictionary = list(csv_reader)
    print (color_dictionary)
    
print ("Horizontal displacement in pixels: (format must contain '+' or '-' : +100, -250) If empty- will be +0 (center)")
hor_displ = input()
if hor_displ == '':
    hor_displ='+0'
print ("vertical offset in pixels: ( same for horizontal:format must contain '+' or '-' : +100, -250)")
ver_displ = input()
if ver_displ == '':
    ver_displ='+0'

for x in range(first_number,last_number+1):
    print(x)
    #full_command = "-font "+ "arial" + " -fill "+ "white" + " -pointsize " + "60" + " -gravity center -draw " + '"text ' + "0"+","+"300" + " '" + "TEXT TO BE DISPLAYED" +"'"+'" ' + " '1.jpg' '/output/"+ str(x) +".jpg'"
    if color == 'random':
        color_used = random.choice(color_dictionary)
    else:
        color_used = color
    full_command = "1.jpg -gravity center -pointsize " + str(font_size)+" -font "+font+ " -fill "+ str(str(color_used)[2:-2]) + " -annotate " +hor_displ + ver_displ + " " +str(x) +" " +"output/" +  str(x) +".jpg" 
    print (full_command)
    command = "magick " + full_command
    print (command)
    os.system( command )