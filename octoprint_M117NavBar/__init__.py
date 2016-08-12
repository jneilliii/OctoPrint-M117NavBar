# coding=utf-8

import octoprint.plugin
import re

class M117NavBar(octoprint.plugin.AssetPlugin,octoprint.plugin.TemplatePlugin):
	def AlertM117(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode and cmd.startswith("M117"):
			self._plugin_manager.send_plugin_message(self._identifier, dict(type="popup", msg=re.sub(r'^M117\s?', '', cmd)))
			return
			
	def get_assets(self):
		return dict(js=["js/M117NavBar.js"])
		
	def get_version(self):
		return self._plugin_version
		
	##~~ Softwareupdate hook
	def get_update_information(self):
		return dict(
			M117NavBar=dict(
				displayName="M117NavBar",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-M117NavBar",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-M117NavBar/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "M117NavBar"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = M117NavBar()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.AlertM117,
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}