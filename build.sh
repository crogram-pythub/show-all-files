# _*_ coding:utf-8 _*_

pyinstaller\
    --clean\
    --noconfirm\
    -w\
    build.spec

# or shell
# pyinstaller -F -w --clean -y mac_show_all_files.py

# sign app
sudo codesign --force --deep --sign - ./dist/MacShowAllFiles.app
