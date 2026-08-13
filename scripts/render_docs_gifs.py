"""Render terminal-style docs GIFs. Deterministic. No network."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FONT_PATH = Path(r"C:\Windows\Fonts\consola.ttf")

BG = (13, 17, 23)
FG = (230, 237, 243)
DIM = (139, 148, 158)
GREEN = (63, 185, 80)
AMBER = (210, 153, 34)
RED = (248, 81, 73)
BLUE = (88, 166, 255)
MUTED = (72, 79, 88)


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def new_frame(size: tuple[int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", size, BG)
    return image, ImageDraw.Draw(image)


def draw_chrome(draw: ImageDraw.ImageDraw, width: int, title: str) -> None:
    draw.rounded_rectangle((12, 12, width - 12, 44), radius=8, fill=(22, 27, 34))
    for x, color in ((28, RED), (48, AMBER), (68, GREEN)):
        draw.ellipse((x, 22, x + 12, 34), fill=color)
    draw.text((92, 20), title, font=font(14), fill=DIM)


def save_gif(path: Path, frames: list[Image.Image], durations: list[int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2,
    )


def render_attach() -> None:
    width, height = 880, 400
    body_font = font(18)
    lines = [
        (FG, "$ phaseledger attach ."),
        (DIM, "session  7c1a   ./checkout"),
        (DIM, ""),
        (BLUE, "ports"),
        (AMBER, "  walkaround       admission     unsigned     no VERIFIED"),
        (GREEN, "  trust-meter      observation   attached"),
        (AMBER, "  greenwash        detect        missing      INCOMPLETE"),
        (RED, "  tomorrowci-lab   freshness     blocked      NOT_RUN"),
        (DIM, ""),
        (RED, "advance  refused   no fresh measurer PASS"),
    ]

    frames: list[Image.Image] = []
    durations: list[int] = []
    for count in range(1, len(lines) + 1):
        image, draw = new_frame((width, height))
        draw_chrome(draw, width, "phaseledger — local socket")
        y = 68
        for color, text in lines[:count]:
            draw.text((28, y), text, font=body_font, fill=color)
            y += 30
        if count < len(lines):
            cursor_y = 68 + (count - 1) * 30
            cursor_x = 28 + int(body_font.getlength(lines[count - 1][1])) + 6
            draw.rectangle((cursor_x, cursor_y + 4, cursor_x + 10, cursor_y + 20), fill=FG)
        frames.append(image)
        durations.append(420 if count < len(lines) else 2200)

    save_gif(DOCS / "attach.gif", frames, durations)


def render_loop() -> None:
    width, height = 880, 220
    stages = [
        ("ADMIT", "unsigned", AMBER),
        ("MEASURE", "observation", GREEN),
        ("GATE", "no advance", RED),
        ("DETECT", "INCOMPLETE", AMBER),
        ("RE-RUN", "inconclusive", AMBER),
        ("REPLAY", "no Reality", DIM),
        ("FORECAST", "BLOCKED", RED),
    ]
    box_w, box_h = 108, 72
    gap = 10
    start_x = 20
    top = 70

    frames: list[Image.Image] = []
    durations: list[int] = []
    for active in range(len(stages)):
        image, draw = new_frame((width, height))
        draw_chrome(draw, width, "audit loop — evidence, not a pipeline")
        for i, (name, status, color) in enumerate(stages):
            x = start_x + i * (box_w + gap)
            border = color if i <= active else MUTED
            fill = (22, 27, 34) if i <= active else (17, 20, 26)
            draw.rounded_rectangle((x, top, x + box_w, top + box_h), radius=8, outline=border, width=2, fill=fill)
            title_color = FG if i <= active else MUTED
            status_color = color if i <= active else MUTED
            draw.text((x + 10, top + 12), name, font=font(14), fill=title_color)
            draw.text((x + 10, top + 40), status, font=font(13), fill=status_color)
            if i < len(stages) - 1:
                ax = x + box_w + 3
                ay = top + box_h // 2
                arrow = GREEN if i < active else MUTED
                draw.line((ax, ay, ax + gap - 6, ay), fill=arrow, width=2)
                draw.polygon(
                    [(ax + gap - 6, ay - 4), (ax + gap - 2, ay), (ax + gap - 6, ay + 4)],
                    fill=arrow,
                )
        frames.append(image)
        durations.append(380 if active < len(stages) - 1 else 1800)

    save_gif(DOCS / "audit-loop.gif", frames, durations)


if __name__ == "__main__":
    render_attach()
    render_loop()
    print("wrote", DOCS / "attach.gif")
    print("wrote", DOCS / "audit-loop.gif")
