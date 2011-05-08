Summary:	Metapackage for the Xfce desktop environment
Name:		task-xfce
Version:	2011.0
Release:	%mkrel 2
Epoch:		1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		http://wiki.mandriva.com/en/XfceLive
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

# (tpg) please keep requires in alphabetical order
Suggests:	gdm
Suggests:	orage
Suggests:	gigolo
Suggests:	parole
#Suggests:	squeeze
Suggests:	xarchiver
Suggests:	ristretto
#Suggests:	task-xfce-plugins
Requires:	task-xfce-minimal
Suggests:	thunar-archive-plugin
#Suggests:	thunar-media-tags-plugin
#Suggests:	thunar-shares-plugin
#Suggests:	thunar-svn-plugin
#Suggests:	thunar-thumbnailers
Suggests:	tumbler
Suggests:	xfbib
Suggests:	xfburn
Suggests:	xfmpc
Requires:	xfprint
Suggests:	xfswitch-plugin
Suggests:	xfce4-artwork
Suggests:	xfce4-appfinder
Suggests:	xfce4-screenshooter
Obsoletes:	xfce-trigger-launcher

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce Mandriva Desktop.

Xfce panel plugins can be found in %{name}-plugins.

%package minimal
Summary:	Minimal dependencies needed for Xfce desktop
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive

# (tpg) please keep requires in alphabetical order

Requires:	exo
Requires:	mandriva-xfce-config
Requires:	mousepad
Requires:	terminal
Requires:	thunar
Requires:	thunar-volman
Suggests:	xfce4-icon-theme
Requires:	xfce4-mixer
Requires:	xfce4-panel
Requires:	xfce4-power-manager
Requires:	xfce4-session
Requires:	xfce4-taskmanager
#Requires:	xfce4-volstatus-icon
Requires:	xfce4-settings
Requires:	xfce-utils
Requires:	xfconf
Requires:	xfdesktop
Requires:	xfwm4

%if %mdkversion >= 200900
Suggests:	canberra-gtk
Suggests:	preload
Suggests:	readahead
%endif

Provides:	xfce
Obsoletes:	xfce < 4.5.91

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
Url:		http://wiki.mandriva.com/en/XfceLive
Requires:	task-xfce-minimal

# (tpg) please keep requires in alphabetical order

Suggests:	xfce4-battery-plugin
#Suggests:	xfce4-cddrive-plugin
#Suggests:	xfce4-cellmodem-plugin
#Suggests:	xfce4-clipman-plugin
Suggests:	xfce4-cpufreq-plugin
Suggests:	xfce4-cpugraph-plugin
#Suggests:	xfce4-datetime-plugin
#Suggests:	xfce4-dict-plugin
Suggests:	xfce4-diskperf-plugin
Suggests:	xfce4-eyes-plugin
Suggests:	xfce4-fsguard-plugin
Suggests:	xfce4-genmon-plugin
# disable this for now, due to strange dependancies
#Suggests:	xfce4-linelight-plugin
#Suggests:	xfce4-mailwatch-plugin
#Suggests:	xfce4-minicmd-plugin
#Suggests:	xfce4-mount-plugin
Suggests:	xfce4-mpc-plugin
Suggests:	xfce4-netload-plugin
#Suggests:	xfce4-notes-plugin
#Suggests:	xfce4-places-plugin
#Suggests:	xfce4-playercontrol-plugin
#Suggests:	xfce4-quicklauncher-plugin
Suggests:	xfce4-radio-plugin
#Suggests:	xfce4-rss-plugin
Suggests:	xfce4-sensors-plugin
#Suggests:	xfce4-smartpm-plugin
#Suggests:	xfce4-smartbookmark-plugin
Suggests:	xfce4-systemload-plugin
Suggests:	xfce4-time-out-plugin
#Suggests:	xfce4-timer-plugin
%if %mdkversion > 200900
Suggests:	xfce4-verve-plugin
%endif
Suggests:	xfce4-wavelan-plugin
Suggests:	xfce4-weather-plugin
#Suggests:	xfce4-websearch-plugin
Suggests:	xfce4-wmdock-plugin
#Suggests:	xfce4-xfapplet-plugin
Suggests:	xfce4-xkb-plugin

%description plugins
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce panel plugins.

%package devel
Summary:	Xfce development metapackage
Group:		Development/Other
Url:		http://wiki.mandriva.com/en/XfceLive

# (tpg) please keep requires in alphabetical order
Requires:	libxfcegui4-devel
Requires:	libxfce4ui-devel
Requires:	garcon-devel
#Requires:	libxfce4menu-devel
Requires:	libxfce4util-devel
Requires:	python-xfce
Requires:	thunar-devel
Requires:	xfce4-dev-tools
Requires:	xfce4-panel-devel
Requires:	xfconf-devel
Requires:	exo-devel
#Requires:	xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel
