#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Juni 21, 2022, at 15:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
# Version of PsychoPy: v2022.2.1
### ### ### ###
### IMPORTS ###
### ### ### ###
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy import locale_setup
from psychopy import prefs
#prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import psychopy.iohub as io
from psychopy.hardware import keyboard
import datetime
from datetime import timedelta
import subprocess
import time
from psychopy import logging
import logging_utilities
from questionnaires import likertscale, panas, nasa, affective_slider
from relaxation_video import relaxation_video
from stroop import _stroop, stroop
from wait_some_time import wait_some_time
from eye_closing import eye_closing
from present_text import present_text
from arithmetix import arithmetix
from n_back import nback
from sync_muse_with_psychopy import sync_muse_w_psychopy
from sudoku import sudoku
from sys import platform
from random import SystemRandom
import random
import pandas as pd





### ### ### ### ###
### GENERAL CONFIG LOADING ###
### ### ### ### ###
seconds_per_routine = 600#600

#base_path = 'D:\\MP_2021\\mind-classifier_scripts_branch\\psychopy_study_mp_revised\\'
base_path = '/Users/samikreal/Desktop/Projects/9. Bert Arnrich/3. Project/Psychopy/'
base_path = '/home/dh-mt/Desktop/DH_Thesis/Psychopy/'
video_timer = seconds_per_routine # 10 * 60
eye_closing_timer = 60 # 60.0
timer_for_trails = 45 # 45


nback_time_per_stimulus = 1.0 # 2.000000 
nback_sound_duration = 0.5 # 1.000000
repetitions_actual_nback = 1.0 # 15.0
selfpaced_stroop_timer = 1.0 # 5.500000
stroop_nreps = 5.0 # 100.0

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'study_full'  # from the Builder filename that created this script
expInfo = {
    'participant': '001',
    'Age': '',
    'Gender': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logging_utilities.logger_setup(filename)


endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
    
"""
win.recordFrameIntervals = True
win.refreshThreshold = 1/60 + 0.004
logging.console.setLevel(logging.WARNING)

print('Overall, %i frames were dropped.' % win.nDroppedFrames)
"""
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
#backend needs to be 'ptb' for ubuntu!!!
defaultKeyboard = keyboard.Keyboard(backend='ptb')







# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


### ### ### ### ### ### ### ### ###
### END INITIALIZATION COMPONENTS ###
### ### ### ### ### ### ### ### ###






### ### ### ### ### ###
### High Level Functions ###
### ### ### ### ### ###

###Start function
def start_functions():
    ### ### ### ### ### ### ###
    ### START WELCOME WINDOW ###
    ### ### ### ### ### ### ###
    logging.exp('start_welcome_logging: ' + str(time.time()))

    # ------Prepare to start Routine "WelcomeWindow"-------
    continueRoutine = True
    present_text(thisExp, win, frameTolerance, defaultKeyboard,
                 endExpNow, visual_stim=None, test_text='Welcome to our study!\n\n\nPress [SPACE] to start.',
                 name_for_logs='default_log_name')


    ### ### ### ### ### ### ### ###
    ### DELAY; SYNC MUSE; DELAY ###
    ### ### ### ### ### ### ### ###

    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
    sync_muse_w_psychopy(thisExp, win, expInfo, frameTolerance, defaultKeyboard, endExpNow)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)

    ### ### ### ### ### ### ### ###
    ### START RELAXATION VIDEO ###
    ### ### ### ### ### ### ### ###
    relaxation_video(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, video_timer)

    ### ### ### ### ### ### ###
    ### EYE-CLOSING SESSION ###
    ### ### ### ### ### ### ###
    eye_closing(thisExp, routineTimer, win, eye_closing_timer, frameTolerance, endExpNow, defaultKeyboard, base_path)

    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)





    ### ### ### ###
    ### PANAS ###
    ### ### ### ###
    panas(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')





###Task functions
### ### ### ### ### ###
### ARITHMETIC TASKS ##
### ### ### ### ### ###
def arithmetix_easy():
    routine_time_in_seconds = seconds_per_routine
    #There are 1200 equations in each file. A particpant would need to solve 2 equations per second to finish all of them in 10 minutes.
    num_reps = 1 #Creating too many reps for arithmetix freezes the computer!
    csv_file = 'NeededFiles/easy_tasks.csv'
    text_to_display_before = 'The following task will be simple mental arithmetics. It will encompass addition and substraction.\n\nPlease enter your answer in the textfield using the keyboard. You can submit your answer using the [ENTER]-Key or the button.\n\nPlease note that your time and performance are being measured. To start, hit [SPACE].'
    arithmetix(thisExp, win, frameTolerance, defaultKeyboard, endExpNow,
               expInfo, routine_time_in_seconds, filename, routineTimer, csv_file, text_to_display_before,
               rounding=False, nreps=num_reps, threshold=0.5)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')

def arithmetix_hard():
    routine_time_in_seconds = seconds_per_routine
    #There are 1200 equations in each file. A particpant would need to solve 2 equations per second to finish all of them in 10 minutes.
    num_reps = 1 #Creating too many reps for arithmetix freezes the computer!
    csv_file = 'NeededFiles/hard_tasks.csv'
    text_to_display_before = 'The following task will be hard mental arithmetics. It will encompass addition, substraction, multiplication, and division.\n\nPlease note that rounding is important. You may speed up answering utilizing the threshold (+/- from the correct answer) of 0.5.\n\nPlease enter your answer in the textfield using the keyboard. You can submit your answer using the [ENTER]-Key or the button.\n\nPlease note that your time and performance are being measured. To start, hit [SPACE].'
    arithmetix(thisExp, win, frameTolerance, defaultKeyboard, endExpNow,
               expInfo, routine_time_in_seconds, filename,  routineTimer, csv_file, text_to_display_before,
               rounding=True, nreps=num_reps, threshold=0.5)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')




### ### ### ### ###
###    NBACK   ####
### ### ### ### ###
def n_back_easy():
    routine_time_in_seconds = seconds_per_routine
    routine_time_example_in_seconds = timer_for_trails
    num_reps = 15 * routine_time_in_seconds #this is the potential number of repetitions (used only to have more exercises in case participant finishes too quickly)
    nback(continueRoutine_Part=continueRoutine, experiment_Ref=thisExp, routine_timer_part=routineTimer, win_ref=win,
          easy=True, timer_time_actual=routine_time_in_seconds, timer_time_example=routine_time_example_in_seconds,
          base_path=base_path, frameTolerance=frameTolerance, endExpNow=endExpNow, defaultKeyboard=defaultKeyboard,
          expInfo=expInfo, num_reps=num_reps, with_timer=True)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')


def n_back_hard():
    routine_time_in_seconds = seconds_per_routine
    routine_time_example_in_seconds = timer_for_trails
    num_reps = 15 * routine_time_in_seconds #this is the potential number of repetitions (used only to have more exercises in case participant finishes too quickly)
    nback(continueRoutine_Part=continueRoutine, experiment_Ref=thisExp, routine_timer_part=routineTimer, win_ref=win,
          easy=False, timer_time_actual=routine_time_in_seconds, timer_time_example=routine_time_example_in_seconds,
          base_path=base_path, frameTolerance=frameTolerance, endExpNow=endExpNow, defaultKeyboard=defaultKeyboard,
          expInfo=expInfo, num_reps=num_reps, with_timer=True)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')



### ### ### ###
### STROOP ####
### ### ### ###
def stroop_easy():
    routine_time_in_seconds = seconds_per_routine
    num_reps = 15 * routine_time_in_seconds
    stroop_example_time = timer_for_trails
    stroop(continueRoutine_Part=continueRoutine, experiment_Ref=thisExp, routine_timer_part=routineTimer, win_ref=win,
           easy=True, intro_test_only=False, num_reps=num_reps, timely_shortened=False, seconds_to_stop=30,
           keyboard=keyboard, base_path=base_path, frameTolerance=frameTolerance, endExpNow=endExpNow,
           defaultKeyboard=defaultKeyboard, expInfo=expInfo, stroop_entire_task_time_in_seconds=routine_time_in_seconds,
           stroop_example_time=stroop_example_time)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')



def stroop_hard():
    routine_time_in_seconds = seconds_per_routine
    num_reps = 15 * routine_time_in_seconds
    stroop_example_time = timer_for_trails
    stroop(continueRoutine_Part=continueRoutine, experiment_Ref=thisExp, routine_timer_part=routineTimer, win_ref=win,
           easy=False, intro_test_only=False, num_reps=num_reps, timely_shortened=False, seconds_to_stop=30,
           keyboard=keyboard, base_path=base_path, frameTolerance=frameTolerance, endExpNow=endExpNow,
           defaultKeyboard=defaultKeyboard, expInfo=expInfo, stroop_entire_task_time_in_seconds=routine_time_in_seconds,
           stroop_example_time=stroop_example_time)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ###
    ###   NASA  ###
    ### ### ### ###
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)

    ### ### ### ### ### ###
    ### AFFECTIVE SLIDER ###
    ### ### ### ### ### ###
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,
                   time_in_ms=500)

    ### ### ### ### ### ###
    ###   LIKERT SCALE  ###
    ### ### ### ### ### ###
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')



def sudoku_easy():
    #'''
    global win
    win = sudoku(win, seconds_per_routine, thisExp, frameTolerance, defaultKeyboard, endExpNow, easy=True)

    #Nasa
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)
    #Affective Slider
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    #Likert Scale
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')
    #'''
    pass

def sudoku_hard():
    #'''
    global win
    win = sudoku(win, seconds_per_routine, thisExp, frameTolerance, defaultKeyboard, endExpNow, easy=False)

    #Nasa
    nasa(continueRoutine, thisExp, routineTimer, win, endExpNow, defaultKeyboard, frameTolerance)
    #Affective Slider
    affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
    #Likert Scale
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='mental effort')
    likertscale(experiment_Ref=thisExp, win_ref=win, for_which='stress')
    #'''
    pass


#base_path + 'NeededFiles/conditions.xlsx'
def change_csv_for_german_keyboard(path, revert=False):
    pd.io.formats.excel.ExcelFormatter.header_style = None

    df = pd.read_excel(path, index_col=None)
    #print(df.head(8))

    if revert == False:
        df['corrAns'] = np.where((df['corrAns'] == 'y'), 'z', df['corrAns'])
    else:
        df['corrAns'] = np.where((df['corrAns'] == 'z'), 'y', df['corrAns'])
    df.to_excel(path, index=False)




### ### ### ### ### ###
###   TASKS START   ###
### ### ### ### ### ###

#Correct answer for german keyboard
excel_path = base_path + 'NeededFiles/conditions.xlsx'
change_csv_for_german_keyboard(excel_path, revert=False)



thisExp.addData('ENTIRE_EXPERIMENT_TASKS.started', win.getFutureFlipTime(clock=None))
continueRoutine = True

if platform == "linux" or platform == "linux2":
    tasks_function_list = [arithmetix_easy, arithmetix_hard, n_back_easy, n_back_hard, stroop_easy, stroop_hard, sudoku_easy, sudoku_hard]
elif platform == "darwin":
    tasks_function_list = [arithmetix_easy, arithmetix_hard, n_back_easy, n_back_hard, stroop_easy, stroop_hard]
else:
    raise OSError("This code only works on Linux or Mac (darwin)")


os_random = SystemRandom()
seed = os_random.randrange(datetime.date.today().day ** 5)
random.Random(seed).shuffle(tasks_function_list)
string = "Order of tasks: ["
for i in tasks_function_list:
    string = string + i.__name__ + ", "
string = string + "]"
string = F'Order of tasks for this experiment: {string}'
thisExp.nextEntry()
thisExp.addData('Order_of_tasks_for_this_experiment', string)
thisExp.nextEntry()
logging.log(level=logging.EXP, msg=string)





# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#Functions at the start of the experiment
continueRoutine = start_functions()


#'''
#run all tasks in the shuffled order
for task_function in tasks_function_list:
    task_function()

#'''






### ### ### ### ### ###
### GOODBYE ROUTINE ###
### ### ### ### ### ###

#Revert answer correction for German keyboard
change_csv_for_german_keyboard(excel_path, revert=True)

# Initialize components for Routine "GoodbyeTasks"
GoodbyeTasksClock = core.Clock()
FinishedTasks = visual.TextStim(win=win, name='FinishedTasks',
    text='You have now completed both of the tasks.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0)

# Initialize components for Routine "GOODBYE_"
GOODBYE_Clock = core.Clock()
ByeByeTrial = visual.TextStim(win=win, name='ByeByeTrial',
    text='Congratulations! You are done!\nThank you very much for participating in our trial. :) \n\nPlease remove the Muse headband and the Empatica watch and hand them over to your instructor.\n\nPlease do not stop recording.\n\nPress [SPACE] to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
key_resp_24 = keyboard.Keyboard()


# Initialize components for Routine "END"
ENDClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='Thank you.\n\nPress [ENTER] to exit the study.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
key_resp_25 = keyboard.Keyboard()



# ------Prepare to start Routine "GoodbyeTasks"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeTasksComponents = [FinishedTasks]
for thisComponent in GoodbyeTasksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeTasksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GoodbyeTasks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeTasksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeTasksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FinishedTasks* updates
    if FinishedTasks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FinishedTasks.frameNStart = frameN  # exact frame index
        FinishedTasks.tStart = t  # local t and not account for scr refresh
        FinishedTasks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FinishedTasks, 'tStartRefresh')  # time at next scr refresh
        FinishedTasks.setAutoDraw(True)
    if FinishedTasks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FinishedTasks.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            FinishedTasks.tStop = t  # not accounting for scr refresh
            FinishedTasks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FinishedTasks, 'tStopRefresh')  # time at next scr refresh
            FinishedTasks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeTasksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodbyeTasks"-------
for thisComponent in GoodbyeTasksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FinishedTasks.started', FinishedTasks.tStartRefresh)
thisExp.addData('FinishedTasks.stopped', FinishedTasks.tStopRefresh)

### ### ###
### PANAS #
### ### ###
panas(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard)
continueRoutine = True
wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)

### ### ### ###
### GOODBYE ###
### ### ### ###

# ------Prepare to start Routine "GOODBYE_"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
GOODBYE_Components = [ByeByeTrial, key_resp_24]
for thisComponent in GOODBYE_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GOODBYE_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GOODBYE_"-------
while continueRoutine:
    # get current time
    t = GOODBYE_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GOODBYE_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ByeByeTrial* updates
    if ByeByeTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ByeByeTrial.frameNStart = frameN  # exact frame index
        ByeByeTrial.tStart = t  # local t and not account for scr refresh
        ByeByeTrial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ByeByeTrial, 'tStartRefresh')  # time at next scr refresh
        ByeByeTrial.setAutoDraw(True)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GOODBYE_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GOODBYE_"-------
for thisComponent in GOODBYE_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ByeByeTrial.started', ByeByeTrial.tStartRefresh)
thisExp.addData('ByeByeTrial.stopped', ByeByeTrial.tStopRefresh)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.addData('key_resp_24.started', key_resp_24.tStartRefresh)
thisExp.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
thisExp.nextEntry()
# the Routine "GOODBYE_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



### ### ### ### ### ### ### ###
### DELAY; SYNC MUSE; DELAY ###
### ### ### ### ### ### ### ###
continueRoutine = True
wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)
sync_muse_w_psychopy(thisExp, win, expInfo, frameTolerance, defaultKeyboard, endExpNow)
wait_some_time(continueRoutine, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)



### ### ###
### END ###
### ### ###

# ------Prepare to start Routine "END"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
# keep track of which components have finished
ENDComponents = [text_18, key_resp_25]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "END"-------
while continueRoutine:
    # get current time
    t = ENDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.addData('key_resp_25.started', key_resp_25.tStartRefresh)
thisExp.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
thisExp.nextEntry()
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

### ### ### ### ###
### CLOSING CALLS #
### ### ### ### ###

thisExp.addData('ENTIRE_EXPERIMENT_TASKS.stopped', win.getFutureFlipTime(clock=None))

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
