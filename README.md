# Looking-while-listening Task

The aim of this project is to create a variant of the looking-while-listening task, usually used on preverbal infants to assess their lexical capacities and their understanding of certain common words. In this version of the task, instead of analysing the participants' gazes, the participants will only have to click on the right picture with their mouse. 
The task will work like this : On each trial, participants will see two pictures displayed on the right and left sides of their screen and will hear, after 4 seconds, a target-word prompting them to click at one of the objects presented on the screen. Once the participant has clicked on one of the two pictures, the next trial starts. If the participant has not clicked on any pictures, the pictures will remain on the screen for 4 sec after the target-word onset and then the next trial will start. Participants will see four times each of the four picture-pairs accompanied either by the name of one of the object or the other (2 times each). Each picture-pair, therefore, will be seen by the participant four times. Because this task was originally developped for infants it is a very easy task. In my variant, I will ask the participant to be as fast as possible in responding at each trial. I will collect participants' data in a separate text file which will contain : participant id number, the trial (what was the target word), the words-pair, the accuracy (has the participants clicked on the right picture) and the response time. In addition to this datafile, two histograms will be printed at the end of the experiment : one for participants' accuracy and one for participants' reaction time for each target words. 

# The code

The code can be divided in two parts : the first part is for data analysis and the second one is the experimental task. Four different modules are used : Expyriment, os.path, matplotlib and random. I will describe how they are used in the following section. 

## Experimental task

- Main matrix : "tableau" : 
This matrix groups the stimuli paths that will be used during the task. This matrix is composed of 16 rows and 4 columns, each row representing one of the sixteen trials in the task. Each row of the matrix contains four elements : the audio-stimuli path (which will prompt the target-word in each trial), the first visual-stimuli path (picture 1), the second stimuli path (picture 2) and finally an integer (1 or 2) indicating if the target word is picure 1 or picture 2. Here the 'os.path.join' module allows the code to be portable and to work on every operating systems. 

- Using expyriment to create the experimental task:
I create a new Experiment object by calling the Experiment class in the submodule design and name it “Looking-while-listening task”. Immediately after I initialize this experiment to be the active one. This does the following:
Starts an experimental clock, creates the screen and creates an event file. Others expyriment modules allow to set different experimental parameters, for example the mouse-cursor, the fixation cross, the data variable names... Then, starting the experiment does the following two things: presents a screen asking for the subject number and creates a data file in which the data will be stored (.xpd file in a folder called 'data'). The .xpd file is a csv file which can be imported in Excel, R or Python with pandas. Similarly, different expyriment modules will be used to create the button-boxes in the task, to present the stimuli in each trial, to set the duration of a trial and to end the experiment.

- The experimental loop :
The loop does the following : it randomizes the presentation order of the 16 trials of the task. In each trial, it presents the stimuli and registers participant's response (accuracy) and reaction time. It then adds every data variable to the datafile 'data' and to the empty matrix 'tabData' that will be used to create histograms. Starts again until the 16 trials (i.e : i = 16) have been presented to the participant. 

## Data analysis part : 
I use matplotlib for plots and histograms. 

- function 'Trueinstances' :
function that takes as an argument a matrix and verifies if the second argument in each row of the matrix is "True". This will allow to compute the participant's matching accuracy by knowing how many time he has clicked on the target-words (how many "true instances"). 

- function 'AccuracyPlot' : 
Takes as an argument a matrix. Will create a histogram showing how many matches between a target word and a picture were accurate and how many were innacurate (i.e. True or False). Uses the function 'Trueinstances'.

- function 'moyenne' : 
function that takes two arguments, a matrix and a string. It computes the mean reaction time of participants for the two instances of the same target-word.For example if the target-word is "couche", it will first look at the reaction time in the first trial with this target word and then search for the second trial with the same target word to compute the mean reaction time of these two trials. 

- function RTplot : 
Takes a matrix as an argument and creates a histogram with the mean participant's reaction time for each target-word in the experimental task. It uses the function 'moyenne'.

# Prior programming experience, what I have learned since then and what I missed in this course

Before this academic year, I had never heard about programming or python. I discovered it during the first PCBS class and the first DataCamp class of the cogmaster. Although I understand why it is so important in cognitive sciences, I find it difficult to learn and I still need a lot of time to master a programming language. This project, even though it is quite 'simple', took me a very long time to code entirely. Furthermore, I did not manage to code my initial idea for this project, which was to track the mouse-cursor motion for each trial instead of collecting participant's reaction time for each trial.
During these first months I really learnt the basics of programming : using modules, creating loops, manipulating pathnames and using the terminal. I also learnt about different data structures (lists, matrixes, tuples, functions, dictionaries...), different modules (expyriment, numpy, os, matplotlib, pandas,...) and how to use them. What I crucially miss is experience: it is really difficult to me to spot what is needed to debug a code or implement complex functions for example. In summary, I still struggle to master the very specific syntax of programming languages even though I am quite satisfied with what I have learnt until now. 
I found this course very detailed. A lot of material was at our disposal and it was easy to ask for help whenever we had questions. Furthermore, orienting the exercices and examples of codes studied in class towards cognitive sciences makes the module much more interesting than a simple programming class. Nevertheless, I really struggled to follow the rythm of the class. I think that maybe, by separating students by their level in programming skills, it would be easier for beginners like me to understand the main concepts in programming. 
