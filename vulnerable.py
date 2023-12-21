import re
import matplotlib.pyplot as plt

def analyze_user_vulnerability(log_file_path, threshold=2, blocked_locations=['LocationA', 'LocationB']):
    # Define patterns for extracting relevant information
    user_pattern = re.compile(r'User: (\S+)')
    action_pattern = re.compile(r'Action: (\S+)')
    location_pattern = re.compile(r'Location: (\S+)')

    # Open the log file
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Initialize counters
    user_blocked_counts = {}
    user_locations = {}

    # Analyze each log entry
    for log in logs:
        user_match = user_pattern.search(log)
        action_match = action_pattern.search(log)
        location_match = location_pattern.search(log)

        if user_match and action_match:
            # Extract user, action, and location information from the log entry
            user = user_match.group(1)
            user=user.lower()
            action = action_match.group(1)
            location = location_match.group(1) if location_match else None

            # Count "Blocked Site" actions for each user
            if action.lower() == 'blocked':
                user_blocked_counts[user] = user_blocked_counts.get(user, 0) + 1
                user_locations[user] = location

    # Check if the dictionary is not empty
    if user_blocked_counts:
        # Determine user vulnerability based on the threshold
        vulnerable_users = [user for user, count in user_blocked_counts.items() if count >= threshold and user_locations.get(user) in blocked_locations]
        not_vulnerable_users = [user for user, count in user_blocked_counts.items() if count < threshold or user_locations.get(user) not in blocked_locations]

        # Print vulnerability status
        print("Vulnerable Users:", vulnerable_users)
        print("Not Vulnerable Users:", not_vulnerable_users)

        # Visualize user vulnerability
        users, counts = zip(*user_blocked_counts.items())

        # Set colors based on vulnerability
        colors = ['red' if user in vulnerable_users else 'blue' for user in users]

        plt.bar(range(len(users)), counts, align='center', alpha=0.7, color=colors)
        plt.xticks(range(len(users)), users)
        plt.ylabel('Number of Blocked Sites')
        plt.title('User Vulnerability Analysis')
        plt.show()

        # Block users based on location
        for user in vulnerable_users:
            # Implement your blocking logic here, e.g., block_user(user)
            print(f"Blocking user {user} from {user_locations[user]}")

    else:
        print("No log entries found or no 'Blocked Site' actions recorded.")

# Example usage
log_file_path = 'zescaler\\zscaler_logs.txt'
analyze_user_vulnerability(log_file_path)
