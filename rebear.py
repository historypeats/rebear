#!/usr/bin/python2.6
import os
import sys
from datetime import datetime
from subprocess import call
from Cocoa import *
from Foundation import *
from PyObjCTools import AppHelper


# Commands
imagesnap = '%s/imagesnap' % os.getcwd()
screenaver = '/System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app'
screensaver_action = 'open'


class AppDelegate(NSObject):
	def applicationDidFinishLaunching_(self, aNotification):
		NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, handler)


def get_filename():
	'''Return a filename with datetime format'''
	return datetime.now().isoformat() + '.jpg'


def handler(event):
	'''Event handler'''
	try:
		filename = get_filename()
		print '[+] GOTEM!'
		print '[+] Captured to file: %s' % filename

		# Take webcam pic
		call([imagesnap, '-q','-w', '1', filename])

		# Activate screensaver
		call([screensaver_action, screenaver])

		# Closeout
		AppHelper.stopEventLoop()
	except KeyboardInterrupt:
		AppHelper.stopEventLoop()


def banner():
	banner = ''' _____     ______     ______     ______     ______     ______    
/\  == \   /\  ___\   /\  == \   /\  ___\   /\  __ \   /\  == \   
\ \  __<   \ \  __\   \ \  __<   \ \  __\   \ \  __ \  \ \  __<   
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\ 
  \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/ 
                                                                  
Author: historypeats
	'''
	return banner


def main():
	''' Main '''
	print banner()
	print '[+] Starting rebear'

	# Init Global Event Listener
	app = NSApplication.sharedApplication()
	delegate = AppDelegate.alloc().init()
	NSApp().setDelegate_(delegate)
	AppHelper.runEventLoop()


if __name__ == '__main__':
	main()
