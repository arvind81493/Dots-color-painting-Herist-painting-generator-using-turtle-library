

# from prettytable import PrettyTable
# table= PrettyTable()
# table.add_column("students_name",["arvind kumar","karan yadav", "Akit mauraya"])
# table.add_column("grades",["f","B","a+"])
# table.field_names=["students_name","grades"]
# table.add_row(["Hanshika","A"])
# table.align="l"
# print(table)

#
# class User:
#   def __init__(self,user_id,user_name):
#       self.user_id=user_id
#       self.user_name=user_name
#       self.followers=0
#       self.following=0
#
#   def follow(self,user):
#       user.followers += 1
#       self.following+=1
#
#
#
#
# user_1=User("001","arvind")
# user_2=User("002","karan")
# user_1.follow(user_2)
# print(user_1.following)
# print(user_1.followers)
# print(user_2.following)
# print(user_2.followers)
#
# from turtle import Turtle,Screen
#
# tim=Turtle()
# screen=Screen()
# print(screen.canvheight)
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Name",["Arvind kumar","hanshika yadav","Karan Yadav"])
# table.add_column("Grades",["A","B","c"])
# table.align="r"
# table.field_names=["Name","Grades"]
# table.add_row(["Ankit","D"])
# print(table)

#
# from turtle import Turtle , Screen
# import random
#
# 
# screen=Screen()
# colours=["red","green","yellow","blue","skyblue","orange"]
# screen.setup(width=500, height=500)
# user_bet=screen.textinput(title="Make your Bet",prompt="which color  turtle ifs going to win the race ? ")
# y_cor=[-70,-40,-10,20,50,80]
# turtles=[]
# for char in range(0,6):
#     tim = Turtle(shape="turtle")
#     tim.color(colours[char])
#     tim.penup()
#     tim.goto(x=-230,y=y_cor[char])
#     turtles.append(tim)
#
#
# tim.speed("fastest")
# if user_bet:
#     is_on=True
#
# while is_on:
#     for i in turtles:
#          if i.xcor()>240:
#            is_on=False
#            winning_color=i.pencolor()
#            if winning_color==user_bet:
#                print(f"you have won. your winning color is {winning_color}")
#            else:
#                print("you lost!")
#
#          race=random.randint(0,10)
#          i.forward(race)
#
#
#
#
# screen.exitonclick()


#
# def resources_is_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item]>=resources[item]:
#             print(f"sorry there is not sufficient {item}")
#             return False
#         return True
#
# def process_coins():
#     money=0
#     money+=int(input("how many penny do you have : "))*0.01
#     money+=int(input("how many  dimes do you have : "))*0.10
#     money+=int(input("enter how many nickel do you have : "))*0.05
#     money+=int(input("how many quater do you have : "))*0.25
#     return money
#
# def transaction_successful(money_received,drink_cost):
#     if money_received>=drink_cost:
#         change=money_received-drink_cost
#         global profit
#         profit+=change
#         return True
#     else:
#         return False
# def make_coffee(choice,drink_ingredients):
#     for item in drink_ingredients:
#         resources[item]-=drink_ingredients[item]
#     print(f"here is your drin name {choice} enjoy")
#
# is_on=True
# while is_on:
#  choice=input("what would you like ? espresso/latte/cappuccino")
#  if choice=="off":
#      is_on=False
import turtle
# import random
# import turtle as t
# from turtle import Screen
# tim=t.Turtle()
# screen=Screen
# tim.speed("fastest")
# t.colormode(255)
# position=[0,90,180,270]
# def color():
#      r=random.randint(0,255)
#      g=random.randint(0,255)
#      b=random.randint(0,255)
#      tuple=(r,g,b)
#      return tuple
#
# for char in range(500):
#      tim.pensize(20)
#      tim.color(color())
#      tim.forward(30)
#      tim.setheading(random.choice(position))
#
#
#
#
# screen.exitonclick(
# import random
# import turtle as t
# tim=t.Turtle()
#
# color=["red","purple","green","orange"]
#
# def draw_shapes(num_sides):
#     angel=360/num_sides
#     for char in range(num_sides):
#         tim.forward(100)
#         tim.right(angel)
#
# for char in range(3,11):
#     draw_shapes(char)
#     tim.color(random.choice(color))
# import random
# import turtle as t
# tim=t.Turtle()
# t.colormode(255)
# tim.speed("fastest")
#
# def color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     tuple=(r,g,b)
#     return tuple
#
# while True:
#     tim.color(color())
#     tim.circle(100)
#     tim.setheading((tim.heading() + 10))

# import colorgram
# colors=[]
# color=colorgram.extract("dots paining.jpg",20)
#
# for char in color :
#   r=char.rgb.r
#   g=char.rgb.g
#   b=char.rgb.b
#   colors.append((r,g,b))
#
#
# print(colors)
from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()
colours=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.penup()
tim.setheading(220)
tim.forward(450)
tim.setheading(0)
for char in range(450):
    tim.dot(30,random.choice(colours))

screen.exitonclick()
# import colorgram
# colors=colorgram.extract("dots_paining.jpg",10)
# colors_list=[]
# for char in colors:
#     r=char.rgb.r
#     g=char.rgb.b
#     b=char.rgb.b
#     tuple=(r,g,b)
#     colors_list.append(tuple)
#
# print(colors_list)

# from turtle import Turtle,Screen
# import random
#
# tim=Turtle()
# screen=Screen()
# colours=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
#
#
#
# for _ in range(10):
#   tim.dot(20 ,random.choice(colours))
#
#
#
# screen.exitonclick()