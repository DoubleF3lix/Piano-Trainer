\version "2.22.2"
\language "english"
\layout {
	line-width = #60
	ragged-right = ##f
}
\new GrandStaff <<
\new Staff {
        \key c \major
        \clef treble
        \numericTimeSignature
        e'32
        \bar "|."
    }
\new Staff {
        \key c \major
        \clef bass
        \numericTimeSignature
        \skip 32
        \bar "|."
    }
>>