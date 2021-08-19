import colorgram

# extract 24 colors from an image
colors = colorgram.extract('damien_hirst_painting.jpeg', 24)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
