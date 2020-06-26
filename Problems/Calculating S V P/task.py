length = int(input())
width = int(input())
height = int(input())

sum_edges = 4 * (length + width + height)
area = 2 * (length * width + width * height + length * height)
volume = length * width * height

print(sum_edges)
print(area)
print(volume)
