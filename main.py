import board
import neopixel

DATA_PIN = board.GPIO16
STRIP_LEN = 50

COLOR = {
    "RED": (255, 0 ,0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0)
}

if __name__ == "__main__" :
    strip = neopixel.NeoPixel(DATA_PIN, STRIP_LEN, auto_write=False)
    for i in STRIP_LEN:
        strip[i] = COLOR["RED"]
    # --- for ---
# --- main ---
