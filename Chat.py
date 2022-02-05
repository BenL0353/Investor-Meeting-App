class Chat:
    # this object holds the chat for the application
    # display works as a simple queue, and will always remove the first element as it appends a new one
    # history holds the entire chat, and is updated along with display
    history = []
    display = []

    def __init__(self, topic):
        self.display = [""] * 9
        self.display.append("Welcome to the " + topic + " chat.")

    def __str__(self):
        return "\n".join(self.display)

    def get_display(self):
        return self.display

    def get_history(self):
        return self.history

    def new_message(self, user, message):
        self.display.append(user + ": " + message)
        self.display.pop(0)
        self.history.append(user + ": " + message)
