%define name    gpsim
%define version 0.26.1
%define release %mkrel 1

%define lib_name_orig lib%{name}
%define lib_major 0
%define lib_name %mklibname %{name} %{lib_major}
%define develname %mklibname -d %{name}

Name:           %{name}
Epoch:		1
Version:        %{version}
Release:        %{release}
Summary:        A software simulator for Microchip PIC microcontrollers
Source0:        %{name}-%{version}.tar.gz
Patch0:		gpsim-0.26.1-linkage.patch
Patch1:		gpsim-0.26.1-gtkextra3.patch
Patch2:		gpsim-0.26.1-glibh.patch
License:        GPL
Group:          Development/Other
Url:		http://gpsim.sourceforge.net/
BuildRequires:  readline-devel flex pkgconfig(popt) pkgconfig(glib-2.0)
BuildRequires:  termcap-devel pkgconfig(ncurses) glibc-static-devel
BuildRequires:  libgtk+extra-3-devel

%description
gpsim is a full-featured software simulator for Microchip PIC microcontrollers
distributed under the GNU General Public License.

gpsim has been designed to be as accurate as possible. Accuracy includes the 
entire PIC - from the core to the I/O pins and including ALL of the internal 
peripherals. Thus it's possible to create stimuli and tie them to the I/O pins 
and test the PIC the same PIC the same way you would in the real world.

%package -n     %{lib_name}
Summary:	Main library for %{name}
Group:          System/Libraries

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with libgpsim

%package -n     %{develname}
Summary:        Headers for developing programs that will use libgpsim
Group:          Development/C
Requires:       %{lib_name} = %{epoch}:%{version}
Provides:       %{lib_name_orig}-devel = %{version}-%{release} 
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{lib_name}-devel

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use libgpsim

%prep
%setup -q
%patch0 -p0 -b .link
%patch1 -p2 -b .gtkextra3
%patch2 -p2 -b .glibh

%build
%define _disable_ld_no_undefined 1
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# zap .a and .la
rm -fr %{buildroot}%{_libdir}/*.la

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 1:0.26.1-1mdv2011.0
+ Revision: 676248
- do not use autoconf
- new version 0.26.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.24.0-3mdv2011.0
+ Revision: 610976
- rebuild

* Sun May 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:0.24.0-2mdv2010.1
+ Revision: 544879
- don't ship .a and .la
- enable building the gui and add libgtk+extra-2-devel as a BR
- remove mdkversion < 200900 bits, not needed

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1:0.24.0-1mdv2010.1
+ Revision: 503876
- New version 0.24.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jun 24 2007 Funda Wang <fwang@mandriva.org> 1:0.22.0-1mdv2008.0
+ Revision: 43582
- BR glib2
- Patch not needed
- New version
- Import gpsim



* Sat Apr 15 2006 Couriousous <couriousous@mandriva.org> 1:0.21.11-1mdk
- 0.21.11

* Fri Aug 26 2005 Couriousous <couriousous@mandriva.org> 1:0.21.4-2mdk
- Disable gui as it use an antique gtk+extra no more provided in the distro

* Fri Jul 15 2005 Couriousous <couriousous@mandriva.org> 0.21.4-1mdk
- 0.21.4

* Fri Feb 04 2005 Couriousous <couriousous@mandrake.org> 0.21.2-5mdk
- Rebuild for new libreadline

* Fri Jan 21 2005 Couriousous <couriousous@mandrake.org> 0.21.2-4mdk
- Fix menu ( strange bug ... )
- Fix requires-on-release

* Mon Jan 17 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.21.2-3mdk
- Fix epoch stuff

* Sat Jan 15 2005 Couriousous <couriousous@mandrake.org> 0.21.2-2mdk
- Revert to 0.21.2 since ktechlab don't build with 0.21.3 cvs
- trem <trem@zarb.org>
   - Add buildrequires

* Fri Jan 14 2005 Couriousous <couriousous@mandrake.org> 0.21.3-0.20041231.1mdk
- Update
- Use gtk2

* Mon Jan 10 2005 Couriousous <couriousous@mandrake.org> 0.21.2-1mdk
- First Mandrakelinux release
