YES_RESPONSE = 'y'
NO_RESPONSE = 'n'

def read(prompt=""):
    """Reads from user input with a prompt, strips, and lowers it"""

    return input(prompt).strip().lower()


def wait_for_yn(prompt):
    """Waits for a valid y/n response and then returns it"""

    done = False
    while not done:
        user_input = read(prompt + f" ({YES_RESPONSE}/{NO_RESPONSE}) ")
        done = (user_input == YES_RESPONSE) or (user_input == NO_RESPONSE)
    return user_input
