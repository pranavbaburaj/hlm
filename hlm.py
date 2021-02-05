import click
import os
from clint.textui import colored as color
import requests

class Installer():
	def __init__(self, package):
		self.data = f"{package}.has"
		self.mod = os.path.join(os.getcwd(), "hlib_modules")

		self.folder_exists()
		self.install()

	def folder_exists(self):
		if not os.path.exists(self.mod):
			os.mkdir(self.mod)

	def install(self):
		print(color.green(f"INSTALLING:{self.data}"))
		url = f"https://raw.githubusercontent.com/hascal/hlm-libs/main/libs/{self.data}"
		if self.data not in os.listdir(self.mod):
			try:
				req = requests.get(url)
				if req.content == b'404: Not Found':
					print(color.red(f"Cannot find {self.data}"))
				else:
					self.write_file(req.content)
			except:
				print(color.red("An error occured"))
		else:
			print(color.red("File already exists"))

	def write_file(self,data):
		with open(os.path.join(self.mod, self.data), "wb") as file:
			file.write(data)

class Uninstall():
	def __init__(self, name):
		self.name = f"{name}.has"
		self.mod = os.path.join(os.getcwd(), "hlib_modules")

		self.final_path = os.path.join(self.mod, self.name)

		self.delete()

	def delete(self):
		if os.path.exists(self.final_path):
			os.remove(self.final_path)
		else:
			print(color.red(f"Cannot find {self.final_path}"))

@click.command()
@click.argument('command', type=str)
@click.argument('name', type=str)
def index(command, name):
    if command == "install":
    	i = Installer(name)
    elif command == "uninstall" or command == "remove":
    	u = Uninstall(name)


if __name__ == "__main__":
    index()