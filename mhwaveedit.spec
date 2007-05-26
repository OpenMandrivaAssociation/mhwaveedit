%define name 	mhwaveedit
%define version 1.4.12
%define release %mkrel 1

Summary:	WAV Editing Package
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
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
rm -fr $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

# Menu
mkdir -p %buildroot/%{_menudir}
cat > %buildroot/%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="sound_section.png" section="Multimedia/Sound" \
title="MHWaveEdit" longtitle="WAV audio editor" xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name}
Icon=sound_section.png
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
EOF


%clean
rm -rf %buildroot/

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%_bindir/%name
%_menudir/%name
%_datadir/applications/*


