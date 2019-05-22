Summary:	WAV Editing Package
Name:		mhwaveedit
Version:	1.4.24
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://github.com/magnush/mhwaveedit/
Source0:	https://github.com/magnush/mhwaveedit/archive/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	ladspa-devel
BuildRequires:	lame-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack) >= 0.98.0
BuildRequires:	pkgconfig(libpulse) >= 0.9.10
# For OGG support
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(samplerate)
# For default mixer (alsamixer)
Requires:	alsa-utils


%description
mhWaveEdit is a graphical program for editing sound files. It is completely
free (GPL) and it's written by Magnus Hjorth. It is intended to be
user-friendly and robust. OGG and LAME support are available if installed.

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*/apps/%{name}.png

#-----------------------------------------------------------------------------

%prep
%setup -q


%build
%configure2_5x	--with-default-mixerapp="alsamixer" \
		--with-default-driver="pulse" \
		--without-esound \
		--without-sun \
		--without-arts \
		--with-double-samples
%make


%install
%makeinstall_std

%find_lang %{name}

