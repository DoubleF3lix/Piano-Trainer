from __future__ import annotations

import random
import typing

if typing.TYPE_CHECKING:
    from main_window import MainWindow


class LilypondStaff:
    def __init__(
        self,
        clef: str,
        allowed_notes: list[str],
        allow_chord_picking: bool,
        key: str = "c",
    ):
        self.clef: str = clef
        self.allowed_notes: list[str] = allowed_notes
        self.allow_chord_picking: bool = allow_chord_picking
        self.key: str = key

        self.octave_to_markers = {2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''"}
        self.valid_timings = [1, 2, 4, 8, 16, 32]

    def convert_note_to_lilypond_pitch(self, note: list, no_timing: bool = False):
        # note, octave with markers, random length
        note_timing = "" if no_timing else random.choice(self.valid_timings)
        return (
            f"{note[0]}{self.octave_to_markers[int(note[-1])]}{'' if no_timing else note_timing}",
            note_timing,
        )

    def get_random_note(self):
        # 50% chance of a chord being picked if they're enabled
        allow_chord = self.allow_chord_picking
        if allow_chord:
            allow_chord = bool(random.getrandbits(1))

        # If the 50% check was successful
        if allow_chord:
            note = " ".join(
                set(
                    [
                        self.convert_note_to_lilypond_pitch(
                            random.choice(self.allowed_notes), no_timing=True
                        )[0]
                        for _ in range(
                            min(len(self.allowed_notes), random.randint(2, 5))
                        )
                    ]
                )
            )
            note = note.split(" ")
            random_element = random.randint(0, len(note) - 1)
            note_to_play = note[random_element]

            note[
                random_element
            ] = f"\\single \\override NoteHead.color = SeaGreen\n{note_to_play}"
            note = "\n".join(note)
            note = note.replace("\n", "\n\t\t")
            note_timing = random.choice([1, 2, 4, 8, 16, 32])
            note = f"<\n\t\t{note}\n\t>{note_timing}"
        else:
            note, note_timing = self.convert_note_to_lilypond_pitch(
                random.choice(self.allowed_notes)
            )
            note_to_play = note

        return note, note_to_play, note_timing

    def convert_key_to_signature(self, key: str):
        return {
            "c": "c \\major",
            "g": "g \\major",
            "d": "d \\major",
            "a": "a \\major",
            "e": "e \\major",
            "b": "b \\major",
            "fs": "fs \\major",
            "cs": "cs \\major",
            "f": "f \\major",
            "bf": "bf \\major",
            "ef": "ef \\major",
            "af": "af \\major",
            "df": "df \\major",
            "gf": "gf \\major",
            "cf": "cf \\major",
        }[key]

    def build(self, rest_note_timing: int = 0):
        note_info = (
            [f"\\skip {rest_note_timing}", "", ""]
            if rest_note_timing
            else self.get_random_note()
        )
        return (
            f"""\\new Staff {{
        \\key {self.convert_key_to_signature(self.key)}
        \\clef {self.clef.lower()}
        \\numericTimeSignature
        {note_info[0]}
        \\bar "|."
    }}""",
            note_info[1],
            note_info[2],
        )


class SheetMusicGenerator:
    def __init__(self, pseudo_parent: MainWindow = None):
        self.pseudo_parent = pseudo_parent

    def fetch_settings(self):
        self.enabled_notes: list = []
        self.enabled_key_signatures: list = []
        self.chord_picking_enabled: bool = False
        self.clef: str = ""

        for key, value in self.pseudo_parent.FileAccessAPI.get_setting(
            "enabled_notes"
        ).items():
            if not value:
                continue
            self.enabled_notes.append([key[:-1].lower(), key[-1]])

        self.enabled_key_signatures = [
            key
            for key, value in self.pseudo_parent.FileAccessAPI.get_setting(
                "key_signatures"
            ).items()
            if value
        ]
        self.chord_picking_enabled = self.pseudo_parent.FileAccessAPI.get_setting(
            "chord_picking_enabled"
        )
        self.clef = self.pseudo_parent.FileAccessAPI.get_setting("clef")

    def generate_sheet_music(self):
        self.fetch_settings()

        treble_clef: LilypondStaff = LilypondStaff(
            "Treble",
            self.enabled_notes,
            self.chord_picking_enabled,
            random.choice(self.enabled_key_signatures),
        )
        bass_clef: LilypondStaff = LilypondStaff(
            "Bass",
            self.enabled_notes,
            self.chord_picking_enabled,
            random.choice(self.enabled_key_signatures),
        )

        lilypond_contents = [
            '\\version "2.22.2"',
            '\\language "english"',
            "\\layout {",
            "\tline-width = #60",
            "\tragged-right = ##f",
            "}",
            "\\new GrandStaff <<",
        ]

        clef = self.clef
        if clef == "Random":
            clef = random.choice(["Treble", "Bass"])

        if clef == "Treble":
            built_clef = treble_clef.build()
            lilypond_contents.append(built_clef[0])
            lilypond_contents.append(bass_clef.build(built_clef[2])[0])
        elif clef == "Bass":
            built_clef = bass_clef.build()
            lilypond_contents.append(treble_clef.build(built_clef[2])[0])
            lilypond_contents.append(built_clef[0])

        lilypond_contents.append(">>")

        return "\n".join(lilypond_contents), built_clef[1]
