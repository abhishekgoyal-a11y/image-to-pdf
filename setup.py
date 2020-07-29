import cx_Freeze
executables = [cx_Freeze.Executable("imagetopdf.py")]

cx_Freeze.setup(
    name="IMAGETOPDF",
    options={"build_exe": {"packages": ["tkinter", "PIL", 'time', 'img2pdf']}},
    executables=executables
)
