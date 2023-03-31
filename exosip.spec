%define major 13
%define libname %mklibname exosip2_ %{major}
%define devname %mklibname -d exosip2

Summary:	Extended osip library
Name:		exosip
Version:	5.1.3
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://savannah.nongnu.org/projects/exosip/
Source0:	http://download.savannah.nongnu.org/releases/exosip/libexosip2-%{version}.tar.gz

BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libosip2)

%description
Exosip is a library that hides the complexity of using the SIP protocol for
mutlimedia session establishement. This protocol is mainly to be used by VoIP
telephony applications (endpoints or conference server) but might be also
useful for any application that wish to establish sessions like multiplayer
games.

%package -n 	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}

%package -n 	%{devname}
Summary:	Header files and development libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libexosip2-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}exosip2-devel < 3.6.0

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%autosetup -n libexosip2-%{version} -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libeXosip2.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so

