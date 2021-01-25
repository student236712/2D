import random
import matplotlib.pyplot as plt

balls_positions = []
x_positions = []
y_positions = []

for ball_position in range(0, 4):
    x_positions.append(random.uniform(-10, 10))
    y_positions.append(random.uniform(-10, 10))
    ball_points = [[x_positions], [y_positions]]
    balls_positions.append(ball_points)


for ball in balls_positions:
    plt.scatter(ball[0], ball[1])
    plt.savefig("ball_10.png")
