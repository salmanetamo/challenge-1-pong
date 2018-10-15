""""
Author: Salmane Tamo

The pong game with the following rules:
1.  If the ball hits a vertical wall, the game is over.
2.  If the ball hits a horizontal wall, it bounces off that wall.
3.  If the ball hits the inner face of a paddle, it bounces off the
    paddle.
"""

from aluLib import *

#Dimensions of the window
window_width = 1000
window_height = 600

#Variables related to the two paddles
paddle_height = 100
paddle_width = 20
paddle_speed = 10
left_paddle_y = 0
right_paddle_y = window_height - paddle_height

#Variables related to the ball
ball_x = window_width/2
ball_y = window_height/2
ball_radius = 15
ball_x_speed = 5
ball_y_speed = 5

start = False

def draw_paddles():
    """"
    Draws the two paddles as rectangles
    """
    enable_fill
    set_fill_color(.75, .75, .75)
    draw_rectangle(0, left_paddle_y, paddle_width, paddle_height)
    draw_rectangle(window_width - paddle_width, right_paddle_y, paddle_width, paddle_height)
    move_paddles("a", "z", "left")
    move_paddles("k", "m", "right")


def move_paddles(up_key, down_key, paddle_side):
    """"
    Moves a given paddle depending on the keys pressed

    up_key: key that moves the paddle up
    down_key: key that moves the paddle down
    paddle_side: either right or left ton specify paddle to be moved
    """
    global left_paddle_y, right_paddle_y

    if is_key_pressed(up_key):
        if paddle_side == "left" and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        elif paddle_side == "right" and right_paddle_y > 0:
            right_paddle_y -= paddle_speed

    if is_key_pressed(down_key):
        if paddle_side == "left" and left_paddle_y < window_height - paddle_height:
            left_paddle_y += paddle_speed
        elif paddle_side == "right" and right_paddle_y < window_height - paddle_height:
            right_paddle_y += paddle_speed


def draw_ball():
    """"
    Draws the ball
    """
    set_fill_color(1, .5, 0)
    draw_circle(ball_x, ball_y, ball_radius)


def move_ball():
    """"
    Starts the movement of the ball and ensures it bounces either
    on the horizontal walls or on the paddles
    """
    global ball_x, ball_y, ball_x_speed, ball_y_speed, right_paddle_y, paddle_height
    if start:
        ball_x += ball_x_speed
        ball_y -= ball_y_speed
        if moved_beyond_right_wall(ball_x, ball_y):
            if right_paddle_y < ball_y < right_paddle_y + paddle_height:
                ball_x_speed = -1 * ball_x_speed
        if moved_beyond_left_wall(ball_x, ball_y):
            if left_paddle_y < ball_y < left_paddle_y + paddle_height:
                ball_x_speed = -1 * ball_x_speed
        if moved_beyond_upper_wall(ball_x, ball_y):
            ball_y_speed = -1 * ball_y_speed
        if moved_beyond_lower_wall(ball_x, ball_y):
            ball_y_speed = -1 * ball_y_speed


def moved_beyond_right_wall(ball_x_coord, ball_y_coord, wall_x_coord=window_width):
    """"
    Checks for a collision with the right vertical wall.
    Returns true if the ball has moved beyond wall and returns false otherwise

    ball_x_coord: the x coordinate of the ball
    ball_y_coord: the y coordinate of the ball
    wall_x_coord: the x coordinate of the wall
    """
    global ball_radius, paddle_height
    if ball_y_coord > window_height or ball_y_coord < 0:
        return False
    return ball_x_coord + ball_radius > wall_x_coord - paddle_width


def moved_beyond_left_wall(ball_x_coord, ball_y_coord, wall_x_coord=0):
    """"
    Checks for a collision with the left vertical wall.
    Returns true if the ball has moved beyond wall and returns false otherwise

    ball_x_coord: the x coordinate of the ball
    ball_y_coord: the y coordinate of the ball
    wall_x_coord: the x coordinate of the wall
    """
    global ball_radius, paddle_height
    if ball_y_coord > window_height or ball_y_coord < 0:
        return False
    return ball_x_coord - ball_radius < wall_x_coord + paddle_width


def moved_beyond_upper_wall(ball_x_coord, ball_y_coord, wall_y_coord=0):
    """"
    Checks for a collision with the upper horizontal wall.
    Returns true if the ball has moved beyond wall and returns false otherwise

    ball_x_coord: the x coordinate of the ball
    ball_y_coord: the y coordinate of the ball
    wall_x_coord: the y coordinate of the wall
    """
    global ball_radius, paddle_height
    if ball_x_coord > window_width or ball_x_coord < 0:
        return False
    return ball_y_coord - ball_radius < wall_y_coord


def moved_beyond_lower_wall(ball_x_coord, ball_y_coord, wall_y_coord=window_height):
    """"
    Checks for a collision with the lower horizontal wall.
    Returns true if the ball has moved beyond wall and returns false otherwise

    ball_x_coord: the x coordinate of the ball
    ball_y_coord: the y coordinate of the ball
    wall_y_coord: the y coordinate of the wall
    """
    global ball_radius, paddle_height
    if ball_x_coord > window_width or ball_x_coord < 0:
        return False
    return ball_y_coord + ball_radius > wall_y_coord


def start_game():
    """"
    Starts the game once the space key is pressed
    """
    global left_paddle_y, right_paddle_y, ball_x, ball_y, ball_x_speed, ball_y_speed, start
    if is_key_pressed(" "):
        left_paddle_y = 0
        right_paddle_y = window_height - paddle_height

        ball_x = window_width / 2
        ball_y = window_height / 2
        ball_x_speed = 5
        ball_y_speed = 5
        start = True


def play_game():
    """"
    Calls the necessary functions to play the game
    """
    clear()
    start_game()
    draw_paddles()
    draw_ball()
    move_ball()
    if is_key_pressed("q"):
        cs1_quit()


if __name__ == "__main__":
    start_graphics(play_game, width=window_width, height=window_height)
