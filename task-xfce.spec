Summary:	Metapackage for the Xfce desktop environment
Name:		task-xfce
Version:	2013.0
Release:	3
Epoch:		1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		http://wiki.mandriva.com/en/XfceLive
BuildArch:	noarch

# (tpg) please keep requires in alphabetical order
Suggests:	eatmonkey
Suggests:	slim
Suggests:	orage
Suggests:	gigolo
Suggests:	midori
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
Requires:	xfce4-terminal
Requires:	thunar
Requires:	thunar-volman
Suggests:	xfce4-icon-theme
Requires:	xfce4-mixer
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
dependencies for running the Xfce panel plugins.

%package devel
Summary:	Xfce development metapackage
Group:		Development/Other
Url:		http://wiki.mandriva.com/en/XfceLive

# (tpg) please keep requires in alphabetical order
#Requires:	libxfcegui4-devel
Requires:	libxfce4ui-devel
Requires:	garcon-devel
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
dependencies for Xfce development environment.

%files

%files minimal

%files plugins

%files devel


%changelog
* Mon Apr 09 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-7
+ Revision: 789961
- fix requires

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-6
+ Revision: 789913
- enable few panel plugins
- reeanble few components

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-4
+ Revision: 789693
- add conflicts on xfce-utils

* Fri Apr 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-3
+ Revision: 789520
- disable most of xfce apps and plugins
- enable xfce4-timer-plugin
- enable genmon and wmdock plugins
- enable xfce4-xkb-plugin
- enable xfce4-sensors-plugin
- enable mpc, radio and weather plugins

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-2
+ Revision: 633065
- update requires lists for all xfce apps and panel plugins

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2011.0-1mdv2011.0
+ Revision: 579680
- change versioning
- disable suggests on apps that do not work with current xfce 4.7.0

* Sun Oct 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.1-4mdv2010.0
+ Revision: 456685
- suggests parole, a nwe media player for Xfce
- spec file clean

* Mon Jul 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.1-3mdv2010.0
+ Revision: 400834
- add suggest on task-xfce-plugins on task-xfce (pointed out by Dr_ST)

* Mon Jul 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.1-2mdv2010.0
+ Revision: 392973
- add suggests on gdm

* Wed Apr 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.1-1mdv2010.0
+ Revision: 368751
- update to new version 4.6.1

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.0-2mdv2009.1
+ Revision: 360330
- do not suggest xfmedia

* Sat Mar 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.6.0-1mdv2009.1
+ Revision: 350785
- version bump
- suggest thunar-shares-plugin

* Sat Feb 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.99.1-0.2mdv2009.1
+ Revision: 340222
- suggests gigolo instead of sion

* Mon Feb 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.99.1-0.1mdv2009.1
+ Revision: 339015
- bum version tag
- suggests xfswitch-plugin
- xfce4-screenshooter is no longer a panel plugin

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.92-0.1mdv2009.1
+ Revision: 324354
- suggests sion, a GIO/GVFS frontend
- bump version tag

* Fri Jan 02 2009 Jérôme Soyer <saispo@mandriva.org> 1:4.5.91-0.4mdv2009.1
+ Revision: 323290
- Bump Release
- Exclude python-xfce for version under < 2009 and wait for a fix

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - suggests xfce4-verve-plugin

* Tue Oct 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.91-0.3mdv2009.1
+ Revision: 298068
- add requires on xfconf, thunar-volman and xfce4-power-manager
- fix Url's

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.91-0.2mdv2009.1
+ Revision: 294903
- remove notification-daemon-xfce as it breaks the update and it seems not needed anymore

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.5.91-0.1mdv2009.1
+ Revision: 294552
- Xfce4.6 beta1 is landing on cooker
- remove xfce-mcs-manager and xfce-mcs-plugins, suppressed by xfconf and xfce4-settings

* Mon Oct 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-8mdv2009.1
+ Revision: 293345
- suggests thunar-shares

* Sat Sep 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-7mdv2009.0
+ Revision: 288836
- Suggests readahead

* Thu Sep 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-6mdv2009.0
+ Revision: 288171
- Suggests preload

* Mon Sep 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-5mdv2009.0
+ Revision: 286683
- use suggests for aumix
- suggests canberra-gtk for mdv 200900

* Tue Sep 16 2008 Jérôme Soyer <saispo@mandriva.org> 1:4.4.2-4mdv2009.0
+ Revision: 285113
- Add aumix to task-xfce because volume keys need it (thks ffixxx)

* Sun Jul 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-3mdv2009.0
+ Revision: 250441
- suggests xfce4-linelight-plugin

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-2mdv2009.0
+ Revision: 194655
- update plugin name
- require mandriva-xfce-config, rather only suggesting it

* Sun Feb 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.4.2-1mdv2008.1
+ Revision: 174385
- change versioning to be closer with upstream
- do not require all non-xfce software

* Fri Jan 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.0-4mdv2008.1
+ Revision: 157751
- add thunar-svn-plugin
- add clamtk
- requires gpa

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.0-3mdv2008.1
+ Revision: 120502
- correct obsoletes
- add xfce4-artwork
- obsolete older release of task-xfce and subpackages

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 2008.0-2mdv2008.1
+ Revision: 119203
- Bump Release
- Add Suggests on xfce4-rss-plugins
- Switch gtfp to filezilla (the one is so buggy)

* Wed Dec 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.0-1mdv2008.1
+ Revision: 119113
- use Suggests for some not-so-necessary xfce related stuff

* Wed Dec 05 2007 Jérôme Soyer <saispo@mandriva.org> 2008-25mdv2008.1
+ Revision: 115779
- Bump release
- Add xfce4-websearch-plugin

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing in description

* Thu Nov 22 2007 Thierry Vignaud <tv@mandriva.org> 2008-24mdv2008.1
+ Revision: 111292
- drop noarch tag thus, thus really fixing bug #35717 by applying not applied bit

* Thu Nov 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-23mdv2008.1
+ Revision: 111093
- disable conflicts on xarchiver for now, fix bug #35658
- handle requires of OO.org under non ix86 archs, fix bug #35717

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-22mdv2008.1
+ Revision: 110709
- xfce4-taskmanager
- xfce4-volstatus-icon

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-21mdv2008.1
+ Revision: 110591
- update requires for Xfce 4.4.2
- suggest plugins rather than hardcode requires in plugins subpackage (not all plugins are really needed)
- remove wengophone
- add xfce4-wmdock-plugin
- correct requires for xfce 4.4.2
- update description for the task-xfce-minimal package
- add conditionals for old mdv releases
- requires openoffice.org-gtk
- requires catfish

* Thu Nov 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-20mdv2008.1
+ Revision: 104408
- new license policy
- favors qalculate-gtk over gcalctool
- requires gtk-recordmydesktop
- remove eog
- move xfce-dev-tools to the task-xfce-devel

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Sep 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-19mdv2008.0
+ Revision: 93477
- require deluge and f-spot
- requires mandriva-xfce-config for task-xfce-minimal
- get back to ristretto

* Fri Sep 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-18mdv2008.0
+ Revision: 91948
- mozilla-firefox is the default web browser

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2008-17mdv2008.0
+ Revision: 90299
- rebuild

* Sun Sep 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-16mdv2008.0
+ Revision: 83582
- remove ristretto in favor of mirage
  remove rhythmbox in favor of exaile
  remove evince in favor of epdfview
- tango theme seems to be broken,at least it looks uglier than rodent :)

* Tue Aug 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-14mdv2008.0
+ Revision: 72684
- gthumb is being replaced with ristretto
- switch f-spot with gthumb
- smart plugin for panel has a new name

* Wed Jun 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-13mdv2008.0
+ Revision: 41742
- remove requires on mandriva stuff
- task-xfce is now pure task package
  o all configuration files and scriplets have been moved to the xfce-config-X (where X stands for Free, One and Powerpack)
  o you have to install xfce-config-X to have Xfce composed to your current theme
- add xfce-cddrive-plugin

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-12mdv2008.0
+ Revision: 36756
- add plugins and devel subpackage (plus corresponding requires)
- some cleans
- spec file clean

* Thu Jun 07 2007 Jérôme Soyer <saispo@mandriva.org> 2008-11mdv2008.0
+ Revision: 36598
- Introduce blino's changes :)

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - move %%post scriplet to the task-xfce-minimal package
    - add url
    - only package minimal should provide files

* Tue Jun 05 2007 Jérôme Soyer <saispo@mandriva.org> 2008-9mdv2008.0
+ Revision: 35878
- Cleanup
- Clean Up
- Clean Up
- Clean Up

* Tue Jun 05 2007 Jérôme Soyer <saispo@mandriva.org> 2008-8mdv2008.0
+ Revision: 35842
- bump release
- Split packages
- Comment abiword and gnumeric

* Tue Jun 05 2007 Jérôme Soyer <saispo@mandriva.org> 2008-6mdv2008.0
+ Revision: 35810
- Move some Requires

* Fri Jun 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2008-5mdv2008.0
+ Revision: 34398
- s/XFCE/Xfce
- s/notification-daemon/notification-daemon-xfce
- spec file clean

* Thu May 31 2007 Jérôme Soyer <saispo@mandriva.org> 2008-4mdv2008.0
+ Revision: 33096
- Fix permissions

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - s/xfce4-artwork/xfce-artwork

* Mon May 28 2007 Jérôme Soyer <saispo@mandriva.org> 2008-3mdv2008.0
+ Revision: 31942
- Add gdm

* Fri May 25 2007 Jérôme Soyer <saispo@mandriva.org> 2008-2mdv2008.0
+ Revision: 31196
- Fix sed
- Mandriva Integration

* Wed Apr 25 2007 Jérôme Soyer <saispo@mandriva.org> 2008-1mdv2008.0
+ Revision: 18147
- Task XFCE


* Thu Feb 01 2007 Jérôme Soyer <saispo@mandriva.org> 2007-11mdv2007.0
+ Revision: 115828
- Use notification-daemon instead of notification-daemon-xfce

* Fri Jan 12 2007 Jérôme Soyer <saispo@mandriva.org> 2007-10mdv2007.1
+ Revision: 108127
- Bump Release
- Only task-xfce
- Remove task-xfce-plugins

* Fri Jan 12 2007 Jérôme Soyer <saispo@mandriva.org> 2007-9mdv2007.1
+ Revision: 107821
- Bump Release
- Remove Requires

* Wed Jan 10 2007 Jérôme Soyer <saispo@mandriva.org> 2007-8mdv2007.1
+ Revision: 107244
- Remove plugins

* Wed Jan 10 2007 Jérôme Soyer <saispo@mandriva.org> 2007-7mdv2007.1
+ Revision: 107229
- Deactivate some plugins
- Deactivate some plugins

* Wed Jan 10 2007 Jérôme Soyer <saispo@mandriva.org> 2007-6mdv2007.1
+ Revision: 107136
- Add Provides/Obsoletes
- Remove cpufreq-plugin Requires

* Thu Jan 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2007-4mdv2007.1
+ Revision: 104010
- Add Require

* Wed Jan 03 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2007-3mdv2007.1
+ Revision: 103697
- Fix Require

* Wed Jan 03 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2007-2mdv2007.1
+ Revision: 103652
- Fix sub-packages name

* Tue Jan 02 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2007-1mdv2007.1
+ Revision: 103283
- Import task-xfce

