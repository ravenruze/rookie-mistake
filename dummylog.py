server_log = [
    "2026-02-21T10:00:01.123Z [INFO] systemd: Started Engine-X Web Server.",
    "2026-02-21T10:05:22.456Z [ERROR] auth-service: Invalid password for user 'ravenruze' from 192.168.1.45",
    "2026-02-21T10:10:05.789Z [INFO] kernel: TCP: eth0 link up, 1000Mbps, full duplex.",
    "2026-02-21T10:15:33.012Z [WARN] disk-monitor: Partition /var/log is 85% full.",
    "2026-02-21T10:20:44.345Z [ERROR] db-client: ConnectionLost: Failed to connect to database at 10.0.0.5:5432",
    "2026-02-21T10:25:12.678Z [INFO] cron-job: Backup-routine-daily started for /home/data.",
    "2026-02-21T10:26:01.910Z [ERROR] security-audit: Unauthorized access attempt detected on port 22 (SSH).",
    "2026-02-21T10:30:55.234Z [WARN] load-balancer: High latency detected on upstream Web-01.",
    "2026-02-21T10:35:10.567Z [INFO] update-manager: 14 packages successfully upgraded.",
    "2026-02-21T10:40:00.001Z [ERROR] python-runtime: Traceback (most recent call last): NameError: name 'shutil' is not defined"
]

active_servers = [
    {
        "name": "Web-Server-01",
        "status": "active",
        "ip": "192.168.10.101",
        "role": "frontend"
    },
    {
        "name": "DB-Primary-01",
        "status": "active",
        "ip": "192.168.10.201",
        "role": "database"
    },
    {
        "name": "Auth-Service-Node",
        "status": "maintenance",
        "ip": "192.168.10.150",
        "role": "api"
    },
    {
        "name": "Load-Balancer-01",
        "status": "active",
        "ip": "192.168.10.10",
        "role": "traffic-manager"
    },
    {
        "name": "Backup-Storage",
        "status": "offline",
        "ip": "192.168.10.250",
        "role": "storage"
    }
]

def log_counter():
    error = 0
    warn = 0
    info = 0
    for i in range(len(server_log)):
        if '[ERROR]' in server_log[i]:
            error += 1
        elif '[WARN]' in server_log[i]:
            warn += 1
        elif '[INFO]' in server_log[i]:
            info += 1
    print(f'ditemukan {error} ERROR, {warn} WARN, dan {info} INFO')

log_counter()