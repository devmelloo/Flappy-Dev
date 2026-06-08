import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(
                   script="main.py", 
                   icon="bases/icon.ico",
                    target_name="Flappy Dev.exe"
                   ) ]
cx_Freeze.setup(
    name = "Flappy Dev",
    options={
        "build_exe":{
            "packages":["pygame", "pyttsx3", "pyttsx3.drivers", "pyttsx3.drivers.sapi5", "comtypes"],
            "include_files":["bases","recursos","log.dat"]
        }
    }, executables = executaveis
)
