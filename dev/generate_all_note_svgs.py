# Run from root directory
# TODO impossible ottova lines (like 15va doesn't work with octave 6 or 7)
# TODO this also takes over an hour to run, wouldn't recommend
# I'm just gonna bundle lilypond with it for now
import os
import shutil
import subprocess

from util import Note

LP_DIRECTORY = "assets/note_svg/lilypond"
BATCH_SIZE = 5

def generate_lilypond_file_content(key, treble_note, bass_note, treble_ottova_value, bass_ottova_value):
    return f"""
\\version "2.24.2"
\\language "english"
\\layout {{
	line-width = #60
	ragged-right = ##f
}}
\\new GrandStaff <<
\\new Staff {{
    \\key {key} \\major
    \\clef treble
    \\numericTimeSignature
    \ottava #{treble_ottova_value}
    {treble_note}
    \\bar "|."
}}
\\new Staff {{
    \\key {key} \\major
    \\clef bass
    \\numericTimeSignature
    \ottava #{bass_ottova_value}
    {bass_note}
    \\bar "|."
}}
>>
""".strip()


def generate_ly_files():
    note_names = ["a", "as", "b", "c", "cs", "d", "ds", "e", "f", "fs", "g", "gs"]
    all_possible_notes = []

    for octave in range(2, 8):
        if octave == 2:
            all_possible_notes.extend(f"{q}2" for q in note_names[note_names.index("cs") :])
        elif octave == 7:
            all_possible_notes.extend(f"{q}7" for q in note_names[: note_names.index("d")])
        else:
            all_possible_notes.extend(f"{q}{octave}" for q in note_names)

    all_possible_notes = [Note.parse_from_full(q) for q in all_possible_notes]

    for note in all_possible_notes:
        for key in ["c", "g", "d", "a", "e", "b", "fs", "cs", "f", "bf", "ef", "af", "df", "gf", "cf"]:
            for ottova_value in range(-2, 3):
                with open(os.path.join(LP_DIRECTORY, f"{str(note)}_{key}_{ottova_value}_treble.ly"), "w") as outfile:
                    outfile.write(generate_lilypond_file_content(key, note.lilypond_format, "\\skip 4", ottova_value, 0))
                with open(os.path.join(LP_DIRECTORY, f"{str(note)}_{key}_{ottova_value}_bass.ly"), "w") as outfile:
                    outfile.write(generate_lilypond_file_content(key, "\\skip 4", note.lilypond_format, 0, ottova_value))

                print(f"Generated {str(note)}_{key}_{ottova_value}_treble.ly and {str(note)}_{key}_{ottova_value}_bass.ly")


def compile_lilypond_file(dir: str, file_name: str):
    return subprocess.Popen(["lilypond", "--loglevel=NONE", "--svg", "-dcrop", file_name], cwd=dir, shell=True)

def compile_ly_files():
    processes: list[subprocess.Popen] = []
    file_processed_count = 0

    for lilypond_file in os.listdir(LP_DIRECTORY):
        if lilypond_file.endswith(".ly"):
            file_processed_count += 1
            if lilypond_file[:-2] + "cropped.svg" in os.listdir(LP_DIRECTORY):
                print(f"Skipping {lilypond_file} because it has been compiled already")
                continue

            processes.append(compile_lilypond_file(LP_DIRECTORY, lilypond_file))

            if len(processes) == BATCH_SIZE:
                for process in processes:
                    process.wait()

                print(f"{round(file_processed_count / 9150 * 100, 2)}% done - ({file_processed_count}/9150)")
                processes.clear()
    else:
        for process in processes:
            process.wait()

        print(f"Finished batch with remaining {len(processes)} processes")
        processes.clear()


def cleanup_svgs():
    for svg_file in os.listdir(LP_DIRECTORY):
        if svg_file.endswith(".cropped.svg"):
            shutil.move(os.path.join(LP_DIRECTORY, svg_file), os.path.join("assets", "note_svg", svg_file.replace(".cropped.svg", ".svg")))
            print(f"Moved {svg_file} to assets/note_svg")

    for svg_file in os.listdir(LP_DIRECTORY):
        if svg_file.endswith(".svg"):
            os.remove(os.path.join(LP_DIRECTORY, svg_file))
            print(f"Removed uncropped {svg_file}")


# generate_ly_files()
# compile_ly_files()
cleanup_svgs()