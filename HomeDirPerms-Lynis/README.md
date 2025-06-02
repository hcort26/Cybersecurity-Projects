# Home Directory Permissions Checker

This project includes two Bash scripts designed to check and optionally fix insecure permissions on user home directories. It’s aimed at enhancing system security by ensuring that only the directory owner can access its contents.

## 📂 Project Files
- `check_home_dir_perms.sh`: Scans home directories and reports insecure permissions.
- `fix_home_dir_perms.sh`: Scans home directories, lists vulnerable ones, and offers the option to fix them.

## 🔑 Key Features
- **Permission Scanning**: Checks permissions on `/Users/*` directories to identify insecure settings.
- **Owner Identification**: Reports the owner of each directory for additional insight.
- **Fix Option**: Provides an option to automatically apply secure permissions (`chmod 700`) to vulnerable directories.
- **Cross-Compatibility**: Designed for macOS systems using `stat -f "%Sp"` and `stat -f "%Su"`.
