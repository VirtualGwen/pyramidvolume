base_area = 0
volume = 0
def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    volume = base_area * pyramid_height * (1/3)
    return volume

length = float(input())
width = float(input())
height = float(input())
print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))
