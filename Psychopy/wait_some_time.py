from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.hardware import keyboard
from logging_utilities import log_time
import logging_utilities

def wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500):
    # Initialize components for Routine "delay_500"
    logging_utilities.log_time(True, 'Delay')
    experiment_Ref.addData('Delay.started', win.getFutureFlipTime(clock=None))

    routine_timer_part = core.CountdownTimer()

    delay_500Clock = core.Clock()
    textEmpty = visual.TextStim(win=win, name='textEmpty',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0)

    # ------Prepare to start Routine "delay_500"-------
    continueRoutine_Part = True
    time_in_seconds = time_in_ms/1000
    routine_timer_part.add(time_in_seconds)
    # update component parameters for each repeat
    # keep track of which components have finished
    delay_500Components = [textEmpty]
    for thisComponent in delay_500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delay_500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "delay_500"-------
    while continueRoutine_Part and routine_timer_part.getTime() > 0:
        # get current time
        t = delay_500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delay_500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEmpty* updates
        if textEmpty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEmpty.frameNStart = frameN  # exact frame index
            textEmpty.tStart = t  # local t and not account for scr refresh
            textEmpty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEmpty, 'tStartRefresh')  # time at next scr refresh
            textEmpty.setAutoDraw(True)
        if textEmpty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textEmpty.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textEmpty.tStop = t  # not accounting for scr refresh
                textEmpty.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textEmpty, 'tStopRefresh')  # time at next scr refresh
                textEmpty.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in delay_500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "delay_500"-------
    for thisComponent in delay_500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textEmpty.started', textEmpty.tStartRefresh)
    experiment_Ref.addData('textEmpty.stopped', textEmpty.tStopRefresh)

    experiment_Ref.addData('Delay.ended', win.getFutureFlipTime(clock=None))
    logging_utilities.log_time(False, 'Delay')

