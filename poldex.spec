#
# Conditional build:
%bcond_without	autodeps	- don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl.UTF-8):   Nakładka na poldka
Name:		poldex
Version:	0.17.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5aea7ff274936439c98b65fa016a1510
Patch0:		%{name}-epoch.patch
#URL:		http://www.yogib.risp.pl/
%if %{with autodeps}
BuildRequires:	perl-Curses
BuildRequires:	perl-Locale-gettext
BuildRequires:	perl-RPM
%endif
BuildRequires:	rpm-perlprov
Requires:	poldek
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice frontend to poldek written in Perl.

%description -l pl.UTF-8
Przyjemna nakładka na poldka napisana w Perlu.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -R locale $RPM_BUILD_ROOT%{_datadir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
