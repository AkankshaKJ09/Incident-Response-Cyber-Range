import tkinter as tk
from tkinter import scrolledtext
from attack_simulator import write_log
from detection_engine import detect_threats
from response_engine import respond
from forensic_module import get_logs
from report_generator import generate_report

# 🎨 Color Palette (clean + colorful)
BG = "#E6F0FF"
HEADER = "#4F46E5"
CARD = "#FFFFFF"
BTN = "#6366F1"
TEXT = "#1F2937"
ALERT = "#EF4444"
SUCCESS = "#10B981"

# -------- RESET --------
def reset():
    log_box.delete(1.0, tk.END)
    alert_box.delete(1.0, tk.END)
    response_box.delete(1.0, tk.END)

# -------- UPDATE SYSTEM --------
def update_system():
    alerts = detect_threats()
    actions = respond(alerts)

    alert_box.delete(1.0, tk.END)
    response_box.delete(1.0, tk.END)

    for a in alerts:
        alert_box.insert(tk.END, a + "\n")

    for act in actions:
        response_box.insert(tk.END, act + "\n")

# -------- BRUTE FORCE WINDOW --------
def brute_window():
    win = tk.Toplevel(root)
    win.title("Login Simulation")
    win.geometry("300x250")
    win.configure(bg="#F0F9FF")

    tk.Label(win, text="🔐 Login System", bg="#F0F9FF",
             font=("Segoe UI", 12, "bold")).pack(pady=10)

    tk.Entry(win).pack(pady=5)
    pwd = tk.Entry(win, show="*")
    pwd.pack(pady=5)

    attempts = {"count": 0}

    def login():
        attempts["count"] += 1
        msg = f"Login attempt {attempts['count']} (Wrong)"
        write_log("LOGIN_FAILED", msg)

        log_box.insert(tk.END, msg + "\n")
        log_box.see(tk.END)

        update_system()

    tk.Button(win, text="Login", bg="#6366F1", fg="white",
              command=login).pack(pady=10)

# -------- MALWARE WINDOW --------
def malware_window():
    win = tk.Toplevel(root)
    win.title("Malware Execution")
    win.geometry("300x200")
    win.configure(bg="#FFF7ED")

    tk.Label(win, text="⚠ Run suspicious file?", bg="#FFF7ED",
             font=("Segoe UI", 12, "bold")).pack(pady=20)

    def run():
        write_log("MALWARE_EXECUTION", "File executed")
        log_box.insert(tk.END, "⚠ Suspicious file executed\n")
        update_system()

    tk.Button(win, text="Run File", bg="red", fg="white",
              command=run).pack()

# -------- EXFIL WINDOW --------
def exfil_window():
    win = tk.Toplevel(root)
    win.title("Data Transfer")
    win.geometry("300x200")
    win.configure(bg="#ECFDF5")

    tk.Label(win, text="📡 Start Data Transfer?", bg="#ECFDF5",
             font=("Segoe UI", 12, "bold")).pack(pady=20)

    def start():
        for i in range(1, 6):
            msg = f"Sending chunk {i}"
            write_log("DATA_EXFILTRATION", msg)
            log_box.insert(tk.END, msg + "\n")

        update_system()

    tk.Button(win, text="Start Transfer", bg="#10B981", fg="white",
              command=start).pack()

# -------- REPORT --------
def show_report():
    logs = get_logs()
    alerts = detect_threats()
    actions = respond(alerts)

    report = generate_report(logs, alerts, actions)

    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, report)

# -------- MAIN WINDOW --------
root = tk.Tk()
root.title("Cyber Range Activity 2")
root.geometry("1150x720")
root.configure(bg=BG)

# -------- HEADER --------
header = tk.Frame(root, bg=HEADER, height=80)
header.pack(fill="x")

tk.Label(header, text="Cyber Range Activity 2",
         bg=HEADER, fg="white",
         font=("Segoe UI", 20, "bold")).pack(pady=5)

tk.Label(header, text="Incident Response Automation Cyber Range",
         bg=HEADER, fg="white",
         font=("Segoe UI", 10)).pack()

# -------- MAIN FRAME --------
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=10, pady=10)

# -------- ATTACK PANEL --------
attack_frame = tk.LabelFrame(main, text="🟥 Attack Simulation Panel",
                             bg=CARD, fg=TEXT,
                             font=("Segoe UI", 11, "bold"))
attack_frame.place(x=10, y=10, width=250, height=300)

tk.Button(attack_frame, text="Brute Force Attack",
          bg=BTN, fg="white", command=brute_window).pack(pady=10, fill="x")

tk.Button(attack_frame, text="Malware Attack",
          bg=BTN, fg="white", command=malware_window).pack(pady=10, fill="x")

tk.Button(attack_frame, text="Data Exfiltration",
          bg=BTN, fg="white", command=exfil_window).pack(pady=10, fill="x")

# -------- LOG PANEL --------
log_frame = tk.LabelFrame(main, text="📊 Live Logs & Activity",
                          bg=CARD, fg=TEXT,
                          font=("Segoe UI", 11, "bold"))
log_frame.place(x=270, y=10, width=860, height=350)

log_box = scrolledtext.ScrolledText(log_frame)
log_box.pack(fill="both", expand=True)

# -------- ALERT PANEL --------
alert_frame = tk.LabelFrame(main, text="🚨 Security Alerts",
                            bg="#FEE2E2", fg=ALERT,
                            font=("Segoe UI", 11, "bold"))
alert_frame.place(x=10, y=330, width=550, height=200)

alert_box = scrolledtext.ScrolledText(alert_frame)
alert_box.pack(fill="both", expand=True)

# -------- RESPONSE PANEL --------
response_frame = tk.LabelFrame(main, text="🛡️ Automated Response",
                               bg="#DCFCE7", fg=SUCCESS,
                               font=("Segoe UI", 11, "bold"))
response_frame.place(x=580, y=380, width=550, height=200)

response_box = scrolledtext.ScrolledText(response_frame)
response_box.pack(fill="both", expand=True)

# -------- REPORT BUTTON --------
tk.Button(root, text="📄 Generate Incident Report",
          bg="#111827", fg="white",
          font=("Segoe UI", 12, "bold"),
          command=show_report).pack(pady=10)

root.mainloop()