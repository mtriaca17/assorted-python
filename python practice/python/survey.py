class AnonymousSurvey():
    """collects answers to questions"""
    
    def __init__(self, question):
        """store question, prepare responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the question"""
        print(self.question)
    
    def store_response(self, new_response):
        """add a response to the list"""
        self.responses.append(new_response)
    
    def show_results(self):
        """show all given responses"""
        print('Survey Results:')
        for response in self.responses:
            print(f'- {response}')

# my_survey = AnonymousSurvey('What language do u speak?')

# print('Enter q anytime to quit')
# while True:
#     response = input('Language: ')
#     if response == 'q':
#         break
#     my_survey.store_response(response)

# print('\nthanks for responses.')
# my_survey.show_results()

