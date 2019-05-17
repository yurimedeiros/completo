from cx_Freeze import setup, Executable
 
setup(name='Calculadora de Humanos.py',
    version='1.0',
    description='Esta Calculadora medira sua Massa Corporal, seus Dias, Horas, e Segundos vividos até Hoje.',
    options={'build_exe': {'packages': ['matplotlib']}},
executables = [Executable(
                   script='script.py',
                   base=None
                   icon='my-icon.ico'
                   )
                  ]
)
