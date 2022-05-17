from django.contrib import admin, messages
from users import models
from django_ses.views import DashboardView
from users.models import User


class CaseInsensitiveFilter(admin.filters.SimpleListFilter):
    template = 'dropdown_filter.html'
    title: str
    parameter_name: str
    qs = User.objects.all()

    def lookups(self, request, model_admin):
        data = self.qs.values_list(self.title)
        values = list(sorted(set([x[0].lower() for x in data])))
        return [(x, x) for x in values]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            field = f"{self.title}__iexact"
            return queryset.filter(
                **{
                    field: value.lower()
                }
            )
        return queryset


class StateFilter(CaseInsensitiveFilter):
    title = 'state_current'
    parameter_name = title


class DistrictFilter(CaseInsensitiveFilter):
    title = 'district_current'
    parameter_name = title


class UserAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display_links = ('username', 'name')
    list_display = ('username', 'name', 'email', 'blood_group', 'is_active', 'is_staff',
                    'is_superuser')
    search_fields = ('name__startswith', 'username__startswith', 'contact_number__startswith',
                     'whatsapp_number__startswith')
    list_filter = (StateFilter, DistrictFilter, 'is_superuser', 'is_active', 'is_staff', 'qualification')

    def make_active(self, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(self, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")

    def has_delete_permission(self, request, obj=None):
        return False

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")


admin.site.register(models.User, UserAdmin)
