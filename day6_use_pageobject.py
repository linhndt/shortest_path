import time
import unittest
from selenium import webdriver
from asker.landing_page import LandingPage as AskerLP
from explainer.landing_page import LandingPage as ExpertLP
from asker.home_page import Homepage as AskerHP
from explainer.home_page import Homepage as ExpertHP
from explainer.workspace import Workspace as ExpertWS
from asker.workspace import WorkSpace as AskerWS


class PostQuestion(unittest.TestCase):

    asker_driver = None
    expert_driver = None
    asker_url = "https://www.got-it.ai/solutions/excel-chat/"
    expert_url = "https://expert.excelchat.co"

    @classmethod
    def setUpClass(cls):
        driver1 = webdriver.Chrome(executable_path="./chromedriver")
        driver2 = webdriver.Chrome(executable_path="./chromedriver")
        cls.asker_driver = driver1
        cls.expert_driver = driver2

    def asker_login(self):
        self.asker_driver.get(self.asker_url)
        asker_po = AskerLP(self.asker_driver)
        asker_po.login_successfully("asker@gmail.com", "123")

    def expert_login(self):
        self.expert_driver.get(self.expert_url)
        expert_po = ExpertLP(self.expert_driver)
        expert_po.login("expert@gmail.com", "123")

    def test_post_question_no_file(self):
        self.asker_login()
        self.expert_login()

        # expert starts working
        expert_po = ExpertHP(self.expert_driver)
        expert_po.start_working()

        # asker posts question
        asker_po = AskerHP(self.asker_driver)
        asker_po.post_question_no_file()

        # expert claim question
        expert_ws = ExpertWS(self.expert_driver)
        expert_ws.claim_question("Sam")

        # is asker connected with expert
        asker_ws = AskerWS(self.asker_driver)
        asker_ws.is_at_workspace()

    @classmethod
    def tearDownClass(cls):
        cls.asker_driver.close()
        cls.expert_driver.close()


if __name__ == "__main__":
    unittest.main()
