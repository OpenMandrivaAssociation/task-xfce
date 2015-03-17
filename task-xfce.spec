Summary:	Metapackage for the xfce desktop environment
Name:		task-xfce
Version:	2015.0
Release:	6
Epoch:		1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		%{disturl}
BuildArch:	noarch

# (tpg) please keep requires in alphabetical order
Suggests:	eatmonkey
Suggests:	slim
Suggests:	orage
Suggests:	gigolo
Suggests:	midori
Requires:	gnome-keyring
Suggests:	parole
#Suggests:	squeeze
Suggests:	xarchiver
Suggests:	ristretto
Requires:	task-xfce-plugins
Requires:	task-xfce-minimal
Suggests:	thunar-archive-plugin
Suggests:	thunar-media-tags-plugin
Suggests:	thunar-shares-plugin
#Suggests:	thunar-svn-plugin
#Suggests:	thunar-vcs-plugin
Suggests:	thunar-thumbnailers
Suggests:	tumbler
Suggests:	xfbib
Suggests:	xfburn
Suggests:	xfmpc
#Requires:	xfprint
#Suggests:	xfswitch-plugin
#Suggests:	xfce4-artwork
Suggests:	xfce4-appfinder
Suggests:	xfce4-screenshooter
Obsoletes:	xfce-trigger-launcher

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the xfce %{distribution} Desktop.

xfce panel plugins can be found in %{name}-plugins.

%package minimal
Summary:	Minimal dependencies needed for xfce desktop
Group:		Graphical desktop/Xfce
Url:		%{disturl}

# (tpg) please keep requires in alphabetical order

Requires:	exo
Requires:	distro-xfce-config-OpenMandriva
Requires:	mousepad
Requires:	xfce4-terminal
Requires:	thunar
Requires:	thunar-volman
Suggests:	xfce4-icon-theme
Requires:	xfce4-pulseaudio-plugin
Requires:	virtual-notification-daemon
Suggests:	xfce4-notifyd
Requires:	xfce4-panel
Requires:	xfce4-power-manager
Requires:	xfce4-session
Requires:	xfce4-taskmanager
Requires:	xfce4-settings
Requires:	xfce4-volumed
Requires:	xfconf
Requires:	xfdesktop
Requires:	xfwm4

Provides:	xfce = %{EVRD}

%description minimal
xfce is a lightweight desktop environment for various *NIX systems.
Designed for productivity, it loads and executes applications fast,
while conserving system resources.

xfce 4.4 embodies the traditional UNIX philosophy of modularity and
re-usability. It consists of a number of components that together
provide the full functionality of the desktop environment. They are
packaged separately and you can pick and choose from the available
packages to create the best personal working environment.

This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal xfce desktop environment.


%package plugins
Summary:	Metapackage for the xfce panel plugins
Group:		Graphical desktop/Xfce
Url:		%{disturl}
Requires:	task-xfce-minimal

# (tpg) please keep requires in alphabetical order

Suggests:	xfce4-battery-plugin
#Suggests:	xfce4-cddrive-plugin
Suggests:	xfce4-cellmodem-plugin
Suggests:	xfce4-clipman-plugin
Suggests:	xfce4-cpufreq-plugin
Suggests:	xfce4-cpugraph-plugin
Suggests:	xfce4-datetime-plugin
Suggests:	xfce4-dict-plugin
Suggests:	xfce4-diskperf-plugin
#Suggests:	xfce4-embed-plugin
Suggests:	xfce4-eyes-plugin
Suggests:	xfce4-fsguard-plugin
Suggests:	xfce4-genmon-plugin
#Suggests:	xfce4-indicator-plugin
#Suggests:	xfce4-linelight-plugin
Suggests:	xfce4-modemlights-plugin
#Suggests:	xfce4-mailwatch-plugin
#Suggests:	xfce4-minicmd-plugin
Suggests:	xfce4-mount-plugin
Suggests:	xfce4-mpc-plugin
Suggests:	xfce4-netload-plugin
Suggests:	xfce4-notes-plugin
Suggests:	xfce4-places-plugin
#Suggests:	xfce4-playercontrol-plugin
Suggests:	xfce4-quicklauncher-plugin
Suggests:	xfce4-radio-plugin
#Suggests:	xfce4-rss-plugin
Suggests:	xfce4-screenshooter-plugin
Suggests:	xfce4-sensors-plugin
Suggests:	xfce4-smartbookmark-plugin
Suggests:	xfce4-smartpm-plugin
Suggests:	xfce4-systemload-plugin
Suggests:	xfce4-time-out-plugin
Suggests:	xfce4-timer-plugin
Suggests:	xfce4-verve-plugin
Suggests:	xfce4-wavelan-plugin
Suggests:	xfce4-weather-plugin
#Suggests:	xfce4-websearch-plugin
Suggests:	xfce4-wmdock-plugin
#Suggests:	xfce4-xfapplet-plugin
Suggests:	xfce4-xkb-plugin
# requires gdm
#Suggests:	xfswitch-plugin

%description plugins
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the xfce panel plugins.

%package devel
Summary:	xfce development metapackage
Group:		Development/Other
Url:		%{disturl}

# (tpg) please keep requires in alphabetical order
#Requires:	libxfcegui4-devel
Requires:	libxfce4ui-devel
Requires:	libgarcon-devel
#Requires:	libxfce4menu-devel
Requires:	libxfce4util-devel
#Requires:	python-xfce
Requires:	thunar-devel
Requires:	xfce4-dev-tools
Requires:	xfce4-panel-devel
Requires:	xfconf-devel
Requires:	exo-devel
#Requires:	xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for xfce development environment.

%files

%files minimal

%files plugins

%files devel
