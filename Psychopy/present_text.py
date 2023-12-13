from psychopy import visual, core
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import logging_utilities


def present_text(experiment_Ref, win, frameTolerance, defaultKeyboard,
                 endExpNow, visual_stim=None, test_text='STILL SAMPLE TEXT', name_for_logs='default_log_name'):

    present_textClock = core.Clock()
    present_textClock.reset()

    logging_utilities.log_time(True, 'presenting the text: {}'.format(test_text))
    experiment_Ref.addData('Present_Text.started', win.getFutureFlipTime(clock=None))

    # Initialize components for Routine "WelcomeWindow"
    intermediate_text_arithmetixClock = core.Clock()
    text_intermediate_text_arithmetixClock = visual.TextStim(win=win, name=name_for_logs,
                                                             text=test_text,
                                                             font='Arial',
                                                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                                             color='white', colorSpace='rgb', opacity=1,
                                                             languageStyle='LTR',
                                                             depth=0.0);
    key_resp_intermediate_text_arithmetixClock = keyboard.Keyboard()


    # ------Prepare to start Routine "intermediate_text_arithmetix"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_intermediate_text_arithmetixClock.keys = []
    key_resp_intermediate_text_arithmetixClock.rt = []
    _key_resp_intermediate_text_arithmetixClock = []
    # keep track of which components have finished
    intermediate_text_arithmetixClockComponents = []
    if visual_stim != None:
        intermediate_text_arithmetixClockComponents = [text_intermediate_text_arithmetixClock,
                                                       key_resp_intermediate_text_arithmetixClock, visual_stim]
    else:
        intermediate_text_arithmetixClockComponents = [text_intermediate_text_arithmetixClock,
                                                       key_resp_intermediate_text_arithmetixClock]

    for thisComponent in intermediate_text_arithmetixClockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intermediate_text_arithmetixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nback_welcome"-------
    while continueRoutine_Part:
        # get current time
        t = intermediate_text_arithmetixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=present_textClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *intermediate_text_arithmetixClock* updates
        if text_intermediate_text_arithmetixClock.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_intermediate_text_arithmetixClock.frameNStart = frameN  # exact frame index
            text_intermediate_text_arithmetixClock.tStart = t  # local t and not account for scr refresh
            text_intermediate_text_arithmetixClock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_intermediate_text_arithmetixClock, 'tStartRefresh')  # time at next scr refresh
            text_intermediate_text_arithmetixClock.setAutoDraw(True)

        # *key_resp_intermediate_text_arithmetixClock* updates
        waitOnFlip = False
        if key_resp_intermediate_text_arithmetixClock.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_intermediate_text_arithmetixClock.frameNStart = frameN  # exact frame index
            key_resp_intermediate_text_arithmetixClock.tStart = t  # local t and not account for scr refresh
            key_resp_intermediate_text_arithmetixClock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_intermediate_text_arithmetixClock, 'tStartRefresh')  # time at next scr refresh
            key_resp_intermediate_text_arithmetixClock.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_intermediate_text_arithmetixClock.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_intermediate_text_arithmetixClock.clearEvents,
                           eventType='keyboard')  # clear events on next screen flip
        if key_resp_intermediate_text_arithmetixClock.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_intermediate_text_arithmetixClock.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_intermediate_text_arithmetixClock.extend(theseKeys)
            if len(_key_resp_intermediate_text_arithmetixClock):
                key_resp_intermediate_text_arithmetixClock.keys = _key_resp_intermediate_text_arithmetixClock[
                    -1].name  # just the last key pressed
                key_resp_intermediate_text_arithmetixClock.rt = _key_resp_intermediate_text_arithmetixClock[-1].rt
                # a response ends the routine
                continueRoutine_Part = False

        if visual_stim != None:
            # *image* updates
            if visual_stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                visual_stim.frameNStart = frameN  # exact frame index
                visual_stim.tStart = t  # local t and not account for scr refresh
                visual_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(visual_stim, 'tStartRefresh')  # time at next scr refresh
                visual_stim.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in intermediate_text_arithmetixClockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "nback_welcome"-------
    for thisComponent in intermediate_text_arithmetixClockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_intermediate_text_arithmetixClock.started',
                           text_intermediate_text_arithmetixClock.tStartRefresh)
    experiment_Ref.addData('text_intermediate_text_arithmetixClock.stopped',
                           text_intermediate_text_arithmetixClock.tStopRefresh)
    # check responses
    if key_resp_intermediate_text_arithmetixClock.keys in ['', [], None]:  # No response was made
        key_resp_intermediate_text_arithmetixClock.keys = None
    experiment_Ref.addData('key_resp_intermediate_text_arithmetixClock.keys',
                           key_resp_intermediate_text_arithmetixClock.keys)
    if key_resp_intermediate_text_arithmetixClock.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_intermediate_text_arithmetixClock.rt',
                               key_resp_intermediate_text_arithmetixClock.rt)
    experiment_Ref.addData('key_resp_intermediate_text_arithmetixClock.started',
                           key_resp_intermediate_text_arithmetixClock.tStartRefresh)
    experiment_Ref.addData('key_resp_intermediate_text_arithmetixClock.stopped',
                           key_resp_intermediate_text_arithmetixClock.tStopRefresh)


    experiment_Ref.addData('Present_Text.stopped', win.getFutureFlipTime(clock=None))
    logging_utilities.log_time(False, 'presenting the text: {}'.format(test_text))
