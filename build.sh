# _*_ coding:utf-8 _*_

pyinstaller -D -w -y --noconfirm build.spec

# sign app
# sudo codesign --force --deep --sign - ./dist/ShowAllFiles.app
