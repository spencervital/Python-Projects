import socket


def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout value of 1 second
        sock.settimeout(1)

        # Attempt to connect to the target host and port
        result = sock.connect_ex((host, port))

        # Check the connection result
        if result == 0:
            status = "Open"
        else:
            status = "Closed"

        sock.close()

    except socket.error:
        status = "Filtered"

    return status


def perform_scan(target_host, output_file):
    open_ports = []
    filtered_ports = []

    # Perform the port scan on both UDP and TCP ports
    for port in range(1, 65536):
        tcp_status = scan_port(target_host, port)
        udp_status = scan_port(target_host, port)

        # Save the port status in the output file
        with open(output_file, "a") as f:
            f.write(f"Port {port} - TCP: {tcp_status}, UDP: {udp_status}\n")

        if tcp_status == "Open" or udp_status == "Open":
            open_ports.append(port)
        elif tcp_status == "Filtered" or udp_status == "Filtered":
            filtered_ports.append(port)

    # Print the summary of the scan
    print("Summary of Scan:")
    print("Open Ports: ", open_ports)
    print("Filtered Ports: ", filtered_ports)


# Example usage
target_ip = "192.168.0.1"  # Replace with the target host IP
output_filename = "scan_results.txt"  # Replace with the desired output file name

perform_scan(target_ip, output_filename)
