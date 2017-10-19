from PIL import Image
import argparse
import glob

args = argparse.ArgumentParser()
args.add_argument('--path', '-p', type=str, default='.', help='Where to look (default: \'.\')')
args.add_argument('--extension', '-e', type=str, default='png', help='Extension to look for (default: png)')
args = args.parse_args()


def main():
    target = '{}/**/*.{}'.format(args.path, args.extension)
    print('Globbing: {}'.format(target))
    for filename in glob.glob(target, recursive=True):
        print('Checking out: {}'.format(filename))
        try:
            img = Image.open(filename)
        except OSError:
            print('Could not load file {}. Skipping.'.format(filename))
            continue
        wid, hei = img.size
        if wid != hei:
            print('{} has different sizes (wid: {}, hei: {})'.format(filename, wid, hei))
            continue
        if not (((wid & (wid - 1)) == 0) and wid != 0):
            print('{} dimensions are not a power of 2 (wid/hei: {})'.format(filename, wid))
            continue
        print('{} is alright'.format(filename))


if __name__ == '__main__':
    main()
