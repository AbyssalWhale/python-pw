param(
	[Parameter(Mandatory = $true, ValueFromPipeline = $true)][string] $path_ToProject,
	[Parameter(Mandatory = $true, ValueFromPipeline = $true)][string] $api_Key
)
$File_Path = "$($path_ToProject)\configs\"
$File_Name = "api_headers.json"
$Body = @"
{
  "key": "$($api_Key)"
}
"@

Write-Host "$($File_Path)$($File_Name)"

if (-not(Test-Path -Path "$($File_Path)$($File_Name)" -PathType Leaf)) {
	New-Item -Path "$($File_Path)" -Name "$($File_Name)" -ItemType "file" -Value "$($Body)"
}
else {
	Write-Host "Existed file has been updated. Path: $($File_Path)$($File_Name)"
	Set-Content -Path "$($File_Path)$($File_Name)" -Value "$($Body)"
}

