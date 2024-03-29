import os
from decouple import config
from pathlib import Path

# Database Information # working with .env.
DB_USER = config('DB_USER')  
DB_PASS = config('DB_PASS')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

# Directory

#ROOT = Path(__file__).resolve().parent.parent
ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(ROOT)
PATH_CSV = os.path.join(ROOT, 'csv')
PATH_CSV = os.path.abspath(PATH_CSV)


ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(ROOT)

PATH_CSV = os.path.join(ROOT, 'csv')
PATH_DB = os.path.join(ROOT, 'db')
PATH_CLEARDATA = os.path.join(ROOT, 'clean_data')
PATH_LOGS = os.path.join(ROOT, 'logs')

# Scraping
PARAIRNOS_WEBSITE = ["parairnos.com"] # Site

ARGENPROP_WEBSITE = ["argenprop.com"] # Site

PARAIRNOS_PROVINCES = {"cordoba":"https://www.parairnos.com/alquileres-en-cordoba",
                       "buenos-aires":"https://www.parairnos.com/alquileres-en-buenos-aires",
                       "mendoza":"https://www.parairnos.com/alquileres-en-mendoza",
		       "mar-del-plata":"https://www.parairnos.com/alquileres-en-mar-del-plata",
		       "rosario":"https://www.parairnos.com/alquileres-en-rosario",
		       "bariloche":"https://www.parairnos.com/alquileres-en-bariloche",
		       "misiones":"https://www.parairnos.com/alquileres-en-misiones",
		       "salta":"https://www.parairnos.com/alquileres-en-salta",
		       "tucuman":"https://www.parairnos.com/alquileres-en-tucuman",
		       "corrientes":"https://www.parairnos.com/alquileres-en-corrientes"} # List of sub-sites

ARGENPROP_PROVINCES = {"cordoba":"https://www.argenprop.com/departamentos/alquiler-temporal/cordoba",
                         "mendoza":"https://www.argenprop.com/departamentos/alquiler-temporal/mendoza-arg",
                        "buenos-aires":"https://www.argenprop.com/departamentos/alquiler-temporal/buenos-aires",
			"mar-del-plata":"https://www.argenprop.com/departamentos/alquiler/mar-del-plata",
                        "rosario":"https://www.argenprop.com/departamentos/alquiler/rosario",
                        "bariloche":"https://www.argenprop.com/departamentos/alquiler/bariloche",
                        "misiones":"https://www.argenprop.com/departamentos/alquiler/misiones",
                        "salta":"https://www.argenprop.com/departamentos/alquiler/salta",
                       "tucuman":"https://www.argenprop.com/departamentos/alquiler/tucuman",
                       "corrientes":"https://www.argenprop.com/departamentos/alquiler/corrientes"}
                                        


# Loggers

LOG_TASKS = 'Tasks' # Name of logger
LOG_CFG = 'logging.conf' # Name of conf file
