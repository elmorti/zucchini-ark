# Returns System.Object[] / Where each item is Microsoft.Management.Infrastructure.CimInstance
Get-CimInstance Win32_Process -Filter "name='ShooterGameServer.exe'" | ForEach-Object {
    $cmdline = $_.CommandLine
    $process = $_.ProcessId
    $items = $cmdline.Split(" ")
    
    $path = $items[0]
    $args = $items[1].Split("?")
    $mapname = $args[0]
    $description = $args[-3].Split("=")[1]
    $rconport = $args[3].Split("=")[1]
    
    $message = 
    "
    # BEGIN
    Path: $path
    ProcessID: $process
    Map: $mapname
    Description: $description
    RCON: $rconport
    Started: $_.CreationDate
    Memory: $_.WorkingSetSize
    # END
    "
    Write-Output $message
}