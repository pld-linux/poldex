#
# Conditional build:
%bcond_without	autodeps	- don't BR packages needed only for resolving deps
#
%include        /usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl):	Nak³adka na poldka
Name:		poldex
Version:	0.17
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.yogib.risp.pl/poldex/%{name}-%{version}.tar.bz2
# Source0-md5:	ba8b3c2731e975f79a3e0b07d5da7694
URL:		http://www.yogib.risp.pl/
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

%description -l pl
Przyjemna nak³adka na poldka napisana w Perlu.

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/*
