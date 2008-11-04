%define package_name    lib%{name}
%define	version	2.1.5
%define release	%mkrel 4

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name

Name:		musicbrainz
Version:	%{version}
Release:	%{release}
Summary:	A software library for accesing MusicBrainz servers
Source:		http://ftp.musicbrainz.org/pub/musicbrainz/%{package_name}-%{version}.tar.bz2
Patch0:		musicbrainz-2.1.5-gcc43-includes.patch
URL:		http://www.musicbrainz.org
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	LGPL
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	python-ctypes
BuildRequires:	autoconf2.5 >= 2.58
BuildRequires:	python-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %develname
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %name 4

%description -n	%develname
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%package -n python-%{name}
Summary:	Python binding to use libmusicbrainz
Group:		Development/Python
Requires:	python-ctypes
Requires:	%{libname} = %{version}-%{release}

%description -n python-%{name}
Python binding to use libmusicbrainz.


%prep
%setup -q -n %{package_name}-%{version}
%patch0 -p1

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}

%makeinstall_std

pushd python 
python setup.py install --prefix=%{buildroot}/%{_prefix}
popd

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n python-%{name}
%defattr(-, root, root)
%doc python/examples/
%{py_puresitedir}/*

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO INSTALL
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_includedir}/musicbrainz
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
