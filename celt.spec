%define name celt
%define version 0.7.1
%define release %mkrel 1
%define major 0
%define libname %mklibname celt0_ %major
%define develname %mklibname -d celt0
%define olddevname %mklibname -d celt

Summary: Ultra-low delay audio codec
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.us.xiph.org/releases/celt/%{name}-%{version}.tar.gz
License: BSD
Group: Sound
Url: http://www.celt-codec.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libogg-devel

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

%package -n %{libname}
Summary: Ultra-low delay audio codec - shared library
Group: System/Libraries

%description -n %{libname}
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

%package -n %develname
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %olddevname < %version

%description -n %develname
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
#gw fails in 0.5.0
#make check

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README TODO
%_bindir/celtdec
%_bindir/celtenc

%files -n %libname
%defattr(-,root,root)
%doc README COPYING
%_libdir/libcelt0.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_includedir/%name
%_libdir/pkgconfig/%name.pc
%_libdir/libcelt0.so
%_libdir/libcelt0.la
%_libdir/libcelt0.a
