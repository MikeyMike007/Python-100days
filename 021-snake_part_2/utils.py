# Constants related to screen
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Snake"
SCREEN_WIDTH = 600
SCREEN_LENGTH = 600

# Constants related to snake
SNAKE_STEP_SIZE = 20
SNAKE_INITIAL_POSITIONS = [(0, 0), (-1 * SNAKE_STEP_SIZE, 0), (-2 * SNAKE_STEP_SIZE, 0)]
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"

# Constans related to food
FOOD_COLOR = "blue"
FOOD_SHAPE = "square"

# Directions in degrees - From Turtle manual
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

# Collision tolerances and thresholds
SNAKE_FOOD_COLLISION_TOLERANCE = 20
HEAD_BODY_COLLISION_TOLERANCE = 10

# Snake speed
SLEEP_TIME = 0.1

# Distance from middle wall in every direction
BOARD_SIDE = 180

# Constants related to scoreboard
SCOREBOARD_COLOR = "white"
SCOREBOARD_POSITION = (0, 200)
SCOREBOARD_ALIGNEMENT = "center"
SCOREBOARD_FONT = ("Arial", 14, "normal")
SCOREBOARD_GAME_OVER_POSITION = (0, 0)
