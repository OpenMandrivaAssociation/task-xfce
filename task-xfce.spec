Name:    	task-xfce
Version: 	2008.0
Release: 	%mkrel 3
Summary: 	Metapackage for the Xfce desktop environment
Group:   	Graphical desktop/Xfce
License: 	GPLv2+
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
Obsoletes:	task-xfce <= 2008-24

# xfce stuff
Requires:	task-xfce-minimal

# non xfce stuff
Requires:	brasero
Requires:	claws-mail
Requires:	catfish
Requires:	deluge
Requires:	ekiga
Requires:	epdfview
Requires:	exaile
Requires:	f-spot
Requires:	gdm
Requires:	filezilla
Requires:	gimp
Requires:	gok
Requires:	gtk-recordmydesktop
Requires:	liferea
Requires:	mozilla-firefox
%if %mdkver >= 2008100
%ifarch x86_64
Requires:	openoffice.org64-gtk
%else
Requires:	openoffice.org-gtk
%endif
%ifarch x86_64
Requires:	openoffice.org64
%else
Requires:	openoffice.org
%endif
%endif
Requires:	orca
Requires:	pidgin
Requires:	ristretto
Requires:	sound-juicer
Requires:	tomboy
Requires:	totem
Requires:	tvtime
Requires:	qalculate-gtk

# (tpg) some additional xfce software
Requires:	thunar-archive-plugin
Requires:	thunar-media-tags-plugin
Requires:	thunar-thumbnailers

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce Mandriva Desktop.

Xfce panel plugins can be found in %{name}-plugins.

%package minimal
Summary: 	Minimal dependencies needed for Xfce desktop
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
Obsoletes:	task-xfce-minimal <= 2008-24

# (tpg) please keep requires in alphabetical order

Requires:       exo
Requires:       mandriva-xfce-config
Requires:       mousepad
Requires:       notification-daemon-xfce
Requires:       orage
Requires:       squeeze
Requires:       terminal
Requires:       thunar
# (tpg) disable for now
#Conflicts:      xarchiver
Suggests:       xfburn
Requires:       xfdesktop
Requires:       xfce4-appfinder
Suggests:       xfce4-artwork
Suggests:       xfce4-icon-theme
Requires:       xfce4-mixer
Requires:       xfce4-panel
Requires:       xfce4-session
Requires:       xfce4-taskmanager
Requires:	xfce4-volstatus-icon
Requires:       xfce-mcs-manager
Requires:       xfce-mcs-plugins
Requires:       xfce-utils
Suggests:       xfmedia
Requires:       xfprint
Requires:       xfwm4
Suggests:       xfwm4-themes

Provides:       xfce
Obsoletes:      xfce

%description minimal
Xfce is a lightweight desktop environment for various *NIX systems.
Designed for productivity, it loads and executes applications fast,
while conserving system resources.

Xfce 4.4 embodies the traditional UNIX philosophy of modularity and
re-usability. It consists of a number of components that together
provide the full functionality of the desktop environment. They are
packaged separately and you can pick and choose from the available
packages to create the best personal working environment.

This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Xfce desktop environment.


%package plugins
Summary:	Metapackage for the Xfce panel plugins
Group:		Graphical desktop/Xfce
Requires:	task-xfce-minimal
Obsoletes:	task-xfce-plugins <= 2008-24

# (tpg) please keep requires in alphabetical order

Suggests:	xfce4-battery-plugin
Suggests:	xfce4-cddrive-plugin
Suggests:	xfce4-cellmodem-plugin
Suggests:	xfce4-clipman-plugin
Suggests:	xfce4-cpu-freq-plugin
Suggests:	xfce4-cpugraph-plugin
Suggests:	xfce4-datetime-plugin
Suggests:	xfce4-dict-plugin
Suggests:	xfce4-diskperf-plugin
Suggests:	xfce4-eyes-plugin
Suggests:	xfce4-fsguard-plugin
Suggests:	xfce4-genmon-plugin
Suggests:	xfce4-mailwatch-plugin
Suggests:	xfce4-minicmd-plugin
Suggests:	xfce4-mount-plugin
Suggests:	xfce4-mpc-plugin
Suggests:	xfce4-netload-plugin
Suggests:	xfce4-notes-plugin
Suggests:	xfce4-places-plugin
Suggests:	xfce4-quicklauncher-plugin
Suggests:	xfce4-radio-plugin
Suggests:	xfce4-rss-plugin
Suggests:	xfce4-screenshooter-plugin
Suggests:	xfce4-sensors-plugin
Suggests:	xfce4-smartpm-plugin
Suggests:	xfce4-smartbookmark-plugin
Suggests:	xfce4-systemload-plugin
Suggests:	xfce4-time-out-plugin
Suggests:	xfce4-timer-plugin
Suggests:	xfce4-verve-plugin
Suggests:	xfce4-wavelan-plugin
Suggests:	xfce4-weather-plugin
Suggests:       xfce4-websearch-plugin
Suggests:	xfce4-wmdock-plugin
Suggests:	xfce4-xfapplet-plugin
Suggests:	xfce4-xkb-plugin
Suggests:	xfce4-xmms-plugin

%description plugins
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce panel plugins.


%package devel
Summary:	Xfce development metapackage
Group:		Development/Other
Obsoletes:	task-xfce-devel <= 2008-24

# (tpg) xfce stuff, please keep in alphabetical order
Requires:	libxfcegui4-devel
Requires:	libxfce4mcs-devel
Requires:	libxfce4util-devel
Requires:	python-xfce
Requires:	thunar-devel
Requires:       xfce4-dev-tools
Requires:	xfce-mcs-manager-devel
Requires:	xfce4-panel-devel
Requires:	xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel
