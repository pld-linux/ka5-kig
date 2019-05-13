%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kig
Summary:	kig
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8903b457ea6443e3b3ce7039d7b3a743
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
#BuildRequires:	boost-python-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
