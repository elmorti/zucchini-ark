Param(
    [CmdletBinding(
        PositionalBinding=$false
    )]

    # Param
    [Parameter(
        Mandatory=$true,
        HelpMessage="Mail to address"
    )]
    [String] $ToAddress,

    # Param
    [Parameter()]
    [string] $Username,
    
    # Param
    [Parameter()]
    [string] $Password,    # TODO: SecureString

    # Param
    [Parameter()]
    [switch] $DryRun
)

$Username = ""
$Password = ""

$message = new-object Net.Mail.MailMessage
#$message.IsBodyHtml = $true
$message.From = ""
$message.To.Add($ToAddress)
$date = Get-Date -Format "MMMM dd yyyy HH:mm K"
$message.Subject = "ARK Servers Report " + $date
$message.Body = Invoke-Expression .\zucchini_ark_get_servers.ps1
$smtp = New-Object Net.Mail.SmtpClient("", "") # TODO: Use config files pattern instead of hard coded
$smtp.EnableSSL = $true
$smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)
$smtp.Send($message)
Write-Host "Mail Sent"  
