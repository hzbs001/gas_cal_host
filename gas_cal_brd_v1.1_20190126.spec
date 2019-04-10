# -*- mode: python -*-

block_cipher = None


a = Analysis(['gas_cal_brd_v1.1_20190126.py'],
             pathex=['D:\\py\\gas_cal_20190126'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gas_cal_brd_v1.1_20190126',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
