data = "hello"
with open('encodeable.txt', 'rb') as f:
    data = f.read()
    print(data)

import png

indexes = []
for ix, letter in enumerate(data):
    # print(f"index {ix} is letter {letter}")
    indexes.append(letter)

width = len(indexes)
height = 1
img = []
for y in range(height):
    row = ()
    for x in range(width):
        row = row + (x, indexes[x], y)
    img.append(row)


with open('gradient.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)


# Read the image and extract the data back
reader = png.Reader(filename='gradient.png')
width, height, rows, info = reader.read()
pixels = list(rows)

# Extract the original data from the green channel (indexes[x])
recovered_data = bytes([pixels[0][i*3 + 1] for i in range(width)])
print(recovered_data)
