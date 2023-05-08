# import turtle
#
# # creating objects from classes Turtle() and Screen()
# timmy = turtle.Turtle()
# print(timmy)
#
# my_screen = turtle.Screen()
#
# # printing attribute (canvheight) of my_screen object
# print(my_screen.canvheight)
#
# # using methods on timmy
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
#
# # calling object method for my_screen
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
