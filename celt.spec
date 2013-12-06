%define api	0
%define major	2
%define libname %mklibname celt %{api} %{major}
%define devname %mklibname -d celt %{api}

Summary:	Ultra-low delay audio codec
Name:		celt
Version:	0.11.3
Release:	8
License:	BSD
Group:		Sound
Url:		http://www.celt-codec.org/
Source0:	http://downloads.us.xiph.org/releases/celt/%{name}-%{version}.tar.gz
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
The package contains the shared library for %{name}.

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
autoreconf -fi
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/celtdec
%{_bindir}/celtenc

%files -n %{libname}
%{_libdir}/libcelt%{api}.so.%{major}*

%files -n %{devname}
%doc README COPYING
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libcelt%{api}.so

