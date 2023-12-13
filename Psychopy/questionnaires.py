from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from wait_some_time import wait_some_time
import logging_utilities
 

def affective_slider(base_path, thisExp, routineTimer, win, frameTolerance, endExpNow, defaultKeyboard):
    logging_utilities.log_time(True, 'Affective-Slider')
    thisExp.addData('AffectiveSlider.started', win.getFutureFlipTime(clock=None))

    # Initialize components for Routine "affectiveSlider"
    affectiveSliderClock = core.Clock()
    sliderValence = visual.Slider(win=win, name='sliderValence',
                                  startValue=0.5, size=(1.0, 0.05), pos=(0, 0.2), units=None,
                                  labels=None, ticks=(0, 0.5, 1), granularity=0.0,
                                  style='rating', styleTweaks=('triangleMarker',), opacity=None,
                                  labelColor='LightGray', markerColor='black', lineColor='LightGray', colorSpace='rgb',
                                  font='Open Sans', labelHeight=0.05,
                                  flip=False, ori=0.0, depth=0, readOnly=False)
    imageValence_0 = visual.ImageStim(
        win=win,
        name='imageValence_0',
        image=base_path + 'NeededFiles/valence_0.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, 0.2), size=(0.1, 0.1),
        color=[1, 1, 1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageValence_1 = visual.ImageStim(
        win=win,
        name='imageValence_1',
        image=base_path + 'NeededFiles/valence_1.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.2), size=(0.1, 0.1),
        color=[1, 1, 1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    sliderArousal = visual.Slider(win=win, name='sliderArousal',
                                  startValue=0.5, size=(1.0, 0.05), pos=(0, -0.2), units=None,
                                  labels=None, ticks=(0, 0.5, 1), granularity=0.0,
                                  style='rating', styleTweaks=('triangleMarker',), opacity=None,
                                  labelColor='LightGray', markerColor='black', lineColor='LightGray', colorSpace='rgb',
                                  font='Open Sans', labelHeight=0.05,
                                  flip=False, ori=0.0, depth=-3, readOnly=False)
    imageArousal_0 = visual.ImageStim(
        win=win,
        name='imageArousal_0',
        image=base_path + 'NeededFiles/arousal_0.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.2), size=(0.1, 0.1),
        color=[1, 1, 1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    imageArousal_1 = visual.ImageStim(
        win=win,
        name='imageArousal_1',
        image=base_path + 'NeededFiles/arousal_1.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.2), size=(0.1, 0.1),
        color=[1, 1, 1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    buttonNext_5 = visual.ButtonStim(win,
                                     text='Next >', font='Arvo',
                                     pos=(0, -0.4),
                                     letterHeight=0.05,
                                     size=(0.2, 0.1), borderWidth=0.0,
                                     fillColor='darkgrey', borderColor=None,
                                     color='white', colorSpace='rgb',
                                     opacity=None,
                                     bold=True, italic=False,
                                     padding=None,
                                     anchor='center',
                                     name='buttonNext_5'
                                     )
    buttonNext_5.buttonClock = core.Clock()
    text_19 = visual.TextStim(win=win, name='text_19',
                              text='Move the slider to rate your level of Pleasure',
                              font='Open Sans',
                              pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=-7.0);
    text_20 = visual.TextStim(win=win, name='text_20',
                              text='Move the slider to rate your level of Arousal',
                              font='Open Sans',
                              pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=-8.0);


    # ------Prepare to start Routine "affectiveSlider"-------
    continueRoutine = True
    # update component parameters for each repeat
    sliderValence.reset()
    sliderArousal.reset()
    # keep track of which components have finished
    affectiveSliderComponents = [sliderValence, imageValence_0, imageValence_1, sliderArousal, imageArousal_0, imageArousal_1, buttonNext_5, text_19, text_20]
    for thisComponent in affectiveSliderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    affectiveSliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "affectiveSlider"-------
    logging_utilities.log_time(True, 'Affective-Slider (Routine)')

    while continueRoutine:
        # get current time
        t = affectiveSliderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=affectiveSliderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sliderValence* updates
        if sliderValence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderValence.frameNStart = frameN  # exact frame index
            sliderValence.tStart = t  # local t and not account for scr refresh
            sliderValence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderValence, 'tStartRefresh')  # time at next scr refresh
            sliderValence.setAutoDraw(True)
        
        # *imageValence_0* updates
        if imageValence_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageValence_0.frameNStart = frameN  # exact frame index
            imageValence_0.tStart = t  # local t and not account for scr refresh
            imageValence_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageValence_0, 'tStartRefresh')  # time at next scr refresh
            imageValence_0.setAutoDraw(True)
        
        # *imageValence_1* updates
        if imageValence_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageValence_1.frameNStart = frameN  # exact frame index
            imageValence_1.tStart = t  # local t and not account for scr refresh
            imageValence_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageValence_1, 'tStartRefresh')  # time at next scr refresh
            imageValence_1.setAutoDraw(True)
        
        # *sliderArousal* updates
        if sliderArousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderArousal.frameNStart = frameN  # exact frame index
            sliderArousal.tStart = t  # local t and not account for scr refresh
            sliderArousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderArousal, 'tStartRefresh')  # time at next scr refresh
            sliderArousal.setAutoDraw(True)
        
        # *imageArousal_0* updates
        if imageArousal_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageArousal_0.frameNStart = frameN  # exact frame index
            imageArousal_0.tStart = t  # local t and not account for scr refresh
            imageArousal_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageArousal_0, 'tStartRefresh')  # time at next scr refresh
            imageArousal_0.setAutoDraw(True)
        
        # *imageArousal_1* updates
        if imageArousal_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageArousal_1.frameNStart = frameN  # exact frame index
            imageArousal_1.tStart = t  # local t and not account for scr refresh
            imageArousal_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageArousal_1, 'tStartRefresh')  # time at next scr refresh
            imageArousal_1.setAutoDraw(True)
        
        # *buttonNext_5* updates
        if buttonNext_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonNext_5.frameNStart = frameN  # exact frame index
            buttonNext_5.tStart = t  # local t and not account for scr refresh
            buttonNext_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonNext_5, 'tStartRefresh')  # time at next scr refresh
            buttonNext_5.setAutoDraw(True)
        if buttonNext_5.status == STARTED:
            # check whether buttonNext_5 has been pressed
            if buttonNext_5.isClicked:
                if not buttonNext_5.wasClicked:
                    buttonNext_5.timesOn.append(buttonNext_5.buttonClock.getTime()) # store time of first click
                    buttonNext_5.timesOff.append(buttonNext_5.buttonClock.getTime()) # store time clicked until
                else:
                    buttonNext_5.timesOff[-1] = buttonNext_5.buttonClock.getTime() # update time clicked until
                if not buttonNext_5.wasClicked:
                    continueRoutine = False  # end routine when buttonNext_5 is clicked
                buttonNext_5.wasClicked = True  # if buttonNext_5 is still clicked next frame, it is not a new click
            else:
                buttonNext_5.wasClicked = False  # if buttonNext_5 is clicked next frame, it is a new click
        else:
            buttonNext_5.wasClicked = False  # if buttonNext_5 is clicked next frame, it is a new click
        
        # *text_19* updates
        if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            text_19.setAutoDraw(True)
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            text_20.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in affectiveSliderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "affectiveSlider"-------
    for thisComponent in affectiveSliderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('sliderValence.response', sliderValence.getRating())
    thisExp.addData('sliderValence.rt', sliderValence.getRT())
    thisExp.addData('sliderValence.started', sliderValence.tStartRefresh)
    thisExp.addData('sliderValence.stopped', sliderValence.tStopRefresh)
    thisExp.addData('imageValence_0.started', imageValence_0.tStartRefresh)
    thisExp.addData('imageValence_0.stopped', imageValence_0.tStopRefresh)
    thisExp.addData('imageValence_1.started', imageValence_1.tStartRefresh)
    thisExp.addData('imageValence_1.stopped', imageValence_1.tStopRefresh)
    thisExp.addData('sliderArousal.response', sliderArousal.getRating())
    thisExp.addData('sliderArousal.rt', sliderArousal.getRT())
    thisExp.addData('sliderArousal.started', sliderArousal.tStartRefresh)
    thisExp.addData('sliderArousal.stopped', sliderArousal.tStopRefresh)
    thisExp.addData('imageArousal_0.started', imageArousal_0.tStartRefresh)
    thisExp.addData('imageArousal_0.stopped', imageArousal_0.tStopRefresh)
    thisExp.addData('imageArousal_1.started', imageArousal_1.tStartRefresh)
    thisExp.addData('imageArousal_1.stopped', imageArousal_1.tStopRefresh)
    thisExp.addData('buttonNext_5.started', buttonNext_5.tStartRefresh)
    thisExp.addData('buttonNext_5.stopped', buttonNext_5.tStopRefresh)
    thisExp.addData('buttonNext_5.numClicks', buttonNext_5.numClicks)
    if buttonNext_5.numClicks:
       thisExp.addData('buttonNext_5.timesOn', buttonNext_5.timesOn)
       thisExp.addData('buttonNext_5.timesOff', buttonNext_5.timesOff)
    else:
       thisExp.addData('buttonNext_5.timesOn', "")
       thisExp.addData('buttonNext_5.timesOff', "")
    thisExp.addData('text_19.started', text_19.tStartRefresh)
    thisExp.addData('text_19.stopped', text_19.tStopRefresh)
    thisExp.addData('text_20.started', text_20.tStartRefresh)
    thisExp.addData('text_20.stopped', text_20.tStopRefresh)
    thisExp.addData('AffectiveSlider.stopped', win.getFutureFlipTime(clock=None))
    thisExp.nextEntry()
    # the Routine "affectiveSlider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    logging_utilities.log_time(False, 'Affective-Slider')

def panas(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref,frameTolerance, endExpNow, defaultKeyboard):

    experiment_Ref.addData('Panas.started', win_ref.getFutureFlipTime(clock=None))

    win = win_ref
    logging_utilities.log_time(True, 'PANAS')
    # Initialize components for Routine "WelcomePANAS"
    WelcomePANASClock = core.Clock()
    textWelcome = visual.TextStim(win=win_ref, name='textWelcome',
        text='Indicate the extent of the stated feelings right now ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keySpace = keyboard.Keyboard()
    textSpaceHint = visual.TextStim(win=win_ref, name='textSpaceHint',
        text='Press [SPACE] to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);

    # Initialize components for Routine "PANAS_1_5"
    PANAS_1_5Clock = core.Clock()
    textInterested = visual.TextStim(win=win_ref, name='textInterested',
        text='Interested',
        font='Open Sans',
        pos=(-0.7, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderInterested = visual.Slider(win=win_ref, name='sliderInterested',
        startValue=None, size=(1, 0.05), pos=(0.2, 0.35), units=None,
        labels=['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=True, ori=0.0, depth=-1, readOnly=False)
    textDistressed = visual.TextStim(win=win_ref, name='textDistressed',
        text='Distressed',
        font='Open Sans',
        pos=(-0.7, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sliderDistressed = visual.Slider(win=win_ref, name='sliderDistressed',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.2), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    textExcited = visual.TextStim(win=win_ref, name='textExcited',
        text='Excited',
        font='Open Sans',
        pos=(-0.7, 0.05), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    sliderExcited = visual.Slider(win=win_ref, name='sliderExcited',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.05), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    textUpset = visual.TextStim(win=win_ref, name='textUpset',
        text='Upset',
        font='Open Sans',
        pos=(-0.7, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    sliderUpset = visual.Slider(win=win_ref, name='sliderUpset',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.1), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    textStrong = visual.TextStim(win=win_ref, name='textStrong',
        text='Strong',
        font='Open Sans',
        pos=(-0.7, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    sliderStrong = visual.Slider(win=win_ref, name='sliderStrong',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.25), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    buttonNext = visual.ButtonStim(win=win_ref, 
        text='Next >', font='Arvo',
        pos=(0.7, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext'
    )
    buttonNext.buttonClock = core.Clock()

    # Initialize components for Routine "PANAS_6_10"
    PANAS_6_10Clock = core.Clock()
    textGuilty = visual.TextStim(win=win_ref, name='textGuilty',
        text='Guilty',
        font='Open Sans',
        pos=(-0.7, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderGuilty = visual.Slider(win=win_ref, name='sliderGuilty',
        startValue=None, size=(1, 0.05), pos=(0.2, 0.35), units=None,
        labels=['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=True, ori=0.0, depth=-1, readOnly=False)
    textScared = visual.TextStim(win=win_ref, name='textScared',
        text='Scared',
        font='Open Sans',
        pos=(-0.7, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sliderScared = visual.Slider(win=win_ref, name='sliderScared',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.2), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    textHostile = visual.TextStim(win=win_ref, name='textHostile',
        text='Hostile',
        font='Open Sans',
        pos=(-0.7, 0.05), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    sliderHostile = visual.Slider(win=win_ref, name='sliderHostile',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.05), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    textEnthusiastic = visual.TextStim(win=win_ref, name='textEnthusiastic',
        text='Enthusiastic',
        font='Open Sans',
        pos=(-0.7, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    sliderEnthusiastic = visual.Slider(win=win_ref, name='sliderEnthusiastic',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.1), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    textProud = visual.TextStim(win=win_ref, name='textProud',
        text='Proud',
        font='Open Sans',
        pos=(-0.7, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    sliderProud = visual.Slider(win=win_ref, name='sliderProud',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.25), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    buttonNext_2 = visual.ButtonStim(win=win_ref, 
        text='Next >', font='Arvo',
        pos=(0.7, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext_2'
    )
    buttonNext_2.buttonClock = core.Clock()

    # Initialize components for Routine "PANAS_11_15"
    PANAS_11_15Clock = core.Clock()
    textIrritable = visual.TextStim(win=win_ref, name='textIrritable',
        text='Irritable',
        font='Open Sans',
        pos=(-0.7, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderIrritable = visual.Slider(win=win_ref, name='sliderIrritable',
        startValue=None, size=(1, 0.05), pos=(0.2, 0.35), units=None,
        labels=['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=True, ori=0.0, depth=-1, readOnly=False)
    textAlert = visual.TextStim(win=win_ref, name='textAlert',
        text='Alert',
        font='Open Sans',
        pos=(-0.7, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sliderAlert = visual.Slider(win=win_ref, name='sliderAlert',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.2), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    textAshamed = visual.TextStim(win=win_ref, name='textAshamed',
        text='Ashamed',
        font='Open Sans',
        pos=(-0.7, 0.05), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    sliderAshamed = visual.Slider(win=win_ref, name='sliderAshamed',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.05), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    textInspired = visual.TextStim(win=win_ref, name='textInspired',
        text='Inspired',
        font='Open Sans',
        pos=(-0.7, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    sliderInspired = visual.Slider(win=win_ref, name='sliderInspired',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.1), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    textNervous = visual.TextStim(win=win_ref, name='textNervous',
        text='Nervous',
        font='Open Sans',
        pos=(-0.7, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    sliderNervous = visual.Slider(win=win_ref, name='sliderNervous',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.25), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    buttonNext_3 = visual.ButtonStim(win=win_ref, 
        text='Next >', font='Arvo',
        pos=(0.7, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext_3'
    )
    buttonNext_3.buttonClock = core.Clock()

    # Initialize components for Routine "PANAS_16_20"
    PANAS_16_20Clock = core.Clock()
    textDetermined = visual.TextStim(win=win_ref, name='textDetermined',
        text='Determined',
        font='Open Sans',
        pos=(-0.7, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderDetermined = visual.Slider(win=win_ref, name='sliderDetermined',
        startValue=None, size=(1, 0.05), pos=(0.2, 0.35), units=None,
        labels=['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely'], ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=True, ori=0.0, depth=-1, readOnly=False)
    textAttentive = visual.TextStim(win=win_ref, name='textAttentive',
        text='Attentive',
        font='Open Sans',
        pos=(-0.7, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sliderAttentive = visual.Slider(win=win_ref, name='sliderAttentive',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.2), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    textJittery = visual.TextStim(win=win_ref, name='textJittery',
        text='Jittery',
        font='Open Sans',
        pos=(-0.7, 0.05), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    sliderJittery = visual.Slider(win=win_ref, name='sliderJittery',
        startValue=None, size=(1.0, 0.05), pos=(0.2, 0.05), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    textActive = visual.TextStim(win=win_ref, name='textActive',
        text='Active',
        font='Open Sans',
        pos=(-0.7, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    sliderActive = visual.Slider(win=win_ref, name='sliderActive',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.1), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    textAfraid = visual.TextStim(win=win_ref, name='textAfraid',
        text='Afraid',
        font='Open Sans',
        pos=(-0.7, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    sliderAfraid = visual.Slider(win=win_ref, name='sliderAfraid',
        startValue=None, size=(1.0, 0.05), pos=(0.2, -0.25), units=None,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=1.0,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    buttonNext_4 = visual.ButtonStim(win=win_ref, 
        text='Next >', font='Arvo',
        pos=(0.7, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext_4'
    )
    buttonNext_4.buttonClock = core.Clock()
    
    # ------Prepare to start Routine "WelcomePANAS"-------
    continueRoutine_Part = True
    routine_timer_part.add(10.000000)
    # update component parameters for each repeat
    keySpace.keys = []
    keySpace.rt = []
    _keySpace_allKeys = []
    # keep track of which components have finished
    WelcomePANASComponents = [textWelcome, keySpace, textSpaceHint]
    for thisComponent in WelcomePANASComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    WelcomePANASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "WelcomePANAS"-------
    while continueRoutine_Part and routine_timer_part.getTime() > 0:
        # get current time
        t = WelcomePANASClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=WelcomePANASClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            textWelcome.setAutoDraw(True)
        if textWelcome.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textWelcome.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textWelcome.tStop = t  # not accounting for scr refresh
                textWelcome.frameNStop = frameN  # exact frame index
                win_ref.timeOnFlip(textWelcome, 'tStopRefresh')  # time at next scr refresh
                textWelcome.setAutoDraw(False)
        
        # *keySpace* updates
        waitOnFlip = False
        if keySpace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keySpace.frameNStart = frameN  # exact frame index
            keySpace.tStart = t  # local t and not account for scr refresh
            keySpace.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(keySpace, 'tStartRefresh')  # time at next scr refresh
            keySpace.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(keySpace.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(keySpace.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keySpace.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keySpace.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                keySpace.tStop = t  # not accounting for scr refresh
                keySpace.frameNStop = frameN  # exact frame index
                win_ref.timeOnFlip(keySpace, 'tStopRefresh')  # time at next scr refresh
                keySpace.status = FINISHED
        if keySpace.status == STARTED and not waitOnFlip:
            theseKeys = keySpace.getKeys(keyList=['space'], waitRelease=False)
            _keySpace_allKeys.extend(theseKeys)
            if len(_keySpace_allKeys):
                keySpace.keys = _keySpace_allKeys[-1].name  # just the last key pressed
                keySpace.rt = _keySpace_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False
        
        # *textSpaceHint* updates
        if textSpaceHint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textSpaceHint.frameNStart = frameN  # exact frame index
            textSpaceHint.tStart = t  # local t and not account for scr refresh
            textSpaceHint.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(textSpaceHint, 'tStartRefresh')  # time at next scr refresh
            textSpaceHint.setAutoDraw(True)
        if textSpaceHint.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textSpaceHint.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textSpaceHint.tStop = t  # not accounting for scr refresh
                textSpaceHint.frameNStop = frameN  # exact frame index
                win_ref.timeOnFlip(textSpaceHint, 'tStopRefresh')  # time at next scr refresh
                textSpaceHint.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in WelcomePANASComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "WelcomePANAS"-------
    for thisComponent in WelcomePANASComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textWelcome.started', textWelcome.tStartRefresh)
    experiment_Ref.addData('textWelcome.stopped', textWelcome.tStopRefresh)
    # check responses
    if keySpace.keys in ['', [], None]:  # No response was made
        keySpace.keys = None
    experiment_Ref.addData('keySpace.keys',keySpace.keys)
    if keySpace.keys != None:  # we had a response
        experiment_Ref.addData('keySpace.rt', keySpace.rt)
    experiment_Ref.addData('keySpace.started', keySpace.tStartRefresh)
    experiment_Ref.addData('keySpace.stopped', keySpace.tStopRefresh)
    experiment_Ref.addData('textSpaceHint.started', textSpaceHint.tStartRefresh)
    experiment_Ref.addData('textSpaceHint.stopped', textSpaceHint.tStopRefresh)

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "PANAS_1_5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderInterested.reset()
    sliderDistressed.reset()
    sliderExcited.reset()
    sliderUpset.reset()
    sliderStrong.reset()
    # keep track of which components have finished
    PANAS_1_5Components = [textInterested, sliderInterested, textDistressed, sliderDistressed, textExcited, sliderExcited, textUpset, sliderUpset, textStrong, sliderStrong, buttonNext]
    for thisComponent in PANAS_1_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PANAS_1_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "PANAS_1_5"-------
    while continueRoutine_Part:
        # get current time
        t = PANAS_1_5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PANAS_1_5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInterested* updates
        if textInterested.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInterested.frameNStart = frameN  # exact frame index
            textInterested.tStart = t  # local t and not account for scr refresh
            textInterested.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInterested, 'tStartRefresh')  # time at next scr refresh
            textInterested.setAutoDraw(True)
        
        # *sliderInterested* updates
        if sliderInterested.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderInterested.frameNStart = frameN  # exact frame index
            sliderInterested.tStart = t  # local t and not account for scr refresh
            sliderInterested.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderInterested, 'tStartRefresh')  # time at next scr refresh
            sliderInterested.setAutoDraw(True)
        
        # *textDistressed* updates
        if textDistressed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textDistressed.frameNStart = frameN  # exact frame index
            textDistressed.tStart = t  # local t and not account for scr refresh
            textDistressed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textDistressed, 'tStartRefresh')  # time at next scr refresh
            textDistressed.setAutoDraw(True)
        
        # *sliderDistressed* updates
        if sliderDistressed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderDistressed.frameNStart = frameN  # exact frame index
            sliderDistressed.tStart = t  # local t and not account for scr refresh
            sliderDistressed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderDistressed, 'tStartRefresh')  # time at next scr refresh
            sliderDistressed.setAutoDraw(True)
        
        # *textExcited* updates
        if textExcited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textExcited.frameNStart = frameN  # exact frame index
            textExcited.tStart = t  # local t and not account for scr refresh
            textExcited.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textExcited, 'tStartRefresh')  # time at next scr refresh
            textExcited.setAutoDraw(True)
        
        # *sliderExcited* updates
        if sliderExcited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderExcited.frameNStart = frameN  # exact frame index
            sliderExcited.tStart = t  # local t and not account for scr refresh
            sliderExcited.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderExcited, 'tStartRefresh')  # time at next scr refresh
            sliderExcited.setAutoDraw(True)
        
        # *textUpset* updates
        if textUpset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textUpset.frameNStart = frameN  # exact frame index
            textUpset.tStart = t  # local t and not account for scr refresh
            textUpset.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textUpset, 'tStartRefresh')  # time at next scr refresh
            textUpset.setAutoDraw(True)
        
        # *sliderUpset* updates
        if sliderUpset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderUpset.frameNStart = frameN  # exact frame index
            sliderUpset.tStart = t  # local t and not account for scr refresh
            sliderUpset.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderUpset, 'tStartRefresh')  # time at next scr refresh
            sliderUpset.setAutoDraw(True)
        
        # *textStrong* updates
        if textStrong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textStrong.frameNStart = frameN  # exact frame index
            textStrong.tStart = t  # local t and not account for scr refresh
            textStrong.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStrong, 'tStartRefresh')  # time at next scr refresh
            textStrong.setAutoDraw(True)
        
        # *sliderStrong* updates
        if sliderStrong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderStrong.frameNStart = frameN  # exact frame index
            sliderStrong.tStart = t  # local t and not account for scr refresh
            sliderStrong.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderStrong, 'tStartRefresh')  # time at next scr refresh
            sliderStrong.setAutoDraw(True)
        
        # *buttonNext* updates
        if buttonNext.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonNext.frameNStart = frameN  # exact frame index
            buttonNext.tStart = t  # local t and not account for scr refresh
            buttonNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonNext, 'tStartRefresh')  # time at next scr refresh
            buttonNext.setAutoDraw(True)
        if buttonNext.status == STARTED:
            # check whether buttonNext has been pressed
            if buttonNext.isClicked:
                if not buttonNext.wasClicked:
                    buttonNext.timesOn.append(buttonNext.buttonClock.getTime()) # store time of first click
                    buttonNext.timesOff.append(buttonNext.buttonClock.getTime()) # store time clicked until
                else:
                    buttonNext.timesOff[-1] = buttonNext.buttonClock.getTime() # update time clicked until
                if not buttonNext.wasClicked:
                    continueRoutine_Part = False  # end routine when buttonNext is clicked
                    None
                buttonNext.wasClicked = True  # if buttonNext is still clicked next frame, it is not a new click
            else:
                buttonNext.wasClicked = False  # if buttonNext is clicked next frame, it is a new click
        else:
            buttonNext.wasClicked = False  # if buttonNext is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in PANAS_1_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "PANAS_1_5"-------
    for thisComponent in PANAS_1_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textInterested.started', textInterested.tStartRefresh)
    experiment_Ref.addData('textInterested.stopped', textInterested.tStopRefresh)
    experiment_Ref.addData('sliderInterested.response', sliderInterested.getRating())
    experiment_Ref.addData('sliderInterested.rt', sliderInterested.getRT())
    experiment_Ref.addData('sliderInterested.started', sliderInterested.tStartRefresh)
    experiment_Ref.addData('sliderInterested.stopped', sliderInterested.tStopRefresh)
    experiment_Ref.addData('textDistressed.started', textDistressed.tStartRefresh)
    experiment_Ref.addData('textDistressed.stopped', textDistressed.tStopRefresh)
    experiment_Ref.addData('sliderDistressed.response', sliderDistressed.getRating())
    experiment_Ref.addData('sliderDistressed.rt', sliderDistressed.getRT())
    experiment_Ref.addData('sliderDistressed.started', sliderDistressed.tStartRefresh)
    experiment_Ref.addData('sliderDistressed.stopped', sliderDistressed.tStopRefresh)
    experiment_Ref.addData('textExcited.started', textExcited.tStartRefresh)
    experiment_Ref.addData('textExcited.stopped', textExcited.tStopRefresh)
    experiment_Ref.addData('sliderExcited.response', sliderExcited.getRating())
    experiment_Ref.addData('sliderExcited.rt', sliderExcited.getRT())
    experiment_Ref.addData('sliderExcited.started', sliderExcited.tStartRefresh)
    experiment_Ref.addData('sliderExcited.stopped', sliderExcited.tStopRefresh)
    experiment_Ref.addData('textUpset.started', textUpset.tStartRefresh)
    experiment_Ref.addData('textUpset.stopped', textUpset.tStopRefresh)
    experiment_Ref.addData('sliderUpset.response', sliderUpset.getRating())
    experiment_Ref.addData('sliderUpset.rt', sliderUpset.getRT())
    experiment_Ref.addData('sliderUpset.started', sliderUpset.tStartRefresh)
    experiment_Ref.addData('sliderUpset.stopped', sliderUpset.tStopRefresh)
    experiment_Ref.addData('textStrong.started', textStrong.tStartRefresh)
    experiment_Ref.addData('textStrong.stopped', textStrong.tStopRefresh)
    experiment_Ref.addData('sliderStrong.response', sliderStrong.getRating())
    experiment_Ref.addData('sliderStrong.rt', sliderStrong.getRT())
    experiment_Ref.addData('sliderStrong.started', sliderStrong.tStartRefresh)
    experiment_Ref.addData('sliderStrong.stopped', sliderStrong.tStopRefresh)
    experiment_Ref.addData('buttonNext.started', buttonNext.tStartRefresh)
    experiment_Ref.addData('buttonNext.stopped', buttonNext.tStopRefresh)
    experiment_Ref.addData('buttonNext.numClicks', buttonNext.numClicks)
    if buttonNext.numClicks:
       experiment_Ref.addData('buttonNext.timesOn', buttonNext.timesOn)
       experiment_Ref.addData('buttonNext.timesOff', buttonNext.timesOff)
    else:
       experiment_Ref.addData('buttonNext.timesOn', "")
       experiment_Ref.addData('buttonNext.timesOff', "")
    # the Routine "PANAS_1_5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "PANAS_6_10"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderGuilty.reset()
    sliderScared.reset()
    sliderHostile.reset()
    sliderEnthusiastic.reset()
    sliderProud.reset()
    # keep track of which components have finished
    PANAS_6_10Components = [textGuilty, sliderGuilty, textScared, sliderScared, textHostile, sliderHostile, textEnthusiastic, sliderEnthusiastic, textProud, sliderProud, buttonNext_2]
    for thisComponent in PANAS_6_10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PANAS_6_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "PANAS_6_10"-------
    while continueRoutine_Part:
        # get current time
        t = PANAS_6_10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PANAS_6_10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textGuilty* updates
        if textGuilty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textGuilty.frameNStart = frameN  # exact frame index
            textGuilty.tStart = t  # local t and not account for scr refresh
            textGuilty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textGuilty, 'tStartRefresh')  # time at next scr refresh
            textGuilty.setAutoDraw(True)
        
        # *sliderGuilty* updates
        if sliderGuilty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderGuilty.frameNStart = frameN  # exact frame index
            sliderGuilty.tStart = t  # local t and not account for scr refresh
            sliderGuilty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderGuilty, 'tStartRefresh')  # time at next scr refresh
            sliderGuilty.setAutoDraw(True)
        
        # *textScared* updates
        if textScared.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textScared.frameNStart = frameN  # exact frame index
            textScared.tStart = t  # local t and not account for scr refresh
            textScared.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textScared, 'tStartRefresh')  # time at next scr refresh
            textScared.setAutoDraw(True)
        
        # *sliderScared* updates
        if sliderScared.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderScared.frameNStart = frameN  # exact frame index
            sliderScared.tStart = t  # local t and not account for scr refresh
            sliderScared.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderScared, 'tStartRefresh')  # time at next scr refresh
            sliderScared.setAutoDraw(True)
        
        # *textHostile* updates
        if textHostile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textHostile.frameNStart = frameN  # exact frame index
            textHostile.tStart = t  # local t and not account for scr refresh
            textHostile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textHostile, 'tStartRefresh')  # time at next scr refresh
            textHostile.setAutoDraw(True)
        
        # *sliderHostile* updates
        if sliderHostile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderHostile.frameNStart = frameN  # exact frame index
            sliderHostile.tStart = t  # local t and not account for scr refresh
            sliderHostile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderHostile, 'tStartRefresh')  # time at next scr refresh
            sliderHostile.setAutoDraw(True)
        
        # *textEnthusiastic* updates
        if textEnthusiastic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnthusiastic.frameNStart = frameN  # exact frame index
            textEnthusiastic.tStart = t  # local t and not account for scr refresh
            textEnthusiastic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnthusiastic, 'tStartRefresh')  # time at next scr refresh
            textEnthusiastic.setAutoDraw(True)
        
        # *sliderEnthusiastic* updates
        if sliderEnthusiastic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderEnthusiastic.frameNStart = frameN  # exact frame index
            sliderEnthusiastic.tStart = t  # local t and not account for scr refresh
            sliderEnthusiastic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderEnthusiastic, 'tStartRefresh')  # time at next scr refresh
            sliderEnthusiastic.setAutoDraw(True)
        
        # *textProud* updates
        if textProud.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textProud.frameNStart = frameN  # exact frame index
            textProud.tStart = t  # local t and not account for scr refresh
            textProud.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textProud, 'tStartRefresh')  # time at next scr refresh
            textProud.setAutoDraw(True)
        
        # *sliderProud* updates
        if sliderProud.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderProud.frameNStart = frameN  # exact frame index
            sliderProud.tStart = t  # local t and not account for scr refresh
            sliderProud.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderProud, 'tStartRefresh')  # time at next scr refresh
            sliderProud.setAutoDraw(True)
        
        # *buttonNext_2* updates
        if buttonNext_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonNext_2.frameNStart = frameN  # exact frame index
            buttonNext_2.tStart = t  # local t and not account for scr refresh
            buttonNext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonNext_2, 'tStartRefresh')  # time at next scr refresh
            buttonNext_2.setAutoDraw(True)
        if buttonNext_2.status == STARTED:
            # check whether buttonNext_2 has been pressed
            if buttonNext_2.isClicked:
                if not buttonNext_2.wasClicked:
                    buttonNext_2.timesOn.append(buttonNext_2.buttonClock.getTime()) # store time of first click
                    buttonNext_2.timesOff.append(buttonNext_2.buttonClock.getTime()) # store time clicked until
                else:
                    buttonNext_2.timesOff[-1] = buttonNext_2.buttonClock.getTime() # update time clicked until
                if not buttonNext_2.wasClicked:
                    continueRoutine_Part = False  # end routine when buttonNext_2 is clicked
                    None
                buttonNext_2.wasClicked = True  # if buttonNext_2 is still clicked next frame, it is not a new click
            else:
                buttonNext_2.wasClicked = False  # if buttonNext_2 is clicked next frame, it is a new click
        else:
            buttonNext_2.wasClicked = False  # if buttonNext_2 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in PANAS_6_10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "PANAS_6_10"-------
    for thisComponent in PANAS_6_10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textGuilty.started', textGuilty.tStartRefresh)
    experiment_Ref.addData('textGuilty.stopped', textGuilty.tStopRefresh)
    experiment_Ref.addData('sliderGuilty.response', sliderGuilty.getRating())
    experiment_Ref.addData('sliderGuilty.rt', sliderGuilty.getRT())
    experiment_Ref.addData('sliderGuilty.started', sliderGuilty.tStartRefresh)
    experiment_Ref.addData('sliderGuilty.stopped', sliderGuilty.tStopRefresh)
    experiment_Ref.addData('textScared.started', textScared.tStartRefresh)
    experiment_Ref.addData('textScared.stopped', textScared.tStopRefresh)
    experiment_Ref.addData('sliderScared.response', sliderScared.getRating())
    experiment_Ref.addData('sliderScared.rt', sliderScared.getRT())
    experiment_Ref.addData('sliderScared.started', sliderScared.tStartRefresh)
    experiment_Ref.addData('sliderScared.stopped', sliderScared.tStopRefresh)
    experiment_Ref.addData('textHostile.started', textHostile.tStartRefresh)
    experiment_Ref.addData('textHostile.stopped', textHostile.tStopRefresh)
    experiment_Ref.addData('sliderHostile.response', sliderHostile.getRating())
    experiment_Ref.addData('sliderHostile.rt', sliderHostile.getRT())
    experiment_Ref.addData('sliderHostile.started', sliderHostile.tStartRefresh)
    experiment_Ref.addData('sliderHostile.stopped', sliderHostile.tStopRefresh)
    experiment_Ref.addData('textEnthusiastic.started', textEnthusiastic.tStartRefresh)
    experiment_Ref.addData('textEnthusiastic.stopped', textEnthusiastic.tStopRefresh)
    experiment_Ref.addData('sliderEnthusiastic.response', sliderEnthusiastic.getRating())
    experiment_Ref.addData('sliderEnthusiastic.rt', sliderEnthusiastic.getRT())
    experiment_Ref.addData('sliderEnthusiastic.started', sliderEnthusiastic.tStartRefresh)
    experiment_Ref.addData('sliderEnthusiastic.stopped', sliderEnthusiastic.tStopRefresh)
    experiment_Ref.addData('textProud.started', textProud.tStartRefresh)
    experiment_Ref.addData('textProud.stopped', textProud.tStopRefresh)
    experiment_Ref.addData('sliderProud.response', sliderProud.getRating())
    experiment_Ref.addData('sliderProud.rt', sliderProud.getRT())
    experiment_Ref.addData('sliderProud.started', sliderProud.tStartRefresh)
    experiment_Ref.addData('sliderProud.stopped', sliderProud.tStopRefresh)
    experiment_Ref.addData('buttonNext_2.started', buttonNext_2.tStartRefresh)
    experiment_Ref.addData('buttonNext_2.stopped', buttonNext_2.tStopRefresh)
    experiment_Ref.addData('buttonNext_2.numClicks', buttonNext_2.numClicks)
    if buttonNext_2.numClicks:
       experiment_Ref.addData('buttonNext_2.timesOn', buttonNext_2.timesOn)
       experiment_Ref.addData('buttonNext_2.timesOff', buttonNext_2.timesOff)
    else:
       experiment_Ref.addData('buttonNext_2.timesOn', "")
       experiment_Ref.addData('buttonNext_2.timesOff', "")
    # the Routine "PANAS_6_10" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "PANAS_11_15"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderIrritable.reset()
    sliderAlert.reset()
    sliderAshamed.reset()
    sliderInspired.reset()
    sliderNervous.reset()
    # keep track of which components have finished
    PANAS_11_15Components = [textIrritable, sliderIrritable, textAlert, sliderAlert, textAshamed, sliderAshamed, textInspired, sliderInspired, textNervous, sliderNervous, buttonNext_3]
    for thisComponent in PANAS_11_15Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PANAS_11_15Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "PANAS_11_15"-------
    while continueRoutine_Part:
        # get current time
        t = PANAS_11_15Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PANAS_11_15Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textIrritable* updates
        if textIrritable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textIrritable.frameNStart = frameN  # exact frame index
            textIrritable.tStart = t  # local t and not account for scr refresh
            textIrritable.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textIrritable, 'tStartRefresh')  # time at next scr refresh
            textIrritable.setAutoDraw(True)
        
        # *sliderIrritable* updates
        if sliderIrritable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderIrritable.frameNStart = frameN  # exact frame index
            sliderIrritable.tStart = t  # local t and not account for scr refresh
            sliderIrritable.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderIrritable, 'tStartRefresh')  # time at next scr refresh
            sliderIrritable.setAutoDraw(True)
        
        # *textAlert* updates
        if textAlert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAlert.frameNStart = frameN  # exact frame index
            textAlert.tStart = t  # local t and not account for scr refresh
            textAlert.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAlert, 'tStartRefresh')  # time at next scr refresh
            textAlert.setAutoDraw(True)
        
        # *sliderAlert* updates
        if sliderAlert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderAlert.frameNStart = frameN  # exact frame index
            sliderAlert.tStart = t  # local t and not account for scr refresh
            sliderAlert.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderAlert, 'tStartRefresh')  # time at next scr refresh
            sliderAlert.setAutoDraw(True)
        
        # *textAshamed* updates
        if textAshamed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAshamed.frameNStart = frameN  # exact frame index
            textAshamed.tStart = t  # local t and not account for scr refresh
            textAshamed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAshamed, 'tStartRefresh')  # time at next scr refresh
            textAshamed.setAutoDraw(True)
        
        # *sliderAshamed* updates
        if sliderAshamed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderAshamed.frameNStart = frameN  # exact frame index
            sliderAshamed.tStart = t  # local t and not account for scr refresh
            sliderAshamed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderAshamed, 'tStartRefresh')  # time at next scr refresh
            sliderAshamed.setAutoDraw(True)
        
        # *textInspired* updates
        if textInspired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInspired.frameNStart = frameN  # exact frame index
            textInspired.tStart = t  # local t and not account for scr refresh
            textInspired.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInspired, 'tStartRefresh')  # time at next scr refresh
            textInspired.setAutoDraw(True)
        
        # *sliderInspired* updates
        if sliderInspired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderInspired.frameNStart = frameN  # exact frame index
            sliderInspired.tStart = t  # local t and not account for scr refresh
            sliderInspired.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderInspired, 'tStartRefresh')  # time at next scr refresh
            sliderInspired.setAutoDraw(True)
        
        # *textNervous* updates
        if textNervous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textNervous.frameNStart = frameN  # exact frame index
            textNervous.tStart = t  # local t and not account for scr refresh
            textNervous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textNervous, 'tStartRefresh')  # time at next scr refresh
            textNervous.setAutoDraw(True)
        
        # *sliderNervous* updates
        if sliderNervous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderNervous.frameNStart = frameN  # exact frame index
            sliderNervous.tStart = t  # local t and not account for scr refresh
            sliderNervous.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderNervous, 'tStartRefresh')  # time at next scr refresh
            sliderNervous.setAutoDraw(True)
        
        # *buttonNext_3* updates
        if buttonNext_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonNext_3.frameNStart = frameN  # exact frame index
            buttonNext_3.tStart = t  # local t and not account for scr refresh
            buttonNext_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonNext_3, 'tStartRefresh')  # time at next scr refresh
            buttonNext_3.setAutoDraw(True)
        if buttonNext_3.status == STARTED:
            # check whether buttonNext_3 has been pressed
            if buttonNext_3.isClicked:
                if not buttonNext_3.wasClicked:
                    buttonNext_3.timesOn.append(buttonNext_3.buttonClock.getTime()) # store time of first click
                    buttonNext_3.timesOff.append(buttonNext_3.buttonClock.getTime()) # store time clicked until
                else:
                    buttonNext_3.timesOff[-1] = buttonNext_3.buttonClock.getTime() # update time clicked until
                if not buttonNext_3.wasClicked:
                    continueRoutine_Part = False  # end routine when buttonNext_3 is clicked
                    None
                buttonNext_3.wasClicked = True  # if buttonNext_3 is still clicked next frame, it is not a new click
            else:
                buttonNext_3.wasClicked = False  # if buttonNext_3 is clicked next frame, it is a new click
        else:
            buttonNext_3.wasClicked = False  # if buttonNext_3 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in PANAS_11_15Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "PANAS_11_15"-------
    for thisComponent in PANAS_11_15Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textIrritable.started', textIrritable.tStartRefresh)
    experiment_Ref.addData('textIrritable.stopped', textIrritable.tStopRefresh)
    experiment_Ref.addData('sliderIrritable.response', sliderIrritable.getRating())
    experiment_Ref.addData('sliderIrritable.rt', sliderIrritable.getRT())
    experiment_Ref.addData('sliderIrritable.started', sliderIrritable.tStartRefresh)
    experiment_Ref.addData('sliderIrritable.stopped', sliderIrritable.tStopRefresh)
    experiment_Ref.addData('textAlert.started', textAlert.tStartRefresh)
    experiment_Ref.addData('textAlert.stopped', textAlert.tStopRefresh)
    experiment_Ref.addData('sliderAlert.response', sliderAlert.getRating())
    experiment_Ref.addData('sliderAlert.rt', sliderAlert.getRT())
    experiment_Ref.addData('sliderAlert.started', sliderAlert.tStartRefresh)
    experiment_Ref.addData('sliderAlert.stopped', sliderAlert.tStopRefresh)
    experiment_Ref.addData('textAshamed.started', textAshamed.tStartRefresh)
    experiment_Ref.addData('textAshamed.stopped', textAshamed.tStopRefresh)
    experiment_Ref.addData('sliderAshamed.response', sliderAshamed.getRating())
    experiment_Ref.addData('sliderAshamed.rt', sliderAshamed.getRT())
    experiment_Ref.addData('sliderAshamed.started', sliderAshamed.tStartRefresh)
    experiment_Ref.addData('sliderAshamed.stopped', sliderAshamed.tStopRefresh)
    experiment_Ref.addData('textInspired.started', textInspired.tStartRefresh)
    experiment_Ref.addData('textInspired.stopped', textInspired.tStopRefresh)
    experiment_Ref.addData('sliderInspired.response', sliderInspired.getRating())
    experiment_Ref.addData('sliderInspired.rt', sliderInspired.getRT())
    experiment_Ref.addData('sliderInspired.started', sliderInspired.tStartRefresh)
    experiment_Ref.addData('sliderInspired.stopped', sliderInspired.tStopRefresh)
    experiment_Ref.addData('textNervous.started', textNervous.tStartRefresh)
    experiment_Ref.addData('textNervous.stopped', textNervous.tStopRefresh)
    experiment_Ref.addData('sliderNervous.response', sliderNervous.getRating())
    experiment_Ref.addData('sliderNervous.rt', sliderNervous.getRT())
    experiment_Ref.addData('sliderNervous.started', sliderNervous.tStartRefresh)
    experiment_Ref.addData('sliderNervous.stopped', sliderNervous.tStopRefresh)
    experiment_Ref.addData('buttonNext_3.started', buttonNext_3.tStartRefresh)
    experiment_Ref.addData('buttonNext_3.stopped', buttonNext_3.tStopRefresh)
    experiment_Ref.addData('buttonNext_3.numClicks', buttonNext_3.numClicks)
    if buttonNext_3.numClicks:
       experiment_Ref.addData('buttonNext_3.timesOn', buttonNext_3.timesOn)
       experiment_Ref.addData('buttonNext_3.timesOff', buttonNext_3.timesOff)
    else:
       experiment_Ref.addData('buttonNext_3.timesOn', "")
       experiment_Ref.addData('buttonNext_3.timesOff', "")
    # the Routine "PANAS_11_15" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "PANAS_16_20"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderDetermined.reset()
    sliderAttentive.reset()
    sliderJittery.reset()
    sliderActive.reset()
    sliderAfraid.reset()
    # keep track of which components have finished
    PANAS_16_20Components = [textDetermined, sliderDetermined, textAttentive, sliderAttentive, textJittery, sliderJittery, textActive, sliderActive, textAfraid, sliderAfraid, buttonNext_4]
    for thisComponent in PANAS_16_20Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PANAS_16_20Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "PANAS_16_20"-------
    while continueRoutine_Part:
        # get current time
        t = PANAS_16_20Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PANAS_16_20Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textDetermined* updates
        if textDetermined.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textDetermined.frameNStart = frameN  # exact frame index
            textDetermined.tStart = t  # local t and not account for scr refresh
            textDetermined.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textDetermined, 'tStartRefresh')  # time at next scr refresh
            textDetermined.setAutoDraw(True)
        
        # *sliderDetermined* updates
        if sliderDetermined.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderDetermined.frameNStart = frameN  # exact frame index
            sliderDetermined.tStart = t  # local t and not account for scr refresh
            sliderDetermined.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderDetermined, 'tStartRefresh')  # time at next scr refresh
            sliderDetermined.setAutoDraw(True)
        
        # *textAttentive* updates
        if textAttentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAttentive.frameNStart = frameN  # exact frame index
            textAttentive.tStart = t  # local t and not account for scr refresh
            textAttentive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAttentive, 'tStartRefresh')  # time at next scr refresh
            textAttentive.setAutoDraw(True)
        
        # *sliderAttentive* updates
        if sliderAttentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderAttentive.frameNStart = frameN  # exact frame index
            sliderAttentive.tStart = t  # local t and not account for scr refresh
            sliderAttentive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderAttentive, 'tStartRefresh')  # time at next scr refresh
            sliderAttentive.setAutoDraw(True)
        
        # *textJittery* updates
        if textJittery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textJittery.frameNStart = frameN  # exact frame index
            textJittery.tStart = t  # local t and not account for scr refresh
            textJittery.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textJittery, 'tStartRefresh')  # time at next scr refresh
            textJittery.setAutoDraw(True)
        
        # *sliderJittery* updates
        if sliderJittery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderJittery.frameNStart = frameN  # exact frame index
            sliderJittery.tStart = t  # local t and not account for scr refresh
            sliderJittery.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderJittery, 'tStartRefresh')  # time at next scr refresh
            sliderJittery.setAutoDraw(True)
        
        # *textActive* updates
        if textActive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textActive.frameNStart = frameN  # exact frame index
            textActive.tStart = t  # local t and not account for scr refresh
            textActive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textActive, 'tStartRefresh')  # time at next scr refresh
            textActive.setAutoDraw(True)
        
        # *sliderActive* updates
        if sliderActive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderActive.frameNStart = frameN  # exact frame index
            sliderActive.tStart = t  # local t and not account for scr refresh
            sliderActive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderActive, 'tStartRefresh')  # time at next scr refresh
            sliderActive.setAutoDraw(True)
        
        # *textAfraid* updates
        if textAfraid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAfraid.frameNStart = frameN  # exact frame index
            textAfraid.tStart = t  # local t and not account for scr refresh
            textAfraid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAfraid, 'tStartRefresh')  # time at next scr refresh
            textAfraid.setAutoDraw(True)
        
        # *sliderAfraid* updates
        if sliderAfraid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderAfraid.frameNStart = frameN  # exact frame index
            sliderAfraid.tStart = t  # local t and not account for scr refresh
            sliderAfraid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderAfraid, 'tStartRefresh')  # time at next scr refresh
            sliderAfraid.setAutoDraw(True)
        
        # *buttonNext_4* updates
        if buttonNext_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            buttonNext_4.frameNStart = frameN  # exact frame index
            buttonNext_4.tStart = t  # local t and not account for scr refresh
            buttonNext_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonNext_4, 'tStartRefresh')  # time at next scr refresh
            buttonNext_4.setAutoDraw(True)
        if buttonNext_4.status == STARTED:
            # check whether buttonNext_4 has been pressed
            if buttonNext_4.isClicked:
                if not buttonNext_4.wasClicked:
                    buttonNext_4.timesOn.append(buttonNext_4.buttonClock.getTime()) # store time of first click
                    buttonNext_4.timesOff.append(buttonNext_4.buttonClock.getTime()) # store time clicked until
                else:
                    buttonNext_4.timesOff[-1] = buttonNext_4.buttonClock.getTime() # update time clicked until
                if not buttonNext_4.wasClicked:
                    continueRoutine_Part = False  # end routine when buttonNext_4 is clicked
                    None
                buttonNext_4.wasClicked = True  # if buttonNext_4 is still clicked next frame, it is not a new click
            else:
                buttonNext_4.wasClicked = False  # if buttonNext_4 is clicked next frame, it is a new click
        else:
            buttonNext_4.wasClicked = False  # if buttonNext_4 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in PANAS_16_20Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "PANAS_16_20"-------
    for thisComponent in PANAS_16_20Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('textDetermined.started', textDetermined.tStartRefresh)
    experiment_Ref.addData('textDetermined.stopped', textDetermined.tStopRefresh)
    experiment_Ref.addData('sliderDetermined.response', sliderDetermined.getRating())
    experiment_Ref.addData('sliderDetermined.rt', sliderDetermined.getRT())
    experiment_Ref.addData('sliderDetermined.started', sliderDetermined.tStartRefresh)
    experiment_Ref.addData('sliderDetermined.stopped', sliderDetermined.tStopRefresh)
    experiment_Ref.addData('textAttentive.started', textAttentive.tStartRefresh)
    experiment_Ref.addData('textAttentive.stopped', textAttentive.tStopRefresh)
    experiment_Ref.addData('sliderAttentive.response', sliderAttentive.getRating())
    experiment_Ref.addData('sliderAttentive.rt', sliderAttentive.getRT())
    experiment_Ref.addData('sliderAttentive.started', sliderAttentive.tStartRefresh)
    experiment_Ref.addData('sliderAttentive.stopped', sliderAttentive.tStopRefresh)
    experiment_Ref.addData('textJittery.started', textJittery.tStartRefresh)
    experiment_Ref.addData('textJittery.stopped', textJittery.tStopRefresh)
    experiment_Ref.addData('sliderJittery.response', sliderJittery.getRating())
    experiment_Ref.addData('sliderJittery.rt', sliderJittery.getRT())
    experiment_Ref.addData('sliderJittery.started', sliderJittery.tStartRefresh)
    experiment_Ref.addData('sliderJittery.stopped', sliderJittery.tStopRefresh)
    experiment_Ref.addData('textActive.started', textActive.tStartRefresh)
    experiment_Ref.addData('textActive.stopped', textActive.tStopRefresh)
    experiment_Ref.addData('sliderActive.response', sliderActive.getRating())
    experiment_Ref.addData('sliderActive.rt', sliderActive.getRT())
    experiment_Ref.addData('sliderActive.started', sliderActive.tStartRefresh)
    experiment_Ref.addData('sliderActive.stopped', sliderActive.tStopRefresh)
    experiment_Ref.addData('textAfraid.started', textAfraid.tStartRefresh)
    experiment_Ref.addData('textAfraid.stopped', textAfraid.tStopRefresh)
    experiment_Ref.addData('sliderAfraid.response', sliderAfraid.getRating())
    experiment_Ref.addData('sliderAfraid.rt', sliderAfraid.getRT())
    experiment_Ref.addData('sliderAfraid.started', sliderAfraid.tStartRefresh)
    experiment_Ref.addData('sliderAfraid.stopped', sliderAfraid.tStopRefresh)
    experiment_Ref.addData('buttonNext_4.started', buttonNext_4.tStartRefresh)
    experiment_Ref.addData('buttonNext_4.stopped', buttonNext_4.tStopRefresh)
    experiment_Ref.addData('buttonNext_4.numClicks', buttonNext_4.numClicks)
    if buttonNext_4.numClicks:
       experiment_Ref.addData('buttonNext_4.timesOn', buttonNext_4.timesOn)
       experiment_Ref.addData('buttonNext_4.timesOff', buttonNext_4.timesOff)
    else:
       experiment_Ref.addData('buttonNext_4.timesOn', "")
       experiment_Ref.addData('buttonNext_4.timesOff', "")
    # the Routine "PANAS_16_20" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()
    logging_utilities.log_time(False, 'PANAS')
    experiment_Ref.addData('Panas.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()

def likertscale(experiment_Ref, win_ref, for_which='mental effort'):
    logging_utilities.log_time(True, 'likert Scale')
    experiment_Ref.addData('LikertScale.started', win_ref.getFutureFlipTime(clock=None))
    instr = visual.TextStim(win_ref, text='Please rate your {} in a 5-point Likert scale. Press [SPACE] to continue.'.format(for_which) , height=.12, units='norm')
    # event.clearEvents()
    instr.draw()
    win_ref.flip()
    if 'escape' in event.waitKeys():
        core.quit()

    # Example 1 --------(basic choices)--------
    # create a RatingScale object:
    myRatingScale = visual.RatingScale(win_ref, choices=['very, very low', 'low', 'neither low nor high','high','very, very high'],stretch=2)#,
        #textSize=.12, textColor= 'white',textFont= 'Open Sans', pos=[0, -200],
        #acceptKeys='Space', maxTime=0.2)

    # the item to-be-rated or respond to:
    myItem = visual.TextStim(win_ref, text="In solving the preceeding problem, my {} was:".format(for_which), height=.12, units='norm')
    # event.clearEvents()
    while myRatingScale.noResponse:  # show & update until a response has been made
        myItem.draw()
        myRatingScale.draw()
        win_ref.flip()
        if event.getKeys(['escape']):
            core.quit()
    rating = myRatingScale.getRating()
    decisionTime = myRatingScale.getRT()
    choiceHistory = myRatingScale.getHistory()
    #key_resp_16 = keyboard.Keyboard()
    experiment_Ref.addData('Likert_Scale_Rating.' + str(for_which), myRatingScale.getRating())
    experiment_Ref.addData('history.' + str(for_which), myRatingScale.getHistory())
    experiment_Ref.addData('LikertScale.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging.log(level=logging.EXP, msg='Likert-Scale ({}) decision time {} and history {}'.format(for_which, myRatingScale.getRating(), myRatingScale.getHistory()))
    logging_utilities.log_time(False, 'likert Scale')

def nasa(continueRoutine_Part, experiment_Ref, routine_timer_part, win_ref, endExpNow, defaultKeyboard, frameTolerance):
    logging_utilities.log_time(True, 'NASA')
    experiment_Ref.addData('Nasa.started', win_ref.getFutureFlipTime(clock=None))
    # Initialize components for Routine "nasa_instructions_start"
    nasa_instructions_startClock = core.Clock()
    Instructions_1 = visual.TextStim(win=win_ref, name='Instructions_1',
        text='In the follwoing slides you will be answering few questions based on how you felt during the tasks (or video). \n\n\nPlease press space to continue.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0)
    key_resp_21 = keyboard.Keyboard()

    # Initialize components for Routine "nasa_q1"
    nasa_q1Clock = core.Clock()
    Question1 = visual.TextStim(win=win_ref, name='Question1',
        text='Mental Demand\n\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ1 = visual.Slider(win=win_ref, name='sliderQ1',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft1 = visual.TextStim(win=win_ref, name='LabelLeft1',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight1 = visual.TextStim(win=win_ref, name='LabelRight1',
        text='Very High',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_q2"
    nasa_q2Clock = core.Clock()
    Question2 = visual.TextStim(win=win_ref, name='Question2',
        text='Physical Demand \n\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ2 = visual.Slider(win=win_ref, name='sliderQ2',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft2 = visual.TextStim(win=win_ref, name='LabelLeft2',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight2 = visual.TextStim(win=win_ref, name='LabelRight2',
        text='Very High',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_q3"
    nasa_q3Clock = core.Clock()
    Question3 = visual.TextStim(win=win_ref, name='Question3',
        text='Temporal Demand \n\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ3 = visual.Slider(win=win_ref, name='sliderQ3',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft3 = visual.TextStim(win=win_ref, name='LabelLeft3',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight = visual.TextStim(win=win_ref, name='LabelRight',
        text='Very Hign',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_q4"
    nasa_q4Clock = core.Clock()
    Question4 = visual.TextStim(win=win_ref, name='Question4',
        text='Performance\n\nHow successful were you in accomplishing what you were asked to do?\n',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ4 = visual.Slider(win=win_ref, name='sliderQ4',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft4 = visual.TextStim(win=win_ref, name='LabelLeft4',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight4 = visual.TextStim(win=win_ref, name='LabelRight4',
        text='Very High',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_q5"
    nasa_q5Clock = core.Clock()
    Question5 = visual.TextStim(win=win_ref, name='Question5',
        text='Effort \n\nHow hard did you have to work to accomplish your level of performance?',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ5 = visual.Slider(win=win_ref, name='sliderQ5',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft5 = visual.TextStim(win=win_ref, name='LabelLeft5',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight5 = visual.TextStim(win=win_ref, name='LabelRight5',
        text='Very High',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_q6"
    nasa_q6Clock = core.Clock()
    Question6 = visual.TextStim(win=win_ref, name='Question6',
        text='Frustration \n\nHow insecure, discouraged, irritated, stressed,  and annoyed were you?',
        font='Open Sans',
        pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sliderQ6 = visual.Slider(win=win_ref, name='sliderQ6',
        startValue=None, size=(1.0, 0.08), pos=(0, -0.2), units=None,
        labels=None, ticks=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100), granularity=5.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    LabelLeft6 = visual.TextStim(win=win_ref, name='LabelLeft6',
        text='Very Low',
        font='Open Sans',
        pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    LabelRight6 = visual.TextStim(win=win_ref, name='LabelRight6',
        text='Very High',
        font='Open Sans',
        pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "nasa_instructions_middle"
    nasa_instructions_middleClock = core.Clock()
    Instructions_2 = visual.TextStim(win=win_ref, name='Instructions_2',
        text='In the following slides, 2 questions are presented.\n\nPlease select the workload dimension from each pair that was more significant during the task. \nFor the chosen dimension, press on the red square under the question.\n\n\nPress [SPACE] to start.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_22 = keyboard.Keyboard()

    # Initialize components for Routine "nasa_pair_2_3"
    nasa_pair_2_3Clock = core.Clock()
    Question23 = visual.TextStim(win=win_ref, name='Question23',
        text='Physical Demand:\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question32 = visual.TextStim(win=win_ref, name='Question32',
        text='Temporal Demand:\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, -0.09), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ23 = visual.ButtonStim(win_ref, 
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ23'
    )
    ChoseQ23.buttonClock = core.Clock()
    ChoseQ32 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05,0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ32'
    )
    ChoseQ32.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_4_5"
    nasa_pair_4_5Clock = core.Clock()
    Question45 = visual.TextStim(win=win_ref, name='Question45',
        text='Performance:\nHow successful were you in accomplishing what you were asked to do?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question54 = visual.TextStim(win=win_ref, name='Question54',
        text='Effort:\nHow hard did you have to work to accomplish your level of performance?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ45 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.17),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ45'
    )
    ChoseQ45.buttonClock = core.Clock()
    ChoseQ54 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ54'
    )
    ChoseQ54.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_1_2"
    nasa_pair_1_2Clock = core.Clock()
    Question12 = visual.TextStim(win=win_ref, name='Question12',
        text='Mental Demand:\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question21 = visual.TextStim(win=win_ref, name='Question21',
        text='Physical Demand:\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ12 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ12'
    )
    ChoseQ12.buttonClock = core.Clock()
    ChoseQ21 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ21'
    )
    ChoseQ21.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_5_6"
    nasa_pair_5_6Clock = core.Clock()
    Question56 = visual.TextStim(win=win_ref, name='Question56',
        text='Effort:\nHow hard did you have to work to accomplish your level of performance?',
        font='Open Sans',
        pos=(0, 0.30), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question65 = visual.TextStim(win=win_ref, name='Question65',
        text='Frustration \nHow insecure, discouraged, irritated, stressed,  and annoyed were you?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ56 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.17),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ56'
    )
    ChoseQ56.buttonClock = core.Clock()
    ChoseQ65 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ65'
    )
    ChoseQ65.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_2_4"
    nasa_pair_2_4Clock = core.Clock()
    Question24 = visual.TextStim(win=win_ref, name='Question24',
        text='Physical Demand:\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question42 = visual.TextStim(win=win_ref, name='Question42',
        text='Performance:\nHow successful were you in accomplishing what you were asked to do?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ24 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ24'
    )
    ChoseQ24.buttonClock = core.Clock()
    ChoseQ42 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ42'
    )
    ChoseQ42.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_1_5"
    nasa_pair_1_5Clock = core.Clock()
    Question15 = visual.TextStim(win=win_ref, name='Question15',
        text='Mental Demand:\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question51 = visual.TextStim(win=win_ref, name='Question51',
        text='Effort:\nHow hard did you have to work to accomplish your level of performance?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ15 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ15'
    )
    ChoseQ15.buttonClock = core.Clock()
    ChoseQ51 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ51'
    )
    ChoseQ51.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_4_6"
    nasa_pair_4_6Clock = core.Clock()
    Question46 = visual.TextStim(win=win_ref, name='Question46',
        text='Performance:\nHow successful were you in accomplishing what you were asked to do?',
        font='Open Sans',
        pos=(0, 0.30), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question64 = visual.TextStim(win=win_ref, name='Question64',
        text='Frustration \nHow insecure, discouraged, irritated, stressed,  and annoyed were you?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ46 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.17),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ46'
    )
    ChoseQ46.buttonClock = core.Clock()
    ChoseQ64 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ64'
    )
    ChoseQ64.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_2_5"
    nasa_pair_2_5Clock = core.Clock()
    Question25 = visual.TextStim(win=win_ref, name='Question25',
        text='Physical Demand:\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question52 = visual.TextStim(win=win_ref, name='Question52',
        text='Effort:\nHow hard did you have to work to accomplish your level of performance?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ25 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ25'
    )
    ChoseQ25.buttonClock = core.Clock()
    ChoseQ52 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ52'
    )
    ChoseQ52.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_1_4"
    nasa_pair_1_4Clock = core.Clock()
    Question14 = visual.TextStim(win=win_ref, name='Question14',
        text='Mental Demand:\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question41 = visual.TextStim(win=win_ref, name='Question41',
        text='Performance:\nHow successful were you in accomplishing what you were asked to do?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ14 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ14'
    )
    ChoseQ14.buttonClock = core.Clock()
    ChoseQ41 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ41'
    )
    ChoseQ41.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_3_4"
    nasa_pair_3_4Clock = core.Clock()
    Question34 = visual.TextStim(win=win_ref, name='Question34',
        text='Temporal Demand:\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, 0.32), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question43 = visual.TextStim(win=win_ref, name='Question43',
        text='Performance:\nHow successful were you in accomplishing what you were asked to do?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ34 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ34'
    )
    ChoseQ34.buttonClock = core.Clock()
    ChoseQ43 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ43'
    )
    ChoseQ43.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_2_6"
    nasa_pair_2_6Clock = core.Clock()
    Question26 = visual.TextStim(win=win_ref, name='Question26',
        text='Physical Demand:\nHow physically demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question62 = visual.TextStim(win=win_ref, name='Question62',
        text='Frustration \nHow insecure, discouraged, irritated, stressed,  and annoyed were you?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ26 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ26'
    )
    ChoseQ26.buttonClock = core.Clock()
    ChoseQ62 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ62'
    )
    ChoseQ62.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_3_5"
    nasa_pair_3_5Clock = core.Clock()
    Question35 = visual.TextStim(win=win_ref, name='Question35',
        text='Temporal Demand:\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, 0.32), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question53 = visual.TextStim(win=win_ref, name='Question53',
        text='Effort:\nHow hard did you have to work to accomplish your level of performance?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ35 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ35'
    )
    ChoseQ35.buttonClock = core.Clock()
    ChoseQ53 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ53'
    )
    ChoseQ53.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_1_6"
    nasa_pair_1_6Clock = core.Clock()
    Question16 = visual.TextStim(win=win_ref, name='Question16',
        text='Mental Demand:\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question61 = visual.TextStim(win=win_ref, name='Question61',
        text='Frustration \nHow insecure, discouraged, irritated, stressed,  and annoyed were you?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ16 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ16'
    )
    ChoseQ16.buttonClock = core.Clock()
    ChoseQ61 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ61'
    )
    ChoseQ61.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_1_3"
    nasa_pair_1_3Clock = core.Clock()
    Question13 = visual.TextStim(win=win_ref, name='Question13',
        text='Mental Demand:\nHow mentally demanding was the task?',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question31 = visual.TextStim(win=win_ref, name='Question31',
        text='Temporal Demand:\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, -0.09), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ13 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ13'
    )
    ChoseQ13.buttonClock = core.Clock()
    ChoseQ31 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ31'
    )
    ChoseQ31.buttonClock = core.Clock()

    # Initialize components for Routine "nasa_pair_3_6"
    nasa_pair_3_6Clock = core.Clock()
    Question36 = visual.TextStim(win=win_ref, name='Question36',
        text='Temporal Demand:\nHow hurried or rushed was the pace of the task?',
        font='Open Sans',
        pos=(0, 0.32), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Question63 = visual.TextStim(win=win_ref, name='Question63',
        text='Frustration \nHow insecure, discouraged, irritated, stressed,  and annoyed were you?\n',
        font='Open Sans',
        pos=(0, -0.08), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ChoseQ36 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, 0.20),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ36'
    )
    ChoseQ36.buttonClock = core.Clock()
    ChoseQ63 = visual.ButtonStim(win_ref,
        text=None, font='Arvo',
        pos=(0, -0.2),
        letterHeight=0.05,
        size=(0.05, 0.05), borderWidth=0.0,
        fillColor='red', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='ChoseQ63'
    )
    ChoseQ63.buttonClock = core.Clock()

    #TODO: comment out this Second task bs
    # Initialize components for Routine "nasa_goodbyewindow"
    nasa_goodbyewindowClock = core.Clock()
    Goodbye = visual.TextStim(win=win_ref, name='Goodbye',
        text='You have finished the questionnaire. Now you will continue to the second task.',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
        
    nasa_goodbyewin_refdowClock = core.Clock()
        
    # ------Prepare to start Routine "nasa_instructions_start"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_21.keys = []
    key_resp_21.rt = []
    _key_resp_21_allKeys = []

    # keep track of which components have finished
    nasa_instructions_startComponents = [Instructions_1, key_resp_21]
    for thisComponent in nasa_instructions_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_instructions_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_instructions_start"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_instructions_startClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_instructions_startClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_1* updates
        if Instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_1.frameNStart = frameN  # exact frame index
            Instructions_1.tStart = t  # local t and not account for scr refresh
            Instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Instructions_1, 'tStartRefresh')  # time at next scr refresh
            Instructions_1.setAutoDraw(True)
        
        # *key_resp_21* updates
        waitOnFlip = False
        if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_21.frameNStart = frameN  # exact frame index
            key_resp_21.tStart = t  # local t and not account for scr refresh
            key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
            key_resp_21.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_21.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_21.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_21_allKeys.extend(theseKeys)
            if len(_key_resp_21_allKeys):
                key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
                key_resp_21.rt = _key_resp_21_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_instructions_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_instructions_start"-------
    for thisComponent in nasa_instructions_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Instructions_1.started', Instructions_1.tStartRefresh)
    experiment_Ref.addData('Instructions_1.stopped', Instructions_1.tStopRefresh)
    # check responses
    if key_resp_21.keys in ['', [], None]:  # No response was made
        key_resp_21.keys = None
    experiment_Ref.addData('key_resp_21.keys',key_resp_21.keys)
    if key_resp_21.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_21.rt', key_resp_21.rt)
    experiment_Ref.addData('key_resp_21.started', key_resp_21.tStartRefresh)
    experiment_Ref.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
    # the Routine "nasa_instructions_start" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q1"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ1.reset()
    # keep track of which components have finished
    nasa_q1Components = [Question1, sliderQ1, LabelLeft1, LabelRight1]
    for thisComponent in nasa_q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q1"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q1Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q1Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question1* updates
        if Question1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question1.frameNStart = frameN  # exact frame index
            Question1.tStart = t  # local t and not account for scr refresh
            Question1.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question1, 'tStartRefresh')  # time at next scr refresh
            Question1.setAutoDraw(True)
        
        # *sliderQ1* updates
        if sliderQ1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ1.frameNStart = frameN  # exact frame index
            sliderQ1.tStart = t  # local t and not account for scr refresh
            sliderQ1.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ1, 'tStartRefresh')  # time at next scr refresh
            sliderQ1.setAutoDraw(True)
        
        # Check sliderQ1 for response to end routine
        if sliderQ1.getRating() is not None and sliderQ1.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft1* updates
        if LabelLeft1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft1.frameNStart = frameN  # exact frame index
            LabelLeft1.tStart = t  # local t and not account for scr refresh
            LabelLeft1.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft1, 'tStartRefresh')  # time at next scr refresh
            LabelLeft1.setAutoDraw(True)
        
        # *LabelRight1* updates
        if LabelRight1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight1.frameNStart = frameN  # exact frame index
            LabelRight1.tStart = t  # local t and not account for scr refresh
            LabelRight1.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight1, 'tStartRefresh')  # time at next scr refresh
            LabelRight1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q1"-------
    for thisComponent in nasa_q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question1.started', Question1.tStartRefresh)
    experiment_Ref.addData('Question1.stopped', Question1.tStopRefresh)
    experiment_Ref.addData('sliderQ1.response', sliderQ1.getRating())
    experiment_Ref.addData('sliderQ1.rt', sliderQ1.getRT())
    experiment_Ref.addData('sliderQ1.started', sliderQ1.tStartRefresh)
    experiment_Ref.addData('sliderQ1.stopped', sliderQ1.tStopRefresh)
    experiment_Ref.addData('LabelLeft1.started', LabelLeft1.tStartRefresh)
    experiment_Ref.addData('LabelLeft1.stopped', LabelLeft1.tStopRefresh)
    experiment_Ref.addData('LabelRight1.started', LabelRight1.tStartRefresh)
    experiment_Ref.addData('LabelRight1.stopped', LabelRight1.tStopRefresh)
    # the Routine "nasa_q1" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q2"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ2.reset()
    # keep track of which components have finished
    nasa_q2Components = [Question2, sliderQ2, LabelLeft2, LabelRight2]
    for thisComponent in nasa_q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q2"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q2Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q2Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question2* updates
        if Question2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question2.frameNStart = frameN  # exact frame index
            Question2.tStart = t  # local t and not account for scr refresh
            Question2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question2, 'tStartRefresh')  # time at next scr refresh
            Question2.setAutoDraw(True)
        
        # *sliderQ2* updates
        if sliderQ2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ2.frameNStart = frameN  # exact frame index
            sliderQ2.tStart = t  # local t and not account for scr refresh
            sliderQ2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ2, 'tStartRefresh')  # time at next scr refresh
            sliderQ2.setAutoDraw(True)
        
        # Check sliderQ2 for response to end routine
        if sliderQ2.getRating() is not None and sliderQ2.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft2* updates
        if LabelLeft2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft2.frameNStart = frameN  # exact frame index
            LabelLeft2.tStart = t  # local t and not account for scr refresh
            LabelLeft2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft2, 'tStartRefresh')  # time at next scr refresh
            LabelLeft2.setAutoDraw(True)
        
        # *LabelRight2* updates
        if LabelRight2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight2.frameNStart = frameN  # exact frame index
            LabelRight2.tStart = t  # local t and not account for scr refresh
            LabelRight2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight2, 'tStartRefresh')  # time at next scr refresh
            LabelRight2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q2"-------
    for thisComponent in nasa_q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question2.started', Question2.tStartRefresh)
    experiment_Ref.addData('Question2.stopped', Question2.tStopRefresh)
    experiment_Ref.addData('sliderQ2.response', sliderQ2.getRating())
    experiment_Ref.addData('sliderQ2.rt', sliderQ2.getRT())
    experiment_Ref.addData('sliderQ2.started', sliderQ2.tStartRefresh)
    experiment_Ref.addData('sliderQ2.stopped', sliderQ2.tStopRefresh)
    experiment_Ref.addData('LabelLeft2.started', LabelLeft2.tStartRefresh)
    experiment_Ref.addData('LabelLeft2.stopped', LabelLeft2.tStopRefresh)
    experiment_Ref.addData('LabelRight2.started', LabelRight2.tStartRefresh)
    experiment_Ref.addData('LabelRight2.stopped', LabelRight2.tStopRefresh)
    # the Routine "nasa_q2" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q3"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ3.reset()
    # keep track of which components have finished
    nasa_q3Components = [Question3, sliderQ3, LabelLeft3, LabelRight]
    for thisComponent in nasa_q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q3"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q3Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q3Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question3* updates
        if Question3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question3.frameNStart = frameN  # exact frame index
            Question3.tStart = t  # local t and not account for scr refresh
            Question3.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question3, 'tStartRefresh')  # time at next scr refresh
            Question3.setAutoDraw(True)
        
        # *sliderQ3* updates
        if sliderQ3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ3.frameNStart = frameN  # exact frame index
            sliderQ3.tStart = t  # local t and not account for scr refresh
            sliderQ3.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ3, 'tStartRefresh')  # time at next scr refresh
            sliderQ3.setAutoDraw(True)
        
        # Check sliderQ3 for response to end routine
        if sliderQ3.getRating() is not None and sliderQ3.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft3* updates
        if LabelLeft3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft3.frameNStart = frameN  # exact frame index
            LabelLeft3.tStart = t  # local t and not account for scr refresh
            LabelLeft3.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft3, 'tStartRefresh')  # time at next scr refresh
            LabelLeft3.setAutoDraw(True)
        
        # *LabelRight* updates
        if LabelRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight.frameNStart = frameN  # exact frame index
            LabelRight.tStart = t  # local t and not account for scr refresh
            LabelRight.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight, 'tStartRefresh')  # time at next scr refresh
            LabelRight.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q3"-------
    for thisComponent in nasa_q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question3.started', Question3.tStartRefresh)
    experiment_Ref.addData('Question3.stopped', Question3.tStopRefresh)
    experiment_Ref.addData('sliderQ3.response', sliderQ3.getRating())
    experiment_Ref.addData('sliderQ3.rt', sliderQ3.getRT())
    experiment_Ref.addData('sliderQ3.started', sliderQ3.tStartRefresh)
    experiment_Ref.addData('sliderQ3.stopped', sliderQ3.tStopRefresh)
    experiment_Ref.addData('LabelLeft3.started', LabelLeft3.tStartRefresh)
    experiment_Ref.addData('LabelLeft3.stopped', LabelLeft3.tStopRefresh)
    experiment_Ref.addData('LabelRight.started', LabelRight.tStartRefresh)
    experiment_Ref.addData('LabelRight.stopped', LabelRight.tStopRefresh)
    # the Routine "nasa_q3" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q4"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ4.reset()
    # keep track of which components have finished
    nasa_q4Components = [Question4, sliderQ4, LabelLeft4, LabelRight4]
    for thisComponent in nasa_q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q4"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q4Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q4Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question4* updates
        if Question4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question4.frameNStart = frameN  # exact frame index
            Question4.tStart = t  # local t and not account for scr refresh
            Question4.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question4, 'tStartRefresh')  # time at next scr refresh
            Question4.setAutoDraw(True)
        
        # *sliderQ4* updates
        if sliderQ4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ4.frameNStart = frameN  # exact frame index
            sliderQ4.tStart = t  # local t and not account for scr refresh
            sliderQ4.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ4, 'tStartRefresh')  # time at next scr refresh
            sliderQ4.setAutoDraw(True)
        
        # Check sliderQ4 for response to end routine
        if sliderQ4.getRating() is not None and sliderQ4.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft4* updates
        if LabelLeft4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft4.frameNStart = frameN  # exact frame index
            LabelLeft4.tStart = t  # local t and not account for scr refresh
            LabelLeft4.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft4, 'tStartRefresh')  # time at next scr refresh
            LabelLeft4.setAutoDraw(True)
        
        # *LabelRight4* updates
        if LabelRight4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight4.frameNStart = frameN  # exact frame index
            LabelRight4.tStart = t  # local t and not account for scr refresh
            LabelRight4.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight4, 'tStartRefresh')  # time at next scr refresh
            LabelRight4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q4"-------
    for thisComponent in nasa_q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question4.started', Question4.tStartRefresh)
    experiment_Ref.addData('Question4.stopped', Question4.tStopRefresh)
    experiment_Ref.addData('sliderQ4.response', sliderQ4.getRating())
    experiment_Ref.addData('sliderQ4.rt', sliderQ4.getRT())
    experiment_Ref.addData('sliderQ4.started', sliderQ4.tStartRefresh)
    experiment_Ref.addData('sliderQ4.stopped', sliderQ4.tStopRefresh)
    experiment_Ref.addData('LabelLeft4.started', LabelLeft4.tStartRefresh)
    experiment_Ref.addData('LabelLeft4.stopped', LabelLeft4.tStopRefresh)
    experiment_Ref.addData('LabelRight4.started', LabelRight4.tStartRefresh)
    experiment_Ref.addData('LabelRight4.stopped', LabelRight4.tStopRefresh)
    # the Routine "nasa_q4" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ5.reset()
    # keep track of which components have finished
    nasa_q5Components = [Question5, sliderQ5, LabelLeft5, LabelRight5]
    for thisComponent in nasa_q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q5"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q5Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q5Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question5* updates
        if Question5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question5.frameNStart = frameN  # exact frame index
            Question5.tStart = t  # local t and not account for scr refresh
            Question5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question5, 'tStartRefresh')  # time at next scr refresh
            Question5.setAutoDraw(True)
        
        # *sliderQ5* updates
        if sliderQ5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ5.frameNStart = frameN  # exact frame index
            sliderQ5.tStart = t  # local t and not account for scr refresh
            sliderQ5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ5, 'tStartRefresh')  # time at next scr refresh
            sliderQ5.setAutoDraw(True)
        
        # Check sliderQ5 for response to end routine
        if sliderQ5.getRating() is not None and sliderQ5.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft5* updates
        if LabelLeft5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft5.frameNStart = frameN  # exact frame index
            LabelLeft5.tStart = t  # local t and not account for scr refresh
            LabelLeft5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft5, 'tStartRefresh')  # time at next scr refresh
            LabelLeft5.setAutoDraw(True)
        
        # *LabelRight5* updates
        if LabelRight5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight5.frameNStart = frameN  # exact frame index
            LabelRight5.tStart = t  # local t and not account for scr refresh
            LabelRight5.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight5, 'tStartRefresh')  # time at next scr refresh
            LabelRight5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q5"-------
    for thisComponent in nasa_q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question5.started', Question5.tStartRefresh)
    experiment_Ref.addData('Question5.stopped', Question5.tStopRefresh)
    experiment_Ref.addData('sliderQ5.response', sliderQ5.getRating())
    experiment_Ref.addData('sliderQ5.rt', sliderQ5.getRT())
    experiment_Ref.addData('sliderQ5.started', sliderQ5.tStartRefresh)
    experiment_Ref.addData('sliderQ5.stopped', sliderQ5.tStopRefresh)
    experiment_Ref.addData('LabelLeft5.started', LabelLeft5.tStartRefresh)
    experiment_Ref.addData('LabelLeft5.stopped', LabelLeft5.tStopRefresh)
    experiment_Ref.addData('LabelRight5.started', LabelRight5.tStartRefresh)
    experiment_Ref.addData('LabelRight5.stopped', LabelRight5.tStopRefresh)
    # the Routine "nasa_q5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_q6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    sliderQ6.reset()
    # keep track of which components have finished
    nasa_q6Components = [Question6, sliderQ6, LabelLeft6, LabelRight6]
    for thisComponent in nasa_q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_q6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_q6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_q6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question6* updates
        if Question6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question6.frameNStart = frameN  # exact frame index
            Question6.tStart = t  # local t and not account for scr refresh
            Question6.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question6, 'tStartRefresh')  # time at next scr refresh
            Question6.setAutoDraw(True)
        
        # *sliderQ6* updates
        if sliderQ6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderQ6.frameNStart = frameN  # exact frame index
            sliderQ6.tStart = t  # local t and not account for scr refresh
            sliderQ6.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(sliderQ6, 'tStartRefresh')  # time at next scr refresh
            sliderQ6.setAutoDraw(True)
        
        # Check sliderQ6 for response to end routine
        if sliderQ6.getRating() is not None and sliderQ6.status == STARTED:
            continueRoutine_Part = False
        
        # *LabelLeft6* updates
        if LabelLeft6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelLeft6.frameNStart = frameN  # exact frame index
            LabelLeft6.tStart = t  # local t and not account for scr refresh
            LabelLeft6.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelLeft6, 'tStartRefresh')  # time at next scr refresh
            LabelLeft6.setAutoDraw(True)
        
        # *LabelRight6* updates
        if LabelRight6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelRight6.frameNStart = frameN  # exact frame index
            LabelRight6.tStart = t  # local t and not account for scr refresh
            LabelRight6.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(LabelRight6, 'tStartRefresh')  # time at next scr refresh
            LabelRight6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_q6"-------
    for thisComponent in nasa_q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question6.started', Question6.tStartRefresh)
    experiment_Ref.addData('Question6.stopped', Question6.tStopRefresh)
    experiment_Ref.addData('sliderQ6.response', sliderQ6.getRating())
    experiment_Ref.addData('sliderQ6.rt', sliderQ6.getRT())
    experiment_Ref.addData('sliderQ6.started', sliderQ6.tStartRefresh)
    experiment_Ref.addData('sliderQ6.stopped', sliderQ6.tStopRefresh)
    experiment_Ref.addData('LabelLeft6.started', LabelLeft6.tStartRefresh)
    experiment_Ref.addData('LabelLeft6.stopped', LabelLeft6.tStopRefresh)
    experiment_Ref.addData('LabelRight6.started', LabelRight6.tStartRefresh)
    experiment_Ref.addData('LabelRight6.stopped', LabelRight6.tStopRefresh)
    # the Routine "nasa_q6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_instructions_middle"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    key_resp_22.keys = []
    key_resp_22.rt = []
    _key_resp_22_allKeys = []
    # keep track of which components have finished
    nasa_instructions_middleComponents = [Instructions_2, key_resp_22]
    for thisComponent in nasa_instructions_middleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_instructions_middleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_instructions_middle"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_instructions_middleClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_instructions_middleClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_2* updates
        if Instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_2.frameNStart = frameN  # exact frame index
            Instructions_2.tStart = t  # local t and not account for scr refresh
            Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Instructions_2, 'tStartRefresh')  # time at next scr refresh
            Instructions_2.setAutoDraw(True)
        
        # *key_resp_22* updates
        waitOnFlip = False
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            key_resp_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win_ref.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
            win_ref.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_22.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_22_allKeys.extend(theseKeys)
            if len(_key_resp_22_allKeys):
                key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                # a response ends the routine
                continueRoutine_Part = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_instructions_middleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_instructions_middle"-------
    for thisComponent in nasa_instructions_middleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Instructions_2.started', Instructions_2.tStartRefresh)
    experiment_Ref.addData('Instructions_2.stopped', Instructions_2.tStopRefresh)
    # check responses
    if key_resp_22.keys in ['', [], None]:  # No response was made
        key_resp_22.keys = None
    experiment_Ref.addData('key_resp_22.keys',key_resp_22.keys)
    if key_resp_22.keys != None:  # we had a response
        experiment_Ref.addData('key_resp_22.rt', key_resp_22.rt)
    experiment_Ref.addData('key_resp_22.started', key_resp_22.tStartRefresh)
    experiment_Ref.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
    # the Routine "nasa_instructions_middle" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    # ------Prepare to start Routine "nasa_pair_2_3"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_2_3Components = [Question23, Question32, ChoseQ23, ChoseQ32]
    for thisComponent in nasa_pair_2_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_2_3"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_2_3Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_2_3Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question23* updates
        if Question23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question23.frameNStart = frameN  # exact frame index
            Question23.tStart = t  # local t and not account for scr refresh
            Question23.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question23, 'tStartRefresh')  # time at next scr refresh
            Question23.setAutoDraw(True)
        
        # *Question32* updates
        if Question32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question32.frameNStart = frameN  # exact frame index
            Question32.tStart = t  # local t and not account for scr refresh
            Question32.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question32, 'tStartRefresh')  # time at next scr refresh
            Question32.setAutoDraw(True)
        
        # *ChoseQ23* updates
        if ChoseQ23.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ23.frameNStart = frameN  # exact frame index
            ChoseQ23.tStart = t  # local t and not account for scr refresh
            ChoseQ23.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ23, 'tStartRefresh')  # time at next scr refresh
            ChoseQ23.setAutoDraw(True)
        if ChoseQ23.status == STARTED:
            # check whether ChoseQ23 has been pressed
            if ChoseQ23.isClicked:
                if not ChoseQ23.wasClicked:
                    ChoseQ23.timesOn.append(ChoseQ23.buttonClock.getTime()) # store time of first click
                    ChoseQ23.timesOff.append(ChoseQ23.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ23.timesOff[-1] = ChoseQ23.buttonClock.getTime() # update time clicked until
                if not ChoseQ23.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ23 is clicked
                    None
                ChoseQ23.wasClicked = True  # if ChoseQ23 is still clicked next frame, it is not a new click
            else:
                ChoseQ23.wasClicked = False  # if ChoseQ23 is clicked next frame, it is a new click
        else:
            ChoseQ23.wasClicked = False  # if ChoseQ23 is clicked next frame, it is a new click
        
        # *ChoseQ32* updates
        if ChoseQ32.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ32.frameNStart = frameN  # exact frame index
            ChoseQ32.tStart = t  # local t and not account for scr refresh
            ChoseQ32.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ32, 'tStartRefresh')  # time at next scr refresh
            ChoseQ32.setAutoDraw(True)
        if ChoseQ32.status == STARTED:
            # check whether ChoseQ32 has been pressed
            if ChoseQ32.isClicked:
                if not ChoseQ32.wasClicked:
                    ChoseQ32.timesOn.append(ChoseQ32.buttonClock.getTime()) # store time of first click
                    ChoseQ32.timesOff.append(ChoseQ32.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ32.timesOff[-1] = ChoseQ32.buttonClock.getTime() # update time clicked until
                if not ChoseQ32.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ32 is clicked
                    None
                ChoseQ32.wasClicked = True  # if ChoseQ32 is still clicked next frame, it is not a new click
            else:
                ChoseQ32.wasClicked = False  # if ChoseQ32 is clicked next frame, it is a new click
        else:
            ChoseQ32.wasClicked = False  # if ChoseQ32 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_2_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_2_3"-------
    for thisComponent in nasa_pair_2_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question23.started', Question23.tStartRefresh)
    experiment_Ref.addData('Question23.stopped', Question23.tStopRefresh)
    experiment_Ref.addData('Question32.started', Question32.tStartRefresh)
    experiment_Ref.addData('Question32.stopped', Question32.tStopRefresh)
    experiment_Ref.addData('ChoseQ23.started', ChoseQ23.tStartRefresh)
    experiment_Ref.addData('ChoseQ23.stopped', ChoseQ23.tStopRefresh)
    experiment_Ref.addData('ChoseQ23.numClicks', ChoseQ23.numClicks)
    if ChoseQ23.numClicks:
       experiment_Ref.addData('ChoseQ23.timesOn', ChoseQ23.timesOn)
       experiment_Ref.addData('ChoseQ23.timesOff', ChoseQ23.timesOff)
    else:
       experiment_Ref.addData('ChoseQ23.timesOn', "")
       experiment_Ref.addData('ChoseQ23.timesOff', "")
    experiment_Ref.addData('ChoseQ32.started', ChoseQ32.tStartRefresh)
    experiment_Ref.addData('ChoseQ32.stopped', ChoseQ32.tStopRefresh)
    experiment_Ref.addData('ChoseQ32.numClicks', ChoseQ32.numClicks)
    if ChoseQ32.numClicks:
       experiment_Ref.addData('ChoseQ32.timesOn', ChoseQ32.timesOn)
       experiment_Ref.addData('ChoseQ32.timesOff', ChoseQ32.timesOff)
    else:
       experiment_Ref.addData('ChoseQ32.timesOn', "")
       experiment_Ref.addData('ChoseQ32.timesOff', "")
    # the Routine "nasa_pair_2_3" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_4_5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_4_5Components = [Question45, Question54, ChoseQ45, ChoseQ54]
    for thisComponent in nasa_pair_4_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_4_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_4_5"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_4_5Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_4_5Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question45* updates
        if Question45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question45.frameNStart = frameN  # exact frame index
            Question45.tStart = t  # local t and not account for scr refresh
            Question45.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question45, 'tStartRefresh')  # time at next scr refresh
            Question45.setAutoDraw(True)
        
        # *Question54* updates
        if Question54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question54.frameNStart = frameN  # exact frame index
            Question54.tStart = t  # local t and not account for scr refresh
            Question54.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question54, 'tStartRefresh')  # time at next scr refresh
            Question54.setAutoDraw(True)
        
        # *ChoseQ45* updates
        if ChoseQ45.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ45.frameNStart = frameN  # exact frame index
            ChoseQ45.tStart = t  # local t and not account for scr refresh
            ChoseQ45.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ45, 'tStartRefresh')  # time at next scr refresh
            ChoseQ45.setAutoDraw(True)
        if ChoseQ45.status == STARTED:
            # check whether ChoseQ45 has been pressed
            if ChoseQ45.isClicked:
                if not ChoseQ45.wasClicked:
                    ChoseQ45.timesOn.append(ChoseQ45.buttonClock.getTime()) # store time of first click
                    ChoseQ45.timesOff.append(ChoseQ45.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ45.timesOff[-1] = ChoseQ45.buttonClock.getTime() # update time clicked until
                if not ChoseQ45.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ45 is clicked
                    None
                ChoseQ45.wasClicked = True  # if ChoseQ45 is still clicked next frame, it is not a new click
            else:
                ChoseQ45.wasClicked = False  # if ChoseQ45 is clicked next frame, it is a new click
        else:
            ChoseQ45.wasClicked = False  # if ChoseQ45 is clicked next frame, it is a new click
        
        # *ChoseQ54* updates
        if ChoseQ54.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ54.frameNStart = frameN  # exact frame index
            ChoseQ54.tStart = t  # local t and not account for scr refresh
            ChoseQ54.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ54, 'tStartRefresh')  # time at next scr refresh
            ChoseQ54.setAutoDraw(True)
        if ChoseQ54.status == STARTED:
            # check whether ChoseQ54 has been pressed
            if ChoseQ54.isClicked:
                if not ChoseQ54.wasClicked:
                    ChoseQ54.timesOn.append(ChoseQ54.buttonClock.getTime()) # store time of first click
                    ChoseQ54.timesOff.append(ChoseQ54.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ54.timesOff[-1] = ChoseQ54.buttonClock.getTime() # update time clicked until
                if not ChoseQ54.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ54 is clicked
                    None
                ChoseQ54.wasClicked = True  # if ChoseQ54 is still clicked next frame, it is not a new click
            else:
                ChoseQ54.wasClicked = False  # if ChoseQ54 is clicked next frame, it is a new click
        else:
            ChoseQ54.wasClicked = False  # if ChoseQ54 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_4_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_4_5"-------
    for thisComponent in nasa_pair_4_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question45.started', Question45.tStartRefresh)
    experiment_Ref.addData('Question45.stopped', Question45.tStopRefresh)
    experiment_Ref.addData('Question54.started', Question54.tStartRefresh)
    experiment_Ref.addData('Question54.stopped', Question54.tStopRefresh)
    experiment_Ref.addData('ChoseQ45.started', ChoseQ45.tStartRefresh)
    experiment_Ref.addData('ChoseQ45.stopped', ChoseQ45.tStopRefresh)
    experiment_Ref.addData('ChoseQ45.numClicks', ChoseQ45.numClicks)
    if ChoseQ45.numClicks:
       experiment_Ref.addData('ChoseQ45.timesOn', ChoseQ45.timesOn)
       experiment_Ref.addData('ChoseQ45.timesOff', ChoseQ45.timesOff)
    else:
       experiment_Ref.addData('ChoseQ45.timesOn', "")
       experiment_Ref.addData('ChoseQ45.timesOff', "")
    experiment_Ref.addData('ChoseQ54.started', ChoseQ54.tStartRefresh)
    experiment_Ref.addData('ChoseQ54.stopped', ChoseQ54.tStopRefresh)
    experiment_Ref.addData('ChoseQ54.numClicks', ChoseQ54.numClicks)
    if ChoseQ54.numClicks:
       experiment_Ref.addData('ChoseQ54.timesOn', ChoseQ54.timesOn)
       experiment_Ref.addData('ChoseQ54.timesOff', ChoseQ54.timesOff)
    else:
       experiment_Ref.addData('ChoseQ54.timesOn', "")
       experiment_Ref.addData('ChoseQ54.timesOff', "")
    # the Routine "nasa_pair_4_5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_1_2"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_1_2Components = [Question12, Question21, ChoseQ12, ChoseQ21]
    for thisComponent in nasa_pair_1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_1_2"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_1_2Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_1_2Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question12* updates
        if Question12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question12.frameNStart = frameN  # exact frame index
            Question12.tStart = t  # local t and not account for scr refresh
            Question12.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question12, 'tStartRefresh')  # time at next scr refresh
            Question12.setAutoDraw(True)
        
        # *Question21* updates
        if Question21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question21.frameNStart = frameN  # exact frame index
            Question21.tStart = t  # local t and not account for scr refresh
            Question21.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question21, 'tStartRefresh')  # time at next scr refresh
            Question21.setAutoDraw(True)
        
        # *ChoseQ12* updates
        if ChoseQ12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ12.frameNStart = frameN  # exact frame index
            ChoseQ12.tStart = t  # local t and not account for scr refresh
            ChoseQ12.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ12, 'tStartRefresh')  # time at next scr refresh
            ChoseQ12.setAutoDraw(True)
        if ChoseQ12.status == STARTED:
            # check whether ChoseQ12 has been pressed
            if ChoseQ12.isClicked:
                if not ChoseQ12.wasClicked:
                    ChoseQ12.timesOn.append(ChoseQ12.buttonClock.getTime()) # store time of first click
                    ChoseQ12.timesOff.append(ChoseQ12.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ12.timesOff[-1] = ChoseQ12.buttonClock.getTime() # update time clicked until
                if not ChoseQ12.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ12 is clicked
                    None
                ChoseQ12.wasClicked = True  # if ChoseQ12 is still clicked next frame, it is not a new click
            else:
                ChoseQ12.wasClicked = False  # if ChoseQ12 is clicked next frame, it is a new click
        else:
            ChoseQ12.wasClicked = False  # if ChoseQ12 is clicked next frame, it is a new click
        
        # *ChoseQ21* updates
        if ChoseQ21.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ21.frameNStart = frameN  # exact frame index
            ChoseQ21.tStart = t  # local t and not account for scr refresh
            ChoseQ21.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ21, 'tStartRefresh')  # time at next scr refresh
            ChoseQ21.setAutoDraw(True)
        if ChoseQ21.status == STARTED:
            # check whether ChoseQ21 has been pressed
            if ChoseQ21.isClicked:
                if not ChoseQ21.wasClicked:
                    ChoseQ21.timesOn.append(ChoseQ21.buttonClock.getTime()) # store time of first click
                    ChoseQ21.timesOff.append(ChoseQ21.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ21.timesOff[-1] = ChoseQ21.buttonClock.getTime() # update time clicked until
                if not ChoseQ21.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ21 is clicked
                    None
                ChoseQ21.wasClicked = True  # if ChoseQ21 is still clicked next frame, it is not a new click
            else:
                ChoseQ21.wasClicked = False  # if ChoseQ21 is clicked next frame, it is a new click
        else:
            ChoseQ21.wasClicked = False  # if ChoseQ21 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_1_2"-------
    for thisComponent in nasa_pair_1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question12.started', Question12.tStartRefresh)
    experiment_Ref.addData('Question12.stopped', Question12.tStopRefresh)
    experiment_Ref.addData('Question21.started', Question21.tStartRefresh)
    experiment_Ref.addData('Question21.stopped', Question21.tStopRefresh)
    experiment_Ref.addData('ChoseQ12.started', ChoseQ12.tStartRefresh)
    experiment_Ref.addData('ChoseQ12.stopped', ChoseQ12.tStopRefresh)
    experiment_Ref.addData('ChoseQ12.numClicks', ChoseQ12.numClicks)
    if ChoseQ12.numClicks:
       experiment_Ref.addData('ChoseQ12.timesOn', ChoseQ12.timesOn)
       experiment_Ref.addData('ChoseQ12.timesOff', ChoseQ12.timesOff)
    else:
       experiment_Ref.addData('ChoseQ12.timesOn', "")
       experiment_Ref.addData('ChoseQ12.timesOff', "")
    experiment_Ref.addData('ChoseQ21.started', ChoseQ21.tStartRefresh)
    experiment_Ref.addData('ChoseQ21.stopped', ChoseQ21.tStopRefresh)
    experiment_Ref.addData('ChoseQ21.numClicks', ChoseQ21.numClicks)
    if ChoseQ21.numClicks:
       experiment_Ref.addData('ChoseQ21.timesOn', ChoseQ21.timesOn)
       experiment_Ref.addData('ChoseQ21.timesOff', ChoseQ21.timesOff)
    else:
       experiment_Ref.addData('ChoseQ21.timesOn', "")
       experiment_Ref.addData('ChoseQ21.timesOff', "")
    # the Routine "nasa_pair_1_2" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_5_6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_5_6Components = [Question56, Question65, ChoseQ56, ChoseQ65]
    for thisComponent in nasa_pair_5_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_5_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_5_6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_5_6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_5_6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question56* updates
        if Question56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question56.frameNStart = frameN  # exact frame index
            Question56.tStart = t  # local t and not account for scr refresh
            Question56.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question56, 'tStartRefresh')  # time at next scr refresh
            Question56.setAutoDraw(True)
        
        # *Question65* updates
        if Question65.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question65.frameNStart = frameN  # exact frame index
            Question65.tStart = t  # local t and not account for scr refresh
            Question65.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question65, 'tStartRefresh')  # time at next scr refresh
            Question65.setAutoDraw(True)
        
        # *ChoseQ56* updates
        if ChoseQ56.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ56.frameNStart = frameN  # exact frame index
            ChoseQ56.tStart = t  # local t and not account for scr refresh
            ChoseQ56.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ56, 'tStartRefresh')  # time at next scr refresh
            ChoseQ56.setAutoDraw(True)
        if ChoseQ56.status == STARTED:
            # check whether ChoseQ56 has been pressed
            if ChoseQ56.isClicked:
                if not ChoseQ56.wasClicked:
                    ChoseQ56.timesOn.append(ChoseQ56.buttonClock.getTime()) # store time of first click
                    ChoseQ56.timesOff.append(ChoseQ56.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ56.timesOff[-1] = ChoseQ56.buttonClock.getTime() # update time clicked until
                if not ChoseQ56.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ56 is clicked
                    None
                ChoseQ56.wasClicked = True  # if ChoseQ56 is still clicked next frame, it is not a new click
            else:
                ChoseQ56.wasClicked = False  # if ChoseQ56 is clicked next frame, it is a new click
        else:
            ChoseQ56.wasClicked = False  # if ChoseQ56 is clicked next frame, it is a new click
        
        # *ChoseQ65* updates
        if ChoseQ65.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ65.frameNStart = frameN  # exact frame index
            ChoseQ65.tStart = t  # local t and not account for scr refresh
            ChoseQ65.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ65, 'tStartRefresh')  # time at next scr refresh
            ChoseQ65.setAutoDraw(True)
        if ChoseQ65.status == STARTED:
            # check whether ChoseQ65 has been pressed
            if ChoseQ65.isClicked:
                if not ChoseQ65.wasClicked:
                    ChoseQ65.timesOn.append(ChoseQ65.buttonClock.getTime()) # store time of first click
                    ChoseQ65.timesOff.append(ChoseQ65.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ65.timesOff[-1] = ChoseQ65.buttonClock.getTime() # update time clicked until
                if not ChoseQ65.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ65 is clicked
                    None
                ChoseQ65.wasClicked = True  # if ChoseQ65 is still clicked next frame, it is not a new click
            else:
                ChoseQ65.wasClicked = False  # if ChoseQ65 is clicked next frame, it is a new click
        else:
            ChoseQ65.wasClicked = False  # if ChoseQ65 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_5_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_5_6"-------
    for thisComponent in nasa_pair_5_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question56.started', Question56.tStartRefresh)
    experiment_Ref.addData('Question56.stopped', Question56.tStopRefresh)
    experiment_Ref.addData('Question65.started', Question65.tStartRefresh)
    experiment_Ref.addData('Question65.stopped', Question65.tStopRefresh)
    experiment_Ref.addData('ChoseQ56.started', ChoseQ56.tStartRefresh)
    experiment_Ref.addData('ChoseQ56.stopped', ChoseQ56.tStopRefresh)
    experiment_Ref.addData('ChoseQ56.numClicks', ChoseQ56.numClicks)
    if ChoseQ56.numClicks:
       experiment_Ref.addData('ChoseQ56.timesOn', ChoseQ56.timesOn)
       experiment_Ref.addData('ChoseQ56.timesOff', ChoseQ56.timesOff)
    else:
       experiment_Ref.addData('ChoseQ56.timesOn', "")
       experiment_Ref.addData('ChoseQ56.timesOff', "")
    experiment_Ref.addData('ChoseQ65.started', ChoseQ65.tStartRefresh)
    experiment_Ref.addData('ChoseQ65.stopped', ChoseQ65.tStopRefresh)
    experiment_Ref.addData('ChoseQ65.numClicks', ChoseQ65.numClicks)
    if ChoseQ65.numClicks:
       experiment_Ref.addData('ChoseQ65.timesOn', ChoseQ65.timesOn)
       experiment_Ref.addData('ChoseQ65.timesOff', ChoseQ65.timesOff)
    else:
       experiment_Ref.addData('ChoseQ65.timesOn', "")
       experiment_Ref.addData('ChoseQ65.timesOff', "")
    # the Routine "nasa_pair_5_6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_2_4"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_2_4Components = [Question24, Question42, ChoseQ24, ChoseQ42]
    for thisComponent in nasa_pair_2_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_2_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_2_4"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_2_4Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_2_4Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question24* updates
        if Question24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question24.frameNStart = frameN  # exact frame index
            Question24.tStart = t  # local t and not account for scr refresh
            Question24.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question24, 'tStartRefresh')  # time at next scr refresh
            Question24.setAutoDraw(True)
        
        # *Question42* updates
        if Question42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question42.frameNStart = frameN  # exact frame index
            Question42.tStart = t  # local t and not account for scr refresh
            Question42.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question42, 'tStartRefresh')  # time at next scr refresh
            Question42.setAutoDraw(True)
        
        # *ChoseQ24* updates
        if ChoseQ24.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ24.frameNStart = frameN  # exact frame index
            ChoseQ24.tStart = t  # local t and not account for scr refresh
            ChoseQ24.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ24, 'tStartRefresh')  # time at next scr refresh
            ChoseQ24.setAutoDraw(True)
        if ChoseQ24.status == STARTED:
            # check whether ChoseQ24 has been pressed
            if ChoseQ24.isClicked:
                if not ChoseQ24.wasClicked:
                    ChoseQ24.timesOn.append(ChoseQ24.buttonClock.getTime()) # store time of first click
                    ChoseQ24.timesOff.append(ChoseQ24.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ24.timesOff[-1] = ChoseQ24.buttonClock.getTime() # update time clicked until
                if not ChoseQ24.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ24 is clicked
                    None
                ChoseQ24.wasClicked = True  # if ChoseQ24 is still clicked next frame, it is not a new click
            else:
                ChoseQ24.wasClicked = False  # if ChoseQ24 is clicked next frame, it is a new click
        else:
            ChoseQ24.wasClicked = False  # if ChoseQ24 is clicked next frame, it is a new click
        
        # *ChoseQ42* updates
        if ChoseQ42.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ42.frameNStart = frameN  # exact frame index
            ChoseQ42.tStart = t  # local t and not account for scr refresh
            ChoseQ42.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ42, 'tStartRefresh')  # time at next scr refresh
            ChoseQ42.setAutoDraw(True)
        if ChoseQ42.status == STARTED:
            # check whether ChoseQ42 has been pressed
            if ChoseQ42.isClicked:
                if not ChoseQ42.wasClicked:
                    ChoseQ42.timesOn.append(ChoseQ42.buttonClock.getTime()) # store time of first click
                    ChoseQ42.timesOff.append(ChoseQ42.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ42.timesOff[-1] = ChoseQ42.buttonClock.getTime() # update time clicked until
                if not ChoseQ42.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ42 is clicked
                    None
                ChoseQ42.wasClicked = True  # if ChoseQ42 is still clicked next frame, it is not a new click
            else:
                ChoseQ42.wasClicked = False  # if ChoseQ42 is clicked next frame, it is a new click
        else:
            ChoseQ42.wasClicked = False  # if ChoseQ42 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_2_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_2_4"-------
    for thisComponent in nasa_pair_2_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question24.started', Question24.tStartRefresh)
    experiment_Ref.addData('Question24.stopped', Question24.tStopRefresh)
    experiment_Ref.addData('Question42.started', Question42.tStartRefresh)
    experiment_Ref.addData('Question42.stopped', Question42.tStopRefresh)
    experiment_Ref.addData('ChoseQ24.started', ChoseQ24.tStartRefresh)
    experiment_Ref.addData('ChoseQ24.stopped', ChoseQ24.tStopRefresh)
    experiment_Ref.addData('ChoseQ24.numClicks', ChoseQ24.numClicks)
    if ChoseQ24.numClicks:
       experiment_Ref.addData('ChoseQ24.timesOn', ChoseQ24.timesOn)
       experiment_Ref.addData('ChoseQ24.timesOff', ChoseQ24.timesOff)
    else:
       experiment_Ref.addData('ChoseQ24.timesOn', "")
       experiment_Ref.addData('ChoseQ24.timesOff', "")
    experiment_Ref.addData('ChoseQ42.started', ChoseQ42.tStartRefresh)
    experiment_Ref.addData('ChoseQ42.stopped', ChoseQ42.tStopRefresh)
    experiment_Ref.addData('ChoseQ42.numClicks', ChoseQ42.numClicks)
    if ChoseQ42.numClicks:
       experiment_Ref.addData('ChoseQ42.timesOn', ChoseQ42.timesOn)
       experiment_Ref.addData('ChoseQ42.timesOff', ChoseQ42.timesOff)
    else:
       experiment_Ref.addData('ChoseQ42.timesOn', "")
       experiment_Ref.addData('ChoseQ42.timesOff', "")
    # the Routine "nasa_pair_2_4" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_1_5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_1_5Components = [Question15, Question51, ChoseQ15, ChoseQ51]
    for thisComponent in nasa_pair_1_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_1_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_1_5"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_1_5Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_1_5Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question15* updates
        if Question15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question15.frameNStart = frameN  # exact frame index
            Question15.tStart = t  # local t and not account for scr refresh
            Question15.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question15, 'tStartRefresh')  # time at next scr refresh
            Question15.setAutoDraw(True)
        
        # *Question51* updates
        if Question51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question51.frameNStart = frameN  # exact frame index
            Question51.tStart = t  # local t and not account for scr refresh
            Question51.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question51, 'tStartRefresh')  # time at next scr refresh
            Question51.setAutoDraw(True)
        
        # *ChoseQ15* updates
        if ChoseQ15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ15.frameNStart = frameN  # exact frame index
            ChoseQ15.tStart = t  # local t and not account for scr refresh
            ChoseQ15.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ15, 'tStartRefresh')  # time at next scr refresh
            ChoseQ15.setAutoDraw(True)
        if ChoseQ15.status == STARTED:
            # check whether ChoseQ15 has been pressed
            if ChoseQ15.isClicked:
                if not ChoseQ15.wasClicked:
                    ChoseQ15.timesOn.append(ChoseQ15.buttonClock.getTime()) # store time of first click
                    ChoseQ15.timesOff.append(ChoseQ15.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ15.timesOff[-1] = ChoseQ15.buttonClock.getTime() # update time clicked until
                if not ChoseQ15.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ15 is clicked
                    None
                ChoseQ15.wasClicked = True  # if ChoseQ15 is still clicked next frame, it is not a new click
            else:
                ChoseQ15.wasClicked = False  # if ChoseQ15 is clicked next frame, it is a new click
        else:
            ChoseQ15.wasClicked = False  # if ChoseQ15 is clicked next frame, it is a new click
        
        # *ChoseQ51* updates
        if ChoseQ51.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ51.frameNStart = frameN  # exact frame index
            ChoseQ51.tStart = t  # local t and not account for scr refresh
            ChoseQ51.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ51, 'tStartRefresh')  # time at next scr refresh
            ChoseQ51.setAutoDraw(True)
        if ChoseQ51.status == STARTED:
            # check whether ChoseQ51 has been pressed
            if ChoseQ51.isClicked:
                if not ChoseQ51.wasClicked:
                    ChoseQ51.timesOn.append(ChoseQ51.buttonClock.getTime()) # store time of first click
                    ChoseQ51.timesOff.append(ChoseQ51.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ51.timesOff[-1] = ChoseQ51.buttonClock.getTime() # update time clicked until
                if not ChoseQ51.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ51 is clicked
                    None
                ChoseQ51.wasClicked = True  # if ChoseQ51 is still clicked next frame, it is not a new click
            else:
                ChoseQ51.wasClicked = False  # if ChoseQ51 is clicked next frame, it is a new click
        else:
            ChoseQ51.wasClicked = False  # if ChoseQ51 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_1_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_1_5"-------
    for thisComponent in nasa_pair_1_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question15.started', Question15.tStartRefresh)
    experiment_Ref.addData('Question15.stopped', Question15.tStopRefresh)
    experiment_Ref.addData('Question51.started', Question51.tStartRefresh)
    experiment_Ref.addData('Question51.stopped', Question51.tStopRefresh)
    experiment_Ref.addData('ChoseQ15.started', ChoseQ15.tStartRefresh)
    experiment_Ref.addData('ChoseQ15.stopped', ChoseQ15.tStopRefresh)
    experiment_Ref.addData('ChoseQ15.numClicks', ChoseQ15.numClicks)
    if ChoseQ15.numClicks:
       experiment_Ref.addData('ChoseQ15.timesOn', ChoseQ15.timesOn)
       experiment_Ref.addData('ChoseQ15.timesOff', ChoseQ15.timesOff)
    else:
       experiment_Ref.addData('ChoseQ15.timesOn', "")
       experiment_Ref.addData('ChoseQ15.timesOff', "")
    experiment_Ref.addData('ChoseQ51.started', ChoseQ51.tStartRefresh)
    experiment_Ref.addData('ChoseQ51.stopped', ChoseQ51.tStopRefresh)
    experiment_Ref.addData('ChoseQ51.numClicks', ChoseQ51.numClicks)
    if ChoseQ51.numClicks:
       experiment_Ref.addData('ChoseQ51.timesOn', ChoseQ51.timesOn)
       experiment_Ref.addData('ChoseQ51.timesOff', ChoseQ51.timesOff)
    else:
       experiment_Ref.addData('ChoseQ51.timesOn', "")
       experiment_Ref.addData('ChoseQ51.timesOff', "")
    # the Routine "nasa_pair_1_5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_4_6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_4_6Components = [Question46, Question64, ChoseQ46, ChoseQ64]
    for thisComponent in nasa_pair_4_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_4_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_4_6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_4_6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_4_6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question46* updates
        if Question46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question46.frameNStart = frameN  # exact frame index
            Question46.tStart = t  # local t and not account for scr refresh
            Question46.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question46, 'tStartRefresh')  # time at next scr refresh
            Question46.setAutoDraw(True)
        
        # *Question64* updates
        if Question64.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question64.frameNStart = frameN  # exact frame index
            Question64.tStart = t  # local t and not account for scr refresh
            Question64.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question64, 'tStartRefresh')  # time at next scr refresh
            Question64.setAutoDraw(True)
        
        # *ChoseQ46* updates
        if ChoseQ46.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ46.frameNStart = frameN  # exact frame index
            ChoseQ46.tStart = t  # local t and not account for scr refresh
            ChoseQ46.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ46, 'tStartRefresh')  # time at next scr refresh
            ChoseQ46.setAutoDraw(True)
        if ChoseQ46.status == STARTED:
            # check whether ChoseQ46 has been pressed
            if ChoseQ46.isClicked:
                if not ChoseQ46.wasClicked:
                    ChoseQ46.timesOn.append(ChoseQ46.buttonClock.getTime()) # store time of first click
                    ChoseQ46.timesOff.append(ChoseQ46.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ46.timesOff[-1] = ChoseQ46.buttonClock.getTime() # update time clicked until
                if not ChoseQ46.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ46 is clicked
                    None
                ChoseQ46.wasClicked = True  # if ChoseQ46 is still clicked next frame, it is not a new click
            else:
                ChoseQ46.wasClicked = False  # if ChoseQ46 is clicked next frame, it is a new click
        else:
            ChoseQ46.wasClicked = False  # if ChoseQ46 is clicked next frame, it is a new click
        
        # *ChoseQ64* updates
        if ChoseQ64.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ64.frameNStart = frameN  # exact frame index
            ChoseQ64.tStart = t  # local t and not account for scr refresh
            ChoseQ64.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ64, 'tStartRefresh')  # time at next scr refresh
            ChoseQ64.setAutoDraw(True)
        if ChoseQ64.status == STARTED:
            # check whether ChoseQ64 has been pressed
            if ChoseQ64.isClicked:
                if not ChoseQ64.wasClicked:
                    ChoseQ64.timesOn.append(ChoseQ64.buttonClock.getTime()) # store time of first click
                    ChoseQ64.timesOff.append(ChoseQ64.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ64.timesOff[-1] = ChoseQ64.buttonClock.getTime() # update time clicked until
                if not ChoseQ64.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ64 is clicked
                    None
                ChoseQ64.wasClicked = True  # if ChoseQ64 is still clicked next frame, it is not a new click
            else:
                ChoseQ64.wasClicked = False  # if ChoseQ64 is clicked next frame, it is a new click
        else:
            ChoseQ64.wasClicked = False  # if ChoseQ64 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_4_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_4_6"-------
    for thisComponent in nasa_pair_4_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question46.started', Question46.tStartRefresh)
    experiment_Ref.addData('Question46.stopped', Question46.tStopRefresh)
    experiment_Ref.addData('Question64.started', Question64.tStartRefresh)
    experiment_Ref.addData('Question64.stopped', Question64.tStopRefresh)
    experiment_Ref.addData('ChoseQ46.started', ChoseQ46.tStartRefresh)
    experiment_Ref.addData('ChoseQ46.stopped', ChoseQ46.tStopRefresh)
    experiment_Ref.addData('ChoseQ46.numClicks', ChoseQ46.numClicks)
    if ChoseQ46.numClicks:
       experiment_Ref.addData('ChoseQ46.timesOn', ChoseQ46.timesOn)
       experiment_Ref.addData('ChoseQ46.timesOff', ChoseQ46.timesOff)
    else:
       experiment_Ref.addData('ChoseQ46.timesOn', "")
       experiment_Ref.addData('ChoseQ46.timesOff', "")
    experiment_Ref.addData('ChoseQ64.started', ChoseQ64.tStartRefresh)
    experiment_Ref.addData('ChoseQ64.stopped', ChoseQ64.tStopRefresh)
    experiment_Ref.addData('ChoseQ64.numClicks', ChoseQ64.numClicks)
    if ChoseQ64.numClicks:
       experiment_Ref.addData('ChoseQ64.timesOn', ChoseQ64.timesOn)
       experiment_Ref.addData('ChoseQ64.timesOff', ChoseQ64.timesOff)
    else:
       experiment_Ref.addData('ChoseQ64.timesOn', "")
       experiment_Ref.addData('ChoseQ64.timesOff', "")
    # the Routine "nasa_pair_4_6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_2_5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_2_5Components = [Question25, Question52, ChoseQ25, ChoseQ52]
    for thisComponent in nasa_pair_2_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_2_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_2_5"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_2_5Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_2_5Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question25* updates
        if Question25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question25.frameNStart = frameN  # exact frame index
            Question25.tStart = t  # local t and not account for scr refresh
            Question25.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question25, 'tStartRefresh')  # time at next scr refresh
            Question25.setAutoDraw(True)
        
        # *Question52* updates
        if Question52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question52.frameNStart = frameN  # exact frame index
            Question52.tStart = t  # local t and not account for scr refresh
            Question52.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question52, 'tStartRefresh')  # time at next scr refresh
            Question52.setAutoDraw(True)
        
        # *ChoseQ25* updates
        if ChoseQ25.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ25.frameNStart = frameN  # exact frame index
            ChoseQ25.tStart = t  # local t and not account for scr refresh
            ChoseQ25.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ25, 'tStartRefresh')  # time at next scr refresh
            ChoseQ25.setAutoDraw(True)
        if ChoseQ25.status == STARTED:
            # check whether ChoseQ25 has been pressed
            if ChoseQ25.isClicked:
                if not ChoseQ25.wasClicked:
                    ChoseQ25.timesOn.append(ChoseQ25.buttonClock.getTime()) # store time of first click
                    ChoseQ25.timesOff.append(ChoseQ25.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ25.timesOff[-1] = ChoseQ25.buttonClock.getTime() # update time clicked until
                if not ChoseQ25.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ25 is clicked
                    None
                ChoseQ25.wasClicked = True  # if ChoseQ25 is still clicked next frame, it is not a new click
            else:
                ChoseQ25.wasClicked = False  # if ChoseQ25 is clicked next frame, it is a new click
        else:
            ChoseQ25.wasClicked = False  # if ChoseQ25 is clicked next frame, it is a new click
        
        # *ChoseQ52* updates
        if ChoseQ52.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ52.frameNStart = frameN  # exact frame index
            ChoseQ52.tStart = t  # local t and not account for scr refresh
            ChoseQ52.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ52, 'tStartRefresh')  # time at next scr refresh
            ChoseQ52.setAutoDraw(True)
        if ChoseQ52.status == STARTED:
            # check whether ChoseQ52 has been pressed
            if ChoseQ52.isClicked:
                if not ChoseQ52.wasClicked:
                    ChoseQ52.timesOn.append(ChoseQ52.buttonClock.getTime()) # store time of first click
                    ChoseQ52.timesOff.append(ChoseQ52.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ52.timesOff[-1] = ChoseQ52.buttonClock.getTime() # update time clicked until
                if not ChoseQ52.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ52 is clicked
                    None
                ChoseQ52.wasClicked = True  # if ChoseQ52 is still clicked next frame, it is not a new click
            else:
                ChoseQ52.wasClicked = False  # if ChoseQ52 is clicked next frame, it is a new click
        else:
            ChoseQ52.wasClicked = False  # if ChoseQ52 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_2_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_2_5"-------
    for thisComponent in nasa_pair_2_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question25.started', Question25.tStartRefresh)
    experiment_Ref.addData('Question25.stopped', Question25.tStopRefresh)
    experiment_Ref.addData('Question52.started', Question52.tStartRefresh)
    experiment_Ref.addData('Question52.stopped', Question52.tStopRefresh)
    experiment_Ref.addData('ChoseQ25.started', ChoseQ25.tStartRefresh)
    experiment_Ref.addData('ChoseQ25.stopped', ChoseQ25.tStopRefresh)
    experiment_Ref.addData('ChoseQ25.numClicks', ChoseQ25.numClicks)
    if ChoseQ25.numClicks:
       experiment_Ref.addData('ChoseQ25.timesOn', ChoseQ25.timesOn)
       experiment_Ref.addData('ChoseQ25.timesOff', ChoseQ25.timesOff)
    else:
       experiment_Ref.addData('ChoseQ25.timesOn', "")
       experiment_Ref.addData('ChoseQ25.timesOff', "")
    experiment_Ref.addData('ChoseQ52.started', ChoseQ52.tStartRefresh)
    experiment_Ref.addData('ChoseQ52.stopped', ChoseQ52.tStopRefresh)
    experiment_Ref.addData('ChoseQ52.numClicks', ChoseQ52.numClicks)
    if ChoseQ52.numClicks:
       experiment_Ref.addData('ChoseQ52.timesOn', ChoseQ52.timesOn)
       experiment_Ref.addData('ChoseQ52.timesOff', ChoseQ52.timesOff)
    else:
       experiment_Ref.addData('ChoseQ52.timesOn', "")
       experiment_Ref.addData('ChoseQ52.timesOff', "")
    # the Routine "nasa_pair_2_5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_1_4"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_1_4Components = [Question14, Question41, ChoseQ14, ChoseQ41]
    for thisComponent in nasa_pair_1_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_1_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_1_4"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_1_4Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_1_4Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question14* updates
        if Question14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question14.frameNStart = frameN  # exact frame index
            Question14.tStart = t  # local t and not account for scr refresh
            Question14.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question14, 'tStartRefresh')  # time at next scr refresh
            Question14.setAutoDraw(True)
        
        # *Question41* updates
        if Question41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question41.frameNStart = frameN  # exact frame index
            Question41.tStart = t  # local t and not account for scr refresh
            Question41.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question41, 'tStartRefresh')  # time at next scr refresh
            Question41.setAutoDraw(True)
        
        # *ChoseQ14* updates
        if ChoseQ14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ14.frameNStart = frameN  # exact frame index
            ChoseQ14.tStart = t  # local t and not account for scr refresh
            ChoseQ14.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ14, 'tStartRefresh')  # time at next scr refresh
            ChoseQ14.setAutoDraw(True)
        if ChoseQ14.status == STARTED:
            # check whether ChoseQ14 has been pressed
            if ChoseQ14.isClicked:
                if not ChoseQ14.wasClicked:
                    ChoseQ14.timesOn.append(ChoseQ14.buttonClock.getTime()) # store time of first click
                    ChoseQ14.timesOff.append(ChoseQ14.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ14.timesOff[-1] = ChoseQ14.buttonClock.getTime() # update time clicked until
                if not ChoseQ14.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ14 is clicked
                    None
                ChoseQ14.wasClicked = True  # if ChoseQ14 is still clicked next frame, it is not a new click
            else:
                ChoseQ14.wasClicked = False  # if ChoseQ14 is clicked next frame, it is a new click
        else:
            ChoseQ14.wasClicked = False  # if ChoseQ14 is clicked next frame, it is a new click
        
        # *ChoseQ41* updates
        if ChoseQ41.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ41.frameNStart = frameN  # exact frame index
            ChoseQ41.tStart = t  # local t and not account for scr refresh
            ChoseQ41.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ41, 'tStartRefresh')  # time at next scr refresh
            ChoseQ41.setAutoDraw(True)
        if ChoseQ41.status == STARTED:
            # check whether ChoseQ41 has been pressed
            if ChoseQ41.isClicked:
                if not ChoseQ41.wasClicked:
                    ChoseQ41.timesOn.append(ChoseQ41.buttonClock.getTime()) # store time of first click
                    ChoseQ41.timesOff.append(ChoseQ41.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ41.timesOff[-1] = ChoseQ41.buttonClock.getTime() # update time clicked until
                if not ChoseQ41.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ41 is clicked
                    None
                ChoseQ41.wasClicked = True  # if ChoseQ41 is still clicked next frame, it is not a new click
            else:
                ChoseQ41.wasClicked = False  # if ChoseQ41 is clicked next frame, it is a new click
        else:
            ChoseQ41.wasClicked = False  # if ChoseQ41 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_1_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_1_4"-------
    for thisComponent in nasa_pair_1_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question14.started', Question14.tStartRefresh)
    experiment_Ref.addData('Question14.stopped', Question14.tStopRefresh)
    experiment_Ref.addData('Question41.started', Question41.tStartRefresh)
    experiment_Ref.addData('Question41.stopped', Question41.tStopRefresh)
    experiment_Ref.addData('ChoseQ14.started', ChoseQ14.tStartRefresh)
    experiment_Ref.addData('ChoseQ14.stopped', ChoseQ14.tStopRefresh)
    experiment_Ref.addData('ChoseQ14.numClicks', ChoseQ14.numClicks)
    if ChoseQ14.numClicks:
       experiment_Ref.addData('ChoseQ14.timesOn', ChoseQ14.timesOn)
       experiment_Ref.addData('ChoseQ14.timesOff', ChoseQ14.timesOff)
    else:
       experiment_Ref.addData('ChoseQ14.timesOn', "")
       experiment_Ref.addData('ChoseQ14.timesOff', "")
    experiment_Ref.addData('ChoseQ41.started', ChoseQ41.tStartRefresh)
    experiment_Ref.addData('ChoseQ41.stopped', ChoseQ41.tStopRefresh)
    experiment_Ref.addData('ChoseQ41.numClicks', ChoseQ41.numClicks)
    if ChoseQ41.numClicks:
       experiment_Ref.addData('ChoseQ41.timesOn', ChoseQ41.timesOn)
       experiment_Ref.addData('ChoseQ41.timesOff', ChoseQ41.timesOff)
    else:
       experiment_Ref.addData('ChoseQ41.timesOn', "")
       experiment_Ref.addData('ChoseQ41.timesOff', "")
    # the Routine "nasa_pair_1_4" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_3_4"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_3_4Components = [Question34, Question43, ChoseQ34, ChoseQ43]
    for thisComponent in nasa_pair_3_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_3_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_3_4"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_3_4Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_3_4Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question34* updates
        if Question34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question34.frameNStart = frameN  # exact frame index
            Question34.tStart = t  # local t and not account for scr refresh
            Question34.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question34, 'tStartRefresh')  # time at next scr refresh
            Question34.setAutoDraw(True)
        
        # *Question43* updates
        if Question43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question43.frameNStart = frameN  # exact frame index
            Question43.tStart = t  # local t and not account for scr refresh
            Question43.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question43, 'tStartRefresh')  # time at next scr refresh
            Question43.setAutoDraw(True)
        
        # *ChoseQ34* updates
        if ChoseQ34.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ34.frameNStart = frameN  # exact frame index
            ChoseQ34.tStart = t  # local t and not account for scr refresh
            ChoseQ34.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ34, 'tStartRefresh')  # time at next scr refresh
            ChoseQ34.setAutoDraw(True)
        if ChoseQ34.status == STARTED:
            # check whether ChoseQ34 has been pressed
            if ChoseQ34.isClicked:
                if not ChoseQ34.wasClicked:
                    ChoseQ34.timesOn.append(ChoseQ34.buttonClock.getTime()) # store time of first click
                    ChoseQ34.timesOff.append(ChoseQ34.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ34.timesOff[-1] = ChoseQ34.buttonClock.getTime() # update time clicked until
                if not ChoseQ34.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ34 is clicked
                    None
                ChoseQ34.wasClicked = True  # if ChoseQ34 is still clicked next frame, it is not a new click
            else:
                ChoseQ34.wasClicked = False  # if ChoseQ34 is clicked next frame, it is a new click
        else:
            ChoseQ34.wasClicked = False  # if ChoseQ34 is clicked next frame, it is a new click
        
        # *ChoseQ43* updates
        if ChoseQ43.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ43.frameNStart = frameN  # exact frame index
            ChoseQ43.tStart = t  # local t and not account for scr refresh
            ChoseQ43.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ43, 'tStartRefresh')  # time at next scr refresh
            ChoseQ43.setAutoDraw(True)
        if ChoseQ43.status == STARTED:
            # check whether ChoseQ43 has been pressed
            if ChoseQ43.isClicked:
                if not ChoseQ43.wasClicked:
                    ChoseQ43.timesOn.append(ChoseQ43.buttonClock.getTime()) # store time of first click
                    ChoseQ43.timesOff.append(ChoseQ43.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ43.timesOff[-1] = ChoseQ43.buttonClock.getTime() # update time clicked until
                if not ChoseQ43.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ43 is clicked
                    None
                ChoseQ43.wasClicked = True  # if ChoseQ43 is still clicked next frame, it is not a new click
            else:
                ChoseQ43.wasClicked = False  # if ChoseQ43 is clicked next frame, it is a new click
        else:
            ChoseQ43.wasClicked = False  # if ChoseQ43 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_3_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_3_4"-------
    for thisComponent in nasa_pair_3_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question34.started', Question34.tStartRefresh)
    experiment_Ref.addData('Question34.stopped', Question34.tStopRefresh)
    experiment_Ref.addData('Question43.started', Question43.tStartRefresh)
    experiment_Ref.addData('Question43.stopped', Question43.tStopRefresh)
    experiment_Ref.addData('ChoseQ34.started', ChoseQ34.tStartRefresh)
    experiment_Ref.addData('ChoseQ34.stopped', ChoseQ34.tStopRefresh)
    experiment_Ref.addData('ChoseQ34.numClicks', ChoseQ34.numClicks)
    if ChoseQ34.numClicks:
       experiment_Ref.addData('ChoseQ34.timesOn', ChoseQ34.timesOn)
       experiment_Ref.addData('ChoseQ34.timesOff', ChoseQ34.timesOff)
    else:
       experiment_Ref.addData('ChoseQ34.timesOn', "")
       experiment_Ref.addData('ChoseQ34.timesOff', "")
    experiment_Ref.addData('ChoseQ43.started', ChoseQ43.tStartRefresh)
    experiment_Ref.addData('ChoseQ43.stopped', ChoseQ43.tStopRefresh)
    experiment_Ref.addData('ChoseQ43.numClicks', ChoseQ43.numClicks)
    if ChoseQ43.numClicks:
       experiment_Ref.addData('ChoseQ43.timesOn', ChoseQ43.timesOn)
       experiment_Ref.addData('ChoseQ43.timesOff', ChoseQ43.timesOff)
    else:
       experiment_Ref.addData('ChoseQ43.timesOn', "")
       experiment_Ref.addData('ChoseQ43.timesOff', "")
    # the Routine "nasa_pair_3_4" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_2_6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_2_6Components = [Question26, Question62, ChoseQ26, ChoseQ62]
    for thisComponent in nasa_pair_2_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_2_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_2_6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_2_6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_2_6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question26* updates
        if Question26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question26.frameNStart = frameN  # exact frame index
            Question26.tStart = t  # local t and not account for scr refresh
            Question26.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question26, 'tStartRefresh')  # time at next scr refresh
            Question26.setAutoDraw(True)
        
        # *Question62* updates
        if Question62.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question62.frameNStart = frameN  # exact frame index
            Question62.tStart = t  # local t and not account for scr refresh
            Question62.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question62, 'tStartRefresh')  # time at next scr refresh
            Question62.setAutoDraw(True)
        
        # *ChoseQ26* updates
        if ChoseQ26.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ26.frameNStart = frameN  # exact frame index
            ChoseQ26.tStart = t  # local t and not account for scr refresh
            ChoseQ26.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ26, 'tStartRefresh')  # time at next scr refresh
            ChoseQ26.setAutoDraw(True)
        if ChoseQ26.status == STARTED:
            # check whether ChoseQ26 has been pressed
            if ChoseQ26.isClicked:
                if not ChoseQ26.wasClicked:
                    ChoseQ26.timesOn.append(ChoseQ26.buttonClock.getTime()) # store time of first click
                    ChoseQ26.timesOff.append(ChoseQ26.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ26.timesOff[-1] = ChoseQ26.buttonClock.getTime() # update time clicked until
                if not ChoseQ26.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ26 is clicked
                    None
                ChoseQ26.wasClicked = True  # if ChoseQ26 is still clicked next frame, it is not a new click
            else:
                ChoseQ26.wasClicked = False  # if ChoseQ26 is clicked next frame, it is a new click
        else:
            ChoseQ26.wasClicked = False  # if ChoseQ26 is clicked next frame, it is a new click
        
        # *ChoseQ62* updates
        if ChoseQ62.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ62.frameNStart = frameN  # exact frame index
            ChoseQ62.tStart = t  # local t and not account for scr refresh
            ChoseQ62.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ62, 'tStartRefresh')  # time at next scr refresh
            ChoseQ62.setAutoDraw(True)
        if ChoseQ62.status == STARTED:
            # check whether ChoseQ62 has been pressed
            if ChoseQ62.isClicked:
                if not ChoseQ62.wasClicked:
                    ChoseQ62.timesOn.append(ChoseQ62.buttonClock.getTime()) # store time of first click
                    ChoseQ62.timesOff.append(ChoseQ62.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ62.timesOff[-1] = ChoseQ62.buttonClock.getTime() # update time clicked until
                if not ChoseQ62.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ62 is clicked
                    None
                ChoseQ62.wasClicked = True  # if ChoseQ62 is still clicked next frame, it is not a new click
            else:
                ChoseQ62.wasClicked = False  # if ChoseQ62 is clicked next frame, it is a new click
        else:
            ChoseQ62.wasClicked = False  # if ChoseQ62 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_2_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_2_6"-------
    for thisComponent in nasa_pair_2_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question26.started', Question26.tStartRefresh)
    experiment_Ref.addData('Question26.stopped', Question26.tStopRefresh)
    experiment_Ref.addData('Question62.started', Question62.tStartRefresh)
    experiment_Ref.addData('Question62.stopped', Question62.tStopRefresh)
    experiment_Ref.addData('ChoseQ26.started', ChoseQ26.tStartRefresh)
    experiment_Ref.addData('ChoseQ26.stopped', ChoseQ26.tStopRefresh)
    experiment_Ref.addData('ChoseQ26.numClicks', ChoseQ26.numClicks)
    if ChoseQ26.numClicks:
       experiment_Ref.addData('ChoseQ26.timesOn', ChoseQ26.timesOn)
       experiment_Ref.addData('ChoseQ26.timesOff', ChoseQ26.timesOff)
    else:
       experiment_Ref.addData('ChoseQ26.timesOn', "")
       experiment_Ref.addData('ChoseQ26.timesOff', "")
    experiment_Ref.addData('ChoseQ62.started', ChoseQ62.tStartRefresh)
    experiment_Ref.addData('ChoseQ62.stopped', ChoseQ62.tStopRefresh)
    experiment_Ref.addData('ChoseQ62.numClicks', ChoseQ62.numClicks)
    if ChoseQ62.numClicks:
       experiment_Ref.addData('ChoseQ62.timesOn', ChoseQ62.timesOn)
       experiment_Ref.addData('ChoseQ62.timesOff', ChoseQ62.timesOff)
    else:
       experiment_Ref.addData('ChoseQ62.timesOn', "")
       experiment_Ref.addData('ChoseQ62.timesOff', "")
    # the Routine "nasa_pair_2_6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_3_5"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_3_5Components = [Question35, Question53, ChoseQ35, ChoseQ53]
    for thisComponent in nasa_pair_3_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_3_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_3_5"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_3_5Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_3_5Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question35* updates
        if Question35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question35.frameNStart = frameN  # exact frame index
            Question35.tStart = t  # local t and not account for scr refresh
            Question35.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question35, 'tStartRefresh')  # time at next scr refresh
            Question35.setAutoDraw(True)
        
        # *Question53* updates
        if Question53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question53.frameNStart = frameN  # exact frame index
            Question53.tStart = t  # local t and not account for scr refresh
            Question53.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question53, 'tStartRefresh')  # time at next scr refresh
            Question53.setAutoDraw(True)
        
        # *ChoseQ35* updates
        if ChoseQ35.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ35.frameNStart = frameN  # exact frame index
            ChoseQ35.tStart = t  # local t and not account for scr refresh
            ChoseQ35.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ35, 'tStartRefresh')  # time at next scr refresh
            ChoseQ35.setAutoDraw(True)
        if ChoseQ35.status == STARTED:
            # check whether ChoseQ35 has been pressed
            if ChoseQ35.isClicked:
                if not ChoseQ35.wasClicked:
                    ChoseQ35.timesOn.append(ChoseQ35.buttonClock.getTime()) # store time of first click
                    ChoseQ35.timesOff.append(ChoseQ35.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ35.timesOff[-1] = ChoseQ35.buttonClock.getTime() # update time clicked until
                if not ChoseQ35.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ35 is clicked
                    None
                ChoseQ35.wasClicked = True  # if ChoseQ35 is still clicked next frame, it is not a new click
            else:
                ChoseQ35.wasClicked = False  # if ChoseQ35 is clicked next frame, it is a new click
        else:
            ChoseQ35.wasClicked = False  # if ChoseQ35 is clicked next frame, it is a new click
        
        # *ChoseQ53* updates
        if ChoseQ53.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ53.frameNStart = frameN  # exact frame index
            ChoseQ53.tStart = t  # local t and not account for scr refresh
            ChoseQ53.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ53, 'tStartRefresh')  # time at next scr refresh
            ChoseQ53.setAutoDraw(True)
        if ChoseQ53.status == STARTED:
            # check whether ChoseQ53 has been pressed
            if ChoseQ53.isClicked:
                if not ChoseQ53.wasClicked:
                    ChoseQ53.timesOn.append(ChoseQ53.buttonClock.getTime()) # store time of first click
                    ChoseQ53.timesOff.append(ChoseQ53.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ53.timesOff[-1] = ChoseQ53.buttonClock.getTime() # update time clicked until
                if not ChoseQ53.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ53 is clicked
                    None
                ChoseQ53.wasClicked = True  # if ChoseQ53 is still clicked next frame, it is not a new click
            else:
                ChoseQ53.wasClicked = False  # if ChoseQ53 is clicked next frame, it is a new click
        else:
            ChoseQ53.wasClicked = False  # if ChoseQ53 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_3_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_3_5"-------
    for thisComponent in nasa_pair_3_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question35.started', Question35.tStartRefresh)
    experiment_Ref.addData('Question35.stopped', Question35.tStopRefresh)
    experiment_Ref.addData('Question53.started', Question53.tStartRefresh)
    experiment_Ref.addData('Question53.stopped', Question53.tStopRefresh)
    experiment_Ref.addData('ChoseQ35.started', ChoseQ35.tStartRefresh)
    experiment_Ref.addData('ChoseQ35.stopped', ChoseQ35.tStopRefresh)
    experiment_Ref.addData('ChoseQ35.numClicks', ChoseQ35.numClicks)
    if ChoseQ35.numClicks:
       experiment_Ref.addData('ChoseQ35.timesOn', ChoseQ35.timesOn)
       experiment_Ref.addData('ChoseQ35.timesOff', ChoseQ35.timesOff)
    else:
       experiment_Ref.addData('ChoseQ35.timesOn', "")
       experiment_Ref.addData('ChoseQ35.timesOff', "")
    experiment_Ref.addData('ChoseQ53.started', ChoseQ53.tStartRefresh)
    experiment_Ref.addData('ChoseQ53.stopped', ChoseQ53.tStopRefresh)
    experiment_Ref.addData('ChoseQ53.numClicks', ChoseQ53.numClicks)
    if ChoseQ53.numClicks:
       experiment_Ref.addData('ChoseQ53.timesOn', ChoseQ53.timesOn)
       experiment_Ref.addData('ChoseQ53.timesOff', ChoseQ53.timesOff)
    else:
       experiment_Ref.addData('ChoseQ53.timesOn', "")
       experiment_Ref.addData('ChoseQ53.timesOff', "")
    # the Routine "nasa_pair_3_5" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_1_6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_1_6Components = [Question16, Question61, ChoseQ16, ChoseQ61]
    for thisComponent in nasa_pair_1_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_1_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_1_6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_1_6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_1_6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question16* updates
        if Question16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question16.frameNStart = frameN  # exact frame index
            Question16.tStart = t  # local t and not account for scr refresh
            Question16.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question16, 'tStartRefresh')  # time at next scr refresh
            Question16.setAutoDraw(True)
        
        # *Question61* updates
        if Question61.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question61.frameNStart = frameN  # exact frame index
            Question61.tStart = t  # local t and not account for scr refresh
            Question61.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question61, 'tStartRefresh')  # time at next scr refresh
            Question61.setAutoDraw(True)
        
        # *ChoseQ16* updates
        if ChoseQ16.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ16.frameNStart = frameN  # exact frame index
            ChoseQ16.tStart = t  # local t and not account for scr refresh
            ChoseQ16.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ16, 'tStartRefresh')  # time at next scr refresh
            ChoseQ16.setAutoDraw(True)
        if ChoseQ16.status == STARTED:
            # check whether ChoseQ16 has been pressed
            if ChoseQ16.isClicked:
                if not ChoseQ16.wasClicked:
                    ChoseQ16.timesOn.append(ChoseQ16.buttonClock.getTime()) # store time of first click
                    ChoseQ16.timesOff.append(ChoseQ16.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ16.timesOff[-1] = ChoseQ16.buttonClock.getTime() # update time clicked until
                if not ChoseQ16.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ16 is clicked
                    None
                ChoseQ16.wasClicked = True  # if ChoseQ16 is still clicked next frame, it is not a new click
            else:
                ChoseQ16.wasClicked = False  # if ChoseQ16 is clicked next frame, it is a new click
        else:
            ChoseQ16.wasClicked = False  # if ChoseQ16 is clicked next frame, it is a new click
        
        # *ChoseQ61* updates
        if ChoseQ61.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ61.frameNStart = frameN  # exact frame index
            ChoseQ61.tStart = t  # local t and not account for scr refresh
            ChoseQ61.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ61, 'tStartRefresh')  # time at next scr refresh
            ChoseQ61.setAutoDraw(True)
        if ChoseQ61.status == STARTED:
            # check whether ChoseQ61 has been pressed
            if ChoseQ61.isClicked:
                if not ChoseQ61.wasClicked:
                    ChoseQ61.timesOn.append(ChoseQ61.buttonClock.getTime()) # store time of first click
                    ChoseQ61.timesOff.append(ChoseQ61.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ61.timesOff[-1] = ChoseQ61.buttonClock.getTime() # update time clicked until
                if not ChoseQ61.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ61 is clicked
                    None
                ChoseQ61.wasClicked = True  # if ChoseQ61 is still clicked next frame, it is not a new click
            else:
                ChoseQ61.wasClicked = False  # if ChoseQ61 is clicked next frame, it is a new click
        else:
            ChoseQ61.wasClicked = False  # if ChoseQ61 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_1_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_1_6"-------
    for thisComponent in nasa_pair_1_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question16.started', Question16.tStartRefresh)
    experiment_Ref.addData('Question16.stopped', Question16.tStopRefresh)
    experiment_Ref.addData('Question61.started', Question61.tStartRefresh)
    experiment_Ref.addData('Question61.stopped', Question61.tStopRefresh)
    experiment_Ref.addData('ChoseQ16.started', ChoseQ16.tStartRefresh)
    experiment_Ref.addData('ChoseQ16.stopped', ChoseQ16.tStopRefresh)
    experiment_Ref.addData('ChoseQ16.numClicks', ChoseQ16.numClicks)
    if ChoseQ16.numClicks:
       experiment_Ref.addData('ChoseQ16.timesOn', ChoseQ16.timesOn)
       experiment_Ref.addData('ChoseQ16.timesOff', ChoseQ16.timesOff)
    else:
       experiment_Ref.addData('ChoseQ16.timesOn', "")
       experiment_Ref.addData('ChoseQ16.timesOff', "")
    experiment_Ref.addData('ChoseQ61.started', ChoseQ61.tStartRefresh)
    experiment_Ref.addData('ChoseQ61.stopped', ChoseQ61.tStopRefresh)
    experiment_Ref.addData('ChoseQ61.numClicks', ChoseQ61.numClicks)
    if ChoseQ61.numClicks:
       experiment_Ref.addData('ChoseQ61.timesOn', ChoseQ61.timesOn)
       experiment_Ref.addData('ChoseQ61.timesOff', ChoseQ61.timesOff)
    else:
       experiment_Ref.addData('ChoseQ61.timesOn', "")
       experiment_Ref.addData('ChoseQ61.timesOff', "")
    # the Routine "nasa_pair_1_6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_1_3"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_1_3Components = [Question13, Question31, ChoseQ13, ChoseQ31]
    for thisComponent in nasa_pair_1_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_1_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_1_3"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_1_3Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_1_3Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question13* updates
        if Question13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question13.frameNStart = frameN  # exact frame index
            Question13.tStart = t  # local t and not account for scr refresh
            Question13.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question13, 'tStartRefresh')  # time at next scr refresh
            Question13.setAutoDraw(True)
        
        # *Question31* updates
        if Question31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question31.frameNStart = frameN  # exact frame index
            Question31.tStart = t  # local t and not account for scr refresh
            Question31.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question31, 'tStartRefresh')  # time at next scr refresh
            Question31.setAutoDraw(True)
        
        # *ChoseQ13* updates
        if ChoseQ13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ13.frameNStart = frameN  # exact frame index
            ChoseQ13.tStart = t  # local t and not account for scr refresh
            ChoseQ13.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ13, 'tStartRefresh')  # time at next scr refresh
            ChoseQ13.setAutoDraw(True)
        if ChoseQ13.status == STARTED:
            # check whether ChoseQ13 has been pressed
            if ChoseQ13.isClicked:
                if not ChoseQ13.wasClicked:
                    ChoseQ13.timesOn.append(ChoseQ13.buttonClock.getTime()) # store time of first click
                    ChoseQ13.timesOff.append(ChoseQ13.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ13.timesOff[-1] = ChoseQ13.buttonClock.getTime() # update time clicked until
                if not ChoseQ13.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ13 is clicked
                    None
                ChoseQ13.wasClicked = True  # if ChoseQ13 is still clicked next frame, it is not a new click
            else:
                ChoseQ13.wasClicked = False  # if ChoseQ13 is clicked next frame, it is a new click
        else:
            ChoseQ13.wasClicked = False  # if ChoseQ13 is clicked next frame, it is a new click
        
        # *ChoseQ31* updates
        if ChoseQ31.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ31.frameNStart = frameN  # exact frame index
            ChoseQ31.tStart = t  # local t and not account for scr refresh
            ChoseQ31.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ31, 'tStartRefresh')  # time at next scr refresh
            ChoseQ31.setAutoDraw(True)
        if ChoseQ31.status == STARTED:
            # check whether ChoseQ31 has been pressed
            if ChoseQ31.isClicked:
                if not ChoseQ31.wasClicked:
                    ChoseQ31.timesOn.append(ChoseQ31.buttonClock.getTime()) # store time of first click
                    ChoseQ31.timesOff.append(ChoseQ31.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ31.timesOff[-1] = ChoseQ31.buttonClock.getTime() # update time clicked until
                if not ChoseQ31.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ31 is clicked
                    None
                ChoseQ31.wasClicked = True  # if ChoseQ31 is still clicked next frame, it is not a new click
            else:
                ChoseQ31.wasClicked = False  # if ChoseQ31 is clicked next frame, it is a new click
        else:
            ChoseQ31.wasClicked = False  # if ChoseQ31 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_1_3"-------
    for thisComponent in nasa_pair_1_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question13.started', Question13.tStartRefresh)
    experiment_Ref.addData('Question13.stopped', Question13.tStopRefresh)
    experiment_Ref.addData('Question31.started', Question31.tStartRefresh)
    experiment_Ref.addData('Question31.stopped', Question31.tStopRefresh)
    experiment_Ref.addData('ChoseQ13.started', ChoseQ13.tStartRefresh)
    experiment_Ref.addData('ChoseQ13.stopped', ChoseQ13.tStopRefresh)
    experiment_Ref.addData('ChoseQ13.numClicks', ChoseQ13.numClicks)
    if ChoseQ13.numClicks:
       experiment_Ref.addData('ChoseQ13.timesOn', ChoseQ13.timesOn)
       experiment_Ref.addData('ChoseQ13.timesOff', ChoseQ13.timesOff)
    else:
       experiment_Ref.addData('ChoseQ13.timesOn', "")
       experiment_Ref.addData('ChoseQ13.timesOff', "")
    experiment_Ref.addData('ChoseQ31.started', ChoseQ31.tStartRefresh)
    experiment_Ref.addData('ChoseQ31.stopped', ChoseQ31.tStopRefresh)
    experiment_Ref.addData('ChoseQ31.numClicks', ChoseQ31.numClicks)
    if ChoseQ31.numClicks:
       experiment_Ref.addData('ChoseQ31.timesOn', ChoseQ31.timesOn)
       experiment_Ref.addData('ChoseQ31.timesOff', ChoseQ31.timesOff)
    else:
       experiment_Ref.addData('ChoseQ31.timesOn', "")
       experiment_Ref.addData('ChoseQ31.timesOff', "")
    # the Routine "nasa_pair_1_3" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    continueRoutine_Part = True
    wait_some_time(continueRoutine_Part, experiment_Ref, routine_timer_part,win_ref,frameTolerance, endExpNow, defaultKeyboard, time_in_ms = 500)

    # ------Prepare to start Routine "nasa_pair_3_6"-------
    continueRoutine_Part = True
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_pair_3_6Components = [Question36, Question63, ChoseQ36, ChoseQ63]
    for thisComponent in nasa_pair_3_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_pair_3_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_pair_3_6"-------
    while continueRoutine_Part:
        # get current time
        t = nasa_pair_3_6Clock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_pair_3_6Clock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question36* updates
        if Question36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question36.frameNStart = frameN  # exact frame index
            Question36.tStart = t  # local t and not account for scr refresh
            Question36.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question36, 'tStartRefresh')  # time at next scr refresh
            Question36.setAutoDraw(True)
        
        # *Question63* updates
        if Question63.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question63.frameNStart = frameN  # exact frame index
            Question63.tStart = t  # local t and not account for scr refresh
            Question63.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Question63, 'tStartRefresh')  # time at next scr refresh
            Question63.setAutoDraw(True)
        
        # *ChoseQ36* updates
        if ChoseQ36.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ36.frameNStart = frameN  # exact frame index
            ChoseQ36.tStart = t  # local t and not account for scr refresh
            ChoseQ36.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ36, 'tStartRefresh')  # time at next scr refresh
            ChoseQ36.setAutoDraw(True)
        if ChoseQ36.status == STARTED:
            # check whether ChoseQ36 has been pressed
            if ChoseQ36.isClicked:
                if not ChoseQ36.wasClicked:
                    ChoseQ36.timesOn.append(ChoseQ36.buttonClock.getTime()) # store time of first click
                    ChoseQ36.timesOff.append(ChoseQ36.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ36.timesOff[-1] = ChoseQ36.buttonClock.getTime() # update time clicked until
                if not ChoseQ36.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ36 is clicked
                    None
                ChoseQ36.wasClicked = True  # if ChoseQ36 is still clicked next frame, it is not a new click
            else:
                ChoseQ36.wasClicked = False  # if ChoseQ36 is clicked next frame, it is a new click
        else:
            ChoseQ36.wasClicked = False  # if ChoseQ36 is clicked next frame, it is a new click
        
        # *ChoseQ63* updates
        if ChoseQ63.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ChoseQ63.frameNStart = frameN  # exact frame index
            ChoseQ63.tStart = t  # local t and not account for scr refresh
            ChoseQ63.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(ChoseQ63, 'tStartRefresh')  # time at next scr refresh
            ChoseQ63.setAutoDraw(True)
        if ChoseQ63.status == STARTED:
            # check whether ChoseQ63 has been pressed
            if ChoseQ63.isClicked:
                if not ChoseQ63.wasClicked:
                    ChoseQ63.timesOn.append(ChoseQ63.buttonClock.getTime()) # store time of first click
                    ChoseQ63.timesOff.append(ChoseQ63.buttonClock.getTime()) # store time clicked until
                else:
                    ChoseQ63.timesOff[-1] = ChoseQ63.buttonClock.getTime() # update time clicked until
                if not ChoseQ63.wasClicked:
                    continueRoutine_Part = False  # end routine when ChoseQ63 is clicked
                    None
                ChoseQ63.wasClicked = True  # if ChoseQ63 is still clicked next frame, it is not a new click
            else:
                ChoseQ63.wasClicked = False  # if ChoseQ63 is clicked next frame, it is a new click
        else:
            ChoseQ63.wasClicked = False  # if ChoseQ63 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_pair_3_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_pair_3_6"-------
    for thisComponent in nasa_pair_3_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_Ref.addData('Question36.started', Question36.tStartRefresh)
    experiment_Ref.addData('Question36.stopped', Question36.tStopRefresh)
    experiment_Ref.addData('Question63.started', Question63.tStartRefresh)
    experiment_Ref.addData('Question63.stopped', Question63.tStopRefresh)
    experiment_Ref.addData('ChoseQ36.started', ChoseQ36.tStartRefresh)
    experiment_Ref.addData('ChoseQ36.stopped', ChoseQ36.tStopRefresh)
    experiment_Ref.addData('ChoseQ36.numClicks', ChoseQ36.numClicks)
    if ChoseQ36.numClicks:
       experiment_Ref.addData('ChoseQ36.timesOn', ChoseQ36.timesOn)
       experiment_Ref.addData('ChoseQ36.timesOff', ChoseQ36.timesOff)
    else:
       experiment_Ref.addData('ChoseQ36.timesOn', "")
       experiment_Ref.addData('ChoseQ36.timesOff', "")
    experiment_Ref.addData('ChoseQ63.started', ChoseQ63.tStartRefresh)
    experiment_Ref.addData('ChoseQ63.stopped', ChoseQ63.tStopRefresh)
    experiment_Ref.addData('ChoseQ63.numClicks', ChoseQ63.numClicks)
    if ChoseQ63.numClicks:
       experiment_Ref.addData('ChoseQ63.timesOn', ChoseQ63.timesOn)
       experiment_Ref.addData('ChoseQ63.timesOff', ChoseQ63.timesOff)
    else:
       experiment_Ref.addData('ChoseQ63.timesOn', "")
       experiment_Ref.addData('ChoseQ63.timesOff', "")
    # the Routine "nasa_pair_3_6" was not non-slip safe, so reset the non-slip timer
    routine_timer_part.reset()

    #TODO: aqui es donde empieza el goodbye?? Le comento/borro??
    '''
    # ------Prepare to start Routine "nasa_goodbyewin_refdow"-------
    continueRoutine_Part = True
    routine_timer_part.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    nasa_goodbyewin_refdowComponents = [Goodbye]
    for thisComponent in nasa_goodbyewin_refdowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win_ref.getFutureFlipTime(clock="now")
    nasa_goodbyewin_refdowClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "nasa_goodbyewin_refdow"-------
    while continueRoutine_Part and routine_timer_part.getTime() > 0:
        # get current time
        t = nasa_goodbyewin_refdowClock.getTime()
        tThisFlip = win_ref.getFutureFlipTime(clock=nasa_goodbyewin_refdowClock)
        tThisFlipGlobal = win_ref.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Goodbye* updates
        if Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Goodbye.frameNStart = frameN  # exact frame index
            Goodbye.tStart = t  # local t and not account for scr refresh
            Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win_ref.timeOnFlip(Goodbye, 'tStartRefresh')  # time at next scr refresh
            Goodbye.setAutoDraw(True)
        if Goodbye.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Goodbye.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Goodbye.tStop = t  # not accounting for scr refresh
                Goodbye.frameNStop = frameN  # exact frame index
                win_ref.timeOnFlip(Goodbye, 'tStopRefresh')  # time at next scr refresh
                Goodbye.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine_Part:  # a component has requested a forced-end of Routine
            break
        continueRoutine_Part = False  # will revert to True if at least one component still running
        for thisComponent in nasa_goodbyewin_refdowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine_Part = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine_Part:  # don't flip if this routine is over or we'll get a blank screen
            win_ref.flip()

    # -------Ending Routine "nasa_goodbyewin_refdow"-------
    for thisComponent in nasa_goodbyewin_refdowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    experiment_Ref.addData('Goodbye.started', Goodbye.tStartRefresh)
    experiment_Ref.addData('Goodbye.stopped', Goodbye.tStopRefresh)
            
    '''





    experiment_Ref.addData('Nasa.stopped', win_ref.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()
    logging_utilities.log_time(False, 'Nasa')
