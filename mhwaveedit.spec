Summary:	WAV Editing Package
Name: 		mhwaveedit
Version: 	1.4.22
Release: 	1
License: 	GPLv2+
Group: 		Sound
URL: 		https://gna.org/projects/mhwaveedit/
Source0: 	http://download.gna.org/mhwaveedit/%{name}-%{version}.tar.bz2
BuildRequires: 	pkgconfig gtk+2-devel SDL-devel sndfile-devel libalsa-devel
BuildRequires:	jackit-devel libsamplerate-devel ladspa-devel

%description
mhWaveEdit is a graphical program for editing sound files. It is completely
free (GPL) and it's written by Magnus Hjorth. It is intended to be
user-friendly and robust.

OGG and LAME support are available if installed.

%prep
%setup -q

%build
%configure2_5x --without-portaudio
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/mhwaveedit.xpm
%{_mandir}/man1/mhwaveedit.1*


%changelog
* Fri Jul 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.22-1
+ Revision: 811226
- version update 1.4.22

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1.4.21-1
+ Revision: 672525
- new version 1.4.21

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1.4.20-2
+ Revision: 672524
- rebuild

* Sun Dec 26 2010 Yuri Myasoedov <omerta13@mandriva.org> 1.4.20-1mdv2011.0
+ Revision: 625221
- Added man page
- New version 1.4.20

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 1.4.19-1mdv2011.0
+ Revision: 598581
- update to new version 1.4.19

* Thu Mar 18 2010 Funda Wang <fwang@mandriva.org> 1.4.18-1mdv2010.1
+ Revision: 524762
- update to new version 1.4.18

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.4.17-1mdv2010.1
+ Revision: 485788
- new version 1.4.17
- drop merged patch

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 1.4.16-1mdv2010.1
+ Revision: 466186
- new version 1.4.16

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1.4.15-2mdv2010.0
+ Revision: 380840
- use app own desktop file
- New version 1.4.15
- drop arts dep

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 22 2007 Funda Wang <fwang@mandriva.org> 1.4.14-1mdv2008.1
+ Revision: 111174
- New version 1.4.14

* Fri Oct 19 2007 Funda Wang <fwang@mandriva.org> 1.4.13-1mdv2008.1
+ Revision: 100390
- update to new version 1.4.13

  + Thierry Vignaud <tv@mandriva.org>
    - do not harcode icon extension

* Sun Jun 10 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.12-3mdv2008.0
+ Revision: 37843
- d'oh, forgot to remove debian menu from file list
- drop debian menu

* Sat Jun 09 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.12-2mdv2008.0
+ Revision: 37722
- fix %%{Summary} macro (fixes #26921)

* Sat May 26 2007 Austin Acton <austin@mandriva.org> 1.4.12-1mdv2008.0
+ Revision: 31552
- new version

