%include        /usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl):	Nak³adka na poldka
Name:		poldex
Version:	0.15
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.foto-color.info/poldex	
URL:		http://www.foto-color.info/poldex.html	
BuildRequires:	perl-Curses
BuildRequires:	rpm-perlprov
Requires:	poldek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice frontend to poldek written in perl.

%description -l pl
Przyjemna nak³adka na poldka napisana w perlu.

%prep
%setup -qcT
cp %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%attr(755,root,root) %{_sbindir}/*
