from pathlib import Path
import platform


def link(src, dest):
    if dest.exists():
        print(f"Skipping existing: {dest}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"Linking: {src} -> {dest}")
    dest.symlink_to(src)

def create_symlinks(desktop=False):
    home = Path.home()
    current_dir = Path.cwd()
    os_name = platform.system()
    desktop_config = current_dir / "desktop" / "config"

    if os_name == "Windows": # default is Desktop
        tgt = [
            (current_dir / "rime", home / "AppData" / "Roaming" / "Rime"),
        ]
        for t in tgt:
            link(t[0], t[1])

    elif os_name == "Linux": # default is non-Desktop
        if desktop:
            link(current_dir / "rime", home / ".local" / "share" / "fcitx5" / "rime")

    else:
        print(f"Unsupported OS: {os_name}")
        return


if __name__ == "__main__":
    create_symlinks()
    print("Rime setup completed!")
