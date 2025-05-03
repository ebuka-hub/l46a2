import thinker as tk

window = tk.TK()

for i  in range(3):
    for j in range(3):
        frame = tk.frame(
            master = window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5,pady=5)
        label=tk.Label(master=frame, text=f"row {i}/ncolumn{j}")
        label.pack()

        window.mainloop()