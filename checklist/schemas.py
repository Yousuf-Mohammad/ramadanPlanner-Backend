from typing import List, Optional

from ninja import Field, ModelSchema

from checklist.enums import QuranReadUnit
from checklist.models import (
    ChecklistItem,
    DailyActivityChecklist,
    QuranChecklist,
    SalahChecklist,
)


class QuranChecklistIn(ModelSchema):
    last_read_unit: QuranReadUnit

    class Meta:
        model = QuranChecklist
        fields = [
            "unit",
            "last_read_surah",
            "last_read_value",
            "completed_value",
        ]


class QuranChecklistOut(ModelSchema):
    class Meta:
        model = QuranChecklist
        fields = [
            "unit",
            "last_read_surah",
            "last_read_value",
            "completed_value",
        ]


class SalahChecklistOut(ModelSchema):
    class Meta:
        model = SalahChecklist
        fields = [
            "fardh_fajr",
            "fardh_duhr",
            "fardh_asr",
            "fardh_maghrib",
            "fardh_isha",
            "sunnah_fajr",
            "sunnah_duhr",
            "sunnah_asr",
            "sunnah_maghrib",
            "sunnah_isha",
            "sunnah_taraweeh",
            "sunnah_tahajjud",
            "sunnah_duha",
        ]


class ChecklistItemIn(ModelSchema):
    name: str = Field(alias="custom_name")

    class Meta:
        model = ChecklistItem
        fields = ["custom_name"]


class ChecklistItemOut(ModelSchema):
    name: Optional[str]

    class Meta:
        model = ChecklistItem
        fields = [
            "id",
            "is_completed",
        ]


class DailyActivityChecklistOut(ModelSchema):
    items: List[ChecklistItemOut]

    class Meta:
        model = DailyActivityChecklist
        fields = [
            "id",
        ]
