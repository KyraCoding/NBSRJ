import tkinter as tk
from urllib.parse import urlparse, parse_qs
import os

root = tk.Tk()

height = 300
width = 600
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

root.title("NBSRJ")
root.configure(background="pink")
root.minsize(width, height)
root.maxsize(width, height)
root.geometry(f"{width}x{height}+{(scr_width - width) // 2}+{(scr_height - height) // 2}")


header = tk.Frame(root, bg="pink")
header.pack(fill="x")

title = tk.Label(
    header,
    text="NBSRJ",
    font=("Arial", 32, "bold"),
    bg="pink"
)

title.pack(pady=(20,0))

subtitle = tk.Label(
    root,
    text="No BS Roblox Joiner",
    font=("Arial", 14),
    bg="pink"
)
subtitle.pack()
outer = tk.Frame(root, bg="pink", padx=15, pady=15)
outer.pack(pady=20)

form = tk.Frame(outer, bg="pink")
form.pack()

entry = tk.Entry(form, width=40)
entry.grid(row=0, column=0, padx=(0,10), pady=10)

def join():
    link = entry.get()
    if (link.strip() == ""):
        label.config(text="Please enter a link.")
        label.config(fg="red")
        return
    url = urlparse(link)
    if ("roblox.com" not in url.netloc):
        label.config(text="Invalid URL. Please enter a Roblox link.")
        label.config(fg="red")
        return
    queries = parse_qs(url.query)
    if "code" in queries:
        code = queries["code"][0]
        uri = f"roblox://navigation/share_links?code={code}&type=Server"
        os.startfile(uri)
        label.config(text=f"Joining Roblox server with code: {code}")
        label.config(fg="green") 
    elif "privateServerLinkCode" in queries:
        code = queries["privateServerLinkCode"][0]
        uri = f"roblox://experiences/start?placeId=15532962292&privateServerLinkCode={code}"
        os.startfile(uri)
        label.config(text=f"Joining Roblox server with code: {code}")
        label.config(fg="green")  
    else:
        label.config(text="Invalid URL. No code found.")
        label.config(fg="red")
        return
join_button = tk.Button(form, text="Join", command=join)
join_button.grid(row=0, column=1, pady=10)
label = tk.Label(root, text="", bg="pink")
label.pack()



root.mainloop()
