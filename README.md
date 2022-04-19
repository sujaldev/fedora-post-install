# Fedora Post Install

Automating all the things I do after installing fedora with ansible.

# What does it do?

A checked box indicates this step has been implemented.

- [x] Update System
    - [x] Configure DNF
        - Set `installonly_limit` to 0
        - Add `max_parallel_downloads` with value as 20
        - Add `fastest_mirror` with value as True
    - [x] Update
- [x] Configure Boot
    - [x] Disable GRUB menu
    - [x] Disable boot splash screen (I have observed it reduces boot time by 3-4 seconds)
    - [x] Disable unnecessary services slowing down boot
        - `NetworkManager-wait-online.service`
- [ ] Disable Wayland and switch back to Xorg
- [ ] Install Fonts
    - FiraCode Nerd Font
- [ ] Install Applications
    - [ ] vim
    - [ ] sublime text
    - [ ] vscode
    - [ ] google-chrome
    - [ ] fira-code-fonts
    - [ ] starship
    - [ ] jetbrains tools
    - [ ] gnome-tweaks
    - [ ] gnome extensions
    - [ ] qbittorrent
    - [ ] vlc
- [ ] Personalize
    - [ ] Install [Colloid Theme](https://github.com/vinceliuice/Colloid-gtk-theme)
    - [ ] Install [Colloid Icons](https://github.com/vinceliuice/Colloid-icon-theme)
    - [ ] Customize Terminal
        - [ ] Install [Blue Matrix Theme](https://windowsterminalthemes.dev/?theme=Blue%20Matrix)
        - [ ] Set Padding
    - [ ] Setup shortcuts
    - [ ] Configure git
    - [ ] Set wallpaper
    - [ ] Set favourite apps in dock
