# TODO: Use zucchini syncrclone tool
$ConfigFile = ""
$Source = ""
$Destination = ""

$rclone_args = @()
$rclone_args += "--config $ConfigFile"
$rclone_args += $Source
$rclone_args += $Destination

Start-Process -FilePath "" -ArgumentList "--config $ConfigFile sync $Source $Destination" -NoNewWindow # Needs rclone path