import Chat


class Topics:
    # this object holds the topics
    # display is simply a list that holds all topics for the meeting
    # history holds the entire list of topics, and is updated along with display
    # each meeting also has its own chat object
    def __init__(self):
        self.topicList = []
        self.display = ["\n"] * 5
        self.display[0] = "Topics"

    def __str__(self):
        return "\n".join(self.display)

    def get_display(self):
        return self.display

    def get_list(self):
        return self.topicList

    def get_chat(self, index):
        return self.topicList[index][3]

    def new_topic(self, title, time_estimate, description):
        self.topicList.append([title, time_estimate, description, Chat.Chat(title)])
        self.display.append(title + ": " + time_estimate + " minutes\n" + description)
        self.display.pop(1)
