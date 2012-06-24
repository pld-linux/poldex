#
# Conditional build:
%bcond_without	autodeps	- don't BR packages needed only for resolving deps
#
%include        /usr/lib/rpm/macros.perl
Summary:	Frontend to poldek
Summary(pl):	Nak�adka na poldka
Name:		poldex
Version:	0.17.3
Release:	5
License:	GPL
Group:		Applications
#Source0:	http://www.yogib.risp.pl/poldex/%{name}-%{version}.tar.bz2
# more complete source (contains .po file)
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	baea5cfc7fd46c34e401c85f0ab8cd18
URL:		http://www.yogib.risp.pl/
Patch0:		%{name}-pl_update.patch
Patch1:		%{name}-typos.patch
Patch2:		%{name}-tmp.patch
BuildRequires:	gettext-devel
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
Przyjemna nak�adka na poldka napisana w Perlu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
msgfmt -o locale/pl/LC_MESSAGES/poldex.mo locale/pl/LC_MESSAGES/poldex.po

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
