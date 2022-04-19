from unittest import mock

from django.apps import AppConfig

from template_names.mock import mock_render


class TemplateNamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'template_names'

    def ready(self) -> None:
        mock_render()
