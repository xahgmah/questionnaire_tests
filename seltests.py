from selenium import webdriver
import unittest
import steps


class QuestionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.base_url = "https://raccoongang.com"

    def step1(self):
        self.step = steps.FirstStep(self)
        self.step._test_empty_data()
        self.step._test_wrong_email()
        self.step._test_correct_data()
        self.step._test_saved_data()

    def step2(self):
        self.step = steps.SecondStep(self)
        self.step._test_empty_data()
        self.step._test_correct_data()
        self.step._test_saved_data()

    def step3(self):
        self.step = steps.ThirdStep(self)
        self.step._test_empty_data()
        self.step._test_correct_data()
        self.step._test_saved_data()

    def step4(self):
        self.step = steps.ForthStep(self)
        self.step._test_correct_data()

    def list_of_steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self.list_of_steps():
            try:
                print "========== %s ==========" % name
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))

    def tearDown(self):
        self.step.browser.quit()


if __name__ == "__main__":
    unittest.main()
