from cx_Freeze import setup, Executable

setup(
    name = "Чек=хэш",
    version = "0.6",
    description = "Робертоус",
    executables = [Executable("FIle_to_Base64.py")], requires=['telegram']
    )