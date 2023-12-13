import datetime
import time
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout


import logging_utilities
from wait_some_time import wait_some_time


def _stroop(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, target_3, response_stroop_3, sound_stroop_right_3, stroop_sound_wrong_3, num_reps=1.0, time_stroop=5.5, base_path=None, expInfo=None, Stroop_selfpacedClock=None, frameTolerance=None, FINISHED=None, endExpNow=None, defaultKeyboard=None, stroop_task_time_in_seconds=600):
    #TODO: 'target_3.started' este es el importante, si no hay rows en este es que no aparecio el texto!!! (o sea no cuenta)
    #todo: crear un counter como en arithmetix!!

    #TODO: PENsaar porque se duplicarian los entries en el stroop experiment (donde no hay 'target_3.started')

    timer_entire_stroop_task = core.CountdownTimer(stroop_task_time_in_seconds)
    continue_whole_task = True


    while continue_whole_task and timer_entire_stroop_task.getTime() > 0:


        # Initialize stroop-internals
        stroop_last_answer = -1
        strooptrials_selfpaced = data.TrialHandler(nReps=num_reps, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(base_path + 'NeededFiles/conditions.xlsx'),
            seed=None, name='strooptrials_selfpaced')

        experiment_Ref.addLoop(strooptrials_selfpaced)  # add the loop to the experiment
        thisStrooptrials_selfpaced = strooptrials_selfpaced.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStrooptrials_selfpaced.rgb)
        if thisStrooptrials_selfpaced != None:
            for paramName in thisStrooptrials_selfpaced:
                exec('{} = thisStrooptrials_selfpaced[paramName]'.format(paramName))


        for thisStrooptrials_selfpaced in strooptrials_selfpaced: #Loops around each row (task) of the excel file
            routine_timer_part.reset()
            # abbreviate parameter names if possible (e.g. rgb = thisStrooptrials_selfpaced.rgb)
            if thisStrooptrials_selfpaced != None:
                for paramName in thisStrooptrials_selfpaced:
                    exec('{} = thisStrooptrials_selfpaced[paramName]'.format(paramName))

            word = thisStrooptrials_selfpaced['word']
            colour = thisStrooptrials_selfpaced['colour']
            congruent = thisStrooptrials_selfpaced['congruent']
            corrAns = thisStrooptrials_selfpaced['corrAns']


            # ------Prepare to start Routine "Stroop_selfpaced"-------
            continueRoutine_Part = True
            routine_timer_part.add(time_stroop)
            # update component parameters for each repeat
            right_sound_volume = 0
            wrong_sound_volume = 0
            if stroop_last_answer == 1:
                right_sound_volume = 1
                wrong_sound_volume = 0
            elif stroop_last_answer == 2 or stroop_last_answer == 0:
                right_sound_volume = 0
                wrong_sound_volume = 1
            target_3.setColor(colour, colorSpace='rgb')
            target_3.setText(word)
            response_stroop_3.keys = []
            response_stroop_3.rt = []
            _response_stroop_3_allKeys = []
            sound_stroop_right_3.setSound(base_path + 'NeededFiles/Correct_Answer_Sound_Effect.flac', secs=1.0, hamming=True)
            sound_stroop_right_3.setVolume(right_sound_volume, log=False)
            stroop_sound_wrong_3.setSound(base_path + 'NeededFiles/Wrong_Answer_Sound_Effect.flac', secs=1.0, hamming=True)
            stroop_sound_wrong_3.setVolume(wrong_sound_volume, log=False)
            # keep track of which components have finished
            Stroop_selfpacedComponents = [target_3, response_stroop_3, sound_stroop_right_3, stroop_sound_wrong_3]
            for thisComponent in Stroop_selfpacedComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset self-paced timers
            t = 0
            _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
            Stroop_selfpacedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1



            # -------Run Routine "Stroop_selfpaced"-------
            # Listen to answers for the first task (row of the excel file) while there is time left
            # Afterwards it continues to the next row/task
            while continueRoutine_Part and routine_timer_part.getTime() > 0:

                if timer_entire_stroop_task.getTime() <= 0:
                    continue_whole_task = False
                    break

                # get current time
                t = Stroop_selfpacedClock.getTime()
                tThisFlip = win_ref.getFutureFlipTime(clock=Stroop_selfpacedClock)
                tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *target_3* updates
                if target_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    target_3.frameNStart = frameN  # exact frame index
                    target_3.tStart = t  # local t and not account for scr refresh
                    target_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win_ref.timeOnFlip(target_3, 'tStartRefresh')  # time at next scr refresh
                    target_3.setAutoDraw(True)
                if target_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        target_3.tStop = t  # not accounting for scr refresh
                        target_3.frameNStop = frameN  # exact frame index
                        win_ref.timeOnFlip(target_3, 'tStopRefresh')  # time at next scr refresh
                        target_3.setAutoDraw(False)

                # *response_stroop_3* updates
                waitOnFlip = False
                if response_stroop_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    response_stroop_3.frameNStart = frameN  # exact frame index
                    response_stroop_3.tStart = t  # local t and not account for scr refresh
                    response_stroop_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win_ref.timeOnFlip(response_stroop_3, 'tStartRefresh')  # time at next scr refresh
                    response_stroop_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win_ref.callOnFlip(response_stroop_3.clock.reset)  # t=0 on next screen flip
                    win_ref.callOnFlip(response_stroop_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if response_stroop_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_stroop_3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        response_stroop_3.tStop = t  # not accounting for scr refresh
                        response_stroop_3.frameNStop = frameN  # exact frame index
                        win_ref.timeOnFlip(response_stroop_3, 'tStopRefresh')  # time at next scr refresh
                        response_stroop_3.status = FINISHED
                if response_stroop_3.status == STARTED and not waitOnFlip:
                    theseKeys = response_stroop_3.getKeys(keyList=['r','g','b','y', 'z'], waitRelease=False)
                    _response_stroop_3_allKeys.extend(theseKeys)
                    if len(_response_stroop_3_allKeys):
                        response_stroop_3.keys = _response_stroop_3_allKeys[-1].name  # just the last key pressed
                        response_stroop_3.rt = _response_stroop_3_allKeys[-1].rt
                        # was this correct?
                        if (response_stroop_3.keys == str(corrAns)) or (response_stroop_3.keys == corrAns):
                            response_stroop_3.corr = 1
                        else:
                            response_stroop_3.corr = 0
                        # a response ends the routine
                        continueRoutine_Part = False
                # start/stop sound_stroop_right_3
                if sound_stroop_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_stroop_right_3.frameNStart = frameN  # exact frame index
                    sound_stroop_right_3.tStart = t  # local t and not account for scr refresh
                    sound_stroop_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_stroop_right_3.play(when=win_ref)  # sync with win_ref flip
                if sound_stroop_right_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_stroop_right_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_stroop_right_3.tStop = t  # not accounting for scr refresh
                        sound_stroop_right_3.frameNStop = frameN  # exact frame index
                        win_ref.timeOnFlip(sound_stroop_right_3, 'tStopRefresh')  # time at next scr refresh
                        sound_stroop_right_3.stop()
                # start/stop stroop_sound_wrong_3
                if stroop_sound_wrong_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stroop_sound_wrong_3.frameNStart = frameN  # exact frame index
                    stroop_sound_wrong_3.tStart = t  # local t and not account for scr refresh
                    stroop_sound_wrong_3.tStartRefresh = tThisFlipGlobal  # on global time
                    stroop_sound_wrong_3.play(when=win_ref)  # sync with win_ref flip
                if stroop_sound_wrong_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stroop_sound_wrong_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        stroop_sound_wrong_3.tStop = t  # not accounting for scr refresh
                        stroop_sound_wrong_3.frameNStop = frameN  # exact frame index
                        win_ref.timeOnFlip(stroop_sound_wrong_3, 'tStopRefresh')  # time at next scr refresh
                        stroop_sound_wrong_3.stop()

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()

                # check if all components have finished
                if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                    break
                continueRoutine_Part = False  # will revert to True if at least one component still running
                for thisComponent in Stroop_selfpacedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine_Part = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine_Part:  # don't flip if this routine is over, or we'll get a blank screen
                    win_ref.flip()

            # -------Ending Routine "Stroop_selfpaced"-------
            for thisComponent in Stroop_selfpacedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            if not response_stroop_3.keys:
                stroop_last_answer = 0
            else:
                key_pressed = response_stroop_3.keys[0]
                if key_pressed != corrAns:
                    stroop_last_answer = 2
                elif key_pressed == corrAns:
                    stroop_last_answer = 1


            strooptrials_selfpaced.addData('target_3.started', target_3.tStartRefresh)
            strooptrials_selfpaced.addData('target_3.stopped', target_3.tStopRefresh)
            # check responses
            if response_stroop_3.keys in ['', [], None]:  # No response was made
                response_stroop_3.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   response_stroop_3.corr = 1  # correct non-response
                else:
                   response_stroop_3.corr = 0  # failed to respond (incorrectly)
            # store data for strooptrials_selfpaced (TrialHandler)
            strooptrials_selfpaced.addData('Stroop.participant_answer', response_stroop_3.keys)
            strooptrials_selfpaced.addData('Stroop.correct_answer', response_stroop_3.corr)
            if response_stroop_3.keys != None:  # we had a response
                strooptrials_selfpaced.addData('Stroop.response_time', response_stroop_3.rt)

            strooptrials_selfpaced.addData('response_stroop_3.started', response_stroop_3.tStartRefresh)
            strooptrials_selfpaced.addData('response_stroop_3.stopped', response_stroop_3.tStopRefresh)
            sound_stroop_right_3.stop()  # ensure sound has stopped at end of routine
            strooptrials_selfpaced.addData('sound_stroop_right_3.started', sound_stroop_right_3.tStartRefresh)

            strooptrials_selfpaced.addData('sound_stroop_right_3.stopped', sound_stroop_right_3.tStopRefresh)
            stroop_sound_wrong_3.stop()  # ensure sound has stopped at end of routine
            strooptrials_selfpaced.addData('stroop_sound_wrong_3.started', stroop_sound_wrong_3.tStartRefresh)
            strooptrials_selfpaced.addData('stroop_sound_wrong_3.stopped', stroop_sound_wrong_3.tStopRefresh)
            experiment_Ref.nextEntry()

            if response_stroop_3.corr:
                aux = "correct"
            else:
                aux = "incorrect"
            logging.log(level=logging.EXP, msg=F"Participant answer: {response_stroop_3.keys}' is {aux}. Response time: {response_stroop_3.rt}")


            if timer_entire_stroop_task.getTime() <= 0: #SAMIK
                continue_whole_task = False
                break


def stroop(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, easy=True, intro_test_only=False, num_reps=1.0, timely_shortened=False, seconds_to_stop=30, keyboard=None, base_path=None, frameTolerance=None, endExpNow=None, defaultKeyboard=None, expInfo=None, stroop_entire_task_time_in_seconds=600, stroop_example_time=35):
    logging_utilities.log_time(beginning_flag=True, routine_name=F'Stroop_Global')
    experiment_Ref.addData('Stroop_Global.started', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.addData('initial_instructions_stroop_example.started', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()

    finish_time_of_workload_block = None
    if timely_shortened:
        start_of_block = datetime.datetime.now()
        finish_time_of_workload_block = start_of_block + datetime.timedelta(seconds=seconds_to_stop) # could also be: seconds=5
    else:
        start_of_block = datetime.datetime.now()
        finish_time_of_workload_block = start_of_block + datetime.timedelta(seconds=60*60*60*24) # Experimental part here should not extend one full day (sec/min/hour/day)
    
    # Config for easy and hard stroop-tests
    time_stroop = 0
    if easy:
        time_stroop = 5.5
    else:
        time_stroop = 1.0

    ### Initializations start
    # Initialize components for Routine "IntroStroop"
    IntroStroopClock = core.Clock()
    text_2 = visual.TextStim(win=win_ref, name='text_2',
        text='In the next task you will see the name of some colors written in different or same color fonts. You have to choose the colour of the letters, ignoring the word itself. Try to press the respective key as quickly as possible.\n\nred = r\ngreen = g\nblue = b\nyellow = y\n\nYou will start with a trial session now.\n\nPress [SPACE] to start.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "IntroStroop_trial_self"
    IntroStroop_trial_selfClock = core.Clock()
    text_24 = visual.TextStim(win=win_ref, name='text_24',
        text='This is a trial session! \n\nChoose the colour of the letters, ignoring the word. Try to press the respective key as quickly as possible.\n\nred = r\ngreen = g\nblue = b\nyellow = y\n\nPress [SPACE] to start.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_29 = keyboard.Keyboard()

    # Initialize components for Routine "Stroop_selfpaced"
    Stroop_selfpacedClock = core.Clock()
    stroop_last_answer = 0
    target_3 = visual.TextStim(win=win_ref, name='target_3',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    response_stroop_3 = keyboard.Keyboard()
    sound_stroop_right_3 = sound.Sound(base_path + 'NeededFiles/Correct_Answer_Sound_Effect.flac', secs=1.0, stereo=True, hamming=True,
        name='sound_stroop_right_3')
    sound_stroop_right_3.setVolume(1.0)
    stroop_sound_wrong_3 = sound.Sound(base_path + 'NeededFiles/Wrong_Answer_Sound_Effect.flac', secs=1.0, stereo=True, hamming=True,
        name='stroop_sound_wrong_3')
    stroop_sound_wrong_3.setVolume(1.0)

    # Initialize components for Routine "introStroop_self"
    introStroop_selfClock = core.Clock()
    text_25 = visual.TextStim(win=win_ref, name='text_25',
        text='This is the actual task! \n\nChoose the colour of the letters, ignoring the word. Try to press the respective key as quickly as possible.\n\nred = r\ngreen = g\nblue = b\nyellow = y\n\nPress [SPACE] to start.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_30 = keyboard.Keyboard()

    # Initialize components for Routine "stroop_timerstart"
    stroop_timerstartClock = core.Clock()
    stroop_timer = core.Clock()
    stroop_duration = 60

    # Initialize components for Routine "stroop_checktimer"
    stroop_checktimerClock = core.Clock()
    ### Initializations done

    # while datetime.datetime.now() < finish_time_of_workload_block: TODO this lead to an error, in which the iterations were done too frequently; Will have to investigate here more
    # ------Prepare to start Routine "IntroStroop"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    IntroStroopComponents = [text_2, key_resp_2]
    for thisComponent in IntroStroopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    IntroStroopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "IntroStroop"-------
    while continueRoutine_Part and (datetime.datetime.now() < finish_time_of_workload_block):
        # get current time
        t = IntroStroopClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=IntroStroopClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in IntroStroopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "IntroStroop"-------
    for thisComponent in IntroStroopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_2.started', text_2.tStartRefresh)
    experiment_Ref.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    experiment_Ref.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_2.rt', key_resp_2.rt)
    experiment_Ref.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    experiment_Ref.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    experiment_Ref.nextEntry()
    # the Routine "IntroStroop" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    ### STROOP INTRODUCTION SLIDES FOR TRIAL-RUN
    # ------Prepare to start Routine "IntroStroop_trial_self"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_29.keys = []
    key_resp_29.rt = []
    _key_resp_29_allKeys = []
    # keep track of which components have finished
    IntroStroop_trial_selfComponents = [text_24, key_resp_29]
    for thisComponent in IntroStroop_trial_selfComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    IntroStroop_trial_selfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "IntroStroop_trial_self"-------
    while continueRoutine_Part and (datetime.datetime.now() < finish_time_of_workload_block):
        # get current time
        t = IntroStroop_trial_selfClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=IntroStroop_trial_selfClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        
        # *key_resp_29* updates
        waitOnFlip = False
        if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_29.frameNStart = frameN  # exact frame index
            key_resp_29.tStart = t  # local t and not account for scr refresh
            key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
            key_resp_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_29.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_29.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_29_allKeys.extend(theseKeys)
            if len(_key_resp_29_allKeys):
                key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                key_resp_29.rt = _key_resp_29_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in IntroStroop_trial_selfComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "IntroStroop_trial_self"-------
    for thisComponent in IntroStroop_trial_selfComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_24.started', text_24.tStartRefresh)
    experiment_Ref.addData('text_24.stopped', text_24.tStopRefresh)
    # check responses
    if key_resp_29.keys in ['', [], None]:  # No response was made
        key_resp_29.keys = None
    experiment_Ref.addData('key_resp_29.keys',key_resp_29.keys)
    if key_resp_29.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_29.rt', key_resp_29.rt)
    experiment_Ref.addData('key_resp_29.started', key_resp_29.tStartRefresh)
    experiment_Ref.addData('key_resp_29.stopped', key_resp_29.tStopRefresh)
    experiment_Ref.nextEntry()
    # the Routine "IntroStroop_trial_self" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    experiment_Ref.addData('initial_instructions_stroop_example.stopped', win_ref.getFutureFlipTime(clock=None))

    ### STROOP TRIAL RUN, therefore the nReps should always be only set to 1.0!
    ### ONLY DIFFERENCE BETWEEN STROOP TRIAL_RUN AND ACTUAL_RUN IS THAT THE TEXT DISPLAYED BEFOREHAND IS DIFFERENT, AND THE NUM_REPS IS DIFFERENT.
    ### EXTRACT THIS, AND THEN MAKE SURE TO HAVE EVERYWHERE LIKE A LOGGING IN BETWEEN, INDICATING THIS IS NOW THE TRIAL, TRIAL FINISHED, THIS IS NOW THE REAL, REAL FINISHED
    # set up handler to look after randomisation of conditions etc

    stroop_level = 'EASY' if easy else 'HARD'
    experiment_Ref.addData('stroop_level', stroop_level)
    logging_utilities.log_time(beginning_flag=True, routine_name=F'Example Stroop level {stroop_level}')
    experiment_Ref.addData('Example_Stroop.started', win_ref.getFutureFlipTime(clock=None))
    _stroop(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, target_3, response_stroop_3, sound_stroop_right_3, stroop_sound_wrong_3, num_reps=num_reps, time_stroop=time_stroop, base_path=base_path, expInfo=expInfo, Stroop_selfpacedClock=Stroop_selfpacedClock, frameTolerance=frameTolerance, FINISHED=FINISHED, endExpNow=endExpNow, defaultKeyboard=defaultKeyboard, stroop_task_time_in_seconds=stroop_example_time)
    experiment_Ref.addData('Example_Stroop.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Example Stroop level {stroop_level}')


    experiment_Ref.addData('instructions_stroop.started', win_ref.getFutureFlipTime(clock=None))
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, frameTolerance, endExpNow,
                   defaultKeyboard, time_in_ms=500)


    ### STROOP TRIAL RUN COMPLETED. ADD HERE THE CHECK IF THIS IS AN EXAMPLE-RUN. If so, terminate. If not, continue.
    if not intro_test_only:
        # ------Prepare to start Routine "introStroop_self"-------
        continueRoutine_Part = True
        # update component parameters for each repeat
        key_resp_30.keys = []
        key_resp_30.rt = []
        _key_resp_30_allKeys = []
        # keep track of which components have finished
        introStroop_selfComponents = [text_25, key_resp_30]
        for thisComponent in introStroop_selfComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        introStroop_selfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "introStroop_self"-------
        while continueRoutine_Part and (datetime.datetime.now() < finish_time_of_workload_block):
            # get current time
            t = introStroop_selfClock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=introStroop_selfClock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_25* updates
            if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_25.frameNStart = frameN  # exact frame index
                text_25.tStart = t  # local t and not account for scr refresh
                text_25.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                text_25.setAutoDraw(True)
            
            # *key_resp_30* updates
            waitOnFlip = False
            if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_30.frameNStart = frameN  # exact frame index
                key_resp_30.tStart = t  # local t and not account for scr refresh
                key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
                key_resp_30.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win_ref.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
                win_ref.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_30.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_30.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_30_allKeys.extend(theseKeys)
                if len(_key_resp_30_allKeys):
                    key_resp_30.keys = _key_resp_30_allKeys[-1].name  # just the last key pressed
                    key_resp_30.rt = _key_resp_30_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine_Part = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in introStroop_selfComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "introStroop_self"-------
        for thisComponent in introStroop_selfComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        experiment_Ref.addData('text_25.started', text_25.tStartRefresh)
        experiment_Ref.addData('text_25.stopped', text_25.tStopRefresh)
        # check responses
        if key_resp_30.keys in ['', [], None]:  # No response was made
            key_resp_30.keys = None
        experiment_Ref.addData('key_resp_30.keys',key_resp_30.keys)
        if key_resp_30.keys != None:  # we had a response
            experiment_Ref.addData('key_resp_30.rt', key_resp_30.rt)
        experiment_Ref.addData('key_resp_30.started', key_resp_30.tStartRefresh)
        experiment_Ref.addData('key_resp_30.stopped', key_resp_30.tStopRefresh)
        experiment_Ref.nextEntry()
        # the Routine "introStroop_self" was not non-slip safe, so reset the non-slip timer
        routine_timer_part.reset()

        # ------Prepare to start Routine "stroop_timerstart"-------
        continueRoutine_Part = True
        # update component parameters for each repeat
        stroop_timer.reset()
        logging.exp('start_stroop_logging: ' + str(time.time()))
        # keep track of which components have finished
        stroop_timerstartComponents = []
        for thisComponent in stroop_timerstartComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        stroop_timerstartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "stroop_timerstart"-------
        while continueRoutine_Part and (datetime.datetime.now() < finish_time_of_workload_block):
            # get current time
            t = stroop_timerstartClock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=stroop_timerstartClock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in stroop_timerstartComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "stroop_timerstart"-------
        for thisComponent in stroop_timerstartComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "stroop_timerstart" was not non-slip safe, so reset the non-slip timer
        routine_timer_part.reset()

        experiment_Ref.addData('instructions_stroop.stopped', win_ref.getFutureFlipTime(clock=None))


        stroop_level = 'EASY' if easy else 'HARD'
        experiment_Ref.addData('stroop_level', stroop_level)
        logging_utilities.log_time(beginning_flag=True, routine_name=F'Stroop level {stroop_level}')
        experiment_Ref.addData('Stroop.started', win_ref.getFutureFlipTime(clock=None))

        _stroop(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, target_3, response_stroop_3, sound_stroop_right_3, stroop_sound_wrong_3, num_reps=num_reps, time_stroop=time_stroop, base_path=base_path, expInfo=expInfo, Stroop_selfpacedClock=Stroop_selfpacedClock, frameTolerance=frameTolerance, FINISHED=FINISHED, endExpNow=endExpNow, defaultKeyboard=defaultKeyboard, stroop_task_time_in_seconds=stroop_entire_task_time_in_seconds)
        experiment_Ref.addData('Stroop.stopped', win_ref.getFutureFlipTime(clock=None))
        logging_utilities.log_time(beginning_flag=False, routine_name=F'Stroop level {stroop_level}')

        wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, frameTolerance, endExpNow, defaultKeyboard, time_in_ms=500)


        experiment_Ref.addData('Stroop_Global.stopped', win_ref.getFutureFlipTime(clock=None))
        experiment_Ref.nextEntry()
        logging_utilities.log_time(beginning_flag=False, routine_name=F'Stroop_Global')
