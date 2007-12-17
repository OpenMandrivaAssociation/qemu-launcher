%define	name	qemu-launcher
%define	version	1.7.4
%define	release	%mkrel 3

Summary:	Interface to configure and launch Qemu	
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Emulators
URL:		http://projects.wanderings.us/qemu_launcher
Source0:	http://download.gna.org/qemulaunch/%{name}_%{version}.tar.bz2
BuildArch:	noarch
Requires:	perl-Locale-gettext >= 1.04
BuildRequires:	librsvg
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils

%description
A launcher for Qemu that manages Qemu configs and creates disk images
Qemu-launcher provides a point and click interface to Qemu. It also
allows you to create, save, load, and run multiple Qemu VM
configurations. It has a basic interface for creating or convertering
disk images.

Only supports the x86 PC emulator part of Qemu.

%prep
%setup -q 

%build

%install
rm -rf %buildroot
%makeinstall DESTDIR=%buildroot PREFIX=%_prefix

%find_lang %name

desktop-file-install --vendor="" \
 --remove-category="Application" \
 --remove-category="Utility" \
 --add-category="System" \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}

rsvg-convert -a -w 48 -w 48 %buildroot%_iconsdir/hicolor/scalable/apps/qemu-launcher.svg -o %buildroot%_liconsdir/qemu-launcher.png
rsvg-convert -a -w 32 -w 32 %buildroot%_iconsdir/hicolor/scalable/apps/qemu-launcher.svg -o %buildroot%_iconsdir/qemu-launcher.png
rsvg-convert -a -w 16 -w 16 %buildroot%_iconsdir/hicolor/scalable/apps/qemu-launcher.svg -o %buildroot%_miconsdir/qemu-launcher.png

rm -rf %buildroot/%{_datadir}/doc/%name

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc README

%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/qemu-launcher.desktop
%{_iconsdir}/hicolor/*/apps/qemu-launcher.*
