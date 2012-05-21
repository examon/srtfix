#!/usr/bin/env python

# Copyright (C) 2012 exo <exo[at]tty[dot]sk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------
#
# DESCRIPTION:
#
# srtfix is a simple program which is able to fix missing
# "Subtitle number" in the .srt subtitles.
#
# The right format of .srt subtitles should be:
#
# 	1
# 	00:00:20,000 --> 00:00:24,400
#	Altocumulus clouds occur between six thousand
#
# Where "1" is the "Subtitle number".
# Missing "Subtitle number" causes problems for HW player, so they
# cannot sometimes correctly load subtitles.
#
# --------------------------------------------------------------------
#
# USAGE:
#
# 	$ python srtfix.py broken.srt fixed.srt
#
# for more help
#
#	$ python srtfix.py -h
# or
#	$ python srtfix.py --help

from sys import argv

EXIT_FAILURE = 1
EXIT_SUCCESS = 0

def error_bad_argv():
	print "Usage: srtfix.py INPUT OUTPUT"
	print "Try 'srtfix.py -h [--help] for more information."

def show_help():
	print "Usage: srtfix.py INPUT OUTPUT"
	print "INPUT - broken subtitles"
	print "OUTPUT - fixed subtitles"

def check_argv():
	if (len(argv) != 2 and len(argv) != 3):
		error_bad_argv()
		return EXIT_FAILURE
	elif (len(argv) == 2):
		if (argv[1] == "-h" or argv[1] == "--help"):
			show_help()
			return EXIT_FAILURE
		else:
			error_bad_argv()
			return EXIT_FAILURE
	else: return (argv[1], argv[2])	

def main():
	if (check_argv() == EXIT_FAILURE):
		return EXIT_FAILURE
	else:
		INPUT = check_argv()[0]
		OUTPUT = check_argv()[1]

	print "Trying to fix %s" % INPUT

	INPUT_fo = open(INPUT, "r")
	cnt = 1
	buff = []
	buff.append(cnt)
	buff.append("\r\n")
	cnt += 1

	# load broken subtitles from INPUT and fix them
	for line in INPUT_fo:
		if (line == "\r\n"):
			buff.append("\r\n")
			buff.append(cnt)
			cnt += 1
		buff.append(line)
	INPUT_fo.close()

	# save fixed subtitles to OUTPUT
	OUTPUT_fo = open(OUTPUT, "wb")
	for element in buff:
		OUTPUT_fo.write(str(element))
	OUTPUT_fo.close()

	print "%s has been fixed! Check out %s" % (INPUT, OUTPUT)	

if __name__ == "__main__":
	main()
