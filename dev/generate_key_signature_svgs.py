# Run from root directory
import os

root = os.path.join("assets", "key_signatures")

for file in os.listdir(q := os.path.join(root, "lilypond")):
    print(f"Processing {file}...", end=" ")
    os.system(
        f'lilypond --svg --output="assets\\key_signatures" --loglevel=none -dcrop -dno-point-and-click {os.path.join(q, file)}'
    )
    print("done!")

for file in os.listdir(root):
    if file.endswith(".svg") and not file.endswith(".cropped.svg"):
        os.remove(os.path.join(root, file))

for file in os.listdir(root):
    if file.endswith(".cropped.svg"):
        os.rename(os.path.join(root, file), os.path.join(root, f"{file[:-12]}.svg"))
