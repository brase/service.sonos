# -*- coding: utf-8 -*-

import sys
import os
import datetime
import re
import signal
import xbmc
import xbmcaddon

#get path to me
addon_id = 'service.sonos'
selfAddon = xbmcaddon.Addon(id=addon_id)
sonospath = selfAddon.getAddonInfo('path')

#append lib directory
sys.path.append( os.path.join( sonospath, 'resources', 'lib' ) )
from soco import SoCo

class MyPlayer(xbmc.Player):
	def __init__ (self):
		xbmc.Player.__init__( self )
		xbmc.log("SONOS: Player initialized")

	def onPlayBackStarted( self ):
		settings = selfAddon.getSetting
		player_ip = settings('SONOS_PLAYER_IP')

		switch_when_playing = settings('SWITCH_WHEN_PLAYING')
		set_volume = settings('SET_VOLUME')	
		sonos_volume = int(float(settings('SONOS_VOLUME')))
	
		xbmc.log("SONOS: Playback started")
		sonos = SoCo("%s" % player_ip)
		xbmc.log("SONOS: created soco with ip: %s" % player_ip)
		xbmc.log("SONOS: switched to line in: %s" % sonos.switch_to_line_in())
		xbmc.log("SONOS: play: %s" % sonos.play())

		if(set_volume):			
			sonos.volume(sonos_volume)
			xbmc.log("SONOS: set volume to %s" % sonos_volume)

player = MyPlayer()
xbmc.log("SONOS: Started and running.")

while(not xbmc.abortRequested):
    xbmc.sleep(100)
