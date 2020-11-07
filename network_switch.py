import typer
import subprocess
import shutil
from pathlib import Path

app = typer.Typer()

@app.command()
def wifi():
    subprocess.check_call(["sudo", "systemctl", "stop", "hostapd"])
    shutil.copy(Path("/home/pi/scripts/dhcpcd.conf.wifi"), Path("/etc/dhcpcd.conf"))
    shutil.copy(Path("/home/pi/scripts/dnsmasq.conf.wifi"), Path("/etc/dnsmasq.conf"))
    subprocess.check_call(["sudo", "systemctl", "restart", "dhcpcd"])
    subprocess.check_call(["sudo", "systemctl", "restart", "dnsmasq"])



@app.command()
def access_point():
    subprocess.check_call(["sudo", "systemctl", "start", "hostapd"])
    shutil.copy(Path("/home/pi/scripts/dhcpcd.conf.access"), Path("/etc/dhcpcd.conf"))
    shutil.copy(Path("/home/pi/scripts/dnsmasq.conf.access"), Path("/etc/dnsmasq.conf"))
    subprocess.check_call(["sudo", "systemctl", "restart", "dhcpcd"])
    subprocess.check_call(["sudo", "systemctl", "restart", "dnsmasq"])

if __name__ == "__main__":
    app()
