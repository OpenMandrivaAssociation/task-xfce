Name:    	task-xfce
Version: 	2008
Release: 	%mkrel 11
Summary: 	Metapackage for the Xfce desktop environment.
Group:   	Graphical desktop/Xfce
License: 	GPL
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
Source0: 	%{name}.tar.bz2
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

# xfce stuff
Requires:	task-xfce-minimal

# non xfce stuff
Requires:	gok
Requires:	orca
Requires:	rhythmbox
Requires:	totem
Requires:	epiphany
Requires:	epiphany-extensions
Requires:	gcalctool
Requires:	pidgin
Requires:	ekiga
Requires:	tomboy
Requires:	f-spot
Requires:	eog
Requires:	evince
Requires:	gftp
Requires:	claws-mail
Requires:	tvtime
Requires:	sound-juicer
Requires:	brasero
Requires:	gimp
Requires:	gdm
Requires:	liferea
# removed because crash on 2007.1
# Requires:	wengophone

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the Xfce Mandriva Desktop. Xfce plugins not include.

%package minimal
Summary: 	Minimal dependencies needed for Xfce desktop
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
Requires:       exo
Requires:       thunar
Requires:       xfce-panel
Requires:       xfce-utils
Requires:       xfce-mcs-manager
Requires:       xfce-mcs-plugins
Requires:       libxfcegui4-plugins
Requires:       xfprint
Requires:       mousepad
Requires:       notification-daemon-xfce
Requires:       orage
Requires:       terminal
Requires:       thunar
Conflicts:      xarchiver
Requires:       squeeze
Requires:       xfburn
Requires:       xfce-artwork
Requires:       xfce-panel
Requires:       xfce-appfinder
Requires:       xfce-dev-tools
Requires:       xfce-icon-theme
Requires:       xfce-mixer
Requires:       xfce-session
Requires:       xfce-taskmanager
Requires:       xfdesktop
Requires:       xfmedia
Requires:       xfprint
Requires:       xfwm
Requires:       xfwm-themes
Requires:       xfce-utils
Requires:	tango-icon-theme

Provides:       xfce
Obsoletes:      xfce

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Xfce desktop environment.

%prep
%setup -qn %{name}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/X11/xdg
cp -r xfce4/ %{buildroot}/etc/X11/xdg/

%post minimal
if [ "$META_CLASS" == "download" ]; then
    XFCE_GTK_THEME="Ia Ora Free"
elif [ "$META_CLASS" == "desktop" ]; then
    XFCE_GTK_THEME="Ia Ora Orange"
elif [ "$META_CLASS" == "server" ]; then
    XFCE_GTK_THEME="Ia Ora Gray"
fi
if [ -n "$XFCE_GTK_THEME" ]; then
    sed -i "s/\(name=\"Net\/ThemeName.*value=\)\".*\"\/>/\1\"$XFCE_GTK_THEME\"\/>/" /etc/X11/xdg/xfce4/mcs_settings/gtk.xml
fi

%files

%files minimal
%defattr(644,root,root,755)
%{_sysconfdir}/X11/xdg/xfce4/*
