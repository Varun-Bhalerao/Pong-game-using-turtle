import turtle

window = turtle.Screen()
window.title("Pong by Varun")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stops the windows from updating? not sure what this means.. need to confirm.. NEED TO PLAY WITH

#  Add paddles and ball to the screen
#  Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)  # this sets the speed to the maximum possible speed - NEED TO PLAY WITH
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # Normally what turtle does is it traces where it moves. We do not need that in this program.
paddle_a.goto(-350, 0)

#  Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)  # this sets the speed to the maximum possible speed - NEED TO PLAY WITH
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # Normally what turtle does is it traces where it moves. We do not need that in this program.
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)  # this sets the speed to the maximum possible speed - NEED TO PLAY WITH
ball.shape("square")
ball.color("white")
#  ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()  # Normally what turtle does is it traces where it moves. We do not need that in this program.
ball.goto(0, 0)

# score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 20, "normal"))


#  Function to make the paddles and ball move
# paddle A controls

def paddle_a_up():
    y = paddle_a.ycor()  # this command returns the y-coordinate
    y += 20  # this will add 20 pixels to the y-coordinate
    paddle_a.sety(y)  # this command will set y to new y


def paddle_a_down():
    y = paddle_a.ycor()  # this command returns the y-coordinate
    y -= 20  # this will add 20 pixels to the y-coordinate
    paddle_a.sety(y)  # this command will set y to new y


# paddle B controls

def paddle_b_up():
    y = paddle_b.ycor()  # this command returns the y-coordinate
    y += 20  # this will add 20 pixels to the y-coordinate
    paddle_b.sety(y)  # this command will set y to new y


def paddle_b_down():
    y = paddle_b.ycor()  # this command returns the y-coordinate
    y -= 20  # this will add 20 pixels to the y-coordinate
    paddle_b.sety(y)  # this command will set y to new y


#  keyboard binding

window.listen()  # listen to keyboard input
window.onkeypress(paddle_a_up, "w")  # this command says that when 'u' is pressed move the paddle up
window.onkeypress(paddle_a_down, "s")

window.listen()  # listen to keyoard input
window.onkeypress(paddle_b_up, "u")  # this command says that when 'j' is pressed move the paddle up
window.onkeypress(paddle_b_down, "j")

# ball movement in x and y direction

ball.dx = 0.1  # play with this number according to the game speed. Every time the ball moves, it moves by 0.4 pixels
# in X
ball.dy = 0.1  # play with this number according to the game speed Every time the ball moves, it moves by 0.4 pixels
# in Y

# Main game loop
# Everything related to the 'onscreen activity' is going to be covered here

while True:
    window.update()  # used to update the screen every time the loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # this command is going to move the ball 0.5 spaces in positive X
    ball.sety(ball.ycor() + ball.dy)  # # this command is going to move the ball 0.5 spaces in positive Y

    # Combination of the above commands will move the ball in northeast diagonal

    # Border check of the screen
    if ball.ycor() > 290:  # 290 because the height of the screen is +300 and -300 and the ball is +10 and -10
        ball.sety(290)  # setting it back to 290
        ball.dy *= -1  # this is reversing the direction

    if ball.ycor() < -290:  # 290 because the height of the screen is +300 and -300 and the ball is +10 and -10
        ball.sety(-290)  # setting it back to 290
        ball.dy *= -1  # this is reversing the direction

    if ball.xcor() > 390:  # 290 because the height of the screen is +300 and -300 and the ball is +10 and -10
        ball.goto(0, 0)  # setting it back to 0,0
        ball.dx *= -1  # this is reversing the direction
        score_a += 1  # if the ball goes beyond 390, player 'a' gets +1
        pen.clear()  # this allows the code to not overwrite the scores
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 20, "normal"))

    if ball.xcor() < -390:  # 290 because the height of the screen is +300 and -300 and the ball is +10 and -10
        ball.goto(0, 0)  # setting it back to 0,0
        ball.dx *= -1  # this is reversing the direction
        score_b += 1  # if the ball goes beyond 390, player 'b' gets +1
        pen.clear()  # this allows the code to not overwrite the scores
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 20, "normal"))

        # Ball collision with the paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() < 350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1