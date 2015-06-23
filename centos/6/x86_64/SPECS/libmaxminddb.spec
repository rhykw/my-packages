Packager:	rhykw
Name:		libmaxminddb
Version:	1.0.4
Release:	1%{?dist}
Summary:	The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.

Group:		Libraries
License:	Apache License 2.0
URL:		http://dev.maxmind.com/
Source0:	https://github.com/maxmind/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	libtool
#BuildRequires:	pkgconfig

#Requires:	

%package devel
Summary:    The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}


%description
The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.
This is a custom binary format designed to facilitate fast lookups of IP addresses while allowing 
for great flexibility in the type of data associated with an address.

The MaxMind DB format is an open format. The spec is available at http://maxmind.github.io/MaxMind-DB/. 
This spec is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.

See http://dev.maxmind.com/ for more details about MaxMind's GeoIP2 products.

%description devel
The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.


%prep
%setup -q


%build
#./bootstrap
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NOTICE README.md
%attr(755,root,root) %{_libdir}/%{name}.so.?.?.?
%attr(755,root,root) %{_libdir}/%{name}.so.?
%attr(755,root,root) %{_bindir}/mmdblookup
%{_mandir}/man1/mmdblookup.1*



%files devel
%defattr(-,root,root,-)
%attr(755,root,root) %{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_libdir}/%{name}.a
%{_includedir}/maxminddb*.h
%{_mandir}/man3/*.3.*



%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} rhywk <github@rhykw.net>
This is a test build.

