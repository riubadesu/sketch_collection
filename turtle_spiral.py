import turtle

win = turtle.Screen()
win.bgcolor('#255959')
win.setup(width=600, height=600)
turtle.hideturtle()
turtle.speed(1000)
colors = ['#400106', '#D99789']
r = 10
f_start = 100

for x in range(557):
    turtle.color(colors[x % len(colors)])
    turtle.width(0.3)
    turtle.left(179)
    turtle.forward(f_start+r)
    r = r+100
    x = x+0.3

win.exitonclick()
