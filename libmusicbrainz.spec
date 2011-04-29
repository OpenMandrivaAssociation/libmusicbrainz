%define	version	2.1.5
%define release	%mkrel 8
%define major 4
%define libname %mklibname musicbrainz %{major}
%define develname %mklibname -d musicbrainz

Name:		libmusicbrainz
Version:	%{version}
Release:	%{release}
Summary:	A software library for accesing MusicBrainz servers
Source:		http://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.bz2
Patch0:		musicbrainz-2.1.5-gcc43-includes.patch
URL:		http://www.musicbrainz.org
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	LGPLv2+
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	autoconf2.5 >= 2.58

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
Provides:	musicbrainz-devel = %{version}-%{release}
Obsoletes: %mklibname -d musicbrainz 4

%description -n	%develname
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

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
