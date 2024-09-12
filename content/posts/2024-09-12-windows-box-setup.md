title = "Ultimate Guide: How to Set Up a Windows PC from Scratch in 2024 (Step-by-Step)"
date = 2024-09-12T18:13:00+02:00
tags = [
  "windows",
  "configuration",
  "vm",
  "setup",
  "build",
  "winget",
  "rdpclip",
  "pc",
  "clean install",
  "productivity",
]
published = true
+++++

Over the past 3 years, I've used Windows for various things.

With that in mind, I have a common setup I perform when spinning up a new instance.

1. Winget
   - [GitHub - microsoft/winget-cli](https://github.com/microsoft/winget-cli)
   - WinGet is the Windows Package Manager for the CLI(command line interface).

2. [Windows Terminal](https://github.com/microsoft/terminal)
   - Enhance my terminal experience and allow me to use tabs.

3. [Clink](https://github.com/chrisant996/clink)
   - `winget install clink`
   - Makes the command prompt bearable.

4. [LazyGit](https://github.com/jesseduffield/lazygit)
   - `winget install -e --id=JesseDuffield.lazygit`
   - When I am annoying at my command line.

5. Visual Studio Code
   - `winget install -e --id Microsoft.VisualStudioCode`

6. Microsoft Power Toys
   - `winget install --scope machine Microsoft.PowerToys -s winget`

7. RDP Clip Restart Shortcut
	1. Right-click on an empty area of your desktop.
	2. Select New > Shortcut from the context menu.
	3. In the "Create Shortcut" window, enter the following command:

	`cmd /c taskkill /F /IM rdpclip.exe & start rdpclip.exe`

	4. Click "Next".
	5. Give your shortcut a name, such as "Restart RDPClip".
	6. Click "Finish".
	7. This will create a shortcut on your desktop. When you double-click this shortcut, it will:
		1. Force-close the existing rdpclip.exe process
		2. Start a new instance of rdpclip.exe

Enjoy!
