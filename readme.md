# How to install

## Install python3.11
https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

And check the box "Add to PATH"

## Create your venv
`python -m venv .venv`

## Activate your venv
From a powershell :
`.\.venv\Scripts\Activate.ps1`

If you have an error about script execution not enabled, run an administrator powershell with this command : `Set-ExecutionPolicy RemoteSigned`

Then close and reopen a powershell to activate your venv with the previous command.

## Install the dependencies
`pip install -r requirements.txt`
