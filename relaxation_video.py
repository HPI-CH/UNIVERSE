from psychopy.hardware import keyboard
from psychopy import visual
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import logging_utilities
from psychopy import core, logging
import time


def relaxation_video(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard,video_timer):
    thisExp.addData('Relaxation_video_with_instructions.started', win.getFutureFlipTime(clock=None))
    logging_utilities.log_time(True, 'Relaxation-Video with instructions')

    # Initialize components for Routine "PreVideo"
    PreVideoClock = core.Clock()
    Welcome = visual.TextStim(win=win, name='Welcome',
                              text="You are about to watch a video for the next 10 minutes. Please make sure that the computer's sound is on.\n\n\n\n\nPlease press [SPACE] to continue",
                              font='Open Sans',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=0.0)
    key_Space = keyboard.Keyboard()




    # Initialize components for Routine "RelxationVideo"
    RelxationVideoClock = core.Clock()
    """
    RelaxationVideo = visual.VlcMovieStim(win, filename=base_path + 'NeededFiles/relaxation_video.mp4',
        size=600,  # set as `None` to use the native video size
        pos=[0, 0],  # pos specifies the /center/ of the movie stim location
        flipVert=False,  # flip the video picture vertically
        flipHoriz=False,  # flip the video picture horizontally
        loop=False,  # replay the video when it reaches the end
        autoStart=True)  # start the video automatically when first drawn
    """
    RelaxationVideo = visual.MovieStim2(win=win, filename=base_path + 'NeededFiles/relaxation_video.mp4',
                                        size=[1920, 1080], noAudio=False)  # VlcMovieStim
    # RelaxationVideo = visual.MovieStim3(
    #    win=win, name='RelaxationVideo', units='',
    #    noAudio = False,
    #    filename= base_path + 'NeededFiles/relaxation_video.mp4',
    #    ori=0.0, pos=(0, 0), opacity=None,
    #    loop=False, anchor='center',
    #    depth=0.0,
    #    )
    key_resp_17 = keyboard.Keyboard()

    image = visual.ImageStim(
        win=win,
        name='image',
        image=base_path + 'NeededFiles/Speaker_Icon.svg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.03), size=(0.1, 0.1),
        color=[1, 1, 1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)









    # ------Prepare to start Routine "PreVideo"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_Space.keys = []
    key_Space.rt = []
    _key_Space_allKeys = []


    logging.exp('start_video_logging: ' + str(time.time()))

    # keep track of which components have finished
    PreVideoComponents = [Welcome, key_Space, image]
    for thisComponent in PreVideoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PreVideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "PreVideo"-------
    while continueRoutine:
        # get current time
        t = PreVideoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PreVideoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome* updates
        if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome.frameNStart = frameN  # exact frame index
            Welcome.tStart = t  # local t and not account for scr refresh
            Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
            Welcome.setAutoDraw(True)
        
        # *key_Space* updates
        waitOnFlip = False
        if key_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_Space.frameNStart = frameN  # exact frame index
            key_Space.tStart = t  # local t and not account for scr refresh
            key_Space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_Space, 'tStartRefresh')  # time at next scr refresh
            key_Space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_Space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_Space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_Space.status == STARTED and not waitOnFlip:
            theseKeys = key_Space.getKeys(keyList=['space'], waitRelease=False)
            _key_Space_allKeys.extend(theseKeys)
            if len(_key_Space_allKeys):
                key_Space.keys = _key_Space_allKeys[-1].name  # just the last key pressed
                key_Space.rt = _key_Space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PreVideoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "PreVideo"-------
    for thisComponent in PreVideoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome.started', Welcome.tStartRefresh)
    thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
    # check responses
    if key_Space.keys in ['', [], None]:  # No response was made
        key_Space.keys = None
    thisExp.addData('key_Space.keys',key_Space.keys)
    if key_Space.keys != None:  # we had a response
        thisExp.addData('key_Space.rt', key_Space.rt)
    thisExp.addData('key_Space.started', key_Space.tStartRefresh)
    thisExp.addData('key_Space.stopped', key_Space.tStopRefresh)
    thisExp.nextEntry()
    thisExp.addData('image.started', image.tStartRefresh)
    thisExp.addData('image.stopped', image.tStopRefresh)
    # the Routine "PreVideo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "RelxationVideo"-------
    logging_utilities.log_time(True, 'Relaxation-Video')
    thisExp.addData('Relaxation_video.started', win.getFutureFlipTime(clock=None))
    continueRoutine = True
    routineTimer.add(video_timer)
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    RelxationVideoComponents = [RelaxationVideo, key_resp_17]
    for thisComponent in RelxationVideoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RelxationVideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "RelxationVideo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RelxationVideoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RelxationVideoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RelaxationVideo* updates
        if RelaxationVideo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RelaxationVideo.frameNStart = frameN  # exact frame index
            RelaxationVideo.tStart = t  # local t and not account for scr refresh
            RelaxationVideo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RelaxationVideo, 'tStartRefresh')  # time at next scr refresh
            RelaxationVideo.setAutoDraw(True)
        if RelaxationVideo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RelaxationVideo.tStartRefresh + video_timer - frameTolerance:
                # keep track of stop time/frame for later
                RelaxationVideo.tStop = t  # not accounting for scr refresh
                RelaxationVideo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RelaxationVideo, 'tStopRefresh')  # time at next scr refresh
                RelaxationVideo.setAutoDraw(False)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_17.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_17.tStop = t  # not accounting for scr refresh
                key_resp_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_17, 'tStopRefresh')  # time at next scr refresh
                key_resp_17.status = FINISHED
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RelxationVideoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "RelxationVideo"-------
    for thisComponent in RelxationVideoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RelaxationVideo.stop()
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    thisExp.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        thisExp.addData('key_resp_17.rt', key_resp_17.rt)
    thisExp.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    thisExp.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    thisExp.addData('Relaxation_video.stopped', win.getFutureFlipTime(clock=None))
    thisExp.nextEntry()
    logging_utilities.log_time(False, 'Relaxation-Video')
    thisExp.addData('Relaxation_video_with_instructions.stopped', win.getFutureFlipTime(clock=None))
    logging_utilities.log_time(False, 'Relaxation-Video with instructions')
