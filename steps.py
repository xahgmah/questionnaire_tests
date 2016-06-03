from base_step import BaseStep


class FirstStep(BaseStep):
    test_url = "/en/pricing/"
    next_url = "/en/questionnaire/2/"
    fields = {
        "first_name": (BaseStep.FIELD_TEXT, "required"),
        "second_name": (BaseStep.FIELD_TEXT, "required"),
        BaseStep.FIELD_EMAIL: (BaseStep.FIELD_EMAIL, "required"),
        "organization": (BaseStep.FIELD_TEXT, "required"),
        "job_title": (BaseStep.FIELD_TEXT, "required"),
        "website": (BaseStep.FIELD_TEXT, "required"),
        "purpose": (BaseStep.FIELD_TEXTAREA, "required")
    }
    submit_button = "next"


class SecondStep(BaseStep):
    test_url = "/en/questionnaire/2/"
    next_url = "/en/questionnaire/3/"
    fields = {
        "active_users2": (BaseStep.FIELD_RADIO, "required"),
        "registered_users2": (BaseStep.FIELD_RADIO, "required"),
        "hosting": (BaseStep.FIELD_RADIO, "required"),
        "mobileapp": (BaseStep.FIELD_RADIO, "required"),
    }
    submit_button = "next"


class ThirdStep(BaseStep):
    test_url = "/en/questionnaire/3/"
    next_url = "/en/questionnaire/4/"
    fields = {
        "localization2": (BaseStep.FIELD_TEXTAREA, "required"),
        "certificates2": (BaseStep.FIELD_CHECKBOX, "required"),
        "lit2": (BaseStep.FIELD_CHECKBOX, "required"),
        "sso2": (BaseStep.FIELD_CHECKBOX, "required"),
        "scorm": (BaseStep.FIELD_CHECKBOX, "required"),
        "commerce": (BaseStep.FIELD_CHECKBOX, "required"),
        "microsites": (BaseStep.FIELD_CHECKBOX, "required"),
    }
    submit_button = "next"


class ForthStep(BaseStep):
    test_url = "/en/questionnaire/4/"
    next_url = "/en/"
    fields = {
        "xb_enable": (BaseStep.FIELD_TEXTAREA, ""),
        "xb_dev": (BaseStep.FIELD_TEXTAREA, ""),
    }
    submit_button = "finish"

