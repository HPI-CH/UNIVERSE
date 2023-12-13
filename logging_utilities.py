from psychopy import logging
import datetime

def logger_setup(filename):
    logFile = logging.LogFile(filename + '.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

def log_time(beginning_flag=True, routine_name=''):
    if beginning_flag:
        logging.log(level=logging.EXP, msg='Routine {} started at {}'.format(routine_name, str(datetime.datetime.now())))
    else:
        logging.log(level=logging.EXP, msg='Routine {} finished at {}'.format(routine_name, str(datetime.datetime.now())))