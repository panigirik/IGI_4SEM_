import json
import os

from circle import circle_area, circle_perimeter
from square import square_area, square_perimeter

config_path = "/app/config.json"

if os.path.exists(config_path):
    # Читаем конфигурационный файл
    with open(config_path, "r") as file:
        config = json.load(file)
    shape = config["shape"]
    parameter = config["parameter"]
else:
    # Читаем переменные окружения
    shape = os.getenv("SHAPE", "circle")
    parameter = float(os.getenv("PARAMETER", 5))

# Вычисляем площадь и периметр
if shape == "circle":
    area = circle_area(parameter)
    perimeter = circle_perimeter(parameter)
elif shape == "square":
    area = square_area(parameter)
    perimeter = square_perimeter(parameter)
else:
    raise ValueError("Unknown shape!")

print(f"Shape: {shape}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
