import os,glob
import logging
log_format="%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(
	filename='python_files_log.dat',
	filemode='w',
	level=logging.DEBUG,
	format=log_format
	)
l=logging.getLogger()
os.chdir('/home/susi/pgm/')

for file in glob.glob('*.py'):
	print(type(file))
	l.debug(file)
l.info("all done")

