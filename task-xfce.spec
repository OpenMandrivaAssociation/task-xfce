Name:    	task-xfce
Version: 	2008
Release: 	%mkrel 20
Summary: 	Metapackage for the Xfce desktop environment
Group:   	Graphical desktop/Xfce
License: 	GPLv2+
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
Requires:	gftp
Requires:	gimp
Requires:	gok
Requires:	gtk-recordmydesktop
Requires:	liferea
Requires:	mozilla-firefox
%if %mdkver >= 2008100
Requires:	openoffice.org-gtk
%else
Requires:	openoffice.org
%endif
Requires:	orca
Requires:	pidgin
Requires:	ristretto
Requires:	sound-juicer
Requires:	tomboy
Requires:	totem
Requires:	tvtime
Requires:	qalculate-gtk
Requires:	wengophone

# (tpg) some additional xfce software
Requires:	thunar-archive-plugin
Requires:	thunar-media-tags-plugin
Requires:	thunar-thumbnailers
Requires:	xfce-volstatus-icon

%description
This package is a meta-package, meaning that its purpose is to  contain
dependencies for running the Xfce Mandriva Desktop. 

Xfce panel plugins can be found in %{name}-plugins.

%package minimal
Summary: 	Minimal dependencies needed for Xfce desktop
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE

# (tpg) please keep requires in alphabetical order

Requires:       exo
Requires:       mandriva-xfce-config
Requires:       mousepad
Requires:       notification-daemon-xfce
Requires:       orage
Requires:       squeeze
Requires:       terminal
Requires:       thunar
Conflicts:      xarchiver
Requires:       xfburn
Requires:       xfdesktop
Requires:       xfce4-appfinder
Requires:       xfce-artwork
Requires:       xfce4-icon-theme
Requires:       xfce-mcs-manager
Requires:       xfce-mcs-plugins
Requires:       xfce4-mixer
Requires:       xfce4-panel
Requires:       xfce4-session
Requires:       xfce-taskmanager
Requires:       xfce-utils
Requires:       xfmedia
Requires:       xfprint
Requires:       xfwm4
Requires:       xfwm4-themes

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

# (tpg) please keep requires in alphabetical order

Requires:	xfce4-battery-plugin
Requires:	xfce4-cddrive-plugin
Requires:	xfce4-cellmodem-plugin
Requires:	xfce4-clipman-plugin
Requires:	xfce4-cpu-freq-plugin
Requires:	xfce4-cpugraph-plugin
Requires:	xfce4-datetime-plugin
Requires:	xfce4-dict-plugin
Requires:	xfce4-diskperf-plugin
Requires:	xfce4-eyes-plugin
Requires:	xfce4-fsguard-plugin
Requires:	xfce4-genmon-plugin
Requires:	xfce4-mailwatch-plugin
Requires:	xfce4-minicmd-plugin
Requires:	xfce4-mount-plugin
Requires:	xfce4-mpc-plugin
Requires:	xfce4-netload-plugin
Requires:	xfce4-notes-plugin
Requires:	xfce4-places-plugin
Requires:	xfce4-quicklauncher-plugin
Requires:	xfce4-radio-plugin
Requires:	xfce4-screenshooter-plugin
Requires:	xfce4-sensors-plugin
Requires:	xfce4-smartpm-plugin
Requires:	xfce4-smartbookmark-plugin
Requires:	xfce4-systemload-plugin
Requires:	xfce4-time-out-plugin
Requires:	xfce4-timer-plugin
Requires:	xfce4-verve-plugin
Requires:	xfce4-wavelan-plugin
Requires:	xfce4-weather-plugin
Requires:	xfce4-xfapplet-plugin
Requires:	xfce4-xkb-plugin
Requires:	xfce4-xmms-plugin

%description plugins
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce panel plugins.


%package devel
Summary:	Xfce development metapackage
Group:		Development/Other
Requires:	task-xfce-minimal

# (tpg) xfce stuff, please keep in alphabetical order
Requires:	libxfcegui4-devel
Requires:	libxfce4mcs-devel
Requires:	libxfce4util-devel
Requires:	python-xfce
Requires:	thunar-devel
Requires:       xfce4-dev-tools
Requires:	xfce-mcs-manager-devel
Requires:	xfce4-panel-devel
Requires:	xfce-xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel
