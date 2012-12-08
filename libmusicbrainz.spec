%define	version	2.1.5
%define release	%mkrel 9
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
%makeinstall_std

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO INSTALL
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_includedir}/musicbrainz
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-8mdv2011.0
+ Revision: 660267
- mass rebuild

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 2.1.5-7mdv2011.0
+ Revision: 575682
- revert to 2.1.5
- update license

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream version required by amarok

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.5-6mdv2010.0
+ Revision: 425623
- rebuild

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 2.1.5-5mdv2009.1
+ Revision: 329014
- continue renaming of the package
- disable python binding

  + Helio Chissini de Castro <helio@mandriva.com>
    - Moving to proper name

* Mon Aug 18 2008 Emmanuel Andry <eandry@mandriva.org> 2.1.5-4mdv2009.0
+ Revision: 273419
- fix gcc4.3 build with P0 from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Götz Waschk <waschk@mandriva.org> 2.1.5-3mdv2008.1
+ Revision: 101462
- new devel name

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.5-3mdv2008.0
+ Revision: 36910
- rebuild for expat

* Sun May 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.5-2mdv2008.0
+ Revision: 31795
- fix bug #31051

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.5-1mdv2008.0
+ Revision: 31018
- new upstream version
- drop Patch0 (merged upstream)
- spec file clean

