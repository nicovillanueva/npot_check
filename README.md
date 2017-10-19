## Non power-of-two image finder

### Setup
- Python 3.5 or higher
- Pillow (`pip3 install pillow` or `pip3 install -r requirements.txt`)

### Running

    python3 npot.py --path target_path/ --extension png

### Options

- `--path`: Path to recursively check out. Defaults to `.`
- `--extension`: File extension to inspect. Defaults to `png`