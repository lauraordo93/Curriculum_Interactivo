from PIL import Image, ImageDraw
import os

# Asegurarse de que la carpeta exista
os.makedirs("assets/animaciones", exist_ok=True)

# Configuración del GIF
ancho, alto = 480, 480
cuadros = 50
tamano_cuadro = 50
velocidad = 3  # píxeles por frame

imagenes = []

for frame in range(cuadros):
    img = Image.new("RGB", (ancho, alto), "White")  # Color rayas
    draw = ImageDraw.Draw(img)

    for fila in range(0, alto, tamano_cuadro):
        for col in range(0, ancho, tamano_cuadro):
            y_offset = (frame * velocidad) % alto
            y_pos = (fila + y_offset) % alto
            draw.rectangle(
                [col, y_pos, col + tamano_cuadro - 2, y_pos + tamano_cuadro - 2],
                fill="black"  # Fondo
            )

    imagenes.append(img)

# Guardar el GIF en la carpeta
imagenes[0].save("assets/animaciones/animacionCaida.gif", save_all=True, append_images=imagenes[1:], duration=10, loop=0)

print("GIF generado correctamente ✅")