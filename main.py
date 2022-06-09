import turtle

x = 0


turtle.setup (500,500)
kaia = turtle.Turtle()
screen = turtle.Screen()



def drawCircle():
  kaia.circle(50)
  
def drawPattern():
  x = 0
  while x < 36:
    drawCircle()
    kaia.right(10)
    x +=1

  
screen.onkey(drawPattern, "o")
screen.listen()
