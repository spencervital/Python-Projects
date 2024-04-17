import nmap

def scan_vulnerabilities(target_ip):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, arguments='-p-')  # Scan all ports

    for host in scanner.all_hosts():
        if 'tcp' in scanner[host]:
            for port in scanner[host]['tcp']:
                if scanner[host]['tcp'][port]['state'] == 'open':
                    print(f'Open port found: {port}')

# Example usage:
target_ip = '192.168.0.1'
scan_vulnerabilities(target_ip)
