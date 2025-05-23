"""
Console logging module for LinuxOscilloscope project.
Provides consistent console output formatting and control.
"""

import datetime
import inspect
import os
import sys
from typing import Any, Optional

# ANSI color codes for terminal output
COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m'
}

def ConsoleLog(message: Any, 
              level: str = 'info', 
              show_caller: bool = True,
              show_timestamp: bool = False,
              debug: bool = False) -> None:
    """
    Print formatted log messages to the console with optional caller information and timestamps.
    
    Args:
        message: The message to print. Can be any type that can be converted to string.
        level: The log level ('info', 'warning', 'error', 'debug'). Defaults to 'info'.
        show_caller: Whether to show the caller function/module name. Defaults to True.
        show_timestamp: Whether to show the timestamp. Defaults to True.
        debug: If False, suppress all output. Defaults to False.
    """
    if not debug:
        return

    # Convert message to string
    msg = str(message)
    
    # Get timestamp
    timestamp = ''
    if show_timestamp:
        timestamp = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
    
    # Get caller information
    caller = ''
    if show_caller:
        frame = inspect.currentframe()
        # Get caller frame (2 frames up to skip this function and its immediate caller)
        caller_frame = inspect.getouterframes(frame, 2)
        if len(caller_frame) > 1:
            caller_info = caller_frame[1]
            module = os.path.basename(caller_info.filename)
            function = caller_info.function
            caller = f"[{module}::{function}] "
    
    # Set color based on level
    color = COLORS.get('reset')
    prefix = ''
    
    level = level.lower()
    if level == 'error':
        color = COLORS['red']
        prefix = 'ERROR: '
    elif level == 'warning':
        color = COLORS['yellow']
        prefix = 'WARNING: '
    elif level == 'debug':
        color = COLORS['cyan']
        prefix = 'DEBUG: '
    elif level == 'info':
        color = COLORS['green']
    
    # Construct and print the message
    output = f"{color}{timestamp}{caller}{prefix}{msg}{COLORS['reset']}"
    print(output, file=sys.stderr if level == 'error' else sys.stdout)
