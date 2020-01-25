import psutil, socket
from datetime import datetime

def get_monitoring_data():
    """ Gets data structure for homepage """
    host_ip = _get_host_ip()
    return {
        'timestamp': datetime.now(),
        'cpu_load': psutil.cpu_percent(),
        'ip_addr': host_ip,
        'ip_addr_even_odd': _get_ip_even_odd(host_ip)
    }

def _get_host_ip() -> str:
    """ Gets IP address of host """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(('8.8.8.8', 1))
            return s.getsockname()[0]
        except:
            return '127.0.0.1'

def _get_ip_even_odd(ip_addr: str) -> str:
    """ Determine if number groups in IP address are even or odd """
    result = []
    groups = ip_addr.split('.')
    for value in groups:
        if (int(value) % 2) == 0:
            result.append('even')
        else:
            result.append('odd')

    return ".".join(result)
