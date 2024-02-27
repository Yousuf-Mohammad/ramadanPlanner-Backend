from typing import List

from hijridate import Hijri
from ninja_extra import api_controller, http_get, permissions

from content.models import Content
from content.schemas import ContentOut


@api_controller("/contents", tags=["content"], permissions=[permissions.AllowAny])
class ContentAPI:
    @http_get("", response=List[ContentOut])
    def get_content(
        self,
        request,
        year: int = None,
        month: int = None,
        day: int = None,
    ):
        if all((year, month, day)):
            date = Hijri(year, month, day).to_gregorian()
        else:
            date = Hijri.today().to_gregorian()

        return Content.objects.filter(active_start__lte=date, active_end__gte=date)
