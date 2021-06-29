''' admin moudle '''

# pylint: disable=E0402
# type: ignore

from django.contrib import admin

# Register your models here.
from .models import blog
from .models import answer


admin.site.register(blog)
admin.site.register(answer)
