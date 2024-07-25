import subprocess
import sys

def get_installed_packages():
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to get installed packages: {result.stderr}")
        return []

    packages = result.stdout.splitlines()
    formatted_packages = []

    for package in packages:
        # Split the package string by '==' and take the first part, which is the package name
        package_name = package.split('==')[0]
        formatted_packages.append(f'"{package_name}"')

    return formatted_packages

def main():
    packages = get_installed_packages()
    formatted_list = f"[{', '.join(packages)}]"
    print(formatted_list)

if __name__ == "__main__":
    main()
