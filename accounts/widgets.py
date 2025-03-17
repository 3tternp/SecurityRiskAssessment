from django.forms import RadioSelect, CheckboxSelectMultiple

class RadioSelectButtonGroup(RadioSelect):
    """
    This widget renders a Bootstrap 5 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """

    template_name = "widgets/radio_select_button_group.html"

    def __init__(self, attrs=None, choices=()):
        default_attrs = {'class': 'btn-check'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs, choices)

class CheckboxInputGroup(CheckboxSelectMultiple):
    """
    This widget renders a Bootstrap 5 set of checkboxes as buttons horizontally.

    Much more mobile friendly.
    """

    template_name = "widgets/checkbox_input_group.html"

    def __init__(self, attrs=None, choices=()):
        default_attrs = {'class': 'btn-check'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs, choices)

