%define	name	qemu-launcher
%define	version	1.7.4
%define	release	%mkrel 8

Summary:	Interface to configure and launch Qemu	
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Emulators
URL:		http://projects.wanderings.us/qemu_launcher
Source0:	http://download.gna.org/qemulaunch/%{name}_%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

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


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.7.4-8mdv2010.0
+ Revision: 442556
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.7.4-7mdv2009.1
+ Revision: 350154
- 2009.1 rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.7.4-6mdv2009.0
+ Revision: 259913
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.7.4-5mdv2009.0
+ Revision: 247762
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.7.4-3mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Funda Wang <fundawang@mandriva.org> 1.7.4-3mdv2008.0
+ Revision: 73386
- fix menu categories -> should be emulator only now

* Wed Aug 29 2007 Pascal Terjan <pterjan@mandriva.org> 1.7.4-2mdv2008.0
+ Revision: 73361
- Fix desktop file (#32940)

* Wed Jul 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.7.4-1mdv2008.0
+ Revision: 53136
- New release 1.7.4


* Mon Jan 01 2007 Pascal Terjan <pterjan@mandriva.org> 1.7.3-1mdv2007.0
+ Revision: 103016
- 1.7.3

* Sat Dec 02 2006 Pascal Terjan <pterjan@mandriva.org> 1.7.2-1mdv2007.1
+ Revision: 90045
- Oops, xmmlint is actually in libxml2-utils
- BuildRequires xmllint
- 1.7.2
- Import qemu-launcher

* Wed Aug 16 2006 Pascal Terjan <pterjan@mandriva.org> 1.7.0-1mdv2007.0
- New release 1.7.0
- Add Source URL
- XDG menu
- Update icon cache

* Thu Dec 22 2005 Pascal Terjan <pterjan@mandriva.org> 1.5-2mdk
- BuildRequires ImageMagick

* Mon Nov 14 2005 Pascal Terjan <pterjan@mandriva.org> 1.5-1mdk
- 1.5
- Drop P0
- mkrel

* Wed May 25 2005 Pascal Terjan <pterjan@mandriva.org> 1.3-2mdk
- P0 (drop unsupported -keyboard)

* Tue May 24 2005 Pascal Terjan <pterjan@mandriva.org> 1.3-1mdk
- First Package

