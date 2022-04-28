Summary:	Metapackage for the xfce desktop environment
Name:		task-xfce
Version:	4.16
Release:	2
Epoch:		2
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		%{disturl}
BuildArch:	noarch

# (tpg) please keep requires in alphabetical order
Recommends:	eatmonkey
Recommends:	ristretto
Recommends:	thunar-archive-plugin
Recommends:	xfmpc
Recommends:	slim
Recommends:	gigolo
Recommends:	midori
Requires:	gnome-keyring
Recommends:	parole
Recommends:	xarchiver

Requires:	task-xfce-plugins
Requires:	task-xfce-minimal
Suggests:	thunar-archive-plugin
Suggests:	thunar-media-tags-plugin
Suggests:	thunar-shares-plugin
#Suggests:	thunar-svn-plugin
#Suggests:	thunar-vcs-plugin
Recommends:	thunar-thumbnailers
Recommends:	tumbler
Recommends:	xfburn
#Requires:	xfprint
#Suggests:	xfce4-artwork
Obsoletes:	xfce-trigger-launcher

Requires:	task-xfce-minimal
#Recommends:	xfce4-artwork

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
Requires:	xfce4-appfinder
%ifnarch %{ix86}
Requires:	thunar
Requires:	thunar-volman
%endif
#ifarch %{ix86}
#Recommends:	thunar
#Recommends:	thunar-volman
#endif
Suggests:	xfce4-icon-theme
Requires:	xfce4-pulseaudio-plugin
Requires:	virtual-notification-daemon
Requires:	xfce4-notifyd
Requires:	xfce4-panel
Requires:	xfce4-power-manager
Requires:	xfce4-session
Requires:	xfce4-taskmanager
Requires:	xfce4-settings
Requires:	xfce4-screenshooter
Requires:	xfconf
Requires:	xfdesktop
Requires:	xfwm4
Requires:	xfce4-whiskermenu-plugin

Recommends:	canberra-gtk3
Recommends:	adwaita-icon-theme
Recommends:	xfce4-pulseaudio-plugin
Recommends:	task-pulseaudio


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

Recommends:	xfce4-battery-plugin
Recommends:	xfce4-calculator-plugin
Recommends:	xfce4-clipman-plugin
Recommends:	xfce4-cpufreq-plugin
Recommends:	xfce4-cpugraph-plugin
Recommends:	xfce4-datetime-plugin
Recommends:	xfce4-diskperf-plugin
Recommends:	xfce4-embed-plugin
Recommends:	xfce4-equake-plugin
Recommends:	xfce4-eyes-plugin
Recommends:	xfce4-fsguard-plugin
Recommends:	xfce4-genmon-plugin
Recommends:	xfce4-hamster-plugin
Recommends:	xfce4-hotcorner-plugin
Recommends:	xfce4-kbdleds-plugin
Recommends:	xfce4-linelight-plugin
Recommends:	xfce4-mailwatch-plugin
Recommends:	xfce4-mount-plugin
Recommends:	xfce4-mpc-plugin
Recommends:	xfce4-netload-plugin
Recommends:	xfce4-places-plugin
Recommends:	xfce4-pulseaudio-plugin
Recommends:	xfce4-sensors-plugin
Recommends:	xfce4-smartbookmark-plugin
Recommends:	xfce4-statusnotifier-plugin
Recommends:	xfce4-systemload-plugin
Recommends:	xfce4-time-out-plugin
Recommends:	xfce4-timer-plugin
Recommends:	xfce4-verve-plugin
Recommends:	xfce4-wavelan-plugin
Recommends:	xfce4-weather-plugin
Recommends:	xfce4-whiskermenu-plugin
Recommends:	xfce4-xkb-plugin
Recommends:	xfce4-notes-plugin

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
