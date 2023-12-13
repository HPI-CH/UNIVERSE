import datetime
from datetime import timedelta
import subprocess
from psychopy import visual
from psychopy import logging
from present_text import present_text

import logging_utilities


def sudoku(win, seconds_per_routine, experiment_Ref, frameTolerance, defaultKeyboard, endExpNow, easy=True):
    logging_utilities.log_time(beginning_flag=True, routine_name=F'Sudoku Instructions ({easy})')
    experiment_Ref.nextEntry()
    experiment_Ref.addData('Sudoku_Instructions.started', win.getFutureFlipTime(clock=None))
    test_text = F'The next task is a Sudoku {"easy" if easy else "hard"} game.  \n   Press [SPACE] when ready.'
    present_text(experiment_Ref, win, frameTolerance, defaultKeyboard, endExpNow, visual_stim=None, test_text=test_text)






    logging_utilities.log_time(beginning_flag=True, routine_name=F'Sudoku ({easy})')
    experiment_Ref.addData('Sudoku.started', win.getFutureFlipTime(clock=None))
    experiment_Ref.addData('Sudoku.easy_bool', easy)
    ### This is the Sudoku we want for easy and hard mode to run:
    ##### INCLUDED HERE THE START OF THE SUDOKU
    ##### For easy sudoku, no tab should be required with the xdotool, just space
    # In order to release the mouse, we need to close the old window!
    win.close()


    start_of_sudoku_block = datetime.datetime.now()
    # finish_time_of_sudoku = start_of_sudoku_block + timedelta(minutes=1) # could also be: seconds=5
    finish_time_of_sudoku = start_of_sudoku_block + timedelta(seconds=seconds_per_routine)  # could also be: seconds=5

    print('ENTERING THE WHILE LOOP FOR HARD SUDOKU')
    sudoku_num_games_counter = 0
    while datetime.datetime.now() < finish_time_of_sudoku:
        try:
            sudoku_num_games_counter = sudoku_num_games_counter + 1
            seconds_to_go = (finish_time_of_sudoku - datetime.datetime.now()).total_seconds()
            print('TIME UNTIL THE SUDOKU BLOCK SHALL BE FINISHED: {}s'.format(seconds_to_go))
            if easy:
                subprocess.call('timeout {}s gnome-sudoku | xdotool sleep 1 key space'.format(seconds_to_go),
                                timeout=seconds_to_go, shell=True)
            else:
                subprocess.call(
                    'timeout {}s gnome-sudoku | xdotool sleep 1 key Tab Tab Tab space'.format(seconds_to_go),
                    timeout=seconds_to_go, shell=True)

            # newmouse = event.Mouse()
        except subprocess.TimeoutExpired:
            print('DO THE NEXT THINGS HERE TO CHECK ON THE OVERALL TIME')
            break



    
    #DO WE NEED THIS????
    #TODO: add logs with time (total time from experiment) and number of games played

    ## After sudoku, the window-reference needs to be restored each time Sudoku is done:abs
    win = visual.Window(
        size=[1920, 1080], fullscr=True, screen=0,
        winType='pyglet', allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='height')
    #TODO: maybe create this new window in the main function (script) so the reference is not lost?


    experiment_Ref.addData('Sudoku.num_games_counter', sudoku_num_games_counter)
    experiment_Ref.addData('Sudoku.stopped', win.getFutureFlipTime(clock=None))
    logging.log(level=logging.EXP, msg='Number of Sudoku games played: '.format(sudoku_num_games_counter))
    logging_utilities.log_time(beginning_flag=False, routine_name=F'Sudoku ({easy})')

    logging_utilities.log_time(beginning_flag=False, routine_name=F'Sudoku Instructions ({easy})')
    experiment_Ref.addData('Sudoku_Instructions.stopped', win.getFutureFlipTime(clock=None))
    experiment_Ref.nextEntry()

    return win

