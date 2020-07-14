from mycroft import MycroftSkill, intent_file_handler


class RecappTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.recapp.intent')
    def handle_test_recapp(self, message):
        self.speak_dialog('test.recapp')


def create_skill():
    return RecappTest()

