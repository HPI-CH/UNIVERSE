#from psychopy import locale_setup
#from psychopy import prefs
#prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import time
import logging_utilities
from psychopy.hardware import keyboard


def eye_closing(experiment_Ref, routine_timer_part, win_ref, eye_closing_timer, frameTolerance,endExpNow, defaultKeyboard, base_path):
    logging_utilities.log_time(True, 'Eye-Closing')
    experiment_Ref.addData('close_eyes_instruction.started', win_ref.getFutureFlipTime(clock=None))

    win = win_ref
    thisExp = experiment_Ref
    routineTimer = routine_timer_part

    # Initialize components for Routine "ThankYou_close_eyes"
    ThankYou_close_eyesClock = core.Clock()
    text = visual.TextStim(win=win, name='text',
                           text='Thank you for your answers!\n\nWe will now ask you to close your eyes for one minute and relax. You will hear a sound when the minute is over.\n\nPress [SPACE] when you have your eyes closed and are ready to start. Please do not open your eyes again until you hear the sound.',
                           font='Open Sans',
                           pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                           color='white', colorSpace='rgb', opacity=None,
                           languageStyle='LTR',
                           depth=0.0)
    key_resp_20 = keyboard.Keyboard()


    # Initialize components for Routine "eye_closing_baseline"
    eye_closing_baselineClock = core.Clock()
    # sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    #    name='sound_1')
    # sound_1.setVolume(1.0)
    sound_1 = sound.Sound(base_path + 'NeededFiles/eye_closing_sound.wav', secs=1.0, stereo=True, hamming=True,
                          name='sound_1')
    sound_1.setVolume(1.0)
    text_17 = visual.TextStim(win=win, name='text_17',
                              text='Close your eyes until you hear a sound of the computer.',
                              font='Open Sans',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=-1.0)
    key_resp_19 = keyboard.Keyboard()




    # ------Prepare to start Routine "ThankYou_close_eyes"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    ThankYou_close_eyesComponents = [text, key_resp_20]
    for thisComponent in ThankYou_close_eyesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ThankYou_close_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "ThankYou_close_eyes"-------
    while continueRoutine:
        # get current time
        t = ThankYou_close_eyesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ThankYou_close_eyesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYou_close_eyesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ThankYou_close_eyes"-------
    for thisComponent in ThankYou_close_eyesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    thisExp.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        thisExp.addData('key_resp_20.rt', key_resp_20.rt)
    thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
    thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "ThankYou_close_eyes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "eye_closing_baseline"-------
    continueRoutine = True
    routineTimer.add(eye_closing_timer)
    # update component parameters for each repeat
    sound_1 = sound.Sound(base_path + 'NeededFiles/eye_closing_sound.wav', secs=1.0, stereo=True, hamming=True, name='sound_1')
    #sound_1.setSound(base_path + 'NeededFiles/eye_closing_sound.wav', secs=1.0, hamming=True, name='sound_1')
    sound_1.setVolume(1.0, log=False)
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []


    logging.exp('start_baseline_logging: ' + str(time.time()))

    # keep track of which components have finished
    eye_closing_baselineComponents = [sound_1, text_17, key_resp_19]
    for thisComponent in eye_closing_baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eye_closing_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    logging_utilities.log_time(True, 'Eye Closing Routine')
    # -------Run Routine "eye_closing_baseline"-------
    experiment_Ref.addData('Eye_closing.started', win_ref.getFutureFlipTime(clock=None))
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = eye_closing_baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eye_closing_baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        #if sound_1.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
        if sound_1.status == NOT_STARTED and eye_closing_timer - tThisFlip <= 1.0 - frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()
        #if sound_1.status == STARTED and eye_closing_timer - tThisFlip <= 1.0 + frameTolerance:
        if sound_1.status == STARTED and routineTimer.getTime() - frameTolerance <= 0:
            # is it time to stop? (based on global clock, using actual start)
            #TODO: SAMIK: arreglar este de aqui para que sea u poco antes de que se acabe y se escriba al log csv file
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.0 + frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.tStopRefresh = tThisFlipGlobal
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + eye_closing_timer-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_19.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_19.tStop = t  # not accounting for scr refresh
                key_resp_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_19, 'tStopRefresh')  # time at next scr refresh
                key_resp_19.status = FINISHED
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eye_closing_baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "eye_closing_baseline"-------
    for thisComponent in eye_closing_baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('sound_1.started', sound_1.tStartRefresh)
    thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)
    thisExp.addData('text_17.started', text_17.tStartRefresh)
    thisExp.addData('text_17.stopped', text_17.tStopRefresh)
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    thisExp.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        thisExp.addData('key_resp_19.rt', key_resp_19.rt)
    thisExp.addData('key_resp_19.started', key_resp_19.tStartRefresh)
    thisExp.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
    experiment_Ref.addData('Eye_closing.stopped', win_ref.getFutureFlipTime(clock=None))
    thisExp.nextEntry()
    logging_utilities.log_time(False, 'Eye Closing Routine')
    logging_utilities.log_time(False, 'Eye-Closing')
