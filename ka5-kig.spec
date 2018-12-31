%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kig
Summary:	kig
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5d8ce37b6759ddf8a4a671087e82be30
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel >= 5.15
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kparts-devel >= 5.53.0
BuildRequires:	kf5-ktexteditor-devel
BuildRequires:	kf5-kxmlgui-devel >= 5.1
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kig is an application for Interactive Geometry. Features. Allows the
students to interactively explore mathematical figures and concepts
using the computer; Serves as a WYSIWYG tool for drawing mathematical
figures and including them in other documents.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kig
%attr(755,root,root) %{_bindir}/pykig.py
%attr(755,root,root) %{_libdir}/qt5/plugins/kigpart.so
%{_desktopdir}/org.kde.kig.desktop
%{_iconsdir}/hicolor/128x128/apps/kig.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/16x16/apps/kig.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/22x22/apps/kig.png
%{_iconsdir}/hicolor/22x22/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/32x32/apps/kig.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/48x48/apps/kig.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/64x64/apps/kig.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/scalable/apps/kig.svgz
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-kig.svgz
%{_datadir}/kig
%{_datadir}/kservices5/kig_part.desktop
%{_datadir}/kxmlgui5/kig
%lang(ca) %{_mandir}/ca/man1/kig.1*
%lang(de) %{_mandir}/de/man1/kig.1*
%lang(es) %{_mandir}/es/man1/kig.1*
%lang(et) %{_mandir}/et/man1/kig.1*
%lang(it) %{_mandir}/it/man1/kig.1*
%lang(C) %{_mandir}/man1/kig.1*
%lang(nl) %{_mandir}/nl/man1/kig.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kig.1*
%lang(ru) %{_mandir}/ru/man1/kig.1*
%lang(sv) %{_mandir}/sv/man1/kig.1*
%lang(uk) %{_mandir}/uk/man1/kig.1*
%{_datadir}/metainfo/org.kde.kig.appdata.xml
