from enum import Enum

from django.shortcuts import get_object_or_404
from hijridate import Hijri
from ninja_extra import api_controller, http_get, http_patch, http_post, permissions

from checklist.models import (
    ChecklistItem,
    DailyActivityChecklist,
    QuranChecklist,
    SalahChecklist,
)
from checklist.schemas import (
    ChecklistItemIn,
    DailyActivityChecklistOut,
    QuranChecklistIn,
    QuranChecklistOut,
    SalahChecklistOut,
)
from common.schemas import GenericSchemaOut


@api_controller(
    "/checklists", tags=["checklist"], permissions=[permissions.IsAuthenticated]
)
class ChecklistAPI:
    @http_get("/quran", response=QuranChecklistOut)
    def get_quran_checklist(self, request):
        return QuranChecklist.objects.get_or_create(
            user=request.auth, date=Hijri.today().to_gregorian()
        )[0]

    @http_patch("/quran", response=GenericSchemaOut)
    def update_quran_checklist(self, request, quran_checklist_in: QuranChecklistIn):
        quran_checklist = QuranChecklist.objects.get(
            user=request.user, date=Hijri.today().to_gregorian()
        )
        for key, value in quran_checklist_in.dict().items():
            if type(value) is Enum:
                value = value.value
            setattr(quran_checklist, key, value)
        quran_checklist.save()
        return GenericSchemaOut(message="Checklist updated")

    @http_get("/salah", response=SalahChecklistOut)
    def get_salah_checklist(self, request):
        return SalahChecklist.objects.get_or_create(
            user=request.user, date=Hijri.today().to_gregorian()
        )[0]

    @http_patch("/salah/{field}/{value}", response=GenericSchemaOut)
    def update_salah_checklist(self, request, field: str, value: bool):
        salah_checklist = SalahChecklist.objects.get(
            user=request.user, date=Hijri.today().to_gregorian()
        )
        setattr(salah_checklist, field, value)
        salah_checklist.save()
        return GenericSchemaOut(message="Checklist updated")

    @http_get("/activities", response=DailyActivityChecklistOut)
    def get_daily_activity_checklist(self, request):
        return DailyActivityChecklist.objects.get_or_create(
            user=request.user, date=Hijri.today().to_gregorian()
        )[0]

    @http_patch("/activities/{id}/{value}", response=GenericSchemaOut)
    def update_daily_activity_checklist(self, request, id: str, value: bool):
        checklist = DailyActivityChecklist.objects.get(
            user=request.user, date=Hijri.today().to_gregorian()
        )
        item = get_object_or_404(ChecklistItem, checklist=checklist, id=id)
        item.is_completed = value
        item.save()
        return GenericSchemaOut(message="Checklist updated")

    @http_post("/activities", response=GenericSchemaOut)
    def add_daily_activity_checklist(self, request, checklist_in: ChecklistItemIn):
        checklist = DailyActivityChecklist.objects.get(
            user=request.user, date=Hijri.today().to_gregorian()
        )
        ChecklistItem.objects.create(
            custom_name=checklist_in.name,
            checklist=checklist,
            user=request.user,
        )

        return GenericSchemaOut(message="Checklist item added")
