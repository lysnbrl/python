def greet(username):
    message = f"Hola, {username}"

    def display_message():
        print(message)

    return display_message

username = "Foxy"

response = greet(username)

username = "Mercks"

response()
