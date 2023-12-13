from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import sys
import time
import logging_utilities


def _nback(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, poly_ref, key_resp, def_keyresp,
           repetitions_of_nback_file=1,
           nback_colorfile='NeededFiles/ColourTest1.xlsx',
           with_timer=False, timer_duration=60, nback_trialClock=None, expInfo=None, endExpNow=None, frameTolerance=None,
           sound_nback_right=None, base_path=None, sound_nback_wrong=None, nback_fixation_soundClock=None,
           nback_checktimer1Clock=None, n_back_visual_Text_Stim=None):


    nback_loop1 = data.TrialHandler(nReps=repetitions_of_nback_file, method='sequential',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=data.importConditions(nback_colorfile),
                                    seed=None, name='nback_loop1')
    experiment_Ref.addLoop(nback_loop1)  # add the loop to the experiment
    thisNback_loop1 = nback_loop1.trialList[0]  # so we can initialise stimuli with some values

    # abbreviate parameter names if possible (e.g. rgb = thisNback_loop1.rgb)
    if thisNback_loop1 != None:
        for paramName in thisNback_loop1:
            exec('{} = thisNback_loop1[paramName]'.format(paramName))

    # Initialize components for Routine "nback_timerstart"
    nback_timerstartClock = core.Clock()
    nback_timer = core.Clock()
    nback_duration = timer_duration

    # ------Prepare to start Routine "nback_timerstart"-------
    continueRoutine = True
    # update component parameters for each repeat
    nback_timer.reset()

    logging.exp('start_nback_logging: ' + str(time.time()))
    # keep track of which components have finished
    nback_timerstartComponents = []
    for thisComponent in nback_timerstartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nback_timerstartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_timerstart"-------
    while continueRoutine:
        # get current time
        t = nback_timerstartClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nback_timerstartClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # check for quit (typically the Esc key)
        if endExpNow or def_keyresp.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nback_timerstartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nback_timerstart"-------
    for thisComponent in nback_timerstartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "nback_timerstart" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    for thisNback_loop1 in nback_loop1:
        currentLoop = nback_loop1
        # abbreviate parameter names if possible (e.g. rgb = thisNback_loop1.rgb)
        if thisNback_loop1 != None:
            for paramName in thisNback_loop1:
                exec('{} = thisNback_loop1[paramName]'.format(paramName))

        colourtest = thisNback_loop1['colourtest']
        corresp = thisNback_loop1['corresp']

        # ------Prepare to start Routine "nback_trial"-------
        continueRoutine_Part = True
        routine_timer_part.add(2.000000)
        # update component parameters for each repeat
        poly_ref.setFillColor(colourtest)
        poly_ref.setOpacity(1)
        poly_ref.setPos((0, 0))
        poly_ref.setSize((0.20, 0.20))
        poly_ref.setOri(0)
        poly_ref.setLineColor(colourtest)
        poly_ref.setLineWidth(1)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        nback_trialComponents = [poly_ref, key_resp]
        for thisComponent in nback_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        nback_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "nback_trial"-------
        while continueRoutine_Part and routine_timer_part.getTime() > 0:
            # get current time
            t = nback_trialClock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=nback_trialClock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *poly_ref* updates
            if poly_ref.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                poly_ref.frameNStart = frameN  # exact frame index
                poly_ref.tStart = t  # local t and not account for scr refresh
                poly_ref.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(poly_ref, 'tStartRefresh')  # time at next scr refresh
                poly_ref.setAutoDraw(True)
            if poly_ref.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > poly_ref.tStartRefresh + 2 - frameTolerance:
                    # keep track of stop time/frame for later
                    poly_ref.tStop = t  # not accounting for scr refresh
                    poly_ref.frameNStop = frameN  # exact frame index
                    win_ref.timeOnFlip(poly_ref, 'tStopRefresh')  # time at next scr refresh
                    poly_ref.setAutoDraw(False)

            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win_ref.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win_ref.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2 - frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win_ref.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                    key_resp.rt = [key.rt for key in _key_resp_allKeys]
                    # was this correct?
                    if (key_resp.keys == str(corresp)) or (key_resp.keys == corresp):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine_Part = False

            # check for quit (typically the Esc key)
            if endExpNow or def_keyresp.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in nback_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "nback_trial"-------
        for thisComponent in nback_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        nback_loop1.addData('poly_ref.started', poly_ref.tStartRefresh)
        nback_loop1.addData('poly_ref.stopped', poly_ref.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corresp).lower() == 'none':
                key_resp.corr = 1;  # correct non-response
            else:
                key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for nback_loop1 (TrialHandler)
        nback_loop1.addData('key_resp.keys', key_resp.keys)
        nback_loop1.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            nback_loop1.addData('key_resp.rt', key_resp.rt[0])
        nback_loop1.addData('key_resp.started', key_resp.tStartRefresh)
        nback_loop1.addData('key_resp.stopped', key_resp.tStopRefresh)
        space_pressed = False
        nback_event = False

        if key_resp.keys:
            space_pressed = True
        if corresp == ['space']:
            nback_event = True

        if space_pressed and nback_event:
            nback_last_answer = 1
        elif space_pressed and not nback_event:
            nback_last_answer = 2
        elif (not space_pressed) and nback_event:
            nback_last_answer = 2
        else:
            nback_last_answer = 0

        # ------Prepare to start Routine "nback_fixation_sound"-------
        continueRoutine_Part = True
        routine_timer_part.add(1.000000)
        # update component parameters for each repeat
        right_sound_volume = 0
        wrong_sound_volume = 0
        if nback_last_answer == 1:
            right_sound_volume = 1
            wrong_sound_volume = 0
        elif nback_last_answer == 2:
            right_sound_volume = 0
            wrong_sound_volume = 1
        n_back_visual_Text_Stim.setColor('white', colorSpace='rgb')
        n_back_visual_Text_Stim.setPos((0, 0))
        n_back_visual_Text_Stim.setText('+')
        n_back_visual_Text_Stim.setFont('Arial')
        n_back_visual_Text_Stim.setHeight(0.1)
        sound_nback_right.setSound(base_path + 'NeededFiles/Correct_Answer_Sound_Effect.flac', secs=1.0, hamming=True)
        sound_nback_right.setVolume(right_sound_volume, log=False)
        sound_nback_wrong.setSound(base_path + 'NeededFiles/Wrong_Answer_Sound_Effect.flac', secs=1.0, hamming=True)
        sound_nback_wrong.setVolume(wrong_sound_volume, log=False)
        # keep track of which components have finished
        nback_fixation_soundComponents = [n_back_visual_Text_Stim, sound_nback_right, sound_nback_wrong]
        for thisComponent in nback_fixation_soundComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        nback_fixation_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "nback_fixation_sound"-------
        while continueRoutine_Part and routine_timer_part.getTime() > 0:
            # get current time
            t = nback_fixation_soundClock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=nback_fixation_soundClock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *Fix* updates
            if n_back_visual_Text_Stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                n_back_visual_Text_Stim.frameNStart = frameN  # exact frame index
                n_back_visual_Text_Stim.tStart = t  # local t and not account for scr refresh
                n_back_visual_Text_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(n_back_visual_Text_Stim, 'tStartRefresh')  # time at next scr refresh
                n_back_visual_Text_Stim.setAutoDraw(True)
            if n_back_visual_Text_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > n_back_visual_Text_Stim.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    n_back_visual_Text_Stim.tStop = t  # not accounting for scr refresh
                    n_back_visual_Text_Stim.frameNStop = frameN  # exact frame index
                    win_ref.timeOnFlip(n_back_visual_Text_Stim, 'tStopRefresh')  # time at next scr refresh
                    n_back_visual_Text_Stim.setAutoDraw(False)
            # start/stop sound_nback_right
            if sound_nback_right.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                sound_nback_right.frameNStart = frameN  # exact frame index
                sound_nback_right.tStart = t  # local t and not account for scr refresh
                sound_nback_right.tStartRefresh = tThisFlipGlobal  # on global time
                sound_nback_right.play(when=win_ref)  # sync with win flip
            if sound_nback_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_nback_right.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    sound_nback_right.tStop = t  # not accounting for scr refresh
                    sound_nback_right.frameNStop = frameN  # exact frame index
                    win_ref.timeOnFlip(sound_nback_right, 'tStopRefresh')  # time at next scr refresh
                    sound_nback_right.stop()
            # start/stop sound_nback_wrong
            if sound_nback_wrong.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                sound_nback_wrong.frameNStart = frameN  # exact frame index
                sound_nback_wrong.tStart = t  # local t and not account for scr refresh
                sound_nback_wrong.tStartRefresh = tThisFlipGlobal  # on global time
                sound_nback_wrong.play(when=win_ref)  # sync with win flip
            if sound_nback_wrong.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_nback_wrong.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    sound_nback_wrong.tStop = t  # not accounting for scr refresh
                    sound_nback_wrong.frameNStop = frameN  # exact frame index
                    win_ref.timeOnFlip(sound_nback_wrong, 'tStopRefresh')  # time at next scr refresh
                    sound_nback_wrong.stop()

            # check for quit (typically the Esc key)
            if endExpNow or def_keyresp.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in nback_fixation_soundComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "nback_fixation_sound"-------
        for thisComponent in nback_fixation_soundComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        nback_loop1.addData('n_back_visual_Text_Stim.started', n_back_visual_Text_Stim.tStartRefresh)
        nback_loop1.addData('n_back_visual_Text_Stim.stopped', n_back_visual_Text_Stim.tStopRefresh)
        sound_nback_right.stop()  # ensure sound has stopped at end of routine
        nback_loop1.addData('sound_nback_right.started', sound_nback_right.tStartRefresh)
        nback_loop1.addData('sound_nback_right.stopped', sound_nback_right.tStopRefresh)
        sound_nback_wrong.stop()  # ensure sound has stopped at end of routine
        nback_loop1.addData('sound_nback_wrong.started', sound_nback_wrong.tStartRefresh)
        nback_loop1.addData('sound_nback_wrong.stopped', sound_nback_wrong.tStopRefresh)

        # ------Prepare to start Routine "nback_checktimer1"-------
        continueRoutine_Part = True
        # update component parameters for each repeat
        if with_timer and (nback_timer.getTime() > nback_duration):
            nback_loop1.finished = True
        # keep track of which components have finished
        nback_checktimer1Components = []
        for thisComponent in nback_checktimer1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        nback_checktimer1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "nback_checktimer1"-------
        while continueRoutine_Part:
            # get current time
            t = nback_checktimer1Clock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=nback_checktimer1Clock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # check for quit (typically the Esc key)
            if endExpNow or def_keyresp.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in nback_checktimer1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "nback_checktimer1"-------
        for thisComponent in nback_checktimer1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "nback_checktimer1" was not non-slip safe, so reset the non-slip timer
        routine_timer_part.reset()
        experiment_Ref.nextEntry()





def nback(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, easy=True, timer_time_actual=600, timer_time_example=30, base_path=None, frameTolerance=None, endExpNow=None, defaultKeyboard=None, expInfo=None, num_reps=None, with_timer=True):
    logging_utilities.log_time(beginning_flag=True, routine_name=F'Global N-Back')
    # TODO we can use the timer=True here to create the while-loop inside here, checking again and again on the time

    # Initialize components for Routine "nback_welcome"
    nback_welcomeClock = core.Clock()
    text_4 = visual.TextStim(win=win_ref, name='text_4',
                             text="You will now start with the n-back memory task.\n\nYou will be asked to pay attention to a sequence of coloured squares and decide whether you have seen the same square 'n' times before. \nThere will be different sections of the test, which have different values for 'n'.  We will give you a trial session when the value of 'n' changes.\n\nPress [SPACE] to continue.",
                             font='Arial',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0);
    key_resp_5 = keyboard.Keyboard()

    text_nback_instructions = ''
    if easy:
        text_nback_instructions = 'n = 1\n\nThis is a short 1-back test, again, just to help you get started. You will have to press [SPACE] if you decide the coloured square one trial ago was the same as the current one.\n\nPlease press [SPACE] only when you decide the coloured square was repeated. \nNote that you will hear an unpleasant alert sound if you make a mistake and a positive sound if you make a correct answer. \nPress [SPACE] to begin.'
    else:
        text_nback_instructions = 'n = 2\n\nThis is a short 2-back test, again, just to help you get started. You will have to press [SPACE] if you decide the coloured square two trials ago was the same as the current one.\n\nPlease press [SPACE] only when you decide the coloured square was repeated. \nNote that you will hear an unpleasant alert sound if you make a mistake and a positive sound if you make a correct answer. \nPress [SPACE] to begin.'

    # Initialize components for Routine "nback_instructions"
    nback_instructionsClock = core.Clock()
    text_16 = visual.TextStim(win=win_ref, name='text_16',
                              text=text_nback_instructions,
                              font='Arial',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                              color='white', colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=0.0);
    key_resp_18 = keyboard.Keyboard()

    # Initialize components for Routine "nback_fixation_mute"
    nback_fixation_muteClock = core.Clock()
    n_back_text_stimuli = visual.TextStim(win=win_ref, name='n_back_text_stimuli',
                            text='',
                            font='Arial',
                            pos=[0, 0], height=1.0, wrapWidth=None, ori=0,
                            color='white', colorSpace='rgb', opacity=1,
                            languageStyle='LTR',
                            depth=0.0);

    # Initialize components for Routine "nback_trial"
    nback_trialClock = core.Clock()
    polygon = visual.Rect(
        win=win_ref, name='polygon',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0, 0], anchor='center',
        lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    key_resp_nback_trial = keyboard.Keyboard()

    # Initialize components for Routine "nback_fixation_sound"
    nback_fixation_soundClock = core.Clock()
    nback_last_answer = 0
    visual_Text_Stim = visual.TextStim(win=win_ref, name='visual_Text_Stim',
                          text='',
                          font='Arial',
                          pos=[0, 0], height=1.0, wrapWidth=None, ori=0,
                          color='white', colorSpace='rgb', opacity=1,
                          languageStyle='LTR',
                          depth=-1.0);
    sound_nback_right = sound.Sound(base_path + 'NeededFiles/Correct_Answer_Sound_Effect.flac', secs=1.0, stereo=True,
                                    hamming=True, name='sound_nback_right')
    sound_nback_right.setVolume(1.0)
    sound_nback_wrong = sound.Sound(base_path + 'NeededFiles/Wrong_Answer_Sound_Effect.flac', secs=1.0, stereo=True,
                                    hamming=True, name='sound_nback_wrong')
    sound_nback_wrong.setVolume(1.0)

    text_nback_instructions1_actual = ''
    if easy:
        text_nback_instructions1_actual = '\n\nThe actual task starts now!\n\nn = 1\n\nPlease press [SPACE] to continue.'
    else:
        text_nback_instructions1_actual = '\n\nThe actual task starts now!\n\nn = 2\n\nPlease press [SPACE] to continue.'

    # Initialize components for Routine "nback_instructions1_actual"
    nback_instructions1_actualClock = core.Clock()
    text_5 = visual.TextStim(win=win_ref, name='text_5',
                             text=text_nback_instructions1_actual,
                             font='Arial',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0);
    key_resp_6 = keyboard.Keyboard()

    # Initialize components for Routine "nback_timerstart"
    nback_timerstartClock = core.Clock()
    nback_timer = core.Clock()
    nback_duration = 60

    # Initialize components for Routine "nback_trial"
    nback_trialClock = core.Clock()
    polygon = visual.Rect(
        win=win_ref, name='polygon',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=1.0, pos=[0, 0], anchor='center',
        lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=0.0, interpolate=True)
    key_resp_nback_trial = keyboard.Keyboard()

    # Initialize components for Routine "nback_fixation_sound"
    nback_fixation_soundClock = core.Clock()
    nback_last_answer = 0
    visual_Text_Stim = visual.TextStim(win=win_ref, name='visual_Text_Stim',
                          text='',
                          font='Arial',
                          pos=[0, 0], height=1.0, wrapWidth=None, ori=0,
                          color='white', colorSpace='rgb', opacity=1,
                          languageStyle='LTR',
                          depth=-1.0);
    sound_nback_right = sound.Sound(base_path + 'NeededFiles/Correct_Answer_Sound_Effect.flac', secs=1.0, stereo=True,
                                    hamming=True, name='sound_nback_right')
    sound_nback_right.setVolume(1.0)
    sound_nback_wrong = sound.Sound(base_path + 'NeededFiles/Wrong_Answer_Sound_Effect.flac', secs=1.0, stereo=True,
                                    hamming=True, name='sound_nback_wrong')
    sound_nback_wrong.setVolume(1.0)

    # Initialize components for Routine "nback_checktimer1"
    nback_checktimer1Clock = core.Clock()

    # ------Prepare to start Routine "nback_welcome"-------
    logging_utilities.log_time(beginning_flag=True, routine_name=F'Instructions Example N-Back')
    experiment_Ref.addData('N_Back_example_trial_Instructions.started', win_ref.getFutureFlipTime(clock=None))
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    nback_welcomeComponents = [text_4, key_resp_5]
    for thisComponent in nback_welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nback_welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_welcome"-------
    while continueRoutine_Part:
        # get current time
        t = nback_welcomeClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nback_welcomeClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)

        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nback_welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nback_welcome"-------
    for thisComponent in nback_welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_4.started', text_4.tStartRefresh)
    experiment_Ref.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    experiment_Ref.addData('key_resp_5.keys', key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_5.rt', key_resp_5.rt)
    experiment_Ref.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    experiment_Ref.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    experiment_Ref.nextEntry()
    # the Routine "nback_welcome" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nback_instructions"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # keep track of which components have finished
    nback_instructionsComponents = [text_16, key_resp_18]
    for thisComponent in nback_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nback_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_instructions"-------
    while continueRoutine_Part:
        # get current time
        t = nback_instructionsClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nback_instructionsClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)

        # *key_resp_18* updates
        waitOnFlip = False
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nback_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nback_instructions"-------
    for thisComponent in nback_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_16.started', text_16.tStartRefresh)
    experiment_Ref.addData('text_16.stopped', text_16.tStopRefresh)
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    experiment_Ref.addData('key_resp_18.keys', key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_18.rt', key_resp_18.rt)
    experiment_Ref.addData('key_resp_18.started', key_resp_18.tStartRefresh)
    experiment_Ref.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
    experiment_Ref.nextEntry()
    # the Routine "nback_instructions" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nback_fixation_mute"-------
    continueRoutine_Part = True
    routine_timer_part.add(1.000000)
    # update component parameters for each repeat
    n_back_text_stimuli.setColor('white', colorSpace='rgb')
    n_back_text_stimuli.setPos((0, 0))
    n_back_text_stimuli.setText('+')
    n_back_text_stimuli.setFont('Arial')
    n_back_text_stimuli.setHeight(0.1)
    # keep track of which components have finished
    nback_fixation_muteComponents = [n_back_text_stimuli]
    for thisComponent in nback_fixation_muteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nback_fixation_muteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_fixation_mute"-------
    while continueRoutine_Part and routine_timer_part.getTime() > 0:
        # get current time
        t = nback_fixation_muteClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nback_fixation_muteClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *n_back_text_stimuli* updates
        if n_back_text_stimuli.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            n_back_text_stimuli.frameNStart = frameN  # exact frame index
            n_back_text_stimuli.tStart = t  # local t and not account for scr refresh
            n_back_text_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(n_back_text_stimuli, 'tStartRefresh')  # time at next scr refresh
            n_back_text_stimuli.setAutoDraw(True)
        if n_back_text_stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > n_back_text_stimuli.tStartRefresh + 1 - frameTolerance:
                # keep track of stop time/frame for later
                n_back_text_stimuli.tStop = t  # not accounting for scr refresh
                n_back_text_stimuli.frameNStop = frameN  # exact frame index
                win_ref.timeOnFlip(n_back_text_stimuli, 'tStopRefresh')  # time at next scr refresh
                n_back_text_stimuli.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nback_fixation_muteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nback_fixation_mute"-------
    for thisComponent in nback_fixation_muteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('n_back_text_stimuli.started', n_back_text_stimuli.tStartRefresh)
    experiment_Ref.addData('n_back_text_stimuli.stopped', n_back_text_stimuli.tStopRefresh)
    experiment_Ref.addData('N_Back_example_trial_Instructions.stopped', win_ref.getFutureFlipTime(clock=None))
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Instructions Example n-Back')

    clr_file = ''
    if easy:
        clr_file = base_path + 'NeededFiles/ColourTest1.xlsx'
    else:
        clr_file = base_path + 'NeededFiles/ColourTest2.xlsx'

    logging_utilities.log_time(beginning_flag=True, routine_name=F'Example N-Back Trial ({easy})')
    experiment_Ref.addData('N_Back_example_trial.started', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.addData('N_Back_easy_bool', easy)
    ### Don't get confused. This might look like the actual N-Back, but it is just the trial-part, so the very first showcasing of it!
    _nback(continueRoutine_Part=continueRoutine_Part, experiment_Ref=experiment_Ref,
           routine_timer_part=routine_timer_part, win_ref=win_ref,
           poly_ref=polygon, key_resp=key_resp_nback_trial, def_keyresp=defaultKeyboard, repetitions_of_nback_file=num_reps,
           nback_colorfile=clr_file, with_timer=with_timer, timer_duration=timer_time_example, nback_trialClock=nback_trialClock, expInfo=expInfo,
           endExpNow=endExpNow, frameTolerance=frameTolerance, sound_nback_right=sound_nback_right, base_path=base_path,
           sound_nback_wrong=sound_nback_wrong, nback_fixation_soundClock=nback_fixation_soundClock,
           nback_checktimer1Clock=nback_checktimer1Clock, n_back_visual_Text_Stim=visual_Text_Stim)
    experiment_Ref.addData('N_Back_example_trial.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Example N-Back Trial ({easy})')

    # ------Prepare to start Routine "nback_instructions1_actual"-------
    logging_utilities.log_time(beginning_flag=True, routine_name=F'N-Back Instructions')
    experiment_Ref.addData('N_Back_trial_Instructions.started', win_ref.getFutureFlipTime(clock=None))
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    nback_instructions1_actualComponents = [text_5, key_resp_6]
    for thisComponent in nback_instructions1_actualComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nback_instructions1_actualClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_instructions1_actual"-------
    while continueRoutine_Part:
        # get current time
        t = nback_instructions1_actualClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nback_instructions1_actualClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)

        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nback_instructions1_actualComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nback_instructions1_actual"-------
    for thisComponent in nback_instructions1_actualComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_5.started', text_5.tStartRefresh)
    experiment_Ref.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    experiment_Ref.addData('key_resp_6.keys', key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_6.rt', key_resp_6.rt)
    experiment_Ref.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    experiment_Ref.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    experiment_Ref.addData('N_Back_trial_Instructions.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging_utilities.log_time(beginning_flag=False, routine_name=F'N-Back Instructions')
    # the Routine "nback_instructions1_actual" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()
    continueRoutine_Part = True



    clr_file = ''
    if easy:
        clr_file = base_path + 'NeededFiles/ColourTest1_actual.xlsx'
    else:
        clr_file = base_path + 'NeededFiles/ColourTest2_actual.xlsx'


    ### Don't get confused. This might look like the actual N-Back, and it is the actual part, so the long mental-workload part!
    logging_utilities.log_time(beginning_flag=True, routine_name=F'N-Back Trial ({easy})')
    experiment_Ref.addData('N_Back_trial.started', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.addData('N_Back_easy_type_bool', easy)


    _nback(continueRoutine_Part=continueRoutine_Part, experiment_Ref=experiment_Ref,
           routine_timer_part=routine_timer_part, win_ref=win_ref,
           poly_ref=polygon, key_resp=key_resp_nback_trial, def_keyresp=defaultKeyboard, repetitions_of_nback_file=num_reps,
           nback_colorfile=clr_file, with_timer=with_timer, timer_duration=timer_time_actual, nback_trialClock=nback_trialClock,
           expInfo=expInfo,
           endExpNow=endExpNow, frameTolerance=frameTolerance, sound_nback_right=sound_nback_right, base_path=base_path,
           sound_nback_wrong=sound_nback_wrong, nback_fixation_soundClock=nback_fixation_soundClock,
           nback_checktimer1Clock=nback_checktimer1Clock, n_back_visual_Text_Stim=visual_Text_Stim)
    # completed 15.0 repeats of 'nback_loop1_actual'
    experiment_Ref.addData('N_Back_trial.stopped', win_ref.getFutureFlipTime(clock=None))
    logging_utilities.log_time(beginning_flag=False, routine_name=F'N-Back Trial ({easy})')
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Global N-Back')

