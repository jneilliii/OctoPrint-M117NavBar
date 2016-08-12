$(function() {
    function M117NavBarViewModel(parameters) {
        var self = this;

		self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "M117NavBar") {
				// console.log('Ignoring '+plugin);
                return;
            }
			
			if(data.type == "popup") {
				// console.log(data.msg);
				$("#M117NavBar").text(data.msg);
			}
		}

    }

    // This is how our plugin registers itself with the application, by adding some configuration
    // information to the global variable OCTOPRINT_VIEWMODELS
    ADDITIONAL_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        M117NavBarViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request
        // here is the order in which the dependencies will be injected into your view model upon
        // instantiation via the parameters argument
        ["loginStateViewModel"],

        // Finally, this is the list of selectors for all elements we want this view model to be bound to.
        []
    ]);
});