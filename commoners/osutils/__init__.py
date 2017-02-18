import os


def files_by_extension(root, extensions):
	"""
	Returns a list of files that match the extensions given after crawling the root directory
	"""

	assert(os.path.isdir(root))

	file_list = []
	for roots, _, files in os.walk(root):
		for f in files:
			ext = os.path.splitext(f)[1][1:].strip().lower()
			if ext in extensions:
				file_list.append(os.path.join(roots, f))

	return file_list

def has_extension(filename, exts):
	exts = os.path.splitext(f)[1][1:].strip().lower()
	return ext in exts
