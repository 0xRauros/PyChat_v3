# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PyChat.py'],
             pathex=['/Users/lvoerman/Documents/directories/programmeren/python/PyChat_v3'],
             binaries=[],
             datas=[('images/*', 'images'), ('users.txt', '.')],
             hiddenimports=['tkinter', 'tkinter.ttk', 'ttkthemes', 'pycrypto'],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PyChat',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
app = BUNDLE(exe,
             name='PyChat.app',
             icon='icon.ico',
             bundle_identifier=None)
