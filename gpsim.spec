%define name    gpsim
%define version 0.24.0
%define release %mkrel 2

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
Patch0:		gpsim-0.24.0-linkage.patch
License:        GPL
Group:          Development/Other
Url:            http://www.dattalo.com/gnupic/gpsim.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  readline-devel flex popt-devel glib2-devel
BuildRequires:  termcap-devel ncurses-devel glibc-static-devel
BuildRequires:  libgtk+extra-2-devel

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
%patch0 -p0

%build
autoreconf -fi
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# zap .a and .la
rm -fr %{buildroot}%{_libdir}/{*.a,*.la}

%clean
rm -rf $RPM_BUILD_ROOT

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
