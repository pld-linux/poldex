%include        /usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl):	Nak³adka na poldka
Name:		poldex
Version:	0.16.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.foto-color.info/%{name}-%{version}.tar.bz2
# Source0-md5:	0e00c32dd22f7ede30e0181d68fd4eef
URL:		http://www.foto-color.info/poldex.html
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
