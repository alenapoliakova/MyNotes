from enum import Enum


class MyNote(str, Enum):
    all_notes = "all_notes"
    five_recent_notes = "5_recent_notes"
