%define major 2
%define libname %mklibname celt0_ %{major}
%define develname %mklibname -d celt0
%define olddevname %mklibname -d celt

Summary:	Ultra-low delay audio codec
Name:		celt
Version:	0.11.3
Release:	2
Source0:	http://downloads.us.xiph.org/releases/celt/%{name}-%{version}.tar.gz
License:	BSD
Group:		Sound
Url:		http://www.celt-codec.org/
BuildRequires:	pkgconfig(ogg)

%description
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

CELT stands for "Constrained Energy Lapped Transform". It applies some
of the CELP principles, but does everything in the frequency domain,
which removes some of the limitations of CELP. CELT is suitable for
both speech and music and currently features:

* Ultra-low latency (typically from 3 to 9 ms)
* Full audio bandwidth (44.1 kHz and 48 kHz)
* Support for both voice and music
* Stereo support
* Packet loss concealment
* Constant bit-rates from 32 kbps to 128 kbps and above
* A fixed-point version of the encoder and decoder

The CELT codec is meant to close the gap between Vorbis and Speex for
applications where both high quality audio and low delay are desired.

%package -n	%{libname}
Summary:	Ultra-low delay audio codec - shared library
Group:		System/Libraries

%description -n	%{libname}
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

CELT stands for "Constrained Energy Lapped Transform". It applies some
of the CELP principles, but does everything in the frequency domain,
which removes some of the limitations of CELP. CELT is suitable for
both speech and music and currently features:

* Ultra-low latency (typically from 3 to 9 ms)
* Full audio bandwidth (44.1 kHz and 48 kHz)
* Support for both voice and music
* Stereo support
* Packet loss concealment
* Constant bit-rates from 32 kbps to 128 kbps and above
* A fixed-point version of the encoder and decoder

The CELT codec is meant to close the gap between Vorbis and Speex for
applications where both high quality audio and low delay are desired.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
%rename		%{olddevname}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/celtdec
%{_bindir}/celtenc

%files -n %{libname}
%doc README COPYING
%{_libdir}/libcelt0.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libcelt0.so
%{_libdir}/libcelt0.a


%changelog
* Fri May 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.11.3-1
+ Revision: 795787
- version update 0.11.3

* Tue Nov 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.11.1-1
+ Revision: 728884
- reenable check suite
- use %%rename macro
- clean up spec
- new version

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 663362
- mass rebuild

* Fri Dec 24 2010 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 624463
- update to new version 0.10.0

* Wed Nov 17 2010 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 598364
- update to new version 0.9.1

* Mon Nov 08 2010 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 595067
- update to new version 0.9.0

* Mon Jul 19 2010 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 554923
- new version
- new major

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 496957
- new version
- rename library package

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 460846
- update to new version 0.7.0

* Sat Jul 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 397199
- update to new version 0.6.1

* Mon Jul 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.0-1mdv2010.0
+ Revision: 393056
- update to new version 0.6.0

* Wed Feb 18 2009 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 342437
- update to new version 0.5.2

* Fri Dec 19 2008 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 316058
- update to new version 0.5.1

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 299451
- import celt

