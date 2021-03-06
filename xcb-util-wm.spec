Summary:	XCB util-wm module
Name:		xcb-util-wm
Version:	0.4.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	87b19a1cd7bfcb65a24e36c300e03129
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	m4
BuildRequires:	pkg-config
BuildRequires:	xorg-proto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB util-wm module provides the following libraries:
- ewmh: Both client and window-manager helpers for EWMH.
- icccm: Both client and window-manager helpers for ICCCM.

%package devel
Summary:	Header files for XCB util-wm libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util-wm libraries.

%prep
%setup -q

%build
%configure \
	--disable-static	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxcb-ewmh.so.?
%attr(755,root,root) %ghost %{_libdir}/libxcb-icccm.so.?
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so.*.*.*
%attr(755,root,root) %{_libdir}/libxcb-icccm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so
%attr(755,root,root) %{_libdir}/libxcb-icccm.so
%{_includedir}/xcb/*.h
%{_pkgconfigdir}/*.pc

