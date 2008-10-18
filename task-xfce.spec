Name:    	task-xfce
Version: 	4.5.91
Release: 	%mkrel 0.2
Epoch:		1
Summary: 	Metapackage for the Xfce desktop environment
Group:   	Graphical desktop/Xfce
License: 	GPLv2+
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

# (tpg) please keep requires in alphabetical order

Suggests:       orage
Suggests:       squeeze
Suggests:	ristretto
Requires:	task-xfce-minimal
Suggests:	thunar-archive-plugin
Suggests:	thunar-media-tags-plugin
Suggests:	thunar-shares
Suggests:	thunar-svn-plugin
Suggests:	thunar-thumbnailers
Suggests:	xfbib
Suggests:       xfburn
Suggests:       xfmedia
Suggests:	xfmpc
Requires:       xfprint
Suggests:       xfce4-artwork
Suggests:       xfce4-appfinder

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce Mandriva Desktop.

Xfce panel plugins can be found in %{name}-plugins.

%package minimal
Summary: 	Minimal dependencies needed for Xfce desktop
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE

# (tpg) please keep requires in alphabetical order

Requires:       exo
Requires:	mandriva-xfce-config
Requires:       mousepad
Requires:       terminal
Requires:       thunar
Requires:       xfdesktop
Suggests:       xfce4-icon-theme
Requires:       xfce4-mixer
Requires:       xfce4-panel
Requires:       xfce4-session
Requires:       xfce4-taskmanager
Requires:	xfce4-volstatus-icon
Requires:       xfce4-settings
Requires:       xfce-utils
Requires:       xfwm4

Suggests:       aumix
%if %mdkversion >= 200900
Suggests:	canberra-gtk
Suggests:	preload
Suggests:	readahead
%endif

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

Suggests:	xfce4-battery-plugin
Suggests:	xfce4-cddrive-plugin
Suggests:	xfce4-cellmodem-plugin
Suggests:	xfce4-clipman-plugin
Suggests:	xfce4-cpufreq-plugin
Suggests:	xfce4-cpugraph-plugin
Suggests:	xfce4-datetime-plugin
Suggests:	xfce4-dict-plugin
Suggests:	xfce4-diskperf-plugin
Suggests:	xfce4-eyes-plugin
Suggests:	xfce4-fsguard-plugin
Suggests:	xfce4-genmon-plugin
Suggests:	xfce4-linelight-plugin
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

# (tpg) please keep requires in alphabetical order
Requires:	libxfcegui4-devel
Requires:	xfconf-devel
Requires:	libxfce4menu-devel
Requires:	libxfce4util-devel
Requires:	python-xfce
Requires:	thunar-devel
Requires:       xfce4-dev-tools
Requires:	xfce4-panel-devel
Requires:	xfc

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel
