import time 
import webbrowser

print("Hello and welcome to TAKE A BREAK program")
work_time = input("Please Enter Work Time >> (in minutes) : ")
break_time = input("Please Enter Break Time >>  (in minutes) : ")
how_many = input("How many times do you want to take the break! : ")

i = 1

while i <= how_many :
	print
	webbrowser.open("work.html")
	print("WORK >> Start time: " + time.ctime())
	time.sleep(work_time*60)
	print("WORK >> End time: " + time.ctime())
	webbrowser.open("break.html")
	print
	print("BREAK >> Start time: " + time.ctime())
	time.sleep(break_time*60)
	print("BREAK >> End time: " + time.ctime())
	
	i += 1

print
print("Thanks for using my program")