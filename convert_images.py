# convert images

from PIL import Image
from pillow_heif import register_heif_opener
import glob
import os
try:
	import config
except:
	print("You don't have a config.py. Go make one, based on config.example.py")
	exit()
import os

register_heif_opener()

def run():
	print(config.directory)
	for conv in config.conversions:
		if 'compress_tiff' in conv and 1 == conv['compress_tiff']:
			compress_tifs(config.directory)
		else:
			convert_files(config.directory,conv['src'],conv['dst'])

def convert_files(scan_dir,src_type,dst_type):
	print("converting "+src_type+" -> "+dst_type)
	files = glob.glob(scan_dir + "/*."+src_type)
	for f in files:
		print("next file: " +f)
		fname_base = os.path.basename(f)
		fname_split = fname_base.split('.')
		outfile = config.directory + '/' + fname_split[0]+'.'+dst_type
		if not os.path.isfile(outfile):
			try:
				img = Image.open(f)
			except:
				print("cannot open "+fname_base)
				continue
			
			print('creating '+outfile)
			try:
				if 'jpg' == dst_type:
					img.save(outfile, quality=100, optimize=True)
				else:
					img.save(outfile)
			except:
				print("can't create "+outfile)

		else:
			print(outfile+' already exists')

def compress_tifs(scan_dir,odir='compressed'):
	output_dir = scan_dir + '/' + odir
	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
	print('compressing tifs in '+scan_dir)
	extensions = ['tif','tiff','TIF','TIFF']

	compressions = ["jpeg", "tiff_lzw", "webp"]

	files = []
	for e in extensions:
		files = files + glob.glob(scan_dir + "/*."+e)

	files = list(set(files))

	for f in files:
		print("next file: " +f)
		fname_base = os.path.basename(f)
		fname_split = fname_base.split('.')
		for c in compressions:
			outfile = output_dir + '/' + fname_split[0]+'_' + c + '.tif'
			if not os.path.isfile(outfile):
				try:
					img = Image.open(f)
				except:
					print("cannot open "+fname_base)
					continue
				
				print('creating '+outfile)
				try:
					img.save(outfile, compression=c)
				except:
					print("can't create "+outfile)

run()