#
#
#
import PySimpleGUI as sg, Chat, Topics


def new_topic():  # this function is called when the user wants to make a new topic
    layout = [
        [sg.Text("Topic Name"), sg.InputText(key="TOPIC_NAME")],
        [sg.Text("Aprox Time (min)"), sg.InputText(key="TIME")],
        [sg.Text("Description"), sg.InputText(key="DESC")],
        [sg.Submit()]
    ]
    popup = sg.Window('New Topic', layout)
    event, values = popup.read()
    popup.close()
    return values["TOPIC_NAME"], values["TIME"], values["DESC"]


def change_topic(topics):  # this function is called when the user wants to change the topic
    layout = [[sg.Button("main")]]
    i = 0
    for topic in topics:
        layout.append([sg.Button(topic[0], key=i)])
        i += 1
    popup = sg.Window('New Topic', layout)
    event, values = popup.read()
    popup.close()
    return event


def main():
    sg.theme('DarkAmber')

    # initialization of classes
    main_chat = Chat.Chat("main")
    topics = Topics.Topics()
    user = 'admin'  # in future implementation, a user object would handle permissions as well as a username and password
    current_chat = main_chat

    # layout initialization
    layout = [
        [sg.Text(str(topics), key='TOPICS', size=(30, 10)), sg.Text(str(current_chat), key='CHAT', size=(50, 10))],
        [sg.Button("new topic", key="NEW_TOPIC", size=(30, 1)), sg.InputText(key='IN', size=(40, 1)), sg.Button('enter', key="ENTER", size=(10, 1))],
        [sg.Button("change topic", key="CHANGE_TOPIC", size=(30, 1))]
    ]

    window = sg.Window('Meeting', layout)
    while True:
        event, values = window.read()
        print(event, values)

        if event == 'ENTER':  # user entering a message
            current_chat.new_message(user, values["IN"])
            window['CHAT'].update(str(current_chat))
            window['IN'].update("")

        elif event == 'NEW_TOPIC':  # user entering a new topic
            name, time, desc = new_topic()
            topics.new_topic(name, time, desc)
            window["TOPICS"].update(str(topics))

        elif event == 'CHANGE_TOPIC':  # user changing which topic they are using
            new_chat = change_topic(topics.get_list())
            if new_chat == "main":
                current_chat = main_chat
            else:
                current_chat = topics.get_chat(int(new_chat))
            window['CHAT'].update(str(current_chat))

        elif event == sg.WIN_CLOSED:  # user closing the application
            break
    window.close()


if __name__ == '__main__':
    main()
