import turtle
from random import randint
from time import sleep
from math import sqrt, pow

WIN_SCORE = 200

# setup screen
win = turtle.Screen()
win.title("Hungry Turtle")
image = 'tree.gif'
win.bgpic(image)
win.tracer(3)




class Game:
    def __init__(self):

        self.__draw_game_boundry__()
        self.__create_player__()
        self.__create_food__()
        self.__keyboard_bindings__()
        self.score = 0
        self.nextLevelScore = 60
        self.level = 1
        self.speed = 2

    def start(self):
        while True:
            self.player.forward(self.speed)
            self.__boundry_collision__(self.player)
            self.__keyboard_bindings__()
            self.__update_game_screen__()

            for item in self.foodPlate:
                item.forward(1)
                self.__boundry_collision__(item)

                if self.__is_collision__(self.player,item):
                    item.setposition(randint(-250, 250), randint(-250, 250))

                    item.right(randint(0, 360))
                    self.score += 10
                    if self.score > self.nextLevelScore:
                        self.nextLevelScore += 40
                        self.speed += 2
                        self.level += 1

            if self.score > WIN_SCORE:
                self.__update_game_screen__("Congratulations: You Won")
                break


    def __is_collision__(self, t1, t2):
        dist = sqrt(pow(t1.xcor() - t2.xcor(), 2) + pow(t1.ycor() - t2.ycor(), 2))
        if dist < 20:
            return True
        return False

    def __boundry_collision__(self, t):
        if t.xcor() > 240 or t.xcor() < -240 or t.ycor() > 240 or t.ycor() < -240:
            t.right(180)
            # t.right(randint(0, 180))

        # if t.xcor() > 260 or t.xcor() < -260 or t.ycor() > 260 or t.ycor() < -260:
        #     print(t.xcor(), t.ycor(), self.speed)
        #     t.setposition(0,0)

    def __keyboard_bindings__(self):
        def turn_left():
            self.player.left(30)

        def turn_right():
            self.player.right(30)

        def decrease_speed():
            pass

        win.listen()
        win.onkey(turn_left, 'Left')
        win.onkey(turn_right, 'Right')

    def __update_game_screen__(self, screenData=None):
        self.freepen.undo()
        self.freepen.hideturtle()
        self.freepen.setposition(-320, 260)
        if not screenData:
            screenData = "Score: "+str(self.score)+"    "+"Level: "+str(self.level)
        self.freepen.write(screenData, False, align="left", font=("Arial", 14, "normal"))

    def __draw_game_boundry__(self):

        boundry = turtle.Turtle()
        boundry.penup()
        boundry.setposition(-250, -250)
        boundry.pendown()
        boundry.pensize(4)
        for side in range(4):
            boundry.forward(500)
            boundry.left(90)
        # boundry.hideturtle()
        boundry.penup()
        self.freepen = boundry
        self.freepen.hideturtle()

    def __create_player__(self):
        self.player = turtle.Turtle()
        self.player.color("lightblue")
        self.player.penup()
        self.player.shape("turtle")
        self.player.shapesize(2,2,2)

    def __create_food__(self):
        maxFoodObj = 5
        foodObjs= []
        self.foodPlate = foodObjs

        for each in range(maxFoodObj):
            foodObjs.append(turtle.Turtle())
            foodObjs[each].color("red")
            foodObjs[each].shape("circle")
            foodObjs[each].shapesize(0.8, 0.8, 0.8)
            foodObjs[each].speed(0)
            foodObjs[each].penup()
            foodObjs[each].setposition(randint(-250, 250), randint(-250, 250))

game = Game()

try:
    game.start()
    win.mainloop()
except Exception as e:
    # print(e)
    pass

