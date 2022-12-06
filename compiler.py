import fileinput
from os import system as cmd, listdir, path
from shutil import move as shtmove
import hashlib


# Visible part
name = 'ARROWS_to_WASD'
version = 'v1.0.0'

# Invisible part
py_filename = 'arrowstowasd.py'
upx_dir = 'upx'
icon = 'images/icon.ico'
data = 'dependencies/*;.'


# Calculating hashes
def calculate_checksums(filename):
    with open('dist/' + filename, 'rb') as f:
        bytes = f.read()
        md5 = 'MD5: ' + hashlib.md5(bytes).hexdigest()
        sha1 = 'SHA1: ' + hashlib.sha1(bytes).hexdigest()
        sha224 = 'SHA224: ' + hashlib.sha224(bytes).hexdigest()
        sha256 = 'SHA256: ' + hashlib.sha256(bytes).hexdigest()
        sha512 = 'SHA512: ' + hashlib.sha512(bytes).hexdigest()

    with open('.releases/Checksums-' + filename.rsplit('.', 1)[0] + '.txt', 'w') as f:
        f.write('Filename: ' + filename + '\n\n' + md5 + '\n' + sha1 + '\n' + sha224 + '\n' + sha256 + '\n' + sha512 + '\n')

# Preview of the final filename: "NAME_of_FILE-UpxON-v1.0.0.exe"
upx_status = 'UpxOFF'
cmd(f'pyinstaller --onefile --noconsole --icon={icon} --add-data={data} --name={name}-{upx_status}-{version} {py_filename}')
cmd(f'del {name}-{upx_status}-{version}.spec')
cmd('rmdir /s /q build')
calculate_checksums(f'{name}-{upx_status}-{version}.exe')

upx_status = 'UpxON'
cmd(f'pyinstaller --onefile --noconsole --icon={icon} --add-data={data} --upx-dir={upx_dir} --name={name}-{upx_status}-{version} {py_filename}')
cmd(f'del {name}-{upx_status}-{version}.spec')
cmd('rmdir /s /q build')
calculate_checksums(f'{name}-{upx_status}-{version}.exe')

# Move the compiled files into the releases folder
sourceFolder_distPyinstaller = 'dist'
targetFolder_releasesGithub = '.releases'

file_names = listdir(sourceFolder_distPyinstaller)

for filename in file_names:
    shtmove(path.join(sourceFolder_distPyinstaller, filename), targetFolder_releasesGithub)

# Delete "dist" folder
cmd('rmdir /s /q dist')


### Made with ❤️ by @Henrique-Coder (https://github.com/Henrique-Coder) ###
