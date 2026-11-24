"""Keep a Windows PC and its screen awake until this window closes."""

import ctypes
import sys
import tkinter as tk
from tkinter import messagebox, ttk

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


def main():
    if sys.platform != "win32":
        raise SystemExit("Keep Awake requires Windows.")

    set_execution_state = ctypes.windll.kernel32.SetThreadExecutionState
    set_execution_state.argtypes = [ctypes.c_uint32]
    set_execution_state.restype = ctypes.c_uint32

    root = tk.Tk()
    root.withdraw()
    root.title("Keep Awake")
    root.resizable(False, False)

    if not set_execution_state(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED):
        messagebox.showerror("Keep Awake", "Windows rejected the keep-awake request.", parent=root)
        root.destroy()
        return

    try:
        panel = ttk.Frame(root, padding=24)
        panel.pack()
        ttk.Label(panel, text="Keeping your screen and PC awake.").pack(pady=(0, 14))
        ttk.Button(panel, text="Exit", command=root.destroy).pack()
        root.deiconify()
        root.mainloop()
    finally:
        set_execution_state(ES_CONTINUOUS)


if __name__ == "__main__":
    main()
