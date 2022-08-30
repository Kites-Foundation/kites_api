from django.contrib import admin, messages
from users import models
from django_ses.views import DashboardView
from users.models import User, UserProfile


class CaseInsensitiveFilter(admin.filters.SimpleListFilter):
    template = 'dropdown_filter.html'
    title: str
    parameter_name: str
    qs = UserProfile.objects.all()

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
    list_display_links = ('username', 'fullname')
    list_display = ('username', 'fullname', 'email', 'is_active', 'is_staff',
                    'is_superuser')
    search_fields = ('fullname__startswith', 'username__startswith')
    list_filter = ('is_superuser', 'is_active', 'is_staff')

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


class UserProfileAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display_links = ('user',)
    search_fields = ('contact_number__startswith', 'whatsapp_number__startswith')
    list_display = ('user', 'state_current', 'district_current', 'area_of_interest', 'blood_group')
    list_filter = (StateFilter, DistrictFilter, 'state_current', 'district_current', 'area_of_interest', 'qualification', 'blood_group')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.UserProfile, UserProfileAdmin)
