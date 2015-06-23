Packager:	rhykw
Name:		mod_maxminddb
Version:	1.0.1
Release:	1%{?dist}
Summary:	MaxMind DB Apache Module

Group:		System Environment/Daemons
License:	Apache License, Version 2.0
URL:		http://dev.maxmind.com/
Source0:	https://github.com/maxmind/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/rhykw/my-packages/master/centos/6/x86_64/SOURCES/mod_maxminddb-maxminddb.conf
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	libmaxminddb-devel , httpd-devel
Requires:	libmaxminddb-devel , httpd

%description
This module allows you to query MaxMind DB files from Apache 2.2+ using the libmaxminddb library.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}
mv src/.libs/%{name}.so .
%{__strip} -g %{name}.so


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m755 %{name}.so %{buildroot}%{_libdir}/httpd/modules

# Install the config file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/maxminddb.conf


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%doc Changes.md LICENSE README.md
%attr(755,root,root)%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf


%define date    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} rhywk <github@rhykw.net>
This is a test build.

