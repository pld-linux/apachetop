Summary:	Apache top-like display
Summary(pl):	top-podobny wy¶wietlacz pracy apache
Name:		apachetop
Version:	0.4
Release:	1
License:	BSD
Group:		Network/Monitoring
######		Unknown group!
Source0:	http://clueful.shagged.org/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	b0258a0e771c943415717591606c909e
URL:		http://clueful.shagged.org/%{name}
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses-based top-like display for Apache information, including
requests per second, bytes per second, most popular URLs, etc.

%description -l pl
Bazuj±cy na curses top-podobny wy¶wietlacz informacji dla Apache,
w³±czaj±c w to ¿±dania na sekundê, bajty na sekundê, najbardziej
popularne URL-e, itp.

%prep
%setup -q -n ApacheTop-%{version}

%build
%{__make} linux \
	CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
