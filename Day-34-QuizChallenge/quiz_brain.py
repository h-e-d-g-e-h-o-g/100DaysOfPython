import html
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

# Here, i am getting the question in a strange formatted way.
# We are getting html entities in the questions.
# Html entities are used to render those symbols as the text in a browser
# which are used as codes to give structure to the content that is called escaping html entities.
# To unescape the html entities, we need to import html module and use unescape() method of html module.
# unescape() method needs a parameter that it needs to unescape.