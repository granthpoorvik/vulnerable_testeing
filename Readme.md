# User Vulnerability Detection and Blocking

This Python script analyzes user vulnerability based on a log file of user activity. It extracts information about user actions, their locations, and blocks users based on specified criteria.

## How it Works

### 1. Analyzing Vulnerability
The script uses regular expressions to extract user, action, and location information from each log entry. It counts the occurrences of "Blocked Site" actions for each user. The vulnerability of a user is determined based on a specified threshold (default is 2). Users with action counts equal to or greater than the threshold are considered vulnerable.
## 2. Blocking Users

The script supports blocking users based on their location. Users are blocked if they meet the vulnerability criteria (action count >= threshold) and their location is in the specified list of blocked locations.

## 3. Running the Script

To use the script:

1. Clone the repository: `git clone https://github.com/your-username/your-repository.git`
2. Navigate to the repository: `cd your-repository`
3. Install dependencies: `pip install matplotlib`
4. Run the script with your log file: `python analyze_vulnerability.py zscaler_logs.txt`

Replace `zscaler_logs.txt` with the path to your log file.

## 4. Configuration

Customize the script by modifying parameters in the `analyze_user_vulnerability` function:

- `threshold`: The threshold for determining user vulnerability (default is 2).
- `blocked_locations`: List of locations for blocking users.

## 5. Output

The script prints vulnerability status, visualizes user vulnerability using a bar chart, and outputs information about blocking users based on the specified criteria.

## 6. Blocking Mechanism

To implement the user blocking mechanism, you need to replace the comment `# Implement your blocking logic here, e.g., block_user(user)` with the actual code to block the user based on their location. The blocking mechanism may vary depending on the specifics of your application or system.

### 1. Log File Format

The log file should have entries in the following format:

```plaintext
User: <username> Action: <action> Location: <location>
