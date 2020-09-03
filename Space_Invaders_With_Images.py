import turtle
import winsound
import math
import random

# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# Register shape
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0) 
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score on the screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Multiple enemies
num_of_enemies = 5
enemies = []
for i in range(num_of_enemies):
	enemies.append(turtle.Turtle())

# Creat the enemy
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Move player to left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

# Fires the bullet
def fire_bullet():
	if not bullet.isvisible():
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()
		winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
	if distance < 15:
		return True
	else:
		return False

# Create keyboard bidings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


# Main Game Loop
while True:

	for enemy in enemies:
		# Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		if enemy.xcor() > 280:
			# Move all the enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			# Change the enemies direction
			enemyspeed *= -1

		if enemy.xcor() < -280:
			# Move all the enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			# Change the enemies directions
			enemyspeed *= -1

		# Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			# Reset the bullet
			bullet.hideturtle()
			bullet.setposition(0, -400)
			# Makes explosion sound
			winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
			# Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			# Update the score
			score += 10
			scorestring = "Score = %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))

		# Check for a collision between the player and the enemy
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("GAME OVER")
			break

	# Move the bullet
	if bullet.isvisible():
		y = bullet.ycor() + bulletspeed
		bullet.sety(y)

	# Check if bullet reached the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bullet.sety(-240)

wn.mainloop()