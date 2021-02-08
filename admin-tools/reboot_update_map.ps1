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

    # ARK Map Name if just one map
    [Parameter(
        Mandatory=$true
    )]
    [String] $MapName,

    # Set for testing and not doing anything
    [Parameter()]
    [switch] $DryRun
)

Import-Module -Name Z:\dev\zucchini-ark\modules\utils

$cluster_config = ReadConfigFile -config_file_path $ConfigFile

SendARKRCONCommand -mapname $MapName -command "Broadcast The server will be down for maintenance for 15 minutes..."
Start-Sleep -s 2
SendARKRCONCommand -mapname $MapName -command "Broadcast Saving world now and stopping the server in 15 seconds..."
SendARKRCONCommand -mapname $MapName -command "SaveWorld"
Start-Sleep -s 10
SendARKRCONCommand -mapname $MapName -command "Broadcast Stopping server in 5 seconds..."
Start-Sleep -s 5
StopARKProcess -mapname $MapName -dryrun $DryRun
UpdateARKMap -cluster_config $cluster_config -mapname $MapName -dryrun $DryRun
Start-Sleep -s 5
StartARKProcess -cluster_config $cluster_config -mapname $MapName -dryrun $DryRun

Remove-Module -Name utils