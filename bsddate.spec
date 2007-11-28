Summary:	BSD version of date(1) utility
Summary(pl.UTF-8):	Wersja BSD narzędzia date(1)
Name:		bsddate
Version:	6.2
Release:	1
License:	BSD
Group:		Applications
# taken from FreeBSD CVS
Source0:	%{name}.tar.bz2
# Source0-md5:	fdd25d587e4568e5ffd2dc253b9b1117
Patch0:		%{name}-linux.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BSD version of date(1) utility, ported from FreeBSD 6.2.

%description -l pl.UTF-8
Wersja BSD narzędzia date(1) przeniesiona z FreeBSD 6.2.

%prep
%setup -q -n date
%patch0 -p1

head -n 28 date.c > COPYING

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D date $RPM_BUILD_ROOT%{_bindir}/bsddate
install -D date.1 $RPM_BUILD_ROOT%{_mandir}/man1/bsddate.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/bsddate
%{_mandir}/man1/bsddate.1*
