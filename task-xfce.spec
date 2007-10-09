Name:    	task-xfce
Version: 	2008
Release: 	%mkrel 19
Summary: 	Metapackage for the Xfce desktop environment
Group:   	Graphical desktop/Xfce
License: 	GPL
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

# xfce stuff
Requires:	task-xfce-minimal

# non xfce stuff
Requires:	gok
Requires:	orca
Requires:	exaile
Requires:	totem
Requires:	mozilla-firefox
Requires:	gcalctool
Requires:	pidgin
Requires:	ekiga
Requires:	tomboy
Requires:	f-spot
Requires:	ristretto
Requires:	eog
Requires:	epdfview
Requires:	gftp
Requires:	claws-mail
Requires:	tvtime
Requires:	sound-juicer
Requires:	brasero
Requires:	gimp
Requires:	gdm
Requires:	liferea
Requires:	deluge
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
Requires:       xfce-appfinder
Requires:       xfce-artwork
Requires:       xfce-icon-theme
Requires:       xfce-mcs-manager
Requires:       xfce-mcs-plugins
Requires:       xfce-mixer
Requires:       xfce-panel
Requires:       xfce-session
Requires:       xfce-taskmanager
Requires:       xfce-utils
Requires:       xfmedia
Requires:       xfprint
Requires:       xfwm
Requires:       xfwm-themes

Provides:       xfce
Obsoletes:      xfce

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Xfce desktop environment.


%package plugins
Summary:	Metapackage for the Xfce panel plugins
Group:		Graphical desktop/Xfce
Requires:	task-xfce-minimal

# (tpg) please keep requires in alphabetical order

Requires:	xfce-battery-plugin
Requires:	xfce-cddrive-plugin
Requires:	xfce-cellmodem-plugin
Requires:	xfce-clipman-plugin
Requires:	xfce-cpu-freq-plugin
Requires:	xfce-cpugraph-plugin
Requires:	xfce-datetime-plugin
Requires:	xfce-dict-plugin
Requires:	xfce-diskperf-plugin
Requires:	xfce-eyes-plugin
Requires:	xfce-fsguard-plugin
Requires:	xfce-genmon-plugin
Requires:	xfce-mailwatch-plugin
Requires:	xfce-minicmd-plugin
Requires:	xfce-mount-plugin
Requires:	xfce-mpc-plugin
Requires:	xfce-netload-plugin
Requires:	xfce-notes-plugin
Requires:	xfce-places-plugin
Requires:	xfce-quicklauncher-plugin
Requires:	xfce-radio-plugin
Requires:	xfce-screenshooter-plugin
Requires:	xfce-sensors-plugin
Requires:	xfce-smartpm-plugin
Requires:	xfce-smartbookmark-plugin
Requires:	xfce-systemload-plugin
Requires:	xfce-time-out-plugin
Requires:	xfce-timer-plugin
Requires:	xfce-verve-plugin
Requires:	xfce-wavelan-plugin
Requires:	xfce-weather-plugin
Requires:	xfce-xfapplet-plugin
Requires:	xfce-xkb-plugin
Requires:	xfce-xmms-plugin

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
Requires:       xfce-dev-tools
Requires:	xfce-mcs-manager-devel
Requires:	xfce-panel-devel
Requires:	xfce-xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel
