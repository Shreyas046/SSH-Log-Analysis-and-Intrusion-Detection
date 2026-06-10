#!/usr/bin/env python3

import re
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import time


# -----------------------------
# LOG ANALYSIS FUNCTION
# -----------------------------
def analyze_logs(logfile_path):

    attack_patterns = {
        'Failed password': 'Authentication Failure',
        'Invalid user': 'Invalid Username Attempt',
        'Did not receive identification': 'Scanner / Bot Activity',
        'Connection closed': 'Unexpected Connection Closure',
        'Disconnected from': 'SSH Disconnection',
        'Accepted password': 'Successful Login'
    }

    ip_pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+|::1)'
    )

    intrusion_data = []

    with open(logfile_path, 'r', encoding='utf-8', errors='ignore') as logfile:

        for line in logfile:

            for keyword, attack_type in attack_patterns.items():

                if keyword in line:

                    ip_match = ip_pattern.search(line)

                    ip_address = (
                        ip_match.group(0)
                        if ip_match
                        else "Unknown"
                    )

                    timestamp = " ".join(
                        line.split()[:3]
                    )

                    intrusion_data.append({
                        "Timestamp": timestamp,
                        "IP Address": ip_address,
                        "Attack Type": attack_type,
                        "Raw Log Entry": line.strip()
                    })

    return intrusion_data


# -----------------------------
# SCANNING WINDOW
# -----------------------------
def show_scanning():

    scan_window = tk.Toplevel(root)

    scan_window.title("Scanning")
    scan_window.geometry("350x150")
    scan_window.resizable(False, False)

    label = tk.Label(
        scan_window,
        text="Scanning logs for intrusions...",
        font=("Helvetica", 12)
    )

    label.pack(pady=20)

    progress = ttk.Progressbar(
        scan_window,
        orient="horizontal",
        mode="indeterminate",
        length=250
    )

    progress.pack(pady=10)
    progress.start(10)

    scan_window.update()

    time.sleep(3)

    progress.stop()
    scan_window.destroy()


# -----------------------------
# MAIN SCAN FUNCTION
# -----------------------------
def scan_logs():

    folder_path = filedialog.askdirectory(
        title="Select Folder Containing auth.log"
    )

    if not folder_path:
        return

    logfile_path = os.path.join(
        folder_path,
        "auth.log"
    )

    if not os.path.exists(logfile_path):

        messagebox.showerror(
            "Error",
            "auth.log not found in selected folder."
        )

        return

    show_scanning()

    intrusion_data = analyze_logs(logfile_path)

    if intrusion_data:

        df = pd.DataFrame(intrusion_data)

        save_path = filedialog.asksaveasfilename(
            title="Save Report",
            defaultextension=".csv",
            filetypes=[
                ("CSV Files", "*.csv")
            ]
        )

        if save_path:

            df.to_csv(
                save_path,
                index=False
            )

            messagebox.showinfo(
                "Success",
                f"Intrusion report generated:\n\n{save_path}"
            )

    else:

        messagebox.showinfo(
            "Result",
            "No suspicious activity detected."
        )


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()

root.title(
    "SSH Intrusion Detection Tool"
)

root.geometry("650x400")
root.resizable(False, False)

root.configure(
    bg="#1e1e1e"
)

title = tk.Label(
    root,
    text="SSH Intrusion Detection",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=40)

description = tk.Label(
    root,
    text="Analyze Linux authentication logs and detect suspicious SSH activity.",
    font=("Helvetica", 11),
    bg="#1e1e1e",
    fg="#cccccc"
)

description.pack()

scan_button = tk.Button(
    root,
    text="Start Scan",
    command=lambda:
    threading.Thread(
        target=scan_logs
    ).start(),
    font=("Helvetica", 14, "bold"),
    bg="#00C853",
    fg="white",
    padx=20,
    pady=10
)

scan_button.pack(pady=40)

footer = tk.Label(
    root,
    text="SSH Log Analysis and Intrusion Detection System",
    font=("Helvetica", 9),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(
    side="bottom",
    pady=20
)

root.mainloop()