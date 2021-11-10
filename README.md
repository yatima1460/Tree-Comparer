# Tree Comparer

Tool to compare two directory trees

## Usage

```bash
python tree-comparer.py <reference-folder> <test-folder>
```

## Example output

```log
WARNING: File size mismatch C:\Source\ConfuserEx\.git\COMMIT_EDITMSG (16 bytes) and C:\Source\ConfuserEx - Copy\.git\COMMIT_EDITMSG (17 bytes)
WARNING: File hash mismatch "C:\Source\ConfuserEx\.git\config" (70038c476c4da7975e26ee6fd913ee667cd2dcb0) and "C:\Source\ConfuserEx - Copy\.git\config" (7c0ff80c38ecc512476ac7ca7afc6cd8bac9156d)
WARNING: File hash mismatch "C:\Source\ConfuserEx\.git\index" (c96a3d516a4e5943d3320f7041ec318bab1d7169) and "C:\Source\ConfuserEx - Copy\.git\index" (495165514f1600b68424915488d98677b0cdbbb0)
WARNING: File size mismatch C:\Source\ConfuserEx\.git\logs\HEAD (719 bytes) and C:\Source\ConfuserEx - Copy\.git\logs\HEAD (548 bytes)
WARNING: File size mismatch C:\Source\ConfuserEx\.git\logs\refs\heads\master (719 bytes) and C:\Source\ConfuserEx - Copy\.git\logs\refs\heads\master (548 bytes)
WARNING: File hash mismatch "C:\Source\ConfuserEx\.git\logs\refs\remotes\origin\HEAD" (4cf9a3e31e1d80d195e02b50e48bdf7f3dd91f90) and "C:\Source\ConfuserEx - Copy\.git\logs\refs\remotes\origin\HEAD" (1a6ab701d207ec4c83e24f1a92fcb86cef1e141a)
WARNING: File size mismatch C:\Source\ConfuserEx\.git\logs\refs\remotes\origin\master (157 bytes) and C:\Source\ConfuserEx - Copy\.git\logs\refs\remotes\origin\master (162 bytes)
ERROR: File does not exist "C:\Source\ConfuserEx\.git\objects\pack\pack-030914885e22a1452f3a2f9f42145796d4631ca7.idx" in "C:\Source\ConfuserEx - Copy\.git\objects\pack"
ERROR: File does not exist "C:\Source\ConfuserEx\.git\objects\pack\pack-030914885e22a1452f3a2f9f42145796d4631ca7.pack" in "C:\Source\ConfuserEx - Copy\.git\objects\pack"
ERROR: File does not exist "C:\Source\ConfuserEx\.git\objects\pack\pack-031555009f8533ca2cc65a7da7ca42dd98c01cfa.idx" in "C:\Source\ConfuserEx - Copy\.git\objects\pack"
ERROR: File does not exist "C:\Source\ConfuserEx\.git\objects\pack\pack-031555009f8533ca2cc65a7da7ca42dd98c01cfa.pack" in "C:\Source\ConfuserEx - Copy\.git\objects\pack"
ERROR: File does not exist "C:\Source\ConfuserEx\.git\ORIG_HEAD" in "C:\Source\ConfuserEx - Copy\.git"
WARNING: File hash mismatch "C:\Source\ConfuserEx\.git\refs\heads\master" (33822095e4b5436c68bdc1c246e84ba76105f3da) and "C:\Source\ConfuserEx - Copy\.git\refs\heads\master" (23b57e3a89a5a78ae8185afe418f4aff2f986869)
ERROR: Directory does not exist "C:\Source\ConfuserEx - Copy\.git\objects\35" in "C:\Source\ConfuserEx\.git\objects"
ERROR: Directory does not exist "C:\Source\ConfuserEx - Copy\.git\objects\61" in "C:\Source\ConfuserEx\.git\objects"
ERROR: Directory does not exist "C:\Source\ConfuserEx - Copy\.git\objects\a2" in "C:\Source\ConfuserEx\.git\objects"
ERROR: Directory does not exist "C:\Source\ConfuserEx - Copy\.git\objects\ac" in "C:\Source\ConfuserEx\.git\objects"
ERROR: Directory does not exist "C:\Source\ConfuserEx - Copy\.git\objects\e8" in "C:\Source\ConfuserEx\.git\objects"
ERROR: File does not exist "C:\Source\ConfuserEx - Copy\.git\objects\pack\pack-b31374097689293bf14eaeb0740f74f2b19c3c1b.idx" in "C:\Source\ConfuserEx\.git\objects\pack"
ERROR: File does not exist "C:\Source\ConfuserEx - Copy\.git\objects\pack\pack-b31374097689293bf14eaeb0740f74f2b19c3c1b.pack" in "C:\Source\ConfuserEx\.git\objects\pack"
```