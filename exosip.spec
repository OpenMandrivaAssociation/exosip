%define snap 20060217
%define major 5
%define libname %mklibname exosip %major

Summary: 	Extended osip library
Name: 	 	exosip
Version:	2.2.2
Release: 	%mkrel 0.%{snap}.2
License:	GPL
Group:		System/Libraries
URL:		http://savannah.nongnu.org/projects/exosip/
Source0:	%{name}-%{version}-%{snap}.tar.bz2
BuildRequires:	libosip-devel >= 2.2.0
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Exosip is a library that hides the complexity of using the SIP protocol for
mutlimedia session establishement. This protocol is mainly to be used by VoIP
telephony applications (endpoints or conference server) but might be also
useful for any application that wish to establish sessions like multiplayer
games.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep

%setup -q -n %{name}

%build
./autogen.sh

%configure2_5x \
    --disable-ms \
    --disable-josua

%make
										
%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

