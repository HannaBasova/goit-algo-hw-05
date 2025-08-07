from decorators import input_error



@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def show_all_contacts(contacts):
    result = ''
    for name, phone in contacts.items():
        result = result + name + ' : ' + str(phone) + '\n'
    return result


@input_error
def phone_username(args,contacts: dict)-> str|None:
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "No such contact."




