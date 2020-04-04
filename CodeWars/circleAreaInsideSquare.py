import math
def square_area_to_circle(size):
  squareLength=math.sqrt(size)
  circleRadius=squareLength/2

  return round(circleRadius*circleRadius*math.pi,8)

print(square_area_to_circle(20))