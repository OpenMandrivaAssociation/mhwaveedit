%define name 	mhwaveedit
%define version 1.4.14
%define release %mkrel 3
%define	Summary	WAV Editing Package

Summary:	%{Summary}
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPLv2+
Group: 		Sound
URL: 		https://gna.org/projects/mhwaveedit/
Source0: 	http://download.gna.org/mhwaveedit/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: 	pkgconfig gtk+2-devel SDL-devel libsndfile-devel libalsa-devel
BuildRequires:	jackit-devel libsamplerate-devel ladspa-devel
BuildRequires:  arts-devel

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
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*

