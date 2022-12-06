from os import system as cmd, listdir, path
from shutil import move as shtmove


# Visible part
name = 'ARROWS_to_WASD'
version = 'v1.0.0'

# Invisible part
py_filename = 'arrowstowasd.py'
upx_dir = 'upx'
icon = 'images/icon.ico'
data = 'dependencies/*;.'

# Preview of the final filename: "NAME_of_FILE-UpxON-v1.0.0.exe"
upx_status = 'UpxOFF'
cmd(f'pyinstaller --onefile --noconsole --icon={icon} --add-data={data} --name={name}-{upx_status}-{version} {py_filename}')
cmd(f'del {name}-{upx_status}-{version}.spec')
cmd('rmdir /s /q build')

upx_status = 'UpxON'
cmd(f'pyinstaller --onefile --noconsole --icon={icon} --add-data={data} --upx-dir={upx_dir} --name={name}-{upx_status}-{version} {py_filename}')
cmd(f'del {name}-{upx_status}-{version}.spec')
cmd('rmdir /s /q build')

# Move the compiled files into the releases folder
sourceFolder_distPyinstaller = 'dist'
targetFolder_releasesGithub = '.releases'

file_names = listdir(sourceFolder_distPyinstaller)

for filename in file_names:
    shtmove(path.join(sourceFolder_distPyinstaller, filename), targetFolder_releasesGithub)

# Delete "dist" folder
cmd('rmdir /s /q dist')


### Made with ❤️ by @Henrique-Coder (https://github.com/Henrique-Coder) ###
