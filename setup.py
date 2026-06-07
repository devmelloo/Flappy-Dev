import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(
                   script="main.py", 
                   icon="bases/icon.png",
                    target_name="Flappy Dev.exe"
                   ) ]
cx_Freeze.setup(
    name = "Flappy Dev",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bases","recursos"]
        }
    }, executables = executaveis
)
