Code Functionality
Modules Used:

re: Used for regular expression matching.
csv: Used for writing the output into a CSV file.
collections.defaultdict: Simplifies dictionary operations by providing default values for missing keys.
Functions: Each function performs a specific task:

1. count_requests_per_ip(file_path)
Purpose: Counts the total number of requests made by each IP address.
Logic:
Uses a regex pattern (ip_pattern) to extract valid IP addresses from each line of the log file.
Each extracted IP is counted using a defaultdict.
Output: A sorted list of tuples (IP Address, Request Count) in descending order of request counts.

2. most_frequent_endpoint(file_path)
Purpose: Identifies the most frequently accessed endpoint (e.g., /home, /api/data).
Logic:
Uses a regex pattern (endpoint_pattern) to extract endpoints (URLs) from HTTP request lines containing methods like GET, POST, etc.
Counts the occurrences of each endpoint using a defaultdict.
Finds the endpoint with the highest count.
Output: A tuple (Endpoint, Access Count).

3. count_failed_logins(file_path)
Purpose: Counts the number of failed login attempts from each IP address.
Logic:
Looks for error indicators like "401" or "Invalid credentials" in the log file.
Uses the IP regex (ip_pattern) to extract the IPs associated with failed logins.
Each failed attempt is counted using a defaultdict.
Output: A dictionary {IP Address: Failed Login Count}.
4. save_to_csv(requests_per_ip, most_accessed, failed_logins)

Purpose: Saves the analysis results into a CSV file named log_analysis_results.csv.
Logic:
Writes three sections:
Requests per IP with columns IP Address, Request Count.
Most Accessed Endpoint with columns Endpoint, Access Count.
Suspicious Activity with columns IP Address, Failed Login Count.

5. main()
Purpose: Serves as the entry point for the script. Coordinates the workflow:
Reads the log file.
Calls the above functions to analyze data.
Displays results in a formatted output on the terminal.
Saves the results to a CSV file.

Code Flow
Log Analysis Workflow:

Step 1: Count the number of requests per IP using count_requests_per_ip.
Step 2: Identify the most frequently accessed endpoint using most_frequent_endpoint.
Step 3: Count failed login attempts using count_failed_logins.
Output:

Prints a neatly formatted result for:
Requests per IP.
The most frequently accessed endpoint.
Failed login attempts.
Saves all results to log_analysis_results.csv.
CSV Output Structure:

Section 1: Requests per IP (IP Address, Request Count).
Section 2: Most Accessed Endpoint (Endpoint, Access Count).
Section 3: Suspicious Activity (IP Address, Failed Login Count).

Key Features
Regex Patterns:

Extract IP addresses: \b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b
Extract endpoints: "(?:GET|POST|PUT|DELETE|PATCH) (/[^ ]*)"
Sorting and Data Structures:

Uses defaultdict for efficient counting.
Sorts request counts for descending order output.
Error Handling:

The script assumes the log file exists and follows a consistent format.
If no endpoints are found, it handles this gracefully.

![Screenshot 2024-12-04 144153](https://github.com/user-attachments/assets/7d77dbb4-a92d-473f-bc23-190ef69e5c2a)

