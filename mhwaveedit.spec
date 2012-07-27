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
