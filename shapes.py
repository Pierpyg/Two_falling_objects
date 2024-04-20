class Shape:
    def __init__(self, name, drag_coefficient, line_style):
        self.name = name
        self.drag_coefficient = drag_coefficient
        self.line_style = line_style


shapes_data = {
    1: Shape("Sphere", 0.47, "o"),
    2: Shape("Semi-sphere", 0.42, "o"),
    3: Shape("Cone", 0.50, "<"),
    4: Shape("Cube", 1.05, "s"),
    5: Shape("Inclined cube", 0.80, "D"),
    6: Shape("Long cylinder", 0.82, "_"),
    7: Shape("Short cylinder", 1.15, "."),
    8: Shape("Streamlined body", 0.04, "1"),
    9: Shape("Semi-streamlined body", 0.09, "2"),
}
