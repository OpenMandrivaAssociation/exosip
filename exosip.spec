%define major 7
%define libname %mklibname exosip2_ %{major}
%define libname_devel %mklibname -d exosip2

Summary: 	Extended osip library
Name: 	 	exosip
Version:	3.6.0
Release: 	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://savannah.nongnu.org/projects/exosip/
Source0:	http://download.savannah.gnu.org/releases/exosip/libeXosip2-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	libosip2-devel >= %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Exosip is a library that hides the complexity of using the SIP protocol for
mutlimedia session establishement. This protocol is mainly to be used by VoIP
telephony applications (endpoints or conference server) but might be also
useful for any application that wish to establish sessions like multiplayer
games.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}

%package -n 	%{libname_devel}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	libexosip2-devel = %{version}-%{release}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes: 	%{name}-devel < %{version}-%{release}
Obsoletes:	%mklibname -d exosip 5

%description -n %{libname_devel}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q -n libeXosip2-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# don't ship .a, .la
find %{buildroot} -name *.la | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so

