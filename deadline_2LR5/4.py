
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255)
}
print(f"Доступные цвета: {list(colors.keys())}\n")
def mix_colors(color1_rgb, color2_rgb):
    """
    Смешивает два цвета, усредняя их компоненты R, G и B.
    """
    r1, g1, b1 = color1_rgb
    r2, g2, b2 = color2_rgb
    mixed_r = (r1 + r2) // 2
    mixed_g = (g1 + g2) // 2
    mixed_b = (b1 + b2) // 2
    return (mixed_r, mixed_g, mixed_b)
color_name_a = "red"
color_name_b = "blue"
color_a = colors[color_name_a]
color_b = colors[color_name_b]
mixed = mix_colors(color_a, color_b)
print(f"Смешивание цвета '{color_name_a}' {color_a} и цвета '{color_name_b}' {color_b}:")
print(f"Полученный цвет (пурпурный/фиолетовый): {mixed}\n")
def invert_color(color_rgb):
    """
    Инвертирует цвет по формуле: 255 - исходное_значение.
    """
    r, g, b = color_rgb
    inverted_r = 255 - r
    inverted_g = 255 - g
    inverted_b = 255 - b 
    return (inverted_r, inverted_g, inverted_b)
color_to_invert_name = "green"
color_to_invert = colors[color_to_invert_name]
inverted = invert_color(color_to_invert)
print(f"Инвертирование цвета '{color_to_invert_name}' {color_to_invert}:")
print(f"Полученный цвет (пурпурный/фуксия): {inverted}")


