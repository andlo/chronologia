"""The Hebrew hour with the "at" preposition fused onto it.

Hebrew tells the time in the feminine, because שעה is feminine, and writes
the preposition ב־ ("at") joined to the numeral with no space: "בשבע בבוקר"
is at seven in the morning.  The masculine forms are not hour surfaces --
Hebrew names its weekdays by the masculine ordinal, so בשני is Monday.

Anchor 2017-06-27 13:04.
"""
import pytest

from ._corpus import AstroDate, nomatch, parse, start


@pytest.mark.parametrize("text,day,hour", [
    ("בשבע בבוקר", 28, 7),
    ("בשמונה בבוקר", 28, 8),
    ("בעשר בבוקר", 28, 10),
    # afternoon hours are still ahead of the 13:04 anchor, so they stay today
    ("בשלוש אחר הצהריים", 27, 15),
    ("בחמש אחר הצהריים", 27, 17),
    ("באחת בלילה", 28, 1),
])
def test_the_fused_preposition_leaves_the_hour_readable(text, day, hour):
    assert start(text) == AstroDate(2017, 6, day, hour, 0)
    assert parse(text).remainder == ""


def test_it_composes_with_the_additive_fraction():
    assert start("בשבע ורבע בבוקר") == AstroDate(2017, 6, 28, 7, 15)
    assert parse("בשבע ורבע בבוקר").remainder == ""


def test_the_masculine_form_is_still_the_weekday():
    """בשני is Monday, not two o'clock -- the collision fold_he guards."""
    assert start("ביום שני") == AstroDate(2017, 7, 3)
    nomatch("בשני")


def test_the_separate_hour_noun_is_unchanged():
    assert start("בשעה שלוש וחצי") == AstroDate(2017, 6, 28, 3, 30)
