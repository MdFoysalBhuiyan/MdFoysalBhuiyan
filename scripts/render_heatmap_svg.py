import json
from pathlib import Path

with open("data/contributions.json", "r") as f:
    contributions = json.load(f)

cell_size = 12
gap = 3
columns = 53
rows = 7

width = columns * (cell_size + gap)
height = rows * (cell_size + gap)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}" height="{height}"
viewBox="0 0 {width} {height}">

<style>
    .cell {{
        opacity: 0;
        animation: appear 0.4s forwards;
    }}

    @keyframes appear {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
</style>
'''

for i, item in enumerate(contributions):
    col = i // 7
    row = i % 7

    if col >= columns:
        break

    level = item["level"]

    if level == 0:
        opacity = 0.15
    elif level == 1:
        opacity = 0.35
    elif level == 2:
        opacity = 0.55
    elif level == 3:
        opacity = 0.75
    else:
        opacity = 1

    x = col * (cell_size + gap)
    y = row * (cell_size + gap)

    svg += f'''
    <rect
        class="cell"
        x="{x}"
        y="{y}"
        width="{cell_size}"
        height="{cell_size}"
        rx="2"
        fill="#39d353"
        opacity="{opacity}"
        style="animation-delay:{i * 0.01}s"
    />
    '''

svg += "</svg>"

Path("contrib-heatmap.svg").write_text(svg)

print("Created contrib-heatmap.svg")