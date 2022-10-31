from .pomodoro_colors import PomodoroColors


class PomodoroSettings:
    APPLICATION_ICON = 'day28_files/tomato.png'
    APPLICATION_TITLE = 'My Personal Pomodoro'
    BACKGROUND_COLOR = PomodoroColors.YELLOW
    BACKGROUND_IMAGE = 'day28_files/tomato.png'
    CLOCK_VERTICAL_SHIFT = 30
    CLOCK_HORIZONTAL_SHIFT = 0
    DECK_PADDING_Y = (10, 0)
    FONT_BUTTON = ('Courier', 18)
    FONT_DECK = ('Courier', 28)
    FONT_HEADER = ('Courier', 40, 'bold')
    FONT_TIMER = ('Courier', 32, 'bold')
    HEADER_PADDING_Y = (20, 0)
    LABEL_COLOR = PomodoroColors.GREEN
    START_BUTTON_PADDING = (0, 30)
    STOP_BUTTON_PADDING = (30, 0)
    WINDOW_MIN_WIDTH = 250
    WINDOW_MIN_HEIGHT = 250
    WINDOW_PADDING_X = 25
    WINDOW_PADDING_Y = 10

    LONG_BREAK_MIN = 20
    SHORT_BREAK_MIN = 5
    WORK_LENGTH_MIN = 25

    @staticmethod
    def get_timer_font():
        return PomodoroSettings.FONT_TIMER

    @staticmethod
    def get_header_font():
        return PomodoroSettings.FONT_HEADER

    @staticmethod
    def get_check_deck_font():
        return PomodoroSettings.FONT_DECK

    @staticmethod
    def get_work_map():
        return {
            1: {
                'length': PomodoroSettings.WORK_LENGTH_MIN * 60,
                'header': 'Work',
                'color': PomodoroColors.GREEN,
                'is_stage': True
            },
            2: {
                'length': PomodoroSettings.SHORT_BREAK_MIN * 60,
                'header': 'Break',
                'color': PomodoroColors.PINK,
                'is_stage': False
            },
            3: {
                'length': PomodoroSettings.WORK_LENGTH_MIN * 60,
                'header': 'Work',
                'color': PomodoroColors.GREEN,
                'is_stage': True
            },
            4: {
                'length': PomodoroSettings.SHORT_BREAK_MIN * 60,
                'header': 'Break',
                'color': PomodoroColors.PINK,
                'is_stage': False
            },
            5: {
                'length': PomodoroSettings.WORK_LENGTH_MIN * 60,
                'header': 'Work',
                'color': PomodoroColors.GREEN,
                'is_stage': True
            },
            6: {
                'length': PomodoroSettings.SHORT_BREAK_MIN * 60,
                'header': 'Break',
                'color': PomodoroColors.PINK,
                'is_stage': False
            },
            7: {
                'length': PomodoroSettings.WORK_LENGTH_MIN * 60,
                'header': 'Work',
                'color': PomodoroColors.GREEN,
                'is_stage': True
            },
            8: {
                'length': PomodoroSettings.LONG_BREAK_MIN * 60,
                'header': 'Break',
                'color': PomodoroColors.RED,
                'is_stage': False
            },
        }
