import typer
import subprocess
import shutil
from pathlib import Path

app = typer.Typer()

@app.command()
def wifi():
    subprocess.check_call(["sudo", "systemctl", "stop", "hostapd"])
    shutil.copy(Path("~/scripts/dhcpcd.conf.wifi").expanduser(), Path("/etc/dhcpcd.conf"))
    shutil.copy(Path("~/scripts/dnsmasq.conf.wifi").expanduser(), Path("/etc/dnsmasq.conf"))
    subprocess.check_call(["sudo", "systemctl", "restart", "dhcpcd"])
    subprocess.check_call(["sudo", "systemctl", "restart", "dnsmasq"])



@app.command()
def access_point():
    subprocess.check_call(["sudo", "systemctl", "start", "hostapd"])
    shutil.copy(Path("~/scripts/dhcpcd.conf.access").expanduser(), Path("/etc/dhcpcd.conf"))
    shutil.copy(Path("~/scripts/dnsmasq.conf.access").expanduser(), Path("/etc/dnsmasq.conf"))
    subprocess.check_call(["sudo", "systemctl", "restart", "dhcpcd"])
    subprocess.check_call(["sudo", "systemctl", "restart", "dnsmasq"])

if __name__ == "__main__":
    app()
