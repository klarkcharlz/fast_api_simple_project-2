from dotenv import dotenv_values


config = dotenv_values(".env")

TG_TOKEN = config['TG_TOKEN']
