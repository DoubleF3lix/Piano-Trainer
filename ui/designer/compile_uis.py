import os


def compile_uis():
    for file in os.listdir(q := os.path.join("ui", "designer")):
        if file.endswith(".ui"):
            print(f"Compiling {file}...", end=" ")
            os.system(
                f"pyside6-uic {os.path.join(q, file)} > {os.path.join('ui', f'{os.path.splitext(file)[0]}_ui.py')}"
            )
            print("done!")


if __name__ == "__main__":
    compile_uis()
