import PySimpleGUI as sg
#python -m PySimpleGUI.PySimpleGUI upgrade
sg.theme("DarkPurple2")
with open("highscores.txt") as myfile:
	textlines = myfile.readlines()
	
lines = [text.split(",") for text in textlines]
lines2 = []
for line in lines:
	new_line = [line[0].strip(), int(line[1].strip())]
	lines2.append(new_line)

lines2.sort(key=lambda x: x[1], reverse=True)

ranks = set([score for(nam, score) in lines2])
ranks = list(ranks)
ranks.sort(reverse=True)
rankdict = {}
for r,score in enumerate(ranks, 1):
	rankdict[score] = r
lines = []
for line in lines2:
	name, score = line
	rank = rankdict[score]
	lines.append([rank,name,score])


layout1 = [
	[sg.Text("Tower Defense Version 0.1")],
	[sg.Button("Play Tower Defense", size=(15,1))],
	[sg.Button("Settings", size=(15,1))],
	[sg.Button("Credits", size=(15,1))],
	[sg.Button("View Highscores", size=(15,1))],
	[sg.Button("Exit", size=(15,1))],
]

layout2 = [
	[sg.Text("Settings")],
	[sg.Text("Screen Resolution"), sg.Combo(["640x480","800x600","1024x800"], default_value = "1024x800", key="resolution")],
	[sg.Checkbox("Fullscreen", key="fullscreen")],
	[sg.Text("Sound Volume"), sg.Slider(range=(0, 100), default_value=50, resolution=1, orientation="h", key="sound")],
	[sg.Text("Music Volume"), sg.Slider(range=(0, 100), default_value=50, resolution=1, orientation="h", key="music")],
]

layout3 = [
	[sg.Image(filename="data/tuxconsole200.png")],
]

layout4 = [
	[sg.Table(lines, headings=["Rank", "Name", "Score"],
	 cols_justification = ["r","l","r"], col_widths = [5, 30, 8])],
]

layout5 = [
	[sg.Button("easy", size=(12,1))],
	[sg.Button("medium", size=(12,1))],
	[sg.Button("hard", size=(12,1))],
	[sg.Button("elite", size=(12,1))],
]

layout = [
	[sg.Column(layout1),
	 sg.Column(layout2, key="settingsmenu", visible=False),
	 sg.Column(layout3, key="creditsmenu", visible=False),
	 sg.Column(layout4, key="highscoremenu", visible=False),
	 sg.Column(layout5, key="playmenu", visible=False)],
	
	[sg.Text("(c) 2022 by Peter van der Linden")],
	[sg.Text("supported by https://spielend-programmieren.at (Horst JENS)")],
]

window = sg.Window("Tower Defense", layout )
difficulty = "easy"
while True:
	event, values = window.read()
	if event == "Exit":
		break
	if event == "Settings":
		window["settingsmenu"].update(visible = True)
		window["creditsmenu"].update(visible = False)
		window["highscoremenu"].update(visible = False)
		window["playmenu"].update(visible = False)
	if event == "Credits":
		window["creditsmenu"].update(visible = True)
		window["settingsmenu"].update(visible = False)
		window["highscoremenu"].update(visible = False)
		window["playmenu"].update(visible = False)
	if event == "View Highscores":
		window["highscoremenu"].update(visible = True)
		window["settingsmenu"].update(visible = False)
		window["creditsmenu"].update(visible = False)
		window["playmenu"].update(visible = False)
	if event == "Play Tower Defense":
		window["playmenu"].update(visible = True)
		window["settingsmenu"].update(visible = False)
		window["highscoremenu"].update(visible = False)
			
	#------- play untermenüpunkte--------------
	if event in ("easy", "medium", "hard", "elite"):
		difficulty = event
#values dict klonen
#my_values = {k:v for (k,v) in values.items()}	
my_values = values.copy()
my_values["difficulty"] = difficulty
print(my_values)
			
window.close()
