%define	version	4.0.0
%define release	1
%define major 3
%define libname %mklibname musicbrainz %{major}
%define develname %mklibname -d musicbrainz
%define stdevelname %mklibname -d -s musicbrainz 


Name:		libmusicbrainz
Version:	%{version}
Release:	%{release}
Summary:	A software library for accesing MusicBrainz servers
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
Patch0:		cmake_include_dir.patch
URL:		http://www.musicbrainz.org
Group:		Sound
License:	LGPLv2+
BuildRequires:	libexpat-devel >= 2.0.1
BuildRequires:	pkgconfig(neon)
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
sed -i -e 's:-Werror::' {examples,src,tests}/CMakeLists.txt || die
%patch0 -p1

%build
%ifarch ix86
%define libsuff -DLIB_SUFFIX=32
%else 
%define libsuff -DLIB_SUFFIX=64
%endif

cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} %libsuff -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} -DLIB_INSTALL_DIR:PATH=%{_libdir} -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF '-DCMAKE_MODULE_LINKER_FLAGS= -Wl,--as-needed -Wl,--no-undefined -Wl,-z,relro -Wl,-O1 -Wl,--build-id -Wl,--enable-new-dtags -Wl,--unresolved-symbols=ignore-all'

%make


%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %develname
%{_includedir}/musicbrainz4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
