Name:    task-xfce
Version: 2007
Release: %mkrel 11
Summary: Metapackage for the XFCE
Group:   Graphical desktop/Xfce
License: GPL

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Provides: xfce
Obsoletes: xfce

Requires: exo
Requires: thunar
Requires: xfce-panel
Requires: xfce-utils
Requires: xfce-mcs-manager
Requires: xfce-mcs-plugins
Requires: libxfcegui4-plugins
Requires: xfprint
Requires: mousepad
Requires: notification-daemon
Requires: orage
Requires: terminal
Requires: thunar
Requires: xarchiver
Requires: xfburn
Requires: xfce
Requires: xfce4-artwork
Requires: xfce-panel
Requires: xfce4-artwork
Requires: xfce-appfinder
Requires: xfce-dev-tools
Requires: xfce-icon-theme
Requires: xfce-mcs-manager
Requires: xfce-mixer
Requires: xfce-session
Requires: xfce-taskmanager
Requires: xfdesktop
Requires: xfmedia
Requires: xfprint
Requires: xfwm
Requires: xfwm-themes
Requires: xfce-utils

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the XFCE. XFCE plugins not include.

%files


