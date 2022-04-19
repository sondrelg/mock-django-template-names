from unittest import mock

from django.template import Context
from django.template.loader_tags import IncludeNode
from django.template.response import SimpleTemplateResponse
from django.utils.safestring import SafeString


def mock_render():
    """Mock select template rendering to add template names at the content start."""
    # Mock SimpleTemplateResponse.render
    # -- This alters TemplateResponse rendering
    pre_mocked_simpletemplateresponse_callable = SimpleTemplateResponse.render

    def altered_simpletemplateresponse_render(self: SimpleTemplateResponse) -> SimpleTemplateResponse:
        self = pre_mocked_simpletemplateresponse_callable(self)
        self.content = f'<!-- template name: {self.template_name} -->\n'.encode('utf-8') + self.content
        return self

    mock.patch.object(SimpleTemplateResponse, 'render', altered_simpletemplateresponse_render).start()

    # Mock IncludeNode.render
    # -- This alters {% include ... %} tag rendering

    pre_mocked_includenode_callable = IncludeNode.render

    def altered_includenode_render(self: IncludeNode, context: Context) -> SafeString:
        safe_string = pre_mocked_includenode_callable(self, context)
        safe_string = SafeString(f'<!-- template name: {context.template_name} -->\n') + safe_string
        return safe_string

    mock.patch.object(IncludeNode, 'render', altered_includenode_render).start()
