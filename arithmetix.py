from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from wait_some_time import wait_some_time
import logging_utilities
from present_text import present_text
import datetime
from datetime import timedelta


def arithmetix(experiment_Ref, win, frameTolerance, defaultKeyboard, endExpNow, expInfo, seconds_per_routine, filename,
               routine_timer_part, trials_csv, text_to_display_before, rounding, nreps=1.0, threshold=0.5):


    logging_utilities.log_time(True, 'Arithmetix with {}'.format(trials_csv))

    trials = data.TrialHandler(nReps=nreps, method='random',
                               extraInfo=expInfo, originPath=-1,
                               trialList=data.importConditions(trials_csv),
                               seed=None, name='trials')

    trials.addData('Arithmetix_with_instructions.started', win.getFutureFlipTime(clock=None))

    # Initialize components for Routine "Arithmetic_Task"
    Arithmetic_TaskClock = core.Clock()
    text_display = visual.TextStim(win=win, name='text_display',
                                   text='',
                                   font='Open Sans',
                                   pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0,
                                   color='white', colorSpace='rgb', opacity=None,
                                   languageStyle='LTR',
                                   depth=0.0);
    textbox = visual.TextBox2(
        win, text=None, font='Open Sans',
        pos=(0, 0), letterHeight=0.05,
        size=(None, None), borderWidth=2.0,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        lineSpacing=1.0,
        padding=0.0, alignment='center',
        anchor='center',
        fillColor=None, borderColor=None,
        flipHoriz=False, flipVert=False, languageStyle='LTR',
        editable=True,
        name='textbox',
        autoLog=True,
    )


    present_text(experiment_Ref, win, frameTolerance,
                 defaultKeyboard, endExpNow, visual_stim=None, test_text=text_to_display_before,
                 name_for_logs='default_log_name')

    button = visual.ButtonStim(win,
                               text='Submit Your Answer', font='Arvo',
                               pos=(0, -0.25),
                               letterHeight=0.05,
                               size=[0.5, 0.25], borderWidth=0.0,
                               fillColor='darkgrey', borderColor=None,
                               color='white', colorSpace='rgb',
                               opacity=None,
                               bold=True, italic=False,
                               padding=None,
                               anchor='center',
                               name='button'
                               )
    button.buttonClock = core.Clock()








    experiment_Ref.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    start_of_aritmetix_block = datetime.datetime.now()
    finish_time_of_arithmetix = start_of_aritmetix_block + timedelta(
        seconds=seconds_per_routine)  # could also be: seconds=5


    trials.addData('Arithmetix.started', win.getFutureFlipTime(clock=None))
    trials.addData('csv_file_for_arithmetix_trial', trials_csv)
    logging.log(level=logging.DATA, msg='Using csv file "{}" for the arithmetix task'.format(trials_csv))
    t = 0

    for thisTrial in trials:
        start_time_of_aritmetix_trial = datetime.datetime.now()
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))

        a = thisTrial['a']
        op = thisTrial['op']
        b = thisTrial['b']
        answer = thisTrial['answer']

        trials.addData('trial_a', str(a))
        trials.addData('trial_op', str(op))
        trials.addData('trial_b', str(b))
        trials.addData('trial_answer', str(answer))

        # ------Prepare to start Routine "Arithmetic_Task"-------
        continueRoutine_Part = True
        # update component parameters for each repeat
        text_display.setText(str(a) + ' ' + str(op) + ' ' + str(b))
        textbox.reset()
        start_time_for_answer = t
        # keep track of which components have finished
        Arithmetic_TaskComponents = [text_display, textbox, button]
        for thisComponent in Arithmetic_TaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Arithmetic_TaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Arithmetic_Task"-------
        while continueRoutine_Part and (datetime.datetime.now() < finish_time_of_arithmetix):
            # get current time
            t = Arithmetic_TaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Arithmetic_TaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text_display* updates
            if text_display.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                text_display.frameNStart = frameN  # exact frame index
                text_display.tStart = t  # local t and not account for scr refresh
                text_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_display, 'tStartRefresh')  # time at next scr refresh
                text_display.setAutoDraw(True)

            # *textbox* updates
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                textbox.setAutoDraw(True)

            # *button* updates
            if button.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
                # keep track of start time/frame for later
                button.frameNStart = frameN  # exact frame index
                button.tStart = t  # local t and not account for scr refresh
                button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
                button.setAutoDraw(True)
            if button.status == STARTED:
                # check whether button has been pressed
                if button.isClicked:
                    if not button.wasClicked:
                        button.timesOn.append(button.buttonClock.getTime())  # store time of first click
                        button.timesOff.append(button.buttonClock.getTime())  # store time clicked until
                    else:
                        button.timesOff[-1] = button.buttonClock.getTime()  # update time clicked until
                    if not button.wasClicked:
                        continueRoutine_Part = False  # end routine when button is clicked
                        participants_answer = 0
                        try:
                            participants_answer = int(textbox.getText())
                        except:
                            print(
                                'Input {} could not be casted to an int. We\'ll ignore this for now and set the answer to 0.')
                        # participants_answer = textbox.getText() if textbox.getText().isnumeric() else "0"
                        if rounding:
                            # TODO: Check if thresholding works in both fields using button and keybord textbox
                            logging.log(level=logging.DATA,
                                        msg='The answer {} was {}, as {} is close enough (difference of {}) to the correct answer {}'.format(
                                            participants_answer, abs(answer - float(participants_answer)) <= threshold,
                                            participants_answer, abs(answer - float(participants_answer)), answer))
                            logging.log(level=logging.DATA, msg='The time needed for this answer was {}'.format(
                                datetime.datetime.now() - start_time_of_aritmetix_trial))
                            trials.addData('trial_response_time', str(datetime.datetime.now() - start_time_of_aritmetix_trial))
                            trials.addData('trial_participants_answer', str(participants_answer))
                            trials.addData('trial_participants_answer_correct',
                                           str(abs(answer - float(participants_answer)) <= threshold))
                        else:
                            logging.log(level=logging.DATA, msg='The answer {} was {}'.format(participants_answer,
                                                                                              int(participants_answer) == answer))
                            logging.log(level=logging.DATA, msg='The time needed for this answer was {}'.format(
                                datetime.datetime.now() - start_time_of_aritmetix_trial))
                            trials.addData('trial_response_time', str(datetime.datetime.now() - start_time_of_aritmetix_trial))
                            trials.addData('trial_participants_answer', str(participants_answer))
                            trials.addData('trial_participants_answer_correct', str(int(participants_answer) == answer))
                    button.wasClicked = True  # if button is still clicked next frame, it is not a new click
                else:
                    button.wasClicked = False  # if button is clicked next frame, it is a new click
            else:
                button.wasClicked = False  # if button is clicked next frame, it is a new click

            keys = event.getKeys()

            if 'escape' in keys:
                print("QUIT EXPERIMENT")
                core.quit()
            elif 'return' in keys:
                continueRoutine_Part = False  # end routine when button is clicked
                participants_answer = 0
                try:
                    participants_answer = int(textbox.getText())
                except:
                    print('Input {} could not be casted to an int. We\'ll ignore this for now and set the answer to 0.')
                if rounding:
                    # TODO: Check if thresholding works in both fields using button and keybord textbox
                    logging.log(level=logging.DATA,
                                msg='The answer {} was {}, as {} is close enough (difference of {}) to the correct answer {}'.format(
                                    participants_answer, abs(answer - float(participants_answer)) <= threshold,
                                    participants_answer, abs(answer - float(participants_answer)), answer))
                    logging.log(level=logging.DATA, msg='The time needed for this answer was {}'.format(
                        datetime.datetime.now() - start_time_of_aritmetix_trial))
                    trials.addData('trial_response_time', str(datetime.datetime.now() - start_time_of_aritmetix_trial))
                    trials.addData('trial_participants_answer', str(participants_answer))
                    trials.addData('trial_participants_answer_correct',
                                   str(abs(answer - float(participants_answer)) <= threshold))
                else:
                    logging.log(level=logging.DATA, msg='The answer {} was {}'.format(participants_answer,
                                                                                      int(participants_answer) == answer))
                    logging.log(level=logging.DATA, msg='The time needed for this answer was {}'.format(
                        datetime.datetime.now() - start_time_of_aritmetix_trial))
                    trials.addData('trial_response_time', str(datetime.datetime.now() - start_time_of_aritmetix_trial))
                    trials.addData('trial_participants_answer', str(participants_answer))
                    trials.addData('trial_participants_answer_correct', str(int(participants_answer) == answer))

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in Arithmetic_TaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # trials.finished = True
        # -------Ending Routine "Arithmetic_Task"-------
        for thisComponent in Arithmetic_TaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('text_display.started', text_display.tStartRefresh)
        trials.addData('text_display.stopped', text_display.tStopRefresh)
        trials.addData('textbox.text', textbox.text)
        trials.addData('textbox.started', textbox.tStartRefresh)
        trials.addData('textbox.stopped', textbox.tStopRefresh)
        trials.addData('button.started', button.tStartRefresh)
        trials.addData('button.stopped', button.tStopRefresh)
        trials.addData('button.numClicks', button.numClicks)
        if button.numClicks:
            trials.addData('button.timesOn', button.timesOn)
            trials.addData('button.timesOff', button.timesOff)
        else:
            trials.addData('button.timesOn', "")
            trials.addData('button.timesOff', "")
        # the Routine "Arithmetic_Task" was not non-slip safe, so reset the non-slip timer
        routine_timer_part.reset()
        experiment_Ref.nextEntry()

    # completed nreps repeats of 'trials'
    trials.addData('Arithmetix.stopped', win.getFutureFlipTime(clock=None))

    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    csv_name_aux = trials_csv.split("/")[-1]
    trials.saveAsText(filename + "__" + csv_name_aux, delim=',',
                      stimOut=params,
                      dataOut=['n', 'all_mean', 'all_std', 'all_raw'])

    trials.addData('Arithmetix_with_instructions.stopped', win.getFutureFlipTime(clock=None))
    logging_utilities.log_time(False, 'Arithmetix with {}'.format(trials_csv))
