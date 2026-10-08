import os
import random
import struct
import zlib

W = H = 64
SCALE = 10
OUT = "/home/user/kondo/ugoira_pixel_art"


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    ca, cb = rgb(a), rgb(b)
    return "#%02x%02x%02x" % tuple(round(ca[i] * (1 - t) + cb[i] * t) for i in range(3))


class Canvas:
    def __init__(self, bg):
        self.px = [[bg] * W for _ in range(H)]

    def put(self, x, y, c):
        if c and 0 <= x < W and 0 <= y < H:
            self.px[y][x] = c

    def tint(self, x, y, c, a):
        if 0 <= x < W and 0 <= y < H:
            self.px[y][x] = mix(self.px[y][x], c, a)

    def rect(self, x, y, w, h, c):
        for j in range(h):
            for i in range(w):
                self.put(x + i, y + j, c)

    def circle(self, cx, cy, r, c):
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + r:
                    self.put(x, y, c)

    def bands(self, colors, top, bottom):
        step = (bottom - top) / len(colors)
        for i, c in enumerate(colors):
            y0 = round(top + i * step)
            y1 = round(top + (i + 1) * step)
            self.rect(0, y0, W, y1 - y0, c)

    def sprite(self, rows, pal, ox, oy):
        for j, row in enumerate(rows):
            for i, ch in enumerate(row):
                if ch != " " and ch in pal:
                    self.put(ox + i, oy + j, pal[ch])

    def sparkle(self, x, y, c="#fff5e1"):
        for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            self.put(x + dx, y + dy, c)

    def finish(self):
        # lo-fi finish: scanlines, film grain, slight darkening of the lower edge
        rng = random.Random(7)
        for y in range(H):
            for x in range(W):
                c = self.px[y][x]
                if y % 4 == 3:
                    c = mix(c, "#000000", 0.12)
                if rng.random() < 0.02:
                    c = mix(c, "#ffffff", 0.07)
                self.px[y][x] = c

    def write_png(self, path):
        rows = []
        for y in range(H):
            line = bytearray([0])
            for x in range(W):
                r, g, b = rgb(self.px[y][x])
                line += bytes([r, g, b]) * SCALE
            for _ in range(SCALE):
                rows.append(bytes(line))
        raw = b"".join(rows)

        def chunk(tag, data):
            body = tag + data
            return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

        w, h = W * SCALE, H * SCALE
        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress(raw, 9))
        png += chunk(b"IEND", b"")
        with open(path, "wb") as f:
            f.write(png)


# ---- Characters (16 x 20 sprites, placeholder designs) ----
KONDO_ROWS = [
    "     KKKKKK     ",
    "    KHHHHHHK    ",
    "   KHHHHHHHHK   ",
    "   KHHHHHHHHK   ",
    "   KHSSSSSSHK   ",
    "   KSSSSSSSSK   ",
    "   KSESSSSESK   ",
    "   KSSSSSSSSK   ",
    "   KSSMMMMSSK   ",
    "    KSSSSSSK    ",
    "     KKKKKK     ",
    "  KBKTTTTTTKBK  ",
    " KBBKTTTTTTKBBK ",
    " KBBKTTTTTTKBBK ",
    "  KBKTTTTTTKBK  ",
    "    KTTTTTTK    ",
    "    KPPPPPPK    ",
    "    KPPKKPPK    ",
    "    KPPK KPPK   ",
    "    KKK   KKK   ",
]
KONDO_PAL = {
    "K": "#1e1b2e", "H": "#f2a65a", "S": "#f5d0b0", "E": "#1e1b2e",
    "M": "#b5566a", "B": "#4ecdc4", "T": "#3d5a80", "P": "#293241",
}

REI_ROWS = [
    "     KKKKKK     ",
    "    KHHHHHHK    ",
    "   KHHHHHHHHK   ",
    "  KHHHHHHHHHHK  ",
    "  KLHHHHHHHHLK  ",
    "  KLKSSSSSSKLK  ",
    "  KLKSESSESKLK  ",
    "  KLKSSSSSSKLK  ",
    "  KLKSSMMSSKLK  ",
    "   KLKSSSSKLK   ",
    "     KKKKKK     ",
    "  KTTTTTTTTTTK  ",
    " KTTTKTTTTKTTTK ",
    "  KTTTTTTTTTTK  ",
    "   KTTTTTTTTK   ",
    "   KPPPPPPPPK   ",
    "   KPPKKKKPPK   ",
    "   KPPK  KPPK   ",
    "   KKK    KKK   ",
]
REI_PAL = {
    "K": "#1e1b2e", "H": "#7b6cb0", "L": "#5a4c8c", "S": "#f5d0b0",
    "E": "#1e1b2e", "M": "#b5566a", "T": "#c9ada7", "P": "#22223b",
}

ASH_ROWS = [
    "    KRRRRRRK    ",
    "   KRRRRRRRRK   ",
    "  KHHHHHHHHHHK  ",
    "  KHHHHHHHHHHK  ",
    " KHHSSSSSSSSHHK ",
    " KHHSSSSSSSSHHK ",
    " KHHSESSSSESHHK ",
    " KHHSSSSSSSSHHK ",
    " KHHSSMMSSSSHHK ",
    "  KHHSSSSSSHHK  ",
    "   KKKKKKKKKK   ",
    "    KTTTTTTK    ",
    "   KTTDTTDTTK   ",
    "   KTTTTTTTTK   ",
    "   KDDDDDDDDK   ",
    "    KPPKKPPK    ",
    "    KPPK KPPK   ",
    "    KKK  KKK    ",
]
ASH_PAL = {
    "K": "#1e1b2e", "H": "#f08fb0", "R": "#d1495b", "S": "#f5d0b0",
    "E": "#1e1b2e", "M": "#b5566a", "T": "#ffd6a5", "D": "#e5a97a",
    "P": "#5c3d5e",
}


def pad_check(rows, name):
    widths = {len(r) for r in rows}
    if widths != {16}:
        print("warning: sprite", name, "row widths", widths)


for _rows, _name in ((KONDO_ROWS, "kondo"), (REI_ROWS, "rei"), (ASH_ROWS, "ashley")):
    pad_check(_rows, _name)


def sprites_ok():
    return True


# ---- Scenes ----

def scene_first_step():
    c = Canvas("#2b2d42")
    c.bands(["#2b2d42", "#4a3f6b", "#8a5a83", "#e07a5f", "#f2cc8f"], 0, 40)
    c.circle(46, 36, 8, "#ffe8a3")
    for i in range(5):  # stairs rising to the right
        x = 34 + i * 6
        top = 56 - i * 5
        c.rect(x, top, 6, 64 - top, "#5c4b51")
        c.rect(x, top, 6, 1, "#8d7b68")
    c.rect(0, 56, 34, 8, "#3b2f4a")
    c.rect(0, 56, 34, 1, "#6d5b7a")
    c.sparkle(14, 14)
    c.sparkle(24, 8)
    c.sparkle(56, 20)
    c.sprite(KONDO_ROWS, KONDO_PAL, 8, 36)
    return c


def scene_home_ground():
    c = Canvas("#14142b")
    c.bands(["#14142b", "#1b1d3a", "#24305a", "#2d3561"], 0, 44)
    c.rect(36, 8, 20, 20, "#0d1224")
    c.circle(46, 16, 4, "#fdf0d5")
    c.tint(44, 14, "#0d1224", 0.5)
    c.rect(45, 8, 2, 20, "#6b4f3a")
    c.rect(36, 17, 20, 1, "#6b4f3a")
    rng = random.Random(3)
    for _ in range(8):
        c.put(37 + rng.randrange(18), 9 + rng.randrange(18), "#fdf0d5")
    # lamp glow (dithered)
    for y in range(20, 44):
        for x in range(0, 26):
            d = ((x - 9) ** 2 + (y - 40) ** 2) ** 0.5
            if d < 13 and (x + y) % 2 == 0:
                c.tint(x, y, "#f4a261", 0.3)
    c.rect(0, 44, 64, 2, "#8a5a3c")
    c.rect(0, 46, 64, 18, "#3a2a22")
    c.rect(7, 42, 4, 2, "#c0c0c0")
    c.rect(4, 36, 10, 2, "#ffb703")
    c.rect(6, 34, 6, 2, "#ffb703")
    c.rect(56, 40, 5, 4, "#c96a4a")
    c.circle(57, 36, 3, "#58a55c")
    c.circle(54, 38, 2, "#58a55c")
    c.sprite(REI_ROWS, REI_PAL, 26, 26)
    c.sparkle(40, 4, "#f4a261")
    return c


def scene_sugar_bomb():
    c = Canvas("#ffc8dd")
    c.bands(["#ffc8dd", "#ffafcc", "#f7a1c4", "#cdb4db"], 0, 64)
    cx, cy = 32, 24
    for ang in range(0, 360, 20):
        for r in range(10, 22):
            x = round(cx + r * __import__("math").cos(__import__("math").radians(ang)))
            y = round(cy + r * __import__("math").sin(__import__("math").radians(ang)))
            c.put(x, y, "#fff3b0" if r % 3 else "#ff5d8f")
    candy_colors = ["#a2d2ff", "#b9fbc0", "#fdffb6", "#ffffff", "#bde0fe"]
    spots = [(6, 10), (12, 28), (56, 12), (58, 34), (8, 44), (50, 50),
             (20, 56), (40, 4), (56, 54), (30, 58)]
    for i, (x, y) in enumerate(spots):
        col = candy_colors[i % len(candy_colors)]
        c.circle(x, y, 2, col)
        c.put(x - 1, y - 1, "#ffffff")
    c.rect(0, 52, 64, 12, "#f48fb1")
    c.rect(0, 52, 64, 1, "#ffc2d1")
    c.sprite(KONDO_ROWS, KONDO_PAL, 24, 30)
    return c


def scene_masterpiece():
    c = Canvas("#264653")
    c.bands(["#264653", "#2a6f6b", "#2a9d8f", "#e9c46a"], 0, 50)
    c.rect(0, 50, 64, 14, "#6b4f3a")
    for y in range(52, 64, 4):
        c.rect(0, y, 64, 1, "#58402f")
    # easel legs
    for t in range(26):
        c.put(12 - t // 6, 26 + t, "#5c4033")
        c.put(22 + t // 6, 26 + t, "#5c4033")
    # canvas
    c.rect(6, 9, 24, 19, "#8a5a3c")
    c.rect(7, 10, 22, 17, "#f4f1de")
    c.circle(18, 18, 4, "#e76f51")
    c.circle(18, 18, 2, "#f4a261")
    c.rect(10, 24, 14, 1, "#2a9d8f")
    c.rect(12, 12, 1, 8, "#264653")
    c.sparkle(26, 14, "#e76f51")
    # paint splatters on floor
    c.circle(50, 58, 2, "#e76f51")
    c.circle(54, 55, 1, "#2a9d8f")
    c.circle(10, 60, 1, "#ffd166")
    c.sprite(ASH_ROWS, ASH_PAL, 38, 30)
    return c


def scene_best_quality():
    c = Canvas("#120c1f")
    c.bands(["#120c1f", "#1d1333", "#2a1b3d"], 0, 64)
    for x0 in (12, 32, 52):
        for y in range(0, 50):
            hw = int(y * 0.3) + 1
            for x in range(x0 - hw, x0 + hw + 1):
                if (x + y) % 2 == 0:
                    c.tint(x, y, "#ffe066", 0.22)
        c.rect(x0 - 2, 0, 5, 2, "#ffe066")
    c.rect(0, 50, 64, 14, "#3a2a4d")
    c.rect(0, 50, 64, 1, "#8d6cb0")
    c.sprite(KONDO_ROWS, KONDO_PAL, 8, 30)
    c.sprite(REI_ROWS, REI_PAL, 24, 30)
    c.sprite(ASH_ROWS, ASH_PAL, 40, 30)
    for x, y in ((4, 6), (60, 8), (30, 44), (58, 44)):
        c.sparkle(x, y, "#ffe066")
    return c


SCENES = [
    ("01_first_step_kondo.png", scene_first_step),
    ("02_home_ground_rei.png", scene_home_ground),
    ("03_sugar_bomb_kondo.png", scene_sugar_bomb),
    ("04_masterpiece_ashley.png", scene_masterpiece),
    ("05_best_quality_all.png", scene_best_quality),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SCENES:
        canvas = fn()
        canvas.finish()
        canvas.write_png(os.path.join(OUT, name))
        print("wrote", name)
