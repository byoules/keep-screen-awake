# Keep Awake for Windows

Keep Awake keeps your screen on and prevents Windows from sleeping due to inactivity while the app is open. Staying awake also prevents the normal transition from sleep to hibernation.

## Run the Python app

Save `keep_awake_simple_2026-11-24.py` in a folder and open PowerShell in that folder. With Python installed on Windows, run:

```powershell
py .\keep_awake_simple_2026-11-24.py
```

The app starts keeping the screen and PC awake as soon as the window opens. You can minimize it. Click **Exit** or close the window to return to normal Windows power behavior.

For long runs, leave your laptop plugged in, open, and unlocked. Manual sleep, lid-close actions, and battery protection can still take effect.

## Build a standalone EXE

Run these commands on Windows from the same folder:

```powershell
py -m pip install pyinstaller
py -m PyInstaller --onefile --windowed --name KeepAwake .\keep_awake_simple_2026-11-24.py
```

Double-click `dist\KeepAwake.exe` to launch the app. The executable bundles Python and opens without a console window.

## References

- [Windows keep-awake behavior](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate)
- [Windows sleep and hibernation timers](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/display--sleep--and-hibernate-idle-timers)
- [PyInstaller usage](https://pyinstaller.org/en/stable/usage.html)
