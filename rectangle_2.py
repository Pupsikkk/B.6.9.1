from Classes.rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area(),
      rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(10)
circle_2 = Circle(3)

print("Площади кругов:", circle_1.get_radius(),
      circle_2.get_radius())

figures = [rect_1, rect_2, square_1, square_2]

for item in figures:
    if isinstance(item, Square):
        print(item.get_area_square())
    else:
        print(item.get_area())
