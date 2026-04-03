import qrcode
from PIL import Image, ImageDraw

# 🔹 Datos
data = "https://www.facebook.com/profile.php?id=61572496917401"

# 🔹 Crear QR base
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

qr.add_data(data)
qr.make(fit=True)
matrix = qr.get_matrix()

# 🔹 Configuración
box_size = 12
size = len(matrix) * box_size

# 🔹 Imagen transparente
img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# 🔹 Degradado rosa
def gradient_color(y, height):
    r1, g1, b1 = (226, 28, 127)
    r2, g2, b2 = (255, 105, 180)

    ratio = y / height

    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)

    return (r, g, b)

# 🔹 Dibujar puntos redondos
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x]:
            x1 = x * box_size
            y1 = y * box_size
            x2 = x1 + box_size
            y2 = y1 + box_size

            color = gradient_color(y, len(matrix))
            draw.ellipse([x1, y1, x2, y2], fill=color)

# 🔹 Logo (SIN fondo blanco)
logo = Image.open("logo.png").convert("RGBA")

logo_size = int(size * 0.25)
logo = logo.resize((logo_size, logo_size))

# 🔹 Centrar logo
pos = (
    (size - logo_size) // 2,
    (size - logo_size) // 2
)

# 🔹 Pegar logo transparente
img.paste(logo, pos, logo)

# 🔹 Guardar
img.save("qr.png")

print("🔥 QR listo ")