import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对 AnonymouseSurvey 类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        question = "Wath language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.stro_response("Englist")

        self.assertIn('Englist', my_survey.responses)

unittest.main()
