import re
import csv
from collections import defaultdict

# Function to count total requests per IP
def count_requests_per_ip(file_path):
    request_counts = defaultdict(int)
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'  # Regex for IP addresses

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(ip_pattern, line)
            if match:
                ip_address = match.group(0)
                request_counts[ip_address] += 1

    # Sort by number of requests in descending order
    sorted_requests = sorted(request_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_requests

# Function to find the most frequently accessed endpoint
def most_frequent_endpoint(file_path):
    endpoint_counts = defaultdict(int)
    endpoint_pattern = r'"(?:GET|POST|PUT|DELETE|PATCH) (/[^ ]*)'  # Regex for endpoints

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(endpoint_pattern, line)
            if match:
                endpoint = match.group(1)
                endpoint_counts[endpoint] += 1

    # Find the endpoint with the highest count
    if endpoint_counts:
        most_accessed = max(endpoint_counts.items(), key=lambda x: x[1])
        return most_accessed
    else:
        return None, 0

# Function to save results to a CSV file
def save_to_csv(requests_per_ip, most_accessed, failed_logins):
    with open("log_analysis_results.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in requests_per_ip:
            writer.writerow([ip, count])
        writer.writerow([])

        # Write Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])
        writer.writerow([])

        # Write Suspicious Activity (Failed Logins)
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_logins.items():
            writer.writerow([ip, count])

# Function to count failed login attempts
def count_failed_logins(file_path):
    failed_attempts = defaultdict(int)
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'  # Regex for IP addresses

    with open(file_path, 'r') as file:
        for line in file:
            if "401" in line or "Invalid credentials" in line:
                match = re.search(ip_pattern, line)
                if match:
                    ip_address = match.group(0)
                    failed_attempts[ip_address] += 1

    return failed_attempts

# Main program
def main():
    log_file_path = "log_file.txt"  # Path to the log file

    # Total requests per IP
    requests_per_ip = count_requests_per_ip(log_file_path)
    print("Requests Per IP Address:")
    print(f"{'IP Address':<20} {'Request Count':<15}")
    print("-" * 40)
    for ip, count in requests_per_ip:
        print(f"{ip:<20} {count:<15}")
    print("\n")

    # Most frequently accessed endpoint
    most_accessed = most_frequent_endpoint(log_file_path)
    print("Most Frequently Accessed Endpoint:")
    print(f"{'Endpoint':<30} {'Access Count':<15}")
    print("-" * 45)
    if most_accessed[0]:
        print(f"{most_accessed[0]:<30} {most_accessed[1]:<15}")
    else:
        print("No endpoints found in the log file.")
    print("\n")

    # Failed login attempts
    failed_logins = count_failed_logins(log_file_path)
    print("Failed Login Attempts:")
    print(f"{'IP Address':<20} {'Failed Login Count':<15}")
    print("-" * 40)
    for ip, count in failed_logins.items():
        print(f"{ip:<20} {count:<15}")
    print("\n")


    # Save results to CSV
    save_to_csv(requests_per_ip, most_accessed, failed_logins)
    print("Results have been saved to 'log_analysis_results.csv'.")

if __name__ == "__main__":
    main()
