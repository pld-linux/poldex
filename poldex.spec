#
# Conditional build:
# _without_autodeps	- don't BR packages needed only for resolving deps
#
%include        /usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl):	Nak³adka na poldka
Name:		poldex
Version:	0.16.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.foto-color.info/%{name}-%{version}.tar.bz2	
URL:		http://www.foto-color.info/poldex.html	
%{!?_without_autodeps:BuildRequires:	perl-Curses}
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
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%attr(755,root,root) %{_bindir}/*
