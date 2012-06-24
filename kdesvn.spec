Summary:	KDE frontend for subversion
Summary(de):	KDE Frontend f�r Subversion
Summary(pl):	Frontend KDE do subversion
Name:		kdesvn
Version:	0.10.0
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://www.alwins-world.de/programs/download/kdesvn/%{name}-%{version}.tar.bz2
# Source0-md5:	896d62ac8687236f05e984ba6cd69e6b
Patch0:		%{name}-desktop.patch
URL:		http://www.alwins-world.de/programs/kdesvn/
BuildRequires:	cmake >= 2.4.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.293
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
KDE API anstatt einer zus�tzlichen Bibliothek wie GAMBAS und es
benutzt die native subversion Development API anstatt nur die Ausgabe
zu parsen wie die meisten anderen Klienten es tun.

%description -l pl
Kdesvn jest kolejnym klientem subversion. U�ywa jednak natywnego API
KDE zamiast dodatkowej biblioteki jak GAMBAS, jak r�wnie� u�ywa
natywnego API subversion zamiast analizy wyj�cia narz�dzia
dzia�aj�cego z linii polece�, jak to robi� inni klienci subversion.

Program ten stara si� ustawi� wygl�d zbli�ony do standardowego
zarz�dcy plik�w KDE.

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
Biblioteka wsp�dzielona zawieraj�ca wrapper C++ do obs�ugi
subversion. Jest g��wn� cz�ci� kdesvn, ale nie wymaga KDE, wi�c mo�e
by� u�ywana w programach korzystaj�cych z samego Qt.

%package svnqt-devel
Summary:	Wrapper library header files for subversion Qt integration
Summary(pl):	Pliki nag��wkowe wrappera biblioteki subversion dla Qt
Group:		Development/Libraries
Requires:	%{name}-svnqt = %{version}-%{release}
Requires:	qt-devel
Requires:	subversion-devel >= 1.2.0

%description svnqt-devel
Header files for wrapper library for subversion Qt integration.

%description svnqt-devel -l pl
Pliki nag��wkowe biblioteki wsp�dzielonej zawieraj�cej wrapper C++ do
obs�ugi subversion.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX=%{_prefix} .

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
%{_mandir}/man1/kdesvn.1*
%{_mandir}/man1/kdesvnaskpass.1*

%files svnqt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt*.so.*.*.*

%files svnqt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt*.so
%{_libdir}/libsvnqt.la
%{_includedir}/svnqt
