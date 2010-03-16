
Name: libmusicbrainz
Version: 3.0.2
Release: %mkrel 2
Summary: A software library for accesing MusicBrainz servers
Source:	http://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
Patch0: libmusicbrainz-3.0.2-stdcpp.patch
URL: http://www.musicbrainz.org
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPL
BuildRequires: cmake
BuildRequires: neon-devel
BuildRequires: libdiscid-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

#----------------------------------------------------------------------

%define major 6
%define libname %mklibname musicbrainz3_ %{major}

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------

%define develname %mklibname -d musicbrainz

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

%files -n %develname
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .orig

%build
%cmake
%make


%install
rm -rf %{buildroot}

%makeinstall_std -C build

%clean
rm -rf %{buildroot}


