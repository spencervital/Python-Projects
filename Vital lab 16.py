import socket


def scan_port(target_host, target_port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt
        sock.settimeout(1)

        # Attempt to connect to the target port
        result = sock.connect_ex((target_host, target_port))

        if result == 0:
            # Port is open
            return "Open"
        else:
            # Port is closed or filtered
            return "Closed/Filtered"

    except Exception as e:
        # Error occurred during the connection attempt
        return str(e)


def save_results(output_file, results):
    with open(output_file, 'w') as file:
        for port, status in results.items():
            file.write(f"Port {port} - {status}\n")


def perform_port_scan(target_host, output_file):
    open_ports = []
    filtered_ports = []
    results = {}

    for port in range(1, 65536):
        # Scan TCP ports
        result = scan_port(target_host, port)
        if result == "Open":
            open_ports.append(port)
        elif result == "Closed/Filtered":
            filtered_ports.append(port)

        # Store the result in the dictionary
        results[port] = result

    # Save results to the output file
    save_results(output_file, results)

    # Print summary to the screen
    print("Open Ports:")
    print(open_ports)
    print("Filtered Ports:")
    print(filtered_ports)


# Example usage
target_host = input("Enter the target host IP: ")
output_file = input("Enter the name of the output file: ")

perform_port_scan(target_host, output_file)
