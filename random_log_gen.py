import time
import random

log_file_path = 'zescaler\\zscaler_logs.txt'

def generate_random_log_entry():
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    actions = ['Access Granted', 'Blocked Site', 'Access Denied']

    user = random.choice(users)
    action = random.choice(actions)

    return f'Timestamp: {time.strftime("%Y-%m-%d %H:%M:%S")} | User: {user} | Action: {action} | Bandwidth: {random.randint(100, 1000)}\n'

while True:
    with open(log_file_path, 'a') as file:
        log_entry = generate_random_log_entry()
        file.write(log_entry)

    time.sleep(1)
