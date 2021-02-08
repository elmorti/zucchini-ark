Param(
    [CmdletBinding(
        PositionalBinding=$false
    )]

    # ARK Cluster Config File
    [Parameter(
        Mandatory=$true,
        HelpMessage="Specify the JSON config for the ARK Cluster"
    )]
    [String] $ConfigFile,

    # Set for testing and not doing anything
    [Parameter()]
    [switch] $DryRun
)

function ReadConfigFile($config_file_path) {
    if (Test-Path $config_file_path -PathType "Leaf") {
        Get-Content -Raw -Path $config_file_path | ConvertFrom-Json -AsHashtable
    } else {
        Write-Error "Something happened reading config file"
    }
}

function CreateLink($source, $destination) {
    $cmdline_src = "New-Item -ItemType SymbolicLink -Path"
    $cmdline_tgt = "-Target "

    if($DryRun) {
        Write-Host $cmdline_src $destination $cmdline_tgt $source
    } else {
        $testpath = Test-Path -Path $destination
        if ($testpath) {
            Write-Error -Message "$destination already exists, do something about it."
            Exit
        }
        New-Item -ItemType SymbolicLink -Path $destination -Target $source
    }

   
}

function CreateDir($path) {
    $cmdline = "New-Item -ItemType Container -Path"

    if($DryRun) {
        Write-Host $cmdline $path
    } else {
        $testpath = Test-Path -Path $path
        if ($testpath) {
            Write-Error -Message "$path already exists, do something about it."
            Exit
        }
        New-Item -ItemType Container -Path $path
    }


}

function ProcessARK($ark_map_config, $cluster_dir) {
    $settings_dir = $cluster_dir + "\" + $ark_map_config.map_dir + "\" + "ShooterGame"
    $binary_dir = $settings_dir + "\" + "Binaries\Win64"

    # Set ARK Cluster global settings
    Write-Host "Creating the link to game cluster maps and config..."
    CreateLink $cluster_settings_dirname"\Saved"  $settings_dir"\Saved"

    # Install ArkAPI on map
    Write-Host "Installing ArkServerAPI plugin engine..."
    CreateDir $binary_dir"\ArkApi"
    CreateDir $binary_dir"\ArkApi\Plugins"
    CreateLink $cluster_settings_dirname"\ArkApi\ArkApi\Plugins\Permissions" $binary_dir"\ArkApi\Plugins\Permissions"
    $cluster_settings_dirname + "\" + $cluster_config.arkapi | Get-ChildItem | ForEach-Object -Process {
        if( !$_.PSIsContainer ) {
            $name = $_.Name
            CreateLink $_.FullName  $binary_dir"\"$name
        }
    }
    
    # Install cluster-wide plugins
    Write-Host "Installing ArkServerAPI cluster-wide plugins..."
    $cluster_settings_dirname + "\" + $cluster_config.cluster_arkapi_plugins | Get-ChildItem | ForEach-Object -Process {
        $name = $_.Name
        CreateLink $_.FullName  $binary_dir"\ArkApi\Plugins\"$name
    }

    # Install server-wide plugins
    Write-Host "Installing ArkServerAPI plugins for map" $ark_map_config.map_dir "..."
    $cluster_settings_dirname + "\" + $cluster_config.server_arkapi_plugins + "." + $ark_map_config.map_dir | Get-ChildItem | ForEach-Object -Process {
        $name = $_.Name
        CreateLink $_.FullName  $binary_dir"\ArkApi\Plugins\"$name
    }
}

$cluster_config = ReadConfigFile $ConfigFile

$cluster_settings_dirname =
    $cluster_config.root_dir + "\" +
    $cluster_config.cluster_name +"\" +
    $cluster_config.cluster_settings_dirname

$testpath = Test-Path -Path $cluster_settings_dirname -PathType "Container" 
if (-Not $testpath) {
    Write-Error -Message "Cannot read $cluster_settings_dirname as a directory"
    Exit
}

Write-Host "Setting cluster" $cluster_config.cluster_name
$cluster_config.ark_server_config | ForEach-Object -Process {
    $cluster_dir = $cluster_config.root_dir + "\" + $cluster_config.cluster_name
    ProcessARK $_ $cluster_dir
}