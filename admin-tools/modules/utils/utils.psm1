#
# Config validation functions
#

function ValidateConfigFile($config_file_path) {
    Test-Path $config_file_path -PathType "Leaf"
}

function ReadConfigFile($config_file_path) {
    Get-Content -Raw -Path $config_file_path | ConvertFrom-Json -AsHashtable
}

#
# Process management
#
function GetARKProcesses() {
    $arkprocesses = @()
    Get-CimInstance Win32_Process -Filter "name='ShooterGameServer.exe'" | ForEach-Object {
        $arkprocess = @{}
        $arkprocess.Add("CommandLine",$_.CommandLine) # TODO(elmorti): See how to add the item from the process object
        $arkprocess.Add("ProcessId",$_.ProcessId)
        $items = $arkprocess.CommandLine.Split(" ")
        $arkprocess.Add("Path",$items[0])
        $arkprocess.Add("Args",$items[1].Split("?"))
        $arkprocess.Add("MapName",$arkprocess.Args[0])
        $arkprocess.Args | ForEach-Object { # TODO(elmorti): See switch or where-object
            if ($_.Contains("RCONPort")) {
                $arkprocess.Add("RCONPort",$_.Split("=")[1])
            }
            if ($_.Contains("SessionName")) {
                $arkprocess.Add("Description",$_.Split("=")[1])
            }
        }
        $arkprocesses += $arkprocess
    }
    Write-Output $arkprocesses
}

function GetARKProcessByMap($mapname) {
    GetARKProcesses | ForEach-Object {
        if ($_.MapName -eq $mapname) {
            Write-Output $_
        }
    }
}

function StopARKProcess($mapname, $dryrun) {
    $arkprocess = GetARKProcessByMap($mapname)
    Write-Host "Stopping ARK Server...." $arkprocess.ProcessId
    if ($dryrun) {
        Write-Host "Would stop"
    } else {
        Stop-Process -Id $arkprocess.ProcessId -PassThru
    }
}

function GetARKMapConfig($cluster_config, $name) {
    $cluster_config.ark_server_config | ForEach-Object {
        if ($_.map_name -eq $mapname) {
            Write-Output $_
        }
    }
}

function StartARKProcess($cluster_config, $mapname, $dryrun) {
    $ark_map_config = GetARKMapConfig($cluster_config, $mapname)

    $ark_args = $ark_map_config.map_name + "?Listen?bRawSockets"
    $ark_flags = ""
    $ark_map_config.arguments.keys | ForEach-Object  {
        $ark_args += "?"
        $ark_args += $_
        $ark_args += "="
        $ark_args += $ark_map_config.arguments.$_
    }

    $ark_map_config.flags.keys | ForEach-Object  {
        if($ark_map_config.flags.$_) {
            $ark_flags += " -"
            $ark_flags += $_
        }
    }

    $ark_map_config.events.keys | ForEach-Object  {

        if($ark_map_config.events.$_) {
            $ark_flags += " -ActiveEvent="
            $ark_flags += $_
        }
    }

    $ark_flags += " -clusterid=" + $cluster_config.cluster_name
    $opts = $ark_args + $ark_flags

    $cmdline = 
        $cluster_config.root_dir + "\" +
        $cluster_config.cluster_name + "\" +
        $ark_map_config.map_dir + "\ShooterGame\Binaries\Win64\ShooterGameServer.exe"

    if($dryrun) {
        $dryruncmd = ""
        $dryruncmd += "Start-Process"
        $dryruncmd += " -FilePath " 
        $dryruncmd += $cmdline
        $dryruncmd += " -ArgumentList " 
        $dryruncmd += """$opts"""
        $dryruncmd += " -PassThru"
        Write-Output $dryruncmd
    } else {
        Start-Process -FilePath $cmdline -ArgumentList $opts -PassThru
    }
}

#
# Update map functions
#

function UpdateARKMap($cluster_config, $mapname, $dryrun) {
    $mapfullpath = 
        $cluster_config.root_dir + "\" +
        $cluster_config.cluster_name + "\"
    $cluster_config.ark_server_config | ForEach-Object {
        if ($_.map_name -eq $mapname) {
            $mapfullpath += $_.map_dir
        }
    }
            
    $steam_args = @()
    $steam_args += "+login anonymous +force_install_dir"
    $steam_args += $mapfullpath
    $steam_args += "+app_update"
    $steam_args += $cluster_config.steamapp_id
    $steam_args += "+quit"

    if($dryrun) {
        Write-Host "Start-Process -FilePath" $cluster_config.steamcmd "-ArgumentList" """$steam_args"""
    } else {
        Start-Process -FilePath $cluster_config.steamcmd -ArgumentList $steam_args -PassThru | Wait-Process
    }
}

#
# RCON functions
#

# Refactor around, many things can be refactored like RCON commands...
function SendARKRCONCommand($mapname, $command) {
    $arkprocess = GetARKProcessByMap($mapname)
    $rconcli = "" # Path to rcon-cli.exe
    $argumentlist = @("--host localhost", "--password pass", "--port" + $arkprocess.RCONPort, $command)
    Start-Process -FilePath $rconcli -NoNewWindow -ArgumentList $argumentlist -PassThru | Wait-Process
}