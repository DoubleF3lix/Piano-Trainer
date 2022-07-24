import os

for file in os.listdir(q := os.path.join("ui", "designer")):
    if file.endswith(".py"):
        os.system(
            f"pyside6-uic {os.path.join(q, file)} > {os.path.join('ui', f'{os.path.splitext(file)[0]}_ui.py')}"
        )
