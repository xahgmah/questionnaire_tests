from selenium import webdriver
from grail import step


class BaseStep(object):
    FIELD_TEXT = "text"
    FIELD_TEXTAREA = "textarea"
    FIELD_EMAIL = "email"
    FIELD_RADIO = "radio"
    FIELD_CHECKBOX = "checkbox"
    TEST_DATA = {
        FIELD_TEXT: "test",
        FIELD_TEXTAREA: "test",
        FIELD_EMAIL: "test@test.com",
    }
    next_url = None
    test_url = None
    fields = []
    submit_button = ""

    def __init__(self, testcase):
        self.testcase = testcase
        self.browser = self.testcase.browser
        self.browser.get(self.testcase.base_url + self.test_url)

    @step
    def _test_empty_data(self):
        required_fields = 0
        for name, properties in self.fields.iteritems():
            if properties[1] == 'required':
                required_fields += 1
        self.testcase.assertIn('Edx questionary', self.browser.title)
        self.browser.find_element_by_class_name("btn-" + self.submit_button).click()
        self.testcase.assertIn("This field is required.", self.browser.page_source)
        self.testcase.assertEqual(self.testcase.base_url + self.test_url, self.browser.current_url)

    @step
    def _test_wrong_email(self):
        for name, properties in self.fields.iteritems():
            if properties[0] == "email":
                self.browser.find_element_by_name(name).send_keys("test")
        self.browser.find_element_by_class_name("btn-" + self.submit_button).click()
        self.testcase.assertIn("Enter a valid email address.", self.browser.page_source)
        self.testcase.assertEqual(self.testcase.base_url + self.test_url, self.browser.current_url)

    @step
    def _test_correct_data(self):
        for name, properties in self.fields.iteritems():
            if properties[0] == BaseStep.FIELD_RADIO:
                self.browser.find_element_by_xpath("//label[@for='id_" + name + "_0']").click()
            elif properties[0] == BaseStep.FIELD_CHECKBOX:
                self.browser.find_element_by_xpath("//input[@name='" + name + "']/following-sibling::*").click()
            else:
                test_data = self.TEST_DATA[properties[0]]
                field = self.browser.find_element_by_name(name)
                field.clear()
                field.send_keys(test_data)
        self.browser.find_element_by_class_name("btn-" + self.submit_button).click()
        self.testcase.assertFalse(self.browser.find_elements_by_class_name("errorlist"))
        self.testcase.assertNotEqual(self.browser.current_url, self.testcase.base_url + self.test_url)
        self.testcase.assertEqual(self.browser.current_url, self.testcase.base_url + self.next_url)

    @step
    def _test_saved_data(self):
        self.browser.get(self.testcase.base_url + self.test_url)
        for name, properties in self.fields.iteritems():
            field = self.browser.find_element_by_name(name)
            if properties[0] == BaseStep.FIELD_TEXTAREA:
                self.testcase.assertEqual(field.text, self.TEST_DATA[properties[0]])
            elif properties[0] in [BaseStep.FIELD_RADIO, BaseStep.FIELD_CHECKBOX]:
                self.testcase.assertNotEqual(field.get_attribute("value"), "")
            else:
                self.testcase.assertEqual(field.get_attribute("value"), self.TEST_DATA[properties[0]])
