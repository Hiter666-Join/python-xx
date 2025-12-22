#!/usr/bin/env python3
"""
一键修复“包内绝对导入”导致的连环 ModuleNotFoundError
用法：
    python fix_abs_imports.py
"""
import re
import sys
from pathlib import Path

# 需要修复的包名列表（site-packages 里的目录名）
PKGS = ['models', 'quorum']        # 以后如果再出现新的，直接加到这里

# 需要被改成相对导入的子模块名（正则片段）
SUB_MODS = r'acl|base|project|quorum\.base|mail|util|thread|model|mongodb|validation|build|log|schemas'

def fix_package(pkg_dir: Path):
    for py_file in pkg_dir.rglob('*.py'):
        text = orig = py_file.read_text(encoding='utf-8')
        # 1. import xxx  -> from . import xxx
        text = re.sub(rf'^import\s+({SUB_MODS})\s*$',
                      r'from . import \1', text, flags=re.M)
        # 2. from xxx import yyy -> from .xxx import yyy
        text = re.sub(rf'^from\s+({SUB_MODS})\b',
                      r'from .\1', text, flags=re.M)
        if text != orig:
            py_file.write_text(text, encoding='utf-8')
            print(f'FIXED  {py_file.relative_to(pkg_dir.parent)}')

def main():
    # 找到当前解释器的 site-packages 目录
    sp = Path([p for p in sys.path if 'site-packages' in p][0])
    for name in PKGS:
        pkg = sp / name
        if pkg.is_dir():
            fix_package(pkg)
            print(f'✔  {name} 修复完成')
        else:
            print(f'⚠  {name} 未找到，跳过')

if __name__ == '__main__':
    main()
