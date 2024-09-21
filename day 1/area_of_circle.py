# Find area and circumference of circle.
PI = 3.14

def circle_area(radius):
    return (PI*radius**2)


radius = int(input("enter radius of circle: "))

# area = circle_area(radius)
# print(f"area of circle is {area:.2f}")
print(f"area of circle is {circle_area(radius):.2f}")
