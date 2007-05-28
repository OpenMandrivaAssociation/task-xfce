Name:    task-xfce
Version: 2008
Release: %mkrel 3
Summary: Metapackage for the XFCE
Group:   Graphical desktop/Xfce
License: GPL

Source : %name.tar.bz2

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
Requires: gok
Requires: orca
Requires: rhythmbox
Requires: totem
Requires: epiphany
Requires: epiphany-extensions
Requires: gcalctool
Requires: pidgin
Requires: ekiga
Requires: tomboy
Requires: f-spot
Requires: evince
Requires: gftp
Requires: claws-mail
Requires: wengophone
Requires: tvtime
#Requires: abiword
#Requires: gnumeric
Requires: muine
Requires: brasero
Requires: gimp
Requires: gdm

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the XFCE Mandriva Desktop. XFCE plugins not include.

%prep
%setup -q -n task-xfce

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/etc/X11/xdg
cp -r xfce4/ %{buildroot}/etc/X11/xdg/

%post
VALUE=""

if [ -e "/etc/sysconfig/system" ];
then
        STYLE=`cat /etc/sysconfig/system | grep META_CLASS | awk -F= '{ print $2 }'`
        echo $STYLE

        if [ $STYLE == "download" ]; then
                VALUE="Ia Ora Free"
                sed -i "s/\(name=\"Net\/ThemeName.*value=\)\".*\"\/>/\1\"$VALUE\"\/>/" /etc/X11/xdg/xfce4/mcs_settings/gtk.xml
        elif [ $STYLE == "desktop" ]; then
                VALUE="Ia Ora Orange"
                sed -i "s/\(name=\"Net\/ThemeName.*value=\)\".*\"\/>/\1\"$VALUE\"\/>/" /etc/X11/xdg/xfce4/mcs_settings/gtk.xml
        elif [ $STYLE == "server" ]; then
                VALUE="Ia Ora Gray"
                sed -i "s/\(name=\"Net\/ThemeName.*value=\)\".*\"\/>/\1\"$VALUE\"\/>/" /etc/X11/xdg/xfce4/mcs_settings/gtk.xml
        fi
else
	echo "File not found..."
fi

%files
%{_sysconfdir}/X11/xdg/xfce4/*
