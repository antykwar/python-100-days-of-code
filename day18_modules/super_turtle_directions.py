class SuperTurtleDirections:
    DIRECTION_TOP_LEFT = 180
    DIRECTION_TOP_RIGHT = 90
    DIRECTION_BOTTOM_LEFT = 270
    DIRECTION_BOTTOM_RIGHT = 0

    @staticmethod
    def get_list():
        return SuperTurtleDirections.DIRECTION_TOP_LEFT, \
               SuperTurtleDirections.DIRECTION_TOP_RIGHT, \
               SuperTurtleDirections.DIRECTION_BOTTOM_LEFT, \
               SuperTurtleDirections.DIRECTION_BOTTOM_RIGHT
