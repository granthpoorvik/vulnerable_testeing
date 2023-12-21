import re
import matplotlib.pyplot as plt

def analyze_user_activity(log_file_path):
    # Define patterns for extracting relevant information
    user_pattern = re.compile(r'User: (\S+)')
    action_pattern = re.compile(r'Action: (\S+)')

    # Open the log file
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Initialize counters
    user_action_counts = {}

    # Analyze each log entry
    for log in logs:
        user_match = user_pattern.search(log)
        action_match = action_pattern.search(log)

        if user_match and action_match:
            # Extract user and action information from the log entry
            user = user_match.group(1)
            action = action_match.group(1)

            # Count actions for each user
            if user not in user_action_counts:
                user_action_counts[user] = {}
            user_action_counts[user][action] = user_action_counts[user].get(action, 0) + 1

    # Check if the dictionary is not empty
    if user_action_counts:
        # Visualize user activity
        users = list(user_action_counts.keys())
        actions = list(set(action for actions in user_action_counts.values() for action in actions))

        stacked_data = [[user_action_counts[user].get(action, 0) for user in users] for action in actions]

        plt.bar(users, stacked_data[0], label=actions[0], alpha=0.7)
        for i in range(1, len(actions)):
            plt.bar(users, stacked_data[i], bottom=[sum(stacked_data[j][k] for j in range(i)) for k in range(len(users))],
                    label=actions[i], alpha=0.7)

        plt.ylabel('Number of Actions')
        plt.title('User Activity Analysis')
        plt.legend(title='Actions', loc='upper right')
        plt.show()
    else:
        print("No log entries found.")

# Example usage
log_file_path = 'zescaler\\zscaler_logs.txt'
analyze_user_activity(log_file_path)
