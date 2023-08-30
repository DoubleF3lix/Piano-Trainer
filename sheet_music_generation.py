from __future__ import annotations

import enum
import random
import typing

from util import Note

if typing.TYPE_CHECKING:
    from main_window import MainWindow


class StaffType(enum.Enum):
    TREBLE = "treble"
    BASS = "bass"
    RANDOM = "random"


class LilypondStaff:
    def __init__(
        self,
        clef: StaffType,
        note: Note,
        key: str = "c",
    ):
        self.clef = clef
        self.note = note
        self.key = key

        self.key_to_lilypond = {
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
        }


    # if rest_note_timing != 0, use a rest note instead
    def build(self, blank: bool):
        note = (
            # f"\\skip {self.note.length}" if blank else self.note.lilypond_format
            "\\skip 4" if blank else self.note.lilypond_format
        )

        return (
f"""\\new Staff {{
    \\key {self.key_to_lilypond[self.key]}
    \\clef {self.clef.value}
    \\numericTimeSignature
    {note}
    \\bar "|."
}}"""
        )


class SheetMusicGenerator:
    def __init__(self, pseudo_parent: MainWindow = None):
        self.pseudo_parent = pseudo_parent

    def fetch_settings(self):
        self.enabled_notes: list[Note] = [
            Note.parse_from_full(key)
            for key, value in self.pseudo_parent.FileAccessAPI.get_setting(
                "enabled_notes"
            ).items()
            if value
        ]
        self.enabled_key_signatures: list[str] = [
            key
            for key, value in self.pseudo_parent.FileAccessAPI.get_setting(
                "key_signatures"
            ).items()
            if value
        ]
        self.clef: StaffType = StaffType(self.pseudo_parent.FileAccessAPI.get_setting("clef").lower())

    def generate_sheet_music(self) -> tuple[str, Note]:
        self.fetch_settings()

        # Generate the random data ahead of time so it's easier to sync between the two staffs
        random_note = random.choice(self.enabled_notes)
        # random_note.length = random.choice([1, 2, 4, 8, 16])
        random_key_signature = random.choice(self.enabled_key_signatures)

        treble_clef: LilypondStaff = LilypondStaff(
            StaffType.TREBLE,
            random_note,
            random_key_signature
        )
        bass_clef: LilypondStaff = LilypondStaff(
            StaffType.BASS,
            random_note,
            random_key_signature
        )

        lilypond_contents = [
            '\\version "2.24.2"',
            '\\language "english"',
            "\\layout {",
            "\tline-width = #60",
            "\tragged-right = ##f",
            "}",
            "\\new GrandStaff <<",
        ]

        # Just build the clefs in the right order
        clef = self.clef
        if clef == StaffType.RANDOM:
            clef = random.choice([StaffType.TREBLE, StaffType.BASS])

        clef_skip_bool = True if clef == StaffType.TREBLE else False
        lilypond_contents.extend(
            [
                treble_clef.build(not clef_skip_bool),
                bass_clef.build(clef_skip_bool)
            ]
        )

        lilypond_contents.append(">>")

        # Return the finished lilypond string and the note
        return "\n".join(lilypond_contents), random_note
