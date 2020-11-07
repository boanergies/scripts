import typer
import subprocess
import shutil
from pathlib import Path

app = typer.Typer()

@app.command()
def wifi():
    subprocess.check_call(["sudo", "systemctl", "stop", "hostapd"])
    shutil.copy(Path("~/scripts/dhcpcd.conf.wifi").home(), Path("/etc/dhpcd.conf"))
    shutil.copy(Path("~/scripts/dnsmasq.conf.wifi").home(), Path("/etc/dnsmasq.conf"))



@app.command()
def access_point():
    subprocess.check_call(["sudo", "systemctl", "start", "hostapd"])
    shutil.copy(Path("~/scripts/dhcpcd.conf.access").home(), Path("/etc/dhpcd.conf"))
    shutil.copy(Path("~/scripts/dnsmasq.conf.access").home(), Path("/etc/dnsmasq.conf"))

if __name__ == "__main__":
    app()
