from importlib.metadata import version
import pip

packages = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'tensorflow']

for package in packages:
    try:
        __import__(package) 
        print(f'{package} available on your computer.')
        print(version(package))
    except:
        pip.main(['install',package])
        print(f'{package} installed on your computer.')
        print(version(package))

