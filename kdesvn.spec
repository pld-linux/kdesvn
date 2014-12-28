%define		kdever		4.2
%define		qtver		4.8.1

Summary:	KDE frontend for subversion
Summary(de.UTF-8):	KDE Frontend für Subversion
Summary(pl.UTF-8):	Frontend KDE do subversion
Name:		kdesvn
Version:	1.6.0
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://kdesvn.alwins-world.de/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	7e6adc98ff4777a06d5752d3f2b58fa3
Patch0:		%{name}-desktop.patch
URL:		http://www.alwins-world.de/programs/kdesvn/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.4.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	subversion-devel >= 1.6
BuildConflicts:	kdesvn-svnqt-devel < %{version}
Requires:	%{name}-svnqt = %{version}-%{release}
Requires:	kde4-kdelibs >= %{kdever}
Requires:	subversion >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kdesvn is yet another client for subversion. But it uses native KDE
API instead of a extra lib like GAMBAS and it is using the native
subversion delevelopment API instead of just parsing the output of the
commandline tool like most other clients do.

It tries to setup a look and feel like the standard filemanager of
KDE.

%description -l de.UTF-8
Kdesvn ist ein weiterer Subversion Klient. Aber es benutzt die native
KDE API anstatt einer zusätzlichen Bibliothek wie GAMBAS und es
benutzt die native subversion Development API anstatt nur die Ausgabe
zu parsen wie die meisten anderen Klienten es tun.

%description -l pl.UTF-8
Kdesvn jest kolejnym klientem subversion. Używa jednak natywnego API
KDE zamiast dodatkowej biblioteki jak GAMBAS, jak również używa
natywnego API subversion zamiast analizy wyjścia narzędzia
działającego z linii poleceń, jak to robią inni klienci subversion.

Program ten stara się ustawić wygląd zbliżony do standardowego
zarządcy plików KDE.

%package svnqt
Summary:	Wrapper library for subversion Qt integration
Summary(pl.UTF-8):	Wrapper biblioteki subversion do intergracji z Qt
Group:		Libraries
Requires:	subversion-libs >= 1.6

%description svnqt
Shared library which contains a Qt C++ wrapper for subversion. It is
core part of kdesvn but is designed to not require KDE so plain Qt
programs may use it.

%description svnqt -l pl.UTF-8
Biblioteka współdzielona zawierająca wrapper C++ do obsługi
subversion. Jest główną częścią kdesvn, ale nie wymaga KDE, więc może
być używana w programach korzystających z samego Qt.

%package svnqt-devel
Summary:	Wrapper library header files for subversion Qt integration
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera biblioteki subversion dla Qt
Group:		Development/Libraries
Requires:	%{name}-svnqt = %{version}-%{release}
Requires:	QtGui-devel
Requires:	QtSql-devel
Requires:	subversion-devel >= 1.6

%description svnqt-devel
Header files for wrapper library for subversion Qt integration.

%description svnqt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki współdzielonej zawierającej wrapper C++ do
obsługi subversion.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	svnqt -p /sbin/ldconfig
%postun	svnqt -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde4/*.so
%{_desktopdir}/kde4/kdesvn.desktop
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svgz
%{_datadir}/apps/%{name}
%{_datadir}/apps/kdesvnpart
%{_datadir}/apps/kconf_update/kdesvn-use-external-update.sh
%{_datadir}/apps/kconf_update/kdesvnpartrc-use-external.upd
%{_datadir}/config.kcfg/*
%{_datadir}/kde4/services/ServiceMenus/*.desktop
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/*.protocol
%{_datadir}/kde4/services/kded/kdesvnd.desktop
%{_datadir}/dbus-1/interfaces/*.xml
%{_mandir}/man1/kdesvn.1*
%{_mandir}/man1/kdesvnaskpass.1*

%files svnqt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt.so.*

%files svnqt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvnqt.so
%{_includedir}/svnqt
