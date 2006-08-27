Summary:	KDE frontend for subversion
Summary(de):	KDE Frontend für Subversion
Summary(pl):	Frontend KDE do subversion
Name:		kdesvn
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://www.alwins-world.de/programs/download/kdesvn/%{name}-%{version}.tar.bz2
# Source0-md5:	d21c5c6ddc00d1948014149ecffeb5d0
Patch0:		%{name}-desktop.patch
URL:		http://www.alwins-world.de/programs/kdesvn/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kdesvn is yet another client for subversion. But it uses native KDE
API instead of a extra lib like GAMBAS and it is using the native
subversion delevelopment API instead of just parsing the output of the
commandline tool like most other clients do.

It tries to setup a look and feel like the standard filemanager of
KDE.

%description -l de
Kdesvn ist ein weiterer Subversion Klient. Aber es benutzt die native
KDE API anstatt einer zusätzlichen Bibliothek wie GAMBAS und es
benutzt die native subversion Development API anstatt nur die Ausgabe
zu parsen wie die meisten anderen Klienten es tun.

%description -l pl
Kdesvn jest kolejnym klientem subversion. U¿ywa jednak natywnego API
KDE zamiast dodatkowej biblioteki jak GAMBAS, jak równie¿ u¿ywa
natywnego API subversion zamiast analizy wyj¶cia narzêdzia
dzia³aj±cego z linii poleceñ, jak to robi± inni klienci subversion.

Program ten stara siê ustawiæ wygl±d zbli¿ony do standardowego
zarz±dcy plików KDE.

%package svnqt
Summary:	Wrapper library for subversion Qt integration
Summary(pl):	Wrapper biblioteki subversion do intergracji z Qt
Group:		Libraries
Requires:	subversion-libs >= 1.2.0

%description svnqt
Shared library which contains a Qt C++ wrapper for subversion. It is
core part of kdesvn but is designed to not require KDE so plain Qt
programs may use it.

%description svnqt -l pl
Biblioteka wspó³dzielona zawieraj±ca wrapper C++ do obs³ugi
subversion. Jest g³ówn± czê¶ci± kdesvn, ale nie wymaga KDE, wiêc mo¿e
byæ u¿ywana w programach korzystaj±cych z samego Qt.

%package svnqt-devel
Summary:	Wrapper library header files for subversion Qt integration
Summary(pl):	Pliki nag³ówkowe wrappera biblioteki subversion dla Qt
Group:		Development/Libraries
Requires:	%{name}-svnqt = %{version}-%{release}
Requires:	qt-devel
Requires:	subversion-devel >= 1.2.0

%description svnqt-devel
Header files for wrapper library for subversion Qt integration.

%description svnqt-devel -l pl
Pliki nag³ówkowe biblioteki wspó³dzielonej zawieraj±cej wrapper C++ do
obs³ugi subversion.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--with-svn-lib=%{_libdir} \
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	svnqt -p /sbin/ldconfig
%postun	svnqt -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svgz
%{_datadir}/apps/%{name}
%{_datadir}/apps/kdesvnpart
%{_datadir}/services/*.protocol
%{_datadir}/services/kded/kdesvnd.desktop
%{_datadir}/config.kcfg/*
%{_datadir}/apps/konqueror/servicemenus/*.desktop

%files svnqt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt*.so.*.*.*

%files svnqt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt*.so
%{_libdir}/libsvnqt.la
%{_includedir}/svnqt
