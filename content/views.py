from typing import List

from hijridate import Hijri
from ninja_extra import api_controller, http_get, permissions

from content.models import Content
from content.schemas import ContentOut


@api_controller("/contents", tags=["content"], permissions=[permissions.AllowAny])
class ContentAPI:
    @http_get("", response=List[ContentOut])
    def get_content(self, request):
        today = Hijri.today().to_gregorian()
        # TODO if location has an offset, add offset

        return Content.objects.filter(active_start__lte=today, active_end__gte=today)
