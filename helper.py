def welcome(message):
    # new_member_id = message['new_chat_participant']['id']
    new_member_name = message['new_chat_participant']['first_name']
    grp = message['chat']['title']
    welcome_msg = "Hi {0} ,Welcome to {1}.Hope you enjoy your stay here.".format(new_member_name, grp)
    return welcome_msg


def farewell(message):
    # new_member_id = message['new_chat_participant']['id']
    member_name = message['left_chat_participant']['first_name']
    grp = message['chat']['title']
    msg = "Well,it seems {1} was not upto standards of {0}.".format(member_name, grp)
    return msg
