# Fedora Post Install

Automating all the things I do after installing fedora with ansible.

## Support

- Desktop Environment: GNOME
- Distribution: Fedora
    - [ ] versions 35+: not supported due to major changes in GNOME
    - [x] version 35: supported and tested
    - [x] versions below 35: untested

## How to run

- To run defaults
  ```shell
  curl https://raw.githubusercontent.com/sujaldev/fedora-post-install/main/run.sh | sh
  ```

- To pass extra arguments
  ```shell
  curl https://raw.githubusercontent.com/sujaldev/fedora-post-install/main/run.sh | sh -s "has_nvidia_gpu=True personalized=True"
  ```

# What does it do?

A checked box indicates this step has been implemented.

- [x] Preflight
    - [x] Configure DNF
        - Set `installonly_limit` to 0
        - Add `max_parallel_downloads` with value as 20
        - Add `fastest_mirror` with value as True
    - [x] Add RPM Fusion Repository
    - [x] Update System
    - [x] Enable Flathub repository
- [x] Configure Boot
    - [x] Disable GRUB menu
    - [x] Disable boot splash screen (I have observed it reduces boot time by 3-4 seconds)
    - [x] Disable unnecessary services slowing down boot
        - `NetworkManager-wait-online.service`
        - `wpa_supplicant.service`  # I don't use WiFi
    - [x] Masked Services
        - `lvm2-monitor.service`
        - `systemd-udev-settle.service`
- [x] Configure Graphics _(this step is skipped by default)_
    - [x] Disable Wayland and switch back to Xorg
    - [x] Install proprietary nvidia drivers
- [x] Install Fonts
    - FiraCode Nerd Font
- [x] Install Applications
    - [x] vim
    - [x] sublime text
    - [x] vscode
    - [x] google-chrome
    - [x] fira-code-fonts
    - [x] starship
    - [x] jetbrains toolbox
    - [x] gnome-tweaks
    - [x] gnome extensions
    - [x] qbittorrent
    - [x] vlc
    - [x] multimedia plugins
- [x] Install Extensions
    - [x] User Themes
    - [x] Gnome Email Notifications
    - [x] Tray Icons Reloaded
    - [x] Blur my shell
- [x] Personalize _(this step is skipped by default)_
    - [x] Enable minimize & maximize buttons
    - [x] Install [Colloid Theme](https://github.com/vinceliuice/Colloid-gtk-theme)
    - [x] Install [Colloid Icons](https://github.com/vinceliuice/Colloid-icon-theme)
    - [x] Customize Terminal
        - [x] Install [Blue Matrix Theme](https://windowsterminalthemes.dev/?theme=Blue%20Matrix)
        - [x] Set Padding
    - [x] Setup shortcuts
    - [x] Configure git
    - [x] Set wallpaper
    - [x] Set favourite apps in dock
