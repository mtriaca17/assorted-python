import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """survey and set of responses for all test methods"""
        self.my_survey = AnonymousSurvey('What language do u speak?')
        self.responses = ['english', 'filipino', 'german']


    def test_store_single_response(self):
        """test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test three responses"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()