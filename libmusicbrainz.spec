%define major	4
%define libname %mklibname musicbrainz %{major}
%define devname %mklibname -d musicbrainz

Summary:	A software library for accesing MusicBrainz servers
Name:		libmusicbrainz
Version:	2.1.5
Release:	18
Group:		Sound
License:	LGPLv2+
Url:		http://www.musicbrainz.org
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.bz2
Patch0:		musicbrainz-2.1.5-gcc43-includes.patch
BuildRequires:	pkgconfig(expat)

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

%package -n %{devname}
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.


%prep
%setup -q
%apply_patches

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmusicbrainz.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README TODO INSTALL
%{_includedir}/musicbrainz
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

