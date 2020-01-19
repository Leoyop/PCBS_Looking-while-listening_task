# This program runs only with the two folders 'sounds' and 'pictures' containing the audio and visual stimuli for the experiment
import os
import expyriment
from random import randint
import matplotlib.pyplot as plt

""" data analysis part, create histogram for the participant accuracy and its mean reaction time for each of the eight items """

#accuracy function 
def Trueinstances(tab):
    res = 0
    for case in tab:
        if case[1] == "True":
            res += 1
    return res

#Generate accuracy histogram
def AccuracyPlot(tab):
    plt.bar([0, 1], [Trueinstances(tab), len(tab) - Trueinstances(tab)], tick_label=["True", "False"])
    plt.show()

#compute the mean rt for two trials of a target word
def moyenne(tab, string):
    a = 0
    b = 0
    long = 1
 
    for case in tab:
        if case[0] == string and a == 0:
            a = case[2]
        elif case[0] == string and a != 0:
            b = case[2]
            long = 2
 
    return (a+b)/long

# mean reaction time for each target-words + histogram
def RTplot(tab):
    couche = moyenne(tab, 'ELLE_OÙ_COUCHE.wav')
    main = moyenne(tab, 'ELLE_OÙ_MAIN.wav')
    voiture = moyenne(tab, 'ELLE_OÙ_VOITURE.wav')
    ballon = moyenne(tab, 'IL_OÙ_BALLON.wav')
    biberon = moyenne(tab, 'IL_OÙ_BIBERON.wav')
    livre = moyenne(tab, 'IL_OÙ_LIVRE.wav')
    nez = moyenne(tab, 'IL_OÙ_NEZ.wav')
    pied = moyenne(tab, 'IL_OÙ_PIED.wav')
 
    plt.bar([0, 1, 2, 3, 4, 5, 6, 7], [couche, main, voiture, ballon, biberon, livre, nez, pied], tick_label=["Couche", "Main", "Voiture", "Ballon", "Biberon", "Livre", "Nez", "Pied"])
    plt.show()



""" End of data analysis """
 
 
# Matrix (16x4) of each trial in the task. It contains stimuli (sounds and pictures) and the target picture (1 or 2)
tableau = [[os.path.join("sounds", "ELLE_OÙ_COUCHE.wav"), os.path.join("pictures","couche.jpg"), os.path.join("pictures", "main.jpg"), 1], 
[os.path.join("sounds", "ELLE_OÙ_COUCHE.wav"), os.path.join("pictures", "couche.jpg"), os.path.join("pictures", "main.jpg"), 1], 
[os.path.join("sounds", "ELLE_OÙ_VOITURE.wav"), os.path.join("pictures","voiture.jpg"), os.path.join("pictures","balle.jpg"), 1], 
[os.path.join("sounds", "ELLE_OÙ_VOITURE.wav"), os.path.join("pictures","voiture.jpg"), os.path.join("pictures","balle.jpg"), 1], 
[os.path.join("sounds", "IL_OÙ_BIBERON.wav"), os.path.join("pictures", "biberon.jpg"), os.path.join("pictures", "livre.jpg"), 1], 
[os.path.join("sounds","IL_OÙ_BIBERON.wav"), os.path.join("pictures", "biberon.jpg"), os.path.join("pictures", "livre.jpg"), 1], 
[os.path.join("sounds","IL_OÙ_NEZ.wav"), os.path.join("pictures", "nez.jpg"), os.path.join("pictures", "pied.jpg"), 1], 
[os.path.join("sounds", "IL_OÙ_NEZ.wav"), os.path.join("pictures", "nez.jpg"), os.path.join("pictures", "pied.jpg"), 1], 
[os.path.join("sounds", "ELLE_OÙ_MAIN.wav"), os.path.join("pictures", "couche.jpg"), os.path.join("pictures", "main.jpg"), 2], 
[os.path.join("sounds", "ELLE_OÙ_MAIN.wav"), os.path.join("pictures", "couche.jpg"), os.path.join("pictures", "main.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_BALLON.wav"), os.path.join("pictures", "voiture.jpg"), os.path.join("pictures", "balle.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_BALLON.wav"), os.path.join("pictures", "voiture.jpg"), os.path.join("pictures", "balle.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_LIVRE.wav"), os.path.join("pictures", "biberon.jpg"), os.path.join("pictures", "livre.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_LIVRE.wav"), os.path.join("pictures", "biberon.jpg"), os.path.join("pictures", "livre.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_PIED.wav"), os.path.join("pictures", "nez.jpg"), os.path.join("pictures", "pied.jpg"), 2], 
[os.path.join("sounds", "IL_OÙ_PIED.wav"), os.path.join("pictures", "nez.jpg"), os.path.join("pictures", "pied.jpg"), 2]]

exp = expyriment.design.Experiment(name="looking-while-listening task")  # create an Experiment object
#expyriment.control.set_develop_mode(on=True)  ## Set develop mode. Comment for real experiment
 
expyriment.control.initialize(exp)
 
#set mouse cursor and screen size
mouse = expyriment.io.Mouse(show_cursor=True)

 
#create a fixation cross
fixcross = expyriment.stimuli.FixCross(size=(25, 25),
                                 line_width=3,
                                 colour=expyriment.misc.constants.C_WHITE)
 
exp.add_data_variable_names(['sound', 'picture1', 'picture2', 'accuracy', 'rt']) #label different types of data collected
 
expyriment.control.start() #starts the experiment, ask for an id number
fixcross.present()  # clear screen, presenting fixation cross
 
#Matrix for data, will append target stimuli, accuracy and rt for each trial
trueOrFalse = ""
tabData = [["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0]]

#Experimental task
appeared = [] #create an empty list, will append each trial completed
i = 0
while i < 16: #loop until it reaches 16 trials
    ok = False
    while ok == False:
        nbr_aleatoire = randint(0, 15) #randomize the order of the trials
        for _, value in enumerate(appeared):
            if nbr_aleatoire == value :
                break
        else : 
            ok = True
 
    appeared.append(nbr_aleatoire)
    sound = expyriment.stimuli.Audio(tableau[nbr_aleatoire][0]) #define audio stimuli
    image1 = expyriment.stimuli.Picture(tableau[nbr_aleatoire][1], position = (-200, 0)) #define visual stimuli
    image2 = expyriment.stimuli.Picture(tableau[nbr_aleatoire][2], position = (200, 0))
    BB = expyriment.io.TouchScreenButtonBox([image1, image2]) #create a button box for the two visual stimuli
    BB.create()
    BB.show()
 
    sound.present()
 
    response, rt = BB.wait(duration = 8000) 
 
 #Gets only the name of the stimuli (remove "sounds" or "pictures" from their pathname)
    shortSound = tableau[nbr_aleatoire][0][7:] 
    shortImage1 = tableau[nbr_aleatoire][1][9:]
    shortImage2 = tableau[nbr_aleatoire][2][9:]
 
 #check participants' accuracy 
    if response == image1 and tableau[nbr_aleatoire][3] == 1:
        print("1")
        trueOrFalse = "True"
    elif response == image2 and tableau[nbr_aleatoire][3] == 2:
        print("2")
        trueOrFalse = "True"
    else :
        trueOrFalse = "False"
    print(trueOrFalse)
 
 #add data under the label defined earlier
    exp.data.add([shortSound,
                shortImage1,
                shortImage2,
                trueOrFalse,
                 rt])
 
 #add data into 'tabData' that I use to create accuracy and rt histograms
    tabData[i][0] = shortSound 
    tabData[i][1] = trueOrFalse
    tabData[i][2] = rt
 
    fixcross.present()
    exp.clock.wait(1000)
    i += 1 #add 1 to i. Loop keeps going until i reaches 16
 
 
expyriment.control.end(goodbye_text= 'Thanks for taking part to this experiment, see you soon')
 
AccuracyPlot(tabData) #show accuracy histogram
RTplot(tabData) #show rt histogram
 
