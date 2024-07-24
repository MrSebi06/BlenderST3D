# How to install
## Create your venv
`python -m venv .venv`

## Activate your venv
From a powershell :
`.\.venv\Scripts\Activate.ps1`

If you have an error about script execution not enabled, run an administrator powershell with this command : `Set-ExecutionPolicy RemoteSigned`

Then close and reopen a powershell to activate your venv with the previous command.

## Install the dependencies
`pip install -r requirements.txt`