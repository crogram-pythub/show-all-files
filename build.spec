# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

APP_NAME = '显示所有文件'
APP_APP = 'ShowAllFiles.app'
APP_VERSION = '0.0.2'
BUNDLE_IDENTIFIER = 'org.pythub.app.show_all_files'


a = Analysis(['src/showallfiles.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name=APP_NAME,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name=APP_NAME)
app = BUNDLE(coll,
            name=APP_APP,
            icon='resources/logo.icns',
            bundle_identifier=BUNDLE_IDENTIFIER,
            info_plist={
                'CFBundleName': APP_NAME,
                'CFBundleDisplayName': APP_NAME,
                'CFBundleExecutable': APP_NAME,
                'CFBundlePackageType': 'APPL',
                'CFBundleSupportedPlatforms': ['MacOSX'],
                'CFBundleGetInfoString': "Jackson Dou",
                'CFBundleIdentifier': BUNDLE_IDENTIFIER,
                'CFBundleVersion': APP_VERSION,
                'CFBundleInfoDictionaryVersion': APP_VERSION,
                'CFBundleShortVersionString': APP_VERSION,
                'NSHighResolutionCapable': True,
                'LSApplicationCategoryType': 'public.app-category.utilities',
                'NSHumanReadableCopyright': 'Copyright © 2020-2022 Jackson Dou, All Rights Reserved'
            })
