def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return f"the area of the circle is {area}"

def triangle_area(base, height):
    area = (base * height) / 2
    return f"the area of the triangle is {area}"

def square_area(side1, side2):
    area = side1 * side2
    return f"the area of the square is {area}"

while True:
    try:
        def main():
            shape = input("Which shape's area would you like to calculate? ")
            area = 0
            if shape == "circle":
                radius = int(input("What is the radius? "))
                area = circle_area(radius)
            elif shape == "square" or shape.lower() =="rectangle":
                x = int(input("What is the length of the first side? "))
                y = int(input("What is the length of the second side? "))
                area = square_area(x, y)
            elif shape == "triangle":
                x = int(input("What is the length of the height? "))
                y = int(input("What is the length of the bottom? "))
                area = triangle_area(x, y)
            else:
                print("error, invalid shape name")
                return 1 
            print(f"{area}")
            return 0  
        main()
    except:
        print("error, invalid value")