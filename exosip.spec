%define major 7
%define libname %mklibname exosip2_ %{major}
%define libname_devel %mklibname -d exosip2

Summary:	Extended osip library
Name:		exosip
Version:	3.6.0
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://savannah.nongnu.org/projects/exosip/
Source0:	http://download.savannah.gnu.org/releases/exosip/libeXosip2-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libosip2) >= %{version}

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

%package -n 	%{libname_devel}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libexosip2-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}exosip2-devel < 3.6.0

%description -n %{libname_devel}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q -n libeXosip2-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sun Oct 09 2011 Andrey Bondrov <abondrov@mandriva.org> 3.6.0-1mdv2012.0
+ Revision: 703885
- New version 3.6.0, new library major

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-3
+ Revision: 664161
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-2mdv2011.0
+ Revision: 605111
- rebuild

* Thu Apr 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 532874
- new upstream release 3.3.0
- rediff string format patch

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-3mdv2010.1
+ Revision: 511565
- rebuilt against openssl-0.9.8m

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 3.2.0-2mdv2010.0
+ Revision: 437507
- rebuild

* Thu Feb 19 2009 Emmanuel Andry <eandry@mandriva.org> 3.2.0-1mdv2009.1
+ Revision: 342751
- New version 3.2.0
- diff P0 to fix str fmt

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.1.0-2mdv2009.0
+ Revision: 266745
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 3.1.0-1mdv2009.0
+ Revision: 212546
- New version 3.1.0
- New versiono 3.1.0

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 3.0.3-1mdv2008.1
+ Revision: 157685
- Fix group
- Fix build requires (libosip2-devel not libosip-devel)
- Conform to new library policy
- Update to 3.0.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.2.2-0.20060217.2mdv2008.1
+ Revision: 124834
- kill re-definition of %%buildroot on Pixel's request
- import exosip


* Wed Mar 29 2006 Stefan van der Eijk <stefan@eijk.nu> 2.2.2-0.20060217.2mdk
- BuildRequires

* Sun Feb 19 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-0.20060217.1mdk
- new snap (20060217)

* Thu Apr 7 2005 Austin Acton <austin@mandrake.org> 0.9.0.cvs20050407-1mdk
- new cvs checkout

* Thu Feb 10 2005 Austin Acton <austin@mandrake.org> 0.9.0.cvs20050210-1mdk
- initial package
