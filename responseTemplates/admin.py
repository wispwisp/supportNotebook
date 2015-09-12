from django.contrib import admin

from responseTemplates.models import ResponseTemplate, Paragraph


class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 1


class ResponseTemplateAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]


admin.site.register(ResponseTemplate, ResponseTemplateAdmin)
