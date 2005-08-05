Summary:	KDE frontend for subversion
Summary(pl):	Frontend KDE do subversion
Name:		kdesvn
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://www.alwins-world.de/programs/download/kdesvn/%{name}-%{version}.tar.gz
# Source0-md5:	f64a2ab4be6171f9287f190a321043bf
URL:		http://www.alwins-world.de/programs/kdesvn/
BuildRequires:	apr-util-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdesvn is yet another client for subversion. But it uses native KDE
API instead of a extra lib like GAMBAS and it is using the native
subversion delevelopment API instead of just parsing the output of the
commandline tool like most other clients do.

It tries to setup a look and feel like the standard filemanager of
KDE.

%description -l pl
kdesvn jest kolejnym klientem subversion. U¿ywa jednak natywnego API
KDE zamiast dodatkowej biblioteki jak GAMBAS, jak równie¿ u¿ywa
natywnego API subversion zamiast analizy wyj¶cia narzêdzia
dzia³aj±cego z linii poleceñ, jak to robi± inni klienci subversion.

Program ten stara siê ustawiæ wygl±d zbli¿ony do standardowego
zarz±dcy plików KDE.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--with-apr-config=/usr/bin/apr-1-config \
	--with-apu-config=/usr/bin/apu-1-config

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
