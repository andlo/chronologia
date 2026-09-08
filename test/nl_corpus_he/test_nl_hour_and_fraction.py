"""The Hebrew hour closed by an additive fraction.

Hebrew names quarter past and half past by suffixing the fraction with the
conjunction ו־ ("and"): "שלוש ורבע" is three and a quarter, "שלוש וחצי"
three and a half.  The conjunction is part of the word, so the reading is
additive by the surface itself and never counts toward the coming hour the
way Continental-Germanic "halb neun" does.

Anchor 2017-06-27 13:04.
"""
import pytest

from ._corpus import AstroDate, parse, start


@pytest.mark.parametrize("text,hour,minute", [
    ("בשעה שלוש ורבע", 3, 15),
    ("בשעה שלוש וחצי", 3, 30),
    ("שלוש ורבע", 3, 15),
    ("בשעה שמונה וחצי", 8, 30),
    ("מחר בשעה שלוש וחצי", 3, 30),
])
def test_the_additive_fraction_after_the_hour(text, hour, minute):
    assert start(text) == AstroDate(2017, 6, 28, hour, minute)
    assert parse(text).remainder == ""


def test_the_fraction_reads_through_a_meridiem():
    assert start("בשעה שבע וחצי בבוקר") == AstroDate(2017, 6, 28, 7, 30)
    assert parse("בשעה שבע וחצי בבוקר").remainder == ""


def test_the_bare_hour_is_unchanged():
    assert start("בשעה שלוש") == AstroDate(2017, 6, 28, 3, 0)
