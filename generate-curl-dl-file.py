#!/usr/bin/env python3

with open('packages.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(f'url="https://cran-archive.r-project.org/bin/macosx/el-capitan/contrib/3.6/{line}"')
        print(f'output="{line}"')
        print()
