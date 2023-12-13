import datetime
import time
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout


import logging_utilities
from psychopy.hardware import keyboard

def sync_muse_w_psychopy(experiment_Ref, win_ref, expInfo, frameTolerance, defaultKeyboard, endExpNow,
                         text_to_display_for_sync='* STOP! *\n\n DO NOT press any key before the supervisor is present!! \n\nPlease ask the supervisor to come before continuing!! \n\n\nPlease hit [SPACE] strongly four times with your non-dominant hand until the next slide appears.',
                         text_to_display_for_continuation='Thank you!\n\nDuring the experiment, please try to avoid talking and big body movements as much as possible.\n\nPress [ENTER] to continue.'):

    logging_utilities.log_time(beginning_flag=True, routine_name=F'Muse - Psychopy Synchronization)')
    experiment_Ref.nextEntry()
    experiment_Ref.addData('Synchronization_Muse_Psychopy.started', win_ref.getFutureFlipTime(clock=None))

    Sync_muse_psychopyClock = core.Clock()
    text_14 = visual.TextStim(win=win_ref, name='text_14',
                              text=text_to_display_for_sync,
                              font='Open Sans',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=0.0);
    key_resp_14 = keyboard.Keyboard()

    # set up handler to look after randomisation of conditions etc
    sync_loop_muse = data.TrialHandler(nReps=4.0, method='sequential',
                                       extraInfo=expInfo, originPath=-1,
                                       trialList=[None],
                                       seed=None, name='sync_loop_muse')
    experiment_Ref.addLoop(sync_loop_muse)  # add the loop to the experiment
    thisSync_loop_muse = sync_loop_muse.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSync_loop_muse.rgb)
    if thisSync_loop_muse != None:
        for paramName in thisSync_loop_muse:
            exec('{} = thisSync_loop_muse[paramName]'.format(paramName))

    for thisSync_loop_muse in sync_loop_muse:
        currentLoop = sync_loop_muse
        # abbreviate parameter names if possible (e.g. rgb = thisSync_loop_muse.rgb)
        if thisSync_loop_muse != None:
            for paramName in thisSync_loop_muse:
                exec('{} = thisSync_loop_muse[paramName]'.format(paramName))

        # ------Prepare to start Routine "Sync_muse_psychopy"-------
        continueRoutine_Part = True
        # update component parameters for each repeat
        key_resp_14.keys = []
        key_resp_14.rt = []
        _key_resp_14_allKeys = []
        # keep track of which components have finished
        Sync_muse_psychopyComponents = [text_14, key_resp_14]
        for thisComponent in Sync_muse_psychopyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED



        # reset timers
        t = 0
        _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
        Sync_muse_psychopyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Sync_muse_psychopy"-------
        while continueRoutine_Part:
            # get current time
            t = Sync_muse_psychopyClock.getTime()
            tThisFlip = win_ref.getFutureFlipTime(clock=Sync_muse_psychopyClock)
            tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)

            # *key_resp_14* updates
            waitOnFlip = False
            if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                key_resp_14.frameNStart = frameN  # exact frame index
                key_resp_14.tStart = t  # local t and not account for scr refresh
                key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                win_ref.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                key_resp_14.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win_ref.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                win_ref.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_14.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_14_allKeys.extend(theseKeys)
                if len(_key_resp_14_allKeys):
                    key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                    key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine_Part = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine_Part:  # a component has requested a forced-end of Routine
                break
            continueRoutine_Part = False  # will revert to True if at least one component still running
            for thisComponent in Sync_muse_psychopyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine_Part = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
                win_ref.flip()

        # -------Ending Routine "Sync_muse_psychopy"-------
        for thisComponent in Sync_muse_psychopyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sync_loop_muse.addData('text_14.started', text_14.tStartRefresh)
        sync_loop_muse.addData('text_14.stopped', text_14.tStopRefresh)
        # check responses
        if key_resp_14.keys in ['', [], None]:  # No response was made
            key_resp_14.keys = None
        sync_loop_muse.addData('key_resp_14.keys', key_resp_14.keys)
        if key_resp_14.keys != None:  # we had a response
            sync_loop_muse.addData('key_resp_14.rt', key_resp_14.rt)
        sync_loop_muse.addData('key_resp_14.started', key_resp_14.tStartRefresh)
        sync_loop_muse.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
        # the Routine "Sync_muse_psychopy" was not non-slip safe, so reset the non-slip timer
        # routine_timer_part.reset()
        experiment_Ref.nextEntry()

    # ------Prepare to start Routine "post_sync_slide"-------
    post_sync_slideClock = core.Clock()
    text_13 = visual.TextStim(win=win_ref, name='text_13',
                              text=text_to_display_for_continuation,
                              font='Open Sans',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=0.0);
    key_resp_13 = keyboard.Keyboard()

    continueRoutine = True
    # update component parameters for each repeat
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    post_sync_slideComponents = [text_13, key_resp_13]
    for thisComponent in post_sync_slideComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    post_sync_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "post_sync_slide"-------
    while continueRoutine:
        # get current time
        t = post_sync_slideClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=post_sync_slideClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)

        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in post_sync_slideComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "post_sync_slide"-------
    for thisComponent in post_sync_slideComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('text_13.started', text_13.tStartRefresh)
    experiment_Ref.addData('text_13.stopped', text_13.tStopRefresh)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    experiment_Ref.addData('key_resp_13.keys', key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_13.rt', key_resp_13.rt)
    experiment_Ref.addData('key_resp_13.started', key_resp_13.tStartRefresh)
    experiment_Ref.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)

    # the Routine "post_sync_slide" was not non-slip safe, so reset the non-slip timer
    #routineTimer.reset()

    experiment_Ref.addData('Synchronization_Muse_Psychopy.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Muse - Psychopy Synchronization)')

