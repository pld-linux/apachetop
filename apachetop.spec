#
# TODO: fam support is broken (it always needs running & working fam)
#
Summary:	Apache top-like display
Summary(pl.UTF-8):	Podobny do topa program pokazujący pracę Apache'a
Name:		apachetop
Version:	0.12.6
Release:	10
Epoch:		1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.webta.org/apachetop/%{name}-%{version}.tar.gz
# Source0-md5:	604283ac4bbbddd98fc9b1f11381657e
Patch0:		%{name}-debian.patch
Patch1:		%{name}-log_location.patch
Patch2:		%{name}-maxpath.patch
URL:		http://www.webta.org/projects/apachetop/
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	readline-devel
BuildRequires:	adns-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses-based top-like display for Apache information, including
requests per second, bytes per second, most popular URLs, etc.

%description -l pl.UTF-8
Oparty na curses podobny do topa program pokazujący informacje o pracy
Apache'a, włączając w to zapytania na sekundę, bajty na sekundę,
najbardziej popularne URL-e, itp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's#fam#fambroken#g' configure*

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-logfile=/var/log/httpd/access_log

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} %{rpmcppflags} -I/usr/include/ncurses -pthread"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
